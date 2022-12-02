import pandas as pd

# to generating plots, we need the following three lines
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

sales_url = "https://brown-csci0111.github.io/assets/lectures/35/salesdata.csv"
sales_cols = ['month','northwest','northeast','central','southeast','southwest','season']
sales = pd.read_csv(sales_url, header=0, names=sales_cols)

pass