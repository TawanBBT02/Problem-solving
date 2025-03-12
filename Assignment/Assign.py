# นาย กิตติสินธุ์ วรรณวณิชภักดี 6706025510247
# นาย นนทวัฒน์ ประสพรัตน์ 6706022510212
import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    
    locations = {
        "Parking_B1-B4": (1, 😎, "Parking_B5-B8": (1, 6), "Parking_B9-B12": (1, 4),
        "Parking_C1-C5": (6, 😎, "Parking_A": (6, 4), "Parking_Motorcycle": (6, 2),
        "Gate_Top": (2, 7), "Gate_MK": (2, 6), "Gate_KFC": (2, 5), "Gate_PowerBy": (4, 3),
        "MK": (3, 6), "Santafe": (3, 5.5), "Yayoi": (3, 5), "Shabushi": (3, 4.5), "Oishi": (3, 4),
        "Tummua": (3, 3.5), "KFC": (3, 3), "Dairy Queen": (4, 5.5), "Mister Donut": (4, 5),
        "Swensen": (4, 4), "Pizza Company": (5, 5), "Potato Corner": (5, 4), "Annie Ann": (5, 3)
    }
    
    colors = {
        "Parking_B1-B4": "blue", "Parking_B5-B8": "blue", "Parking_B9-B12": "blue",
        "Parking_C1-C5": "blue", "Parking_A": "blue", "Parking_Motorcycle": "blue",
        "Gate_Top": "blue", "Gate_MK": "blue", "Gate_KFC": "blue", "Gate_PowerBy": "blue",
        "MK": "red", "Santafe": "brown", "Yayoi": "magenta", "Shabushi": "darkred", "Oishi": "orangered",
        "Tummua": "black", "KFC": "gray", "Dairy Queen": "darkblue", "Mister Donut": "purple",
        "Swensen": "orange", "Pizza Company": "green", "Potato Corner": "lightgreen", "Annie Ann": "lightblue"
    }
    
    for location, pos in locations.items():
        G.add_node(location, pos=pos, color=colors[location])
    
    edges = [
        ("Parking_B1-B4", "Gate_Top", 2), ("Parking_B1-B4", "Gate_MK", 2),
        ("Parking_B5-B8", "Gate_MK", 2), ("Parking_B5-B8", "Gate_KFC", 2),
        ("Parking_B9-B12", "Gate_KFC", 2), ("Parking_C1-C5", "Gate_Top", 3),
        ("Parking_A", "Gate_PowerBy", 3), ("Parking_Motorcycle", "Gate_PowerBy", 1),
        ("Gate_Top", "MK", 1), ("Gate_MK", "MK", 1), ("Gate_MK", "Santafe", 1),
        ("Gate_MK", "Yayoi", 1), ("Gate_KFC", "Shabushi", 1), ("Gate_KFC", "Oishi", 1),
        ("Gate_KFC", "Tummua", 1), ("Gate_KFC", "KFC", 1),
        ("MK", "Dairy Queen", 2), ("MK", "Mister Donut", 2),
        ("Santafe", "Dairy Queen", 2), ("Yayoi", "Mister Donut", 2),
        ("Mister Donut", "Swensen", 2), ("Swensen", "Pizza Company", 2),
        ("Pizza Company", "Potato Corner", 2), ("Potato Corner", "Annie Ann", 2),
        ("Annie Ann", "Gate_PowerBy", 2)
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    return G, locations, colors

def draw_graph(G, locations, colors, shortest_path=None):
    pos = nx.get_node_attributes(G, 'pos')
    node_colors = [colors[node] for node in G.nodes()]
    
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors, edge_color="gray", font_size=8)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color="red", width=3)
    
    plt.show()

def find_shortest_path(G, start, end):
    try:
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        return path
    except nx.NetworkXNoPath:
        print("No path found.")
        return None

if __name__ == "__main__":
    G, locations, colors = create_graph()
    
    print("Available locations:")
    for loc in locations.keys():
        print(loc)
    
    start = input("Enter parking location or gate: ")
    end = input("Enter restaurant name: ")
    
    if start in locations and end in locations:
        path = find_shortest_path(G, start, end)
        if path:
            print("Shortest path:", " -> ".join(path))
            draw_graph(G, locations, colors, path)
    else:
        print("Invalid input. Please check the location names.")