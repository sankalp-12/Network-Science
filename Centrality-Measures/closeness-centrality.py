# To define no edge exists
INF = 999999999

# Number of vertices 
V = 5

# To add edges in the graph
def AddEdge(graph, source, destination, weight):
    graph[source][destination] = weight

# To calculate CC using Floyd-Warshall Algorithm
def closeness_centrality(graph, n):
    cc_dict = {}
    
    for k in range (0, n):
        for i in range (0, n):
            for j in range (0, n):
                if (graph[i][k] + graph[k][j] < graph[i][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]

    for i in range (0, n):
        temp_sum = 0
        for j in range (0, n):
            if graph[i][j] != INF:
                temp_sum = temp_sum + graph[i][j]
        cc_dict[i] = (n-1)/temp_sum

    return cc_dict
	    
# Create the graph for which we compute the centrality measures    
# Adjacency Matrix with weights [Directed Graphs]
# INITIALISATION
graph = []
for i in range (V):
    temp = []
    for j in range (V):
        if (i == j):
            temp.append(0)
        else:
            temp.append(INF)
    graph.append(temp)

# ADD EDGES
AddEdge(graph, 0, 1, 1)
AddEdge(graph, 0, 2, 1)
AddEdge(graph, 0, 3, 2)
AddEdge(graph, 0, 4, 2)

AddEdge(graph, 1, 0, 1)
AddEdge(graph, 1, 2, 1)
AddEdge(graph, 1, 3, 1)
AddEdge(graph, 1, 4, 1)

AddEdge(graph, 2, 0, 1)
AddEdge(graph, 2, 1, 1)
AddEdge(graph, 2, 3, 2)
AddEdge(graph, 2, 4, 2)

AddEdge(graph, 3, 0, 2)
AddEdge(graph, 3, 1, 1)
AddEdge(graph, 3, 2, 2)
AddEdge(graph, 3, 4, 2)

AddEdge(graph, 4, 0, 2)
AddEdge(graph, 4, 1, 1)
AddEdge(graph, 4, 2, 2)
AddEdge(graph, 4, 3, 2)


print(closeness_centrality(graph, V))

            