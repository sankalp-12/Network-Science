from collections import defaultdict

graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)

# To calculate number of vertices
def numberOfVertices(graph):
    n = 0
    for node in graph:
        n = n + 1
    return n

# TO calulate DC
def degree_centrality(graph, n):
    dc_dict = {}
    for node in graph:
        d = 0
        for neighbour in graph[node]:
            d = d + 1
        dc_dict[node] = d/n
    return dc_dict
	    
# Create the undirected graph for which we compute the centrality measures    
addEdge(graph,'a','b')
addEdge(graph,'a','c')
addEdge(graph,'a','d')
addEdge(graph,'a','e')
addEdge(graph,'a','f')
addEdge(graph,'a','g')
addEdge(graph,'a','h')
addEdge(graph,'a','i')
addEdge(graph,'a','j')
addEdge(graph,'a','k')

print(degree_centrality(graph, numberOfVertices(graph)-1))
