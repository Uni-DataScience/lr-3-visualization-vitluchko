import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    fig, ax = plt.subplots()
    ax.plot(data, label='1D Line Plot', color='b')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('1D Line Plot of Data')
    ax.legend()
    plt.show()


def plot_2d(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='g', label='2D Scatter Plot')
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_title('2D Scatter Plot: X vs Y')
    ax.legend()
    plt.show()


def plot_3d(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', label='3D Scatter Plot')
    ax.set_xlabel('X Variable')
    ax.set_ylabel('Y Variable')
    ax.set_zlabel('Z Variable')
    ax.set_title('3D Scatter Plot: X vs Y vs Z')
    ax.legend()
    plt.show()


# Example data
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)
plot_2d(x, y)
plot_3d(x, y, z)
