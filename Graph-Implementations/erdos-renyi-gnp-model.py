from collections import defaultdict
import random

graph = defaultdict(list)
  
# To create a random graph according to the ER-GNP model
def makeGraph(graph, edgeProbList, weightsTuple, N, P):
    nodesList = []
    for i in range(N):
        nodesList.append(i)

    for node in nodesList:
        for neighbour in nodesList:
            randomProb = random.choices(edgeProbList, weights = weightsTuple, k = 1)
            if randomProb[0] < P:
                if ((node != neighbour) and (neighbour not in graph[node]) and (node not in graph[neighbour])):
                    graph[node].append(neighbour)
                    graph[neighbour].append(node)

print("\nWelcome to Erdős-Rényi (ER) model: G(N, P) simulation!\n\n")

# Take input N and P to generate a random graph of N nodes with independent probability of each edge existing as P
N = int(input("\nPlease type in the number of nodes[N]: "))
P = int(input("\nPlease type in the value of the fixed probability P [0<=P<=100]: "))

edgeProbList = []
weightsTuple = ()
for i in range(101):
    edgeProbList.append(i)
    weightsTuple = weightsTuple + (1,)

print("\n")
print("Creating the random graph...")

makeGraph(graph, edgeProbList, weightsTuple, N, P)

# Print the ring graph
print(graph)