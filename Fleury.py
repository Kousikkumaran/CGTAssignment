import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges.append((u, v))

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def is_connected(self):
        visited = [False] * self.V
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                break
        if i == self.V:
            return True
        self.dfs(i, visited)
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
        return True

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def is_valid_next_edge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        visited = [False] * self.V
        count1 = self.dfs_count(u, visited)

        self.remove_edge(u, v)
        visited = [False] * self.V
        count2 = self.dfs_count(u, visited)

        self.add_edge(u, v)

        return count1 <= count2

    def dfs_count(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfs_count(i, visited)
        return count

    def print_euler_util(self, u, path):
        for v in list(self.graph[u]):
            if self.is_valid_next_edge(u, v):
                path.append((u, v))
                self.remove_edge(u, v)
                self.print_euler_util(v, path)

    def find_euler(self):
        odd = 0
        start_vertex = 0
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                odd += 1
                start_vertex = i
        path = []
        if odd == 0:
            self.print_euler_util(0, path)
        elif odd == 2:
            self.print_euler_util(start_vertex, path)
        else:
            return None
        return path

    def visualize(self, path):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        
        pos = nx.spring_layout(G)

        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=15)
        
        if path:
            edges_in_path = [(u, v) for (u, v) in path] + [(v, u) for (u, v) in path]
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)
        
        plt.show()

def create_graph_from_user_input():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    g = Graph(num_vertices)
    
    print(f"Enter the {num_edges} edges (u v) as space-separated pairs:")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)
        return g

if __name__ == "__main__":
    g = create_graph_from_user_input()
    path = g.find_euler()
    g.visualize(path)

