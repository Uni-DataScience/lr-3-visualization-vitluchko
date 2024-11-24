import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    sns.set(style="whitegrid")

    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='x', y='y', ax=ax)

    ax.grid(True)

    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('Scatter Plot of X vs Y')

    plt.show()

    return fig


# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
