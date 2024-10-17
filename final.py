import networkx as nx
import random
import matplotlib.pyplot as plt

# Havel-Hakimi algorithm to check if a degree sequence is graphical
def havel_hakimi(degrees):
    degrees = [deg for deg in degrees if deg > 0]
    while degrees:
        degrees.sort(reverse=True)
        n = degrees.pop(0)
        if n > len(degrees):
            return False
        for i in range(n):
            degrees[i] -= 1
        degrees = [deg for deg in degrees if deg > 0]
    return True

# Generate a random degree sequence
def generate_random_sequence(num_vertices):
    degrees = [random.randint(1, num_vertices - 1) for _ in range(num_vertices)]
    return degrees

# Create a graph using the Havel-Hakimi algorithm
def create_graph_from_sequence(degrees):
    if havel_hakimi(degrees):
        G = nx.havel_hakimi_graph(degrees)
        return G
    else:
        return None

# Check if the graph is Eulerian
def is_eulerian(graph):
    if nx.is_eulerian(graph):
        return "Eulerian Circuit"
    elif nx.has_eulerian_path(graph):
        return "Eulerian Path"
    else:
        return "Not Eulerian"

# Fleury's algorithm to find Eulerian path/circuit
def fleury_algorithm(graph):
    if not nx.is_eulerian(graph) and not nx.has_eulerian_path(graph):
        return None

    path = list(nx.eulerian_path(graph)) if nx.has_eulerian_path(graph) else list(nx.eulerian_circuit(graph))
    return path

# Assign random weights to the edges
def assign_random_weights(graph):
    for (u, v) in graph.edges():
        graph[u][v]['weight'] = random.randint(1, 10)

# Dijkstra's Algorithm for shortest path
def dijkstra_shortest_path(graph, source):
    return nx.single_source_dijkstra(graph, source)

# Find the MST using Prim's or Kruskal's Algorithm
def find_mst(graph):
    return nx.minimum_spanning_tree(graph, algorithm='prim')

# Find the edge and vertex connectivity
def find_connectivity(graph):
    edge_connectivity = nx.edge_connectivity(graph)
    vertex_connectivity = nx.vertex_connectivity(graph)
    k_connected = vertex_connectivity
    return edge_connectivity, vertex_connectivity, k_connected

# Plotting the graph
def plot_graph(graph, title):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=1000)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title(title)
    plt.show()

# Main function
def main():
    num_vertices = int(input("Enter the number of vertices: "))
    
    # Step 1: Generate a random graphic sequence and create the graph
    degrees = generate_random_sequence(num_vertices)
    print(f"Generated degree sequence: {degrees}")
    graph = create_graph_from_sequence(degrees)
    
    if graph is None:
        print("The degree sequence is not graphical.")
        return
    
    plot_graph(graph, "Generated Graph")
    
    # Step 2: Test if the graph is Eulerian and find Euler path/circuit using Fleury's algorithm
    euler_status = is_eulerian(graph)
    print(f"The graph is: {euler_status}")
    
    if euler_status != "Not Eulerian":
        euler_path = fleury_algorithm(graph)
        print(f"Euler Path/Circuit: {list(euler_path)}")
    
    # Step 3: Assign random weights and find shortest path from a random vertex
    assign_random_weights(graph)
    plot_graph(graph, "Graph with Random Weights")
    
    source_vertex = int(input("Enter the source vertex for shortest path: "))
    shortest_paths = dijkstra_shortest_path(graph, source_vertex)
    print(f"Shortest paths from vertex {source_vertex}: {shortest_paths}")
    
    # Step 4: Find the MST
    mst = find_mst(graph)
    plot_graph(mst, "Minimum Spanning Tree")
    
    # Step 5: Find the edge and vertex connectivity
    edge_conn, vertex_conn, k_connected = find_connectivity(graph)
    print(f"Edge Connectivity: {edge_conn}")
    print(f"Vertex Connectivity: {vertex_conn}")
    print(f"The graph is {k_connected}-connected.")

if __name__ == "__main__":
    main()
