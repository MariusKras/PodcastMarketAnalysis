import pandas as pd
import plotly.express as px
from pandas.core.frame import DataFrame

def plot_hist(df: DataFrame) -> None:
    """
    Plot histogram of ratings from a DataFrame.

    Args:
        df (DataFrame): The DataFrame containing the ratings data.

    Returns:
        None
    """
    fig = px.histogram(
        df,
        title="Distribution of Podcast Ratings",
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_layout(
        yaxis=dict(title="Frequency"),
        xaxis=dict(title="Ratings"),
        bargap=0.1,
        showlegend=False,
        title_x=0.5,
        title_y=0.9,
    )
    fig.show()

def plot_line(df: DataFrame) -> None:
    """
    Plot line chart of data from a DataFrame.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.line(
        df,
        x="review_week",
        y="num_reviews",
        title="Total Number Of Weekly Reviews",
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_layout(
        yaxis=dict(title="Number Of Reviews"),
        xaxis=dict(title="Time"),
        title_x=0.5,
        title_y=0.9,
    )
    fig.show()

def plot_counts(df: DataFrame, title: str) -> None:
    """
    Plot bar chart of counts from a DataFrame.

    Args:
        df (DataFrame): The DataFrame containing the data.
        title (str): The title of the plot.

    Returns:
        None
    """
    fig = px.bar(
        df,
        x="category",
        y="counts",
        title=title,
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_layout(
        xaxis=dict(title="Number Of Podcasts"),
        yaxis=dict(title="Categories"),
        title_x=0.5,
        title_y=0.93,
        xaxis_tickfont=dict(size=11),
    )
    fig.show()

def plot_counts_series(df: DataFrame) -> None:
    """
    Plot bar chart of counts from a Series.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.bar(
        df,
        title="Distribution of New Categories (By Selecting Largest Category)",
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_layout(
        yaxis=dict(title="Number Of Podcasts"),
        xaxis=dict(title="Categories"),
        showlegend=False,
        title_x=0.5,
        title_y=0.9,
        xaxis_tickfont=dict(size=11),
    )
    fig.show()

def plot_box(df: DataFrame) -> None:
    """
    Plot box plot of each categorie counts from a DataFrame.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.box(
        df["category"].value_counts(),
        title="Number Of Reviews In Each Category",
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_layout(
        yaxis=dict(title="Number Of Reviews"),
        xaxis=dict(title="All Podcasts"),
        title_x=0.5,
        title_y=0.9,
        xaxis_tickfont=dict(size=1),
    )
    fig.show()

def plot_ratings_categories(df: DataFrame) -> None:
    """
    Plot proportional stacked bar chart of ratings across categories.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.bar(
        df,
        x="category",
        y=[1, 2, 3, 4, 5],
        labels={"value": "Proportion", "category": "Category", "variable": "Rating"},
        color_discrete_sequence=px.colors.qualitative.Pastel,
        title="Proportions of Ratings Across Categories",
        template="plotly_white",
    )
    fig.update_layout(
        xaxis_tickangle=45,
        title_x=0.5,
        legend_title="Rating",
        height=420,
        xaxis_tickfont=dict(size=11),
    )
    fig.show()

def plot_reviews_month(df: DataFrame) -> None:
    """
    Plot line chart of number of reviews per month by category.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.line(
        df,
        x="year_month",
        y="num_reviews",
        title="Number Of Monthly Reviews By Category",
        color="category",
        template="plotly_white",
    )
    fig.update_layout(
        yaxis=dict(title="Number of Reviews"),
        xaxis=dict(title="Months"),
        legend=dict(title="Categories"),
        height=600,
        title_x=0.42,
        title_y=0.93,
    )
    fig.show()

def plot_true_crime_month(df: DataFrame) -> None:
    """
    Plot line chart of proportion of ratings over time for True-Crime podcasts.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.line(
        df,
        x="year_month",
        y="proportion",
        color="rating",
        template="plotly_white",
        title="Rating Change For True-Crime Podcasts",
    )
    fig.update_layout(
        yaxis=dict(title="Proportion of Ratings"),
        xaxis=dict(title="Months"),
        legend=dict(title="Ratings"),
        title_x=0.5,
        title_y=0.9,
    )
    fig.show()

def plot_podcasts_reviews(df: DataFrame) -> None:
    """
    Plot scatter plot of number of podcasts and total reviews for each category.

    Args:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    fig = px.scatter(
        df,
        x="num_podcasts",
        y="total_reviews",
        hover_name="category",
        title="Number of Podcasts And Reviews For Each Category",
        labels={"num_podcasts": "Number of Podcasts", "total_reviews": "Total Reviews"},
        template="plotly_white",
        color_discrete_sequence=["#1f77b4"],
    )
    fig.update_traces(marker=dict(size=6, opacity=0.8))
    fig.update_layout(title_x=0.5, title_y=0.9)
    fig.show()