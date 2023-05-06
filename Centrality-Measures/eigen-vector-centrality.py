import math

# Number of vertices 
V = 4

# To add edges in the graph
def AddEdge(graph, source, destination):
    graph[source][destination] = 1

# To calculate EVC
def eigen_vector_centrality(graph, vec, n, iter):
    cc_dict = {}
    
    while(iter):
        for i in range (V):
            temp_val = 0
            for j in range (V):
                temp_val = temp_val + (graph[i][j]*vec[i])
            vec[i] = temp_val

        normal = 0
        for i in range (V):
            normal = normal + (vec[i]*vec[i])
        normal = math.sqrt(normal)
        for i in range (V):
            vec[i] = vec[i]/normal
        
        iter = iter - 1

    for i in range (V):
        cc_dict[i] = vec[i]
    return cc_dict
	    
# Create the graph for which we compute the centrality measures    
# Adjacency Matrix with weights [Directed Graphs]
# INITIALISATION
graph = []
for i in range (V):
    temp = []
    for j in range (V):
        temp.append(0)
    graph.append(temp)

# ADD EDGES
AddEdge(graph, 0, 1)
AddEdge(graph, 1, 0)
AddEdge(graph, 1, 2)
AddEdge(graph, 2, 1)
AddEdge(graph, 2, 3)
AddEdge(graph, 3, 2)

# Number of Iterations
iter = 100

# Initial vector
vec = []
for i in range (0, V):
    vec.append(1/V)

print(eigen_vector_centrality(graph, vec, V, iter))