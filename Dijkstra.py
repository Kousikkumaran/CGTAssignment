import random
import heapq
import matplotlib.pyplot as plt
import networkx as nx

def generate_graph(num_vertices, max_weight):
    graph = [[0 if i == j else random.randint(1, max_weight) for j in range(num_vertices)] for i in range(num_vertices)]
    return graph

def dijkstra(graph, src):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[src] = 0
    priority_queue = [(0, src)] 

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        for v in range(num_vertices):
            if graph[u][v] > 0: 
                distance = current_distance + graph[u][v]

                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(priority_queue, (distance, v))

    return distances

def plot_graph(graph):
    G = nx.Graph()
    num_vertices = len(graph)
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] > 0:
                G.add_edge(i, j, weight=graph[i][j])

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16, font_color='black')
        
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    
    plt.title('Random Weighted Graph')
    plt.show()

if __name__ == "__main__":
    num_vertices = 5  
    max_weight = 20   
    graph = generate_graph(num_vertices, max_weight)
    
    print("Generated Graph (Adjacency Matrix):")
    for row in graph:
        print(row)
    
    src = random.randint(0, num_vertices - 1)
    print(f"\nSource Vertex: {src}")
    
    shortest_distances = dijkstra(graph, src)
    
    print("\nShortest distances from source vertex to all vertices:")
    for vertex, distance in enumerate(shortest_distances):
        print(f"Vertex {vertex}: {distance}")

    plot_graph(graph)
