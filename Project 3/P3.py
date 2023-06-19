# Bar char


import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a dataframe
df = pd.read_csv('2020-07-Charging-Data.csv')

# Count the number of stations for each EV Network
network_counts = df['EV Network'].value_counts()

# Create a bar plot
plt.figure(figsize=(10,6))
network_counts.plot(kind='bar', color='skyblue')

plt.title('Number of Charging Stations per EV Network')
plt.xlabel('EV Network')
plt.ylabel('Number of Charging Stations')

# Display the plot
plt.show()


# pie chart


# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy

# # Load the data into a dataframe
# df = pd.read_csv('oregon_vehicle.csv')

# # Group by 'Make' and then 'Model' and count unique combinations
# models_per_brand = df.groupby('Make')['Model'].nunique()

# # Sort in descending order
# models_per_brand = models_per_brand.sort_values(ascending=False)

# # Save the result to a CSV file
# models_per_brand.to_csv('models_per_brand.csv', header=True)

# # Take top 10 brands
# top_10_brands = models_per_brand.head(10)

# # Function to display absolute values instead of percentages
# def absolute_value(val):
#     a  = numpy.round(val/100.*top_10_brands.sum(), 0)
#     return int(a)

# # Generate a pie chart
# plt.figure(figsize=(10,10))
# plt.pie(top_10_brands, labels=top_10_brands.index, autopct=absolute_value)
# plt.title('Top 10 Brands with Most Models')
# plt.show()



# 



# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt

# # load the dataset
# charging_data = pd.read_csv('2020-07-Charging-Data.csv')

# # here we count the number of stations for each city
# city_counts = charging_data['City'].value_counts().reset_index()
# city_counts.columns = ['City', 'StationCount']

# # create an empty graph
# G = nx.Graph()

# # add nodes (cities) to the graph
# for index, row in city_counts.iterrows():
#     G.add_node(row['City'], StationCount=row['StationCount'])

# # add edges between cities with similar number of stations
# # you could define "similar" as you see fit
# # for example, we'll say two cities are similar if the number of stations is within 10% of each other
# for city1 in G.nodes:
#     for city2 in G.nodes:
#         if city1 != city2:
#             count1 = G.nodes[city1]['StationCount']
#             count2 = G.nodes[city2]['StationCount']
#             if abs(count1 - count2) / max(count1, count2) < 0.1:  # adjust this as necessary
#                 G.add_edge(city1, city2)
# # draw the graph
# plt.figure(figsize=(10,10))
# node_sizes = [nx.get_node_attributes(G, 'StationCount')[city]*10 for city in G] # adjust the multiplier for better visualization
# nx.draw(G, with_labels=True, node_size=node_sizes)
# plt.show()
