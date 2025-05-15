"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    """
    Plots a scatter plot showing the relationship between age and fare.
    """
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="age", y="fare", hue="class", ax=ax)
    ax.set_title("Relational Plot: Age vs Fare by Class")
    plt.savefig('relational_plot.png')
    plt.close()
    return


def plot_categorical_plot(df):
    """
    Plots a bar chart showing the count of passengers by class.
    """
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="class", ax=ax)
    ax.set_title("Categorical Plot: Passenger Count by Class")
    plt.savefig('categorical_plot.png')
    plt.close()
    return


def plot_statistical_plot(df):
    """
    Plots a correlation heatmap of the dataset's numeric columns.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Statistical Plot: Correlation Heatmap")
    plt.savefig('statistical_plot.png')
    plt.close()
    return


def statistical_analysis(df, col: str):
    """
    Calculates the four statistical moments (mean, stddev, skewness, kurtosis).
    """
    data = df[col].dropna()
    mean = np.mean(data)
    stddev = np.std(data)
    skew = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)

    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    """
    Preprocesses the dataset by providing basic summary statistics.
    """
    print(df.describe())
    print(df.head())
    print(df.corr(numeric_only=True))
    return df


def writing(moments, col):
    """
    Prints the statistical moments in a human-readable format.
    """
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')

    if moments[2] > 0:
        skewness = 'right skewed'
    elif moments[2] < 0:
        skewness = 'left skewed'
    else:
        skewness = 'not skewed'

    if moments[3] > 0:
        kurtosis = 'leptokurtic'
    elif moments[3] < 0:
        kurtosis = 'platykurtic'
    else:
        kurtosis = 'mesokurtic'

    print(f'The data was {skewness} and {kurtosis}.')
    return


def main():
    """
    Main function to load data, perform preprocessing, statistical analysis, 
    and visualization.
    """
    # Load Titanic dataset
    df =pd.read_csv("titanic.csv")

    # Preprocess data
    df = preprocessing(df)

    # Column to be analyzed
    col = 'fare'

    # Generate plots
    plot_relational_plot(df)
    plot_categorical_plot(df)
    plot_statistical_plot(df)

    # Perform statistical analysis
    moments = statistical_analysis(df, col)

    # Write summary
    writing(moments, col)
    return


if _name_ == '_main_':
    main()
