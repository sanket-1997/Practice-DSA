from collections import deque
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices + 1)]

    
    def add_edge(self, u, v, w, directed = False):
        self.graph[u].append((v,w))
        if not directed:
            self.graph[v].append((u,w))

    def print_graph(self):
        
        for i in range(1, self.V+1):
            print(f"{i} -> ", end="")
            for neighbour, weight in self.graph[i]:
                print(f"({neighbour}, {weight}) ", end="")
            print()
    
    def bfs(self, start):
        visited = [False]*(self.V +1)
        queue = deque([start])
        visited[start] = True
        bfs_order = []

        print("BFS Tranersal", end = " ")
        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbour, _ in self.graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

        return bfs_order
    
    def dfs(self, start):
        visited = [False]*(self.V+1)
        stack = [start]
        dfs_order = []
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                dfs_order.append(node)
                visited[node]= True

            for neighbour, _ in reversed(self.graph[node]):
                if not visited[neighbour]:
                    stack.append(neighbour)

        return dfs_order
    






    



g = Graph(5)
g.add_edge(1,2,4)
g.add_edge(1,3,5)
g.add_edge(1,4,3)
g.add_edge(2,3,6)
g.add_edge(4,5,1)


g.print_graph()


print(g.bfs(4))
print(g.dfs(4))


