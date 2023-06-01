import io
from contextlib import redirect_stdout
from typing import Optional

import pandas as pd
from dotenv import load_dotenv
from plotly import express as px
from plotly import graph_objects as go
from plotly.graph_objects import Figure

from .llm import LLM
from .prompts.generate_python_code import GeneratePythonCodePrompt

load_dotenv()


class ChartGPT:
    def __init__(
        self,
        llm: Optional[str] = "openai",
        conversational: bool = True,
        verbose: bool = False,
        api_key: Optional[str] = None,
    ) -> None:
        """_summary_

        Args:
            llm (Optional[str], optional): _description_. Defaults to "openai".
            conversational (bool, optional): _description_. Defaults to True.
            verbose (bool, optional): _description_. Defaults to False.
        """
        self.llm = LLM(api_key=api_key)
        self.fig = None

    def load(self, data: pd.DataFrame) -> None:
        """Load a DataFrame.

        Args:
            df (pd.DataFrame): A DataFrame.

        Returns:
            None
        """
        self.data = data
        self.data_columns = data.columns

    def plot(self, prompt: str, show_code=False, debug=False) -> Figure:
        """Run the model on a prompt.

        Args:
            prompt (Optional[str]): _description_

        Returns:
            str: _description_
        """

        df_columns = self.data.columns

        self._original_instructions = {
            "question": prompt,
            "df_columns": df_columns,
        }

        if debug:
            code = """
import plotly.express as px

fig = px.bar(df, x="State", y="Population")
fig"""
        else:
            code = self.llm.generate_code(
                GeneratePythonCodePrompt(
                    df_columns=df_columns,
                ),
                prompt,
            )

        fig = self.run_code(
            code,
            self.data,
        )

        self.fig = fig
        fig.show()
        if show_code:
            print(code)
        return

    def run_code(
        self,
        code: str,
        df: pd.DataFrame,
        use_error_correction_framework: bool = False,
    ) -> str:
        """Execute Python code and return the variable on the last line.
        Args:
            code (str): A python code to execute
            df (pd.DataFrame): A full Pandas DataFrame
            use_error_correction_framework (bool): Turn on Error Correction mechanism.
            Default to True

        Returns:

        """
        self.last_run_code = code

        environment: dict = {"pd": pd, "go": go, "px": px, "df": df}

        with redirect_stdout(io.StringIO()) as output:
            n_retries = 0
            while n_retries < 2:
                try:
                    exec(code, environment)
                    code_ran = code
                    break
                except Exception as e:
                    if not use_error_correction_framework:
                        raise e
                    n_retries += 1

        captured_output = output.getvalue()

        lines = code_ran.strip().split("\n")
        last_line = lines[-1].strip()

        try:
            return eval(last_line, environment)
        except Exception:
            return captured_output


if __name__ == "__main__":
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
    )
    cg = ChartGPT()
    cg.load(df)
    cg.plot("State vs. Population", debug=False, show_code=True)
    print(str(cg.fig))
