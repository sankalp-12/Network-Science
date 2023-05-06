from collections import defaultdict
import random

graph = defaultdict(list)

# To create the initial graph
def addEdgeInitial(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# To add edges based on the node chosen through preferential attachment
def addEdge(graph, V, E, newNode):
    nodeRandomProb = calcNodeProb(graph, V, E)
    graph[newNode].append(nodeRandomProb)
    graph[nodeRandomProb[0]].append(newNode)

# To calculate degree of passed node 
def calcNodeDeg(graph, node):
    d = 0
    for neighbour in graph[node]:
        d = d + 1
    return d
	    
# To calculate the probability (preferential attachment) of a Node
def calcNodeProb(graph, V, E):
    nodesList = []
    nodesProbTuple = ()
    for node in graph:
        nodesList.append(node)
        nodeDeg = calcNodeDeg(graph, node)
        nodeProb = nodeDeg / (2 * E)
        nodesProbTuple = nodesProbTuple + (nodeProb,)
    
    nodeChosen = random.choices(nodesList, weights = nodesProbTuple, k = 1)
    return nodeChosen

print("\nWelcome to Barabási-Albert (BA) model simulation!\n\n")

# Start with a complete graph of 2 nodes i.e. an Edge
V = 2
E = 1
Vfinal = int(input("\nPlease type in the final number of nodes: "))
M = int(input("\nPlease type in the value of parameter m (m<=2 as initally there are 2 nodes): "))

print("\n")
print("Creating initial graph...")

addEdgeInitial(graph, 0, 1)

print("\nAdding nodes...")

count = 0
newNodes = Vfinal - 2

for f in range(newNodes):
    print("----------> Step {} <----------".format(count))
    node = V + count 
    print("Node added: {}".format(V + count))
    count += 1
    for e in range(0, M):
        addEdge(graph, node, E + e, node)
    E = E + M


print("\nFinal number of nodes ({}) reached".format(Vfinal))
print(graph)