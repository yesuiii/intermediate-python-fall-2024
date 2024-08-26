#Imports pandas package as pd
import pandas as pd

def plot_data(data):
    # Stores data as DataFrame and returns the plot
    ax = pd.DataFrame(data).plot.hist()
    return ax