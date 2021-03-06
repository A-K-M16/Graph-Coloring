class Grapha:
    def __init__(self, edges, N):
        
        self.adj = [[] for _ in range(N)]
       
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)


def colorGraph(graph):
    
    result = {}

    for u in range(N):

        assigned = set([result.get(i) for i in graph.adj[u] if i in result])
        print(assigned)
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        result[u] = color

    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])



colors = [ "","BLUE","GREEN","RED","YELLOW","ORANGE","PINK","BLACK","BROWN","WHITE",
          "PURPLE","VIOLET"]

edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

N = 6
graph = Grapha(edges, N)
colorGraph(graph)
