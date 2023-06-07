# ChartGPT ✨📊

[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1RokFYWHiW0aZOYpOTXbf3HJIzEslbZ6i?usp=sharing)

ChartGPT is a lightweight and user-friendly tool designed to assist you in visualizing your Pandas dataframes. Whether you are working in a Jupyter notebook or developing a Dash app, ChartGPT makes it effortless to generate stunning charts and plots. 📈

## Features 🌟

- Intuitive integration with Pandas dataframes 🐼
- Supports both Jupyter notebooks and Dash apps 📓🚀
- Simple installation and setup ⚙️

## Installation ⬇️

You can install ChartGPT using pip:

```shell
pip install chartgpt
```

## Example Usage 🎉

### Jupyter Notebook 📔

![ChartGPT in a Jupyter notebook](docs/assets/notebook.png)

```python
from chartgpt import ChartGPT

# Load your Pandas dataframe
df = pd.read_csv('data.csv')

# Load the dataframe into ChartGPT
cg = ChartGPT
cg.load(df)

# Use ChartGPT to plot the dataframe
cg.plot("ask me about my chart!")
```

### Dash App 🚀

![ChartGPT in a Dash app](docs/assets/dash.png)

See Dash example [here]().

## Documentation 📚

For detailed information on how to use ChartGPT, please refer to the [documentation](https://chatgpt.github.io/chart/).

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
