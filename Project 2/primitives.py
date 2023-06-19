import pandas as pd
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import LegendItem, Legend

# Load your data into a pandas DataFrame
df = pd.read_csv('oregon_vehicle.csv')

# Create a new DataFrame with the counts per year
df_yearly = df[df['Make'] == 'Tesla'].groupby('First Reg Year').size().reset_index(name='Count')

# Define the year ranges
year_labels = ['2005-2010', '2010-2015', '2015-2020', '2020-2025']

# Assign a year range to each registration year
df_yearly['Year Range'] = pd.cut(df_yearly['First Reg Year'], bins=[2005, 2010, 2015, 2020, 2025], labels=year_labels)

# Prepare the ColumnDataSource
source = ColumnDataSource(df_yearly)

# Prepare the figure
p = figure(x_range=(2000, 2025), y_range=(0, df_yearly['Count'].max()*1.1), plot_width=600, plot_height=400, 
           title="Tesla Registrations vs Other Brands in Oregon (2005-2025)", tools="hover", tooltips="@Count")

# Plot the triangle symbols for Tesla's registered in a specific time frame
tesla_glyph = p.triangle('First Reg Year', 'Count', source=source, size=10, alpha=0.6, color='Red',
                         selection_color="firebrick", nonselection_fill_alpha=0.3, nonselection_fill_color="grey")

# Create a new DataFrame with the counts per year for other brands
df_yearly_other = df[df['Make'] != 'Tesla'].groupby('First Reg Year').size().reset_index(name='Count')

# Prepare the ColumnDataSource for other brands
source_other = ColumnDataSource(df_yearly_other)

# Plot the star symbols for other brands
other_glyph = p.star('First Reg Year', 'Count', source=source_other, color="blue", size=10, alpha=0.6)

# Create a legend
legend = Legend(items=[
    LegendItem(label="Tesla", renderers=[tesla_glyph]),
    LegendItem(label="Other Brands", renderers=[other_glyph]),
], location="top_left")


# Add the legend to the plot
p.add_layout(legend)

# Set up the layout
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Number of Registrations'

# Show the figure
show(p)



# # Import libraries
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd


# df = pd.read_csv('oregon_vehicle.csv')


# ## Meshgrid
# x, y = np.meshgrid(np.linspace(-5, 5, 10), 
#                    np.linspace(-5, 5, 10))
  
# # Directional vectors
# u = -y/np.sqrt(x**2 + y**2)
# v = x/(x**2 + y**2)
  
# # Plotting Vector Field with QUIVER
# plt.quiver(x, y, u, v, color='g')
# plt.title('Vector Field')
  
# # Setting x, y boundary limits
# plt.xlim(-7, 7)
# plt.ylim(-7, 7)
  
# # Show plot with grid
# plt.grid()
# plt.show()
