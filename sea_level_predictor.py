import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,5), dpi=200)
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=10, marker='.', label='original data')

    # Create first line of best fit
    years_all = pd.concat([df['Year'], pd.Series(data=[y for y in range(df['Year'].iat[-1]+1, 2051)])], ignore_index=True)
    line_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(years_all, line_all.intercept + line_all.slope * years_all, 'r', lw=2, alpha=.6, label='overall trend line')

    # Create second line of best fit
    years_recent = years_all[years_all >= 2000]
    df_recent = df[df['Year'] >= 2000]
    line_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_recent, line_recent.intercept + line_recent.slope * years_recent, 'y', lw=2, alpha=.6, label='recent trend line')

    # Add labels and title
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Sea Level (inches)', fontsize=12)
    plt.title('Rise in Sea Level', fontsize=14)
    plt.legend()
    plt.grid(visible=True, lw=.5, ls='--')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()