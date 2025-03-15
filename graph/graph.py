from matplotlib.font_manager import weight_dict
import networkx as nx
import matplotlib.pyplot as plt
network = nx.Graph()
network.add_nodes_from([1,2,3,4,5,6,7])
color_list = ['gold','red','violet','pink','brown','yellow','gray']
plt.figure(figsize=(6,6))
plt.title("Example of Graoh Representation",size=10)
network.add_edge(6,7,weight= 2)
network.add_edge(6,5)
network.add_edge(5,3)
network.add_edge(7,3)
network.add_edge(3,1)
network.add_edge(5,1,weight= 4)
network.add_edge(1,4)
network.add_edge(1,2)
network.add_edge(4,2)

print(f"This network has now {network.number_of_nodes()} nodes.")

nx.draw_networkx(network,node_color = color_list, with_labels=True)
plt.show()