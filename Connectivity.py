import networkx as nx

def graph_connectivity(graph):
    edge_connectivity = nx.edge_connectivity(graph)
    vertex_connectivity = nx.vertex_connectivity(graph)
    k_connected = vertex_connectivity
    return edge_connectivity, vertex_connectivity, k_connected

# Sample graph with predefined edges
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]

# Create the graph
G = nx.Graph()
G.add_edges_from(edges)

# Calculate edge and vertex connectivity
edge_conn, vertex_conn, k = graph_connectivity(G)

print(f"Sample Graph Edges: {edges}")
print(f"Edge Connectivity: {edge_conn}")
print(f"Vertex Connectivity: {vertex_conn}")
print(f"The value of K for K-connected: {k}")
