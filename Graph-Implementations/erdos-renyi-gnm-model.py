from collections import defaultdict
import random

graph = defaultdict(list)
  
# To create a random graph according to the ER-GNM model
def makeGraph(graph, nodesList, nodeWeights, N, M):
    AdjMatrix = []
    for i in range (N):
        temp = []
        for j in range(N):
            temp.append(0)
        AdjMatrix.append(temp)

    count = 0

    while count < M:
        row = 0
        column = 0
        while (AdjMatrix[row][column] == 1 or AdjMatrix[row][column] == 1 or row == column):
            randomProb = random.choices(nodesList, weights = nodeWeights, k = 2)
            row = randomProb[0]
            column = randomProb[1]

        AdjMatrix[row][column] = 1
        AdjMatrix[column][row] = 1
        
        graph[row].append(column)
        graph[column].append(row)

        count = count + 1
        
print("\nWelcome to Erdős-Rényi (ER) model: G(N, M) simulation!\n\n")

# Take input N and M to generate a random graph of N nodes and M edges with the probability of each type of such graph equal
N = int(input("\nPlease type in the number of nodes[N]: "))
M = int(input("\nPlease type in the number of edges[M]: "))

nodesList = []
nodeWeights = ()
for i in range(N):
    nodesList.append(i)
    nodeWeights = nodeWeights + (1, )

print("\n")
print("Creating the random graph...")

makeGraph(graph, nodesList, nodeWeights, N, M)

# Print the ring graph
print(graph)