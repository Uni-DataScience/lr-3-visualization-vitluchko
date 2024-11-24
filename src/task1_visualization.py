import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    frequency = collections.Counter(data)

    categories = list(frequency.keys())
    counts = list(frequency.values())

    fig, ax = plt.subplots()
    ax.bar(categories, counts, color=['red', 'blue', 'green'])

    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Categories')

    plt.show()

    return fig


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
