#for finding shortest path
import sys
class Graph() :
    def __init__(self,vertices) :
        self.V = vertices
        self.graph = [[0 for i in range (vertices)]for j in range(vertices)]

    def dijkstra(self,source) :
        dist = [sys.maxsize]*self.V
        dist[source] = 0
        visited = [False]*self.V

        for count in range(self.V) :
            u = self.minnodeweight(dist,visited)
            visited[u] = True
            for v in range(self.V) :
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u]+self.graph[u][v] :
                    dist[v] = dist[u]+self.graph[u][v]  
        self.printsolution(dist)

    def minnodeweight(self,dist,visited) :
        mini = sys.maxsize
        for v in range(self.V) :
            if dist[v] < mini and visited[v] == False :
                mini = dist[v]
                min_index = v
        return min_index

    def printsolution(self,dist) :
        print("Distance between source and node is")
        for v in range(self.V) :
            print(v,"dist : ",dist[v])

# driver code
g = Graph(4)
g.graph = [[0.0,1.0,3.0,sys.maxsize],[1.0,0.0,1.0,4.0],[sys.maxsize,4.0,2.0,0.0]]
g.dijkstra(0)

