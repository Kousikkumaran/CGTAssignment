import matplotlib.pyplot as plt
import networkx as nx

def get_edges_from_user():
    edges = []
    while True:
        
        user_input = input("Enter edge (format: A B weight) or 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        try:
           
            u, v, weight = user_input.split()
            weight = float(weight)
            edges.append((u, v, weight))
        except ValueError:
            print("Invalid input. Please enter in format: A B weight")
    return edges

edges = get_edges_from_user()

G = nx.Graph()

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

mst_edges = list(nx.minimum_spanning_edges(G, algorithm='prim', data=False))

mst = nx.Graph()
mst.add_edges_from(mst_edges)

pos = nx.spring_layout(mst)

plt.figure(figsize=(10, 6))
nx.draw(mst, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=14, font_weight='bold')
edge_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_color='red', font_size=12)

plt.title("Minimum Spanning Tree", fontsize=16)
plt.axis('off')  
plt.show()

