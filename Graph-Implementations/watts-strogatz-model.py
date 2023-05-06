from collections import defaultdict
import random

graph = defaultdict(list)

# To create the initial ring graph
def makeInitialGraph(graph, N, K): 
    nodes = []
    for i in range (N):
        nodes.append(i)
    makeLattice(graph, nodes, N, K//2)

# Form ring lattice 
def makeLattice(graph, nodes, N, halfOfK):
    for i, u in enumerate(nodes):
        for j in range(i+1, i+halfOfK+1):
            v = nodes[j % N]
            if v not in graph[u]:
                graph[u].append(v)
            if u not in graph[v]:
                graph[v].append(u)
            
# To calculate the probability (preferential attachment) of a Node
def rewireGraph(graph, edgeProbList, weightsTuple, N, P):
    nodesList = []
    nodeWeights = ()
    for i in range(N):
        nodesList.append(i)
        nodeWeights = nodeWeights + (1, )

    for node in graph:
        for neighbour in graph[node]:
            randomProb = random.choices(edgeProbList, weights = weightsTuple, k = 1)
            if randomProb[0] < P:
                w = node
                while ((w == node) or (w in graph[node])): 
                    temp = random.choices(nodesList, weights = nodeWeights, k = 1)
                    w = temp[0]
                graph[node].remove(neighbour)
                graph[neighbour].remove(node)
                graph[node].append(w)
                graph[w].append(node)

print("\nWelcome to Watts-Strogatz (WS) model simulation!\n\n")

# Take input N and K to form initial ring graph of N nodes joining its' K nearest neighbours
N = int(input("\nPlease type in the initial number of nodes[N]: "))
K = int(input("\nPlease type in the value of parameter K [K<=N]: "))
P = int(input("\nPlease type in the value of the fixed probability P [0<=P<=100]: "))

print("\n")
print("Creating initial ring graph...")

makeInitialGraph(graph, N, K)

# Print the ring graph
print(graph)

edgeProbList = []
weightsTuple = ()
for i in range(101):
    edgeProbList.append(i)
    weightsTuple = weightsTuple + (1,)

print("\n Rewiring graph...\n")

rewireGraph(graph, edgeProbList, weightsTuple, N, P)

# Print the rewired graph
print(graph)

