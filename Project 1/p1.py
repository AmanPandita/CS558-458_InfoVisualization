
import os

import pandas as pd
import matplotlib
import geopandas as gpd
import squarify
import numpy as np
import seaborn as sns
import folium
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objs as go
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# Load your dataset (replace the file path with the path to your dataset)
data = pd.read_csv("oregon_vehicle.csv")

# Filter years by every 15 years
year_filter = data['First Reg Year'].apply(lambda x: x % 5 == 0)
filtered_data = data[year_filter]

# Group the data by year and make, then count the number of registrations
grouped_data = filtered_data.groupby(['First Reg Year', 'Make']).count().reset_index()

# Combine other 149 brands into a single category
grouped_data['Make'] = grouped_data['Make'].apply(lambda x: x if x in ['Tesla', 'Chevrolet', 'Nissan', 'Toyota', 'Ford'] else 'Other 149 Brands')

# Regroup the data to account for the newly combined "Other 149 Brands" category
grouped_data = grouped_data.groupby(['First Reg Year', 'Make']).sum().reset_index()

# Pivot the grouped_data DataFrame to have makes as columns and years as rows
pivoted_data = grouped_data.pivot_table(values='FirstRegisteredDate', index='First Reg Year', columns='Make', fill_value=0)

# Create the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(data=pivoted_data)

# Add title, labels, and legend
plt.title('Average increase in New Electric Vehicle Registrations Every 5 Years (1980-2022)')
plt.xlabel('Brands')
plt.ylabel('Number of Registrations')
plt.legend(pivoted_data.columns, title="Car Brands")

# Display the plot
plt.show()



# #-------------------------------radar map-----------------------------

# brands = ['Tesla', 'Chevrolet', 'Nissan', 'Toyota', 'Ford']

# # Create a dictionary to store the counts of each brand
# brand_counts = {brand: 0 for brand in brands}
# brand_counts['Other 149 brands'] = 0

# # Count the occurrences of each brand
# for brand in data['Make']:
#     if brand in brand_counts:
#         brand_counts[brand] += 1
#     else:
#         brand_counts['Other 149 brands'] += 1

# # Create a radar chart
# angles = np.linspace(0, 2 * np.pi, len(brands) + 2, endpoint=True)
# counts = [brand_counts[brand] for brand in brands]
# counts.append(brand_counts['Other 149 brands'])
# counts += counts[:1]  # Close the radar chart

# fig, ax = plt.subplots(subplot_kw={'polar': True})
# ax.plot(angles, counts, linewidth=1, linestyle='solid', label='Car Registrations')
# ax.fill(angles, counts, 'b', alpha=0.25)

# ax.set_theta_offset(np.pi / 2)
# ax.set_theta_direction(-1)

# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(brands + ['Other 149 brands'])

# ax.set_yticklabels([])

# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
# plt.title("Car Registrations by Brand")
# plt.show()




# # -------------------Tree map ----------------------------------------------------


# # Specify the car brands of interest
# brands = ['Tesla', 'Chevrolet', 'Nissan', 'Toyota', 'Ford']

# # Group other brands into a single category
# data['grouped_make'] = data['Make'].apply(lambda x: x if x in brands else 'Other')

# # Group the data by make and count the number of cars for each make
# make_counts = data.groupby('grouped_make')['Make'].count()

# # Normalize the make_counts values for colormap
# normalized_counts = make_counts / make_counts.max()

# # Create labels with counts
# labels = [f'{make}\n({count})' for make, count in make_counts.items()]

# # Create the treemap
# plt.figure(figsize=(12, 8))
# squarify.plot(sizes=make_counts.values, label=labels, alpha=0.8, color=plt.cm.Reds(normalized_counts))

# # Add title and axis labels
# plt.title('Number of Cars by Make')
# plt.axis('off')

# # Display the treemap
# plt.show()







# # ---------------------Number of registratins over time vs time------------------------------------------



# # Convert the date columns to datetime objects
# data['FirstRegisteredDate'] = pd.to_datetime(data['FirstRegisteredDate'], format='%A, %B %d, %Y')
# data['LastRegisteredDate'] = pd.to_datetime(data['LastRegisteredDate'], format='%A, %B %d, %Y')

# # Extract the year and month from the date columns
# data['YearMonthFirst'] = data['FirstRegisteredDate'].dt.strftime('%Y')
# data['YearMonthLast'] = data['LastRegisteredDate'].dt.strftime('%Y')

# # Group the data by year and month and count the number of registrations
# resampled_data = data.groupby('YearMonthFirst').count()

# # Create the time series plot
# plt.figure(figsize=(12, 6))
# plt.plot(resampled_data.index, resampled_data['FirstRegisteredDate'], label='First Registered')
# # plt.plot(resampled_data.index, resampled_data['LastRegisteredDate'], label='Last Registered')

# # Add title, labels, and legend
# plt.title('Number of Registrations Over Time')
# plt.xlabel('Time')
# plt.ylabel('Number of Registrations')
# plt.legend()

# # Display the plot
# plt.show()

#----------------------------------------------------------------------

# Specify the car brands of interest
# brands = ['Tesla']


# # Group other brands into a single category
# data['grouped_make'] = data['Make'].apply(lambda x: x if x in brands else 'Other')

# # Convert the date columns to datetime objects
# data['FirstRegisteredDate'] = pd.to_datetime(data['FirstRegisteredDate'], format='%A, %B %d, %Y')
# data['LastRegisteredDate'] = pd.to_datetime(data['LastRegisteredDate'], format='%A, %B %d, %Y')

# # Extract the year from the date columns
# data['YearFirst'] = data['FirstRegisteredDate'].dt.strftime('%Y')
# data['YearLast'] = data['LastRegisteredDate'].dt.strftime('%Y')

# # Group the data by year and make, then count the number of registrations
# resampled_data = data.groupby(['YearFirst', 'grouped_make']).count().reset_index()

# # Create the time series plot
# plt.figure(figsize=(12, 6))

# for brand in brands + ['Other']:
#     brand_data = resampled_data[resampled_data['grouped_make'] == brand]
#     plt.plot(brand_data['YearFirst'], brand_data['FirstRegisteredDate'], label=brand)

# # Add title, labels, and legend
# plt.title('Number of Registrations Over Time')
# plt.xlabel('Time')
# plt.ylabel('Number of Registrations')
# plt.legend()

# # # Set the x-axis limits
# # plt.xlim(1980, 2022)

# # Display the plot
# plt.show()





#--------------------------------------------------------------------------------------



# # Specify the car brands of interest
# brands = ['Tesla', 'Chevrolet', 'Nissan', 'Toyota', 'Ford']

# # Group other brands into a single category
# data['grouped_make'] = data['Make'].apply(lambda x: x if x in brands else 'Other')

# # Convert the date columns to datetime objects
# data['FirstRegisteredDate'] = pd.to_datetime(data['FirstRegisteredDate'], format='%A, %B %d, %Y')
# data['LastRegisteredDate'] = pd.to_datetime(data['LastRegisteredDate'], format='%A, %B %d, %Y')

# # Extract the year from the date columns
# data['YearFirst'] = data['FirstRegisteredDate'].dt.strftime('%Y-%m')
# data['YearLast'] = data['LastRegisteredDate'].dt.strftime('%Y-%m')

# # Group the data by year and make, then count the number of registrations
# resampled_data = data.groupby(['YearFirst', 'grouped_make']).count().reset_index()

# # Filter the data for Tesla and other brands
# tesla_data = resampled_data[resampled_data['grouped_make'] == 'Tesla']
# other_brands_data = resampled_data[resampled_data['grouped_make'] == 'Other']

# # Create the scatter plot
# plt.figure(figsize=(12, 6))
# plt.scatter(tesla_data['YearFirst'], tesla_data['FirstRegisteredDate'], label='Tesla', alpha=0.8)
# plt.scatter(other_brands_data['YearFirst'], other_brands_data['FirstRegisteredDate'], label='Other Brands', alpha=0.8)

# # Add title, labels, and legend
# plt.title('Tesla Sales vs Other Brands Sales Over Time')
# plt.xlabel('Time')
# plt.ylabel('Number of Registrations')
# plt.legend()

# # # Set the x-axis limits
# # plt.xlim(1980, 2022)

# # Display the plot
# plt.show()
