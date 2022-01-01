import networkx as nx
import matplotlib.pyplot as plt

def createGraph(pairs):
  graph  = nx.Graph()

  for pair in pairs:
    friend1, friend2 = pair
    graph.add_edge(friend1, friend2)
  
  nx.draw(graph, with_labels= True, node_color = 'lightblue', node_size = 8)
  plt.show

friendPairs = [['Alice','Bob'], ['Charlie', 'Alice'], ['Susan', 'Clark']]