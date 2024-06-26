import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date', inplace = True)

# Clean data
upper_bound = df['value'].quantile(0.025)
lower_bound = df['value'].quantile(0.975)


df = df[(df['value'] >= upper_bound) & (df['value'] <= lower_bound)] 


def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(10,9))
    plt.plot(df.index, df['value'])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year

    value = df_bar['value'].groupby([df_bar['year'], df_bar['month']]).mean()
    
    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10,9))
    value.plot(kind='bar')
    
    plt.xticks(rotation=45) 
    years = sorted(df_bar['year'].unique())
    plt.xticks(range(len(years)), years) 


    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(months)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
        #FIRST BOX PLOT "Year Wise Box Plot (Trend)"
    fig, ax = plt.subplots(figsize=(10,9))
    sns.boxplot(x='year', y='value', data=df_box)



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

