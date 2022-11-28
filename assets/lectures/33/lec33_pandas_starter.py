import pandas as pd

# if we were generating plots, we would also need the following three lines
#   import matplotlib.pyplot as plt
#   from pandas.plotting import register_matplotlib_converters
#   register_matplotlib_converters()

# read in the data from a URL
url = "https://brown-csci0111.github.io/assets/lectures/33/events.csv"
events = pd.read_csv(url, header=0, 
                     names=["name","email","numtix","discount","delivery"])