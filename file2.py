import plotly.figure_factory as ff
import pandas as pd

dataframe = pd.read_csv("data.csv")

graph2 = ff.create_distplot([dataframe["Weight"].tolist()],["weight"],show_hist=False)
graph2.show()