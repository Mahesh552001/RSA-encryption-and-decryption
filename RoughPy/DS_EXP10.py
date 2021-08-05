
def knapSack(W, wt, val, n):
    K = [[0 for i in range(W+1)]for j in range(n+1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K)
    return K[n][W]
 

wt = list(map(int,input("Give the various weights\n").split()))
val = list(map(int,input("Give the corresponding values\n").split()))
W = int(input("Give the sack weight\n"))
n = len(val)
print(knapSack(W, wt, val, n))


# =============================================================================
# import networkx as nx
# import matplotlib.pyplot as plt
# 
# G=nx.Graph()
# 
# G.add_node("a")
# G.add_nodes_from(["b","c"])
# 
# G.add_edge(1,2)
# edge = ("d", "e")
# G.add_edge(*edge)
# edge = ("a", "b")
# G.add_edge(*edge)
# 
# 
# 
# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
# 
# nx.draw(G)
# plt.show()
# =============================================================================
