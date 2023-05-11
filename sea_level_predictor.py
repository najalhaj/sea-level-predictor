import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linreg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    rng = range(df['Year'].min(), 2051)
    
    ax = plt.plot(rng, linreg.slope * rng + linreg.intercept)

  
    # Create second line of best fit
    linreg2000 = linregress((df.loc[df['Year'] >= 2000, 'Year']),(df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']))

    rng2000 = range(2000, 2051)

    ax = plt.plot(rng2000, linreg2000.slope * rng2000 + linreg2000.intercept)


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()