import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Coordinates of SRM University and home
start_coords = (16.4622500, 80.5068774)
end_coords = (16.4878734, 80.6106702)

# Fetch the road network around the coordinates
G = ox.graph_from_point(start_coords, dist=5000, network_type='drive')

# Find the nearest nodes to the start and end coordinates
start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

# Compute the shortest path using Dijkstra's algorithm
shortest_path = nx.shortest_path(G, start_node, end_node, weight='length')

# Plot the map with the shortest route
fig, ax = ox.plot_graph_route(G, shortest_path, route_linewidth=3, node_size=0, bgcolor='white')
plt.show()
