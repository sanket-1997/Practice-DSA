class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices + 1)]
    
    def add_edge(self, u,v,w, directed = False):

        self.graph[u].append((v,w))
        if not directed:
            self.graph[v].append((u,w))
        
    
    def print_graph(self):
        
        for i in range(1, self.V):
            print(f"{i} -> ", end="")
            for neighbour, weight in self.graph[i]:
                print(f"({neighbour}, {weight}) ", end="")
            
            print()


g = Graph(4)
g.add_edge(1,2,3)
g.add_edge(1,3,2)
g.add_edge(2,4,1)


g.print_graph()