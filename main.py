import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titles = pd.read_csv('titles.csv')
credits = pd.read_csv('credits.csv')
# titles.groupby('type')['imdb_score'].count().plot.pie()
# titles.info()
# credits.info()


def first():
    movie_scores = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
    show_scores = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()
    plt.hist(movie_scores, np.arange(0, 10.2, 0.2))
    plt.hist(show_scores, np.arange(0, 10.2, 0.2))
    plt.title('Histogram of movie and show')
    plt.xlabel("imdb_score")
    plt.ylabel("Number of titles")
    print(titles.groupby(by=["type"])["imdb_score"].mean())
    plt.axvline(movie_scores.mean(), color="k", linestyle="dashed", linewidth=1)
    plt.axvline(show_scores.mean(), color="r", linestyle="dashed", linewidth=1)
    plt.legend(('average film score', 'average show score', 'movie', 'show' ),
           loc='upper left')
    plt.grid()
    plt.show()


def first1():  # інший варіант побудови гістограм
    bins = np.arange(0, 10.2, 0.2)
    hists = titles.hist(column="imdb_score", by="type", bins=bins, edgecolor="black", xlabelsize=5)
    for hist in hists:
        hist.set_xticks(bins)
        hist.set_xlabel("imdb_score")
        hist.set_ylabel("Number of titles")
        # hist.axvline((hist["type"])["imdb_score"].mean(), color="red", linestyle="dashed", linewidth=2)
        hist.grid()
    print(titles.groupby(by=["type"])["imdb_score"].mean())
    plt.show()


def second():
    values = titles[titles["type"] == "SHOW"]["age_certification"].dropna()
    labels, values = np.unique(values, return_counts=True)
    colors = ['yellowgreen', 'blue', 'orange', 'yellow', 'crimson', 'purple']
    plt.pie(values, colors=colors, labels=labels, autopct='%1.1f%%')
    plt.show()


def third():
    pass


def fourth():
    first = titles.sort_values(by="imdb_score", ascending=True).dropna().head(1000)  # ascending - по збільшенню
    second = credits[["id", "name", "role"]][credits["role"] == "ACTOR"]
    merged = pd.merge(first, second, how='inner', on="id")
    print(merged.groupby(by="name")["id"].count().sort_values(ascending=False).head(10))


first()
second()
fourth()
# first1()
