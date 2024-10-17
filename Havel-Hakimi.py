import matplotlib.pyplot as plt
import networkx as nx

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

def plot_graph(degrees):
    G = nx.havel_hakimi_graph(degrees)
    plt.figure(figsize=(8, 8))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_color='black', edge_color='gray')
    plt.title("Graph Representation of Degree Sequence")
    plt.show()

def main():
    degrees = list(map(int, input("Enter the degree sequence (space-separated): ").split()))

    if havel_hakimi(degrees):
        print("The degree sequence is valid. Drawing the graph...")
        plot_graph(degrees)
    else:
        print("The degree sequence is not graphical.")

if __name__ == "__main__":
    main()
