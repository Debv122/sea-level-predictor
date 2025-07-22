import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

# Add data labels for every 10th year
for i, row in df.iterrows():
    if row['Year'] % 10 == 0:
        plt.annotate(f"{int(row['Year'])}\n{row['CSIRO Adjusted Sea Level']:.2f}",
                     (row['Year'], row['CSIRO Adjusted Sea Level']),
                     textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='darkblue')

# Line of best fit for all data
slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(df['Year'].min(), 2051))
plt.plot(years_extended, intercept_all + slope_all * years_extended, 'r', label='Best fit: 1880-2050')

# Line of best fit for data from 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = pd.Series(range(2000, 2051))
plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'g', label='Best fit: 2000-2050')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Save plot
plt.savefig('sea_level_plot.png')
plt.close() 