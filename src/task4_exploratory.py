import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    # 1. Descriptive Statistics
    print("\n\nDescriptive Statistics:")
    descriptive_stats = df.describe().T
    print(descriptive_stats)

    # 2. Outlier Detection using Box Plots
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, orient='h')
    plt.title('Box Plot for Outlier Detection')
    plt.show()

    # 3. Correlation Matrix and Heatmap
    corr_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(corr_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    plt.title('Correlation Matrix Heatmap')
    plt.show()


# Example data
df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})
perform_eda(df)
