import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (>3): "))

if n <= 3:
    print("Enter value greater than 3")
else:
    G = nx.complete_graph(n)
    nx.draw(G, with_labels=True)
    plt.title("Complete Graph")
    plt.show()