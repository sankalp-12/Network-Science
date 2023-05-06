from heapq import heappop, heappush
  
# To define no edge exists
INF = 999999999

# Number of vertices 
V = 5

# To add edges in the graph
def AddEdge(graph, source, destination, weight):
    graph[source].append(tuple((destination, weight)))


# A class to store and update the Heap Node
class Node:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
 
    # Override the __lt__() function to make `Node` class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
def derivePath(prev, i, path):
    if i >= 0:
        derivePath(prev, prev[i], path)
        path.append(i)
 
# Run Dijkstra’s algorithm on the Directed Graph to find out the B/W-ness Centrality
def Djikstra(graph, source, n, freq):
 
    # Create a min-heap and push source node having distance 0
    priority_queue = []
    heappush(priority_queue, Node(source))
 
    # Set initial distance from the source to `v` as infinity and initial distance from the source to `v` as infinity 
    dist = [INF] * n
    dist[source] = 0
 
    # List to track vertices for which minimum cost is already found/visited
    visited = [False] * n
    visited[source] = True
 
    # Stores predecessor of a vertex (to a print path)
    previous = [-1] * n
 
    # Run till min-heap is empty
    while priority_queue:

        # Remove and return the best vertex
        tempNode = heappop(priority_queue)  
        u = tempNode.vertex         
 
        # Do for each neighbor `v` of `u`
        for (v, weight) in graph[u]:
            if not visited[v] and (dist[u] + weight) < dist[v]:       
                dist[v] = dist[u] + weight
                previous[v] = u
                heappush(priority_queue, Node(v, dist[v]))
 
        # Mark vertex `u` as visited so it will not get picked up again
        visited[u] = True
 
    path = []
    for i in range(n):
        if i != source and dist[i] != INF:
            derivePath(previous, i, path)
            l = len(path)
            for i in range (l):
                if i != 0 and i != (l-1):
                    freq[path[i]] = freq[path[i]] + 1
            # print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {path}')
            path.clear()

# To calculate BC using concurrent Djikstra's Algorithms
def betweenness_centrality(graph, n):
    bc_dict = {}
    freq = [0] * n

    for source in range(n):
        Djikstra(graph, source, n, freq)

    for i in range (n):
        bc_dict[i] = freq[i]/((n-1)*(n-2))

    return bc_dict
	    
# Create the graph for which we compute the centrality measures    
# Adjacency Matrix with weights [Directed Graphs]
# INITIALISATION
graph = []
for i in range (V):
    temp = []
    graph.append(temp)

# ADD EDGES
AddEdge(graph, 0, 1, 1)
AddEdge(graph, 0, 2, 1)
AddEdge(graph, 0, 3, 2)
AddEdge(graph, 0, 4, 1)

AddEdge(graph, 1, 0, 1)
AddEdge(graph, 2, 0, 1)
AddEdge(graph, 3, 0, 1)
AddEdge(graph, 4, 0, 1)

print(betweenness_centrality(graph, V))

            