# นาย กิตติสินธุ์ วรรณวณิชภักดี 6706025510247
# นาย นนทวัฒน์ ประสพรัตน์ 6706022510212
import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    
    parking_locations = {
        "Parking_B1-B4": (1, 8), "Parking_B5-B8": (1, 6), "Parking_B9-B12": (1, 4),
        "Parking_C1-C5": (6, 8), "Parking_A": (6, 4), "Parking_Motorcycle": (6, 2)
    }
    
    gate_locations = {
        "Gate_Top": (2, 7), "Gate_MK": (2, 6), "Gate_KFC": (2, 5), "Gate_PowerBy": (4, 3)
    }
    
    restaurant_locations = {
        "MK": (3, 6), "Santafe": (3, 5.5), "Yayoi": (3, 5), "Shabushi": (3, 4.5), "Oishi": (3, 4),
        "Tummua": (3, 3.5), "KFC": (3, 3), "Dairy Queen": (4, 5.5), "Mister Donut": (4, 5),
        "Swensen": (4, 4), "Pizza Company": (5, 5), "Potato Corner": (5, 4), "Annie Ann": (5, 3)
    }
    
    locations = {**parking_locations, **gate_locations, **restaurant_locations}
    
    colors = {
        **{key: "blue" for key in parking_locations},
        **{key: "gray" for key in gate_locations},
        **{
            "MK": "red", "Santafe": "brown", "Yayoi": "magenta", "Shabushi": "darkred", "Oishi": "orangered",
            "Tummua": "black", "KFC": "gray", "Dairy Queen": "darkblue", "Mister Donut": "purple",
            "Swensen": "orange", "Pizza Company": "green", "Potato Corner": "lightgreen", "Annie Ann": "lightblue"
        }
    }
    
    for location, pos in locations.items():
        G.add_node(location, pos=pos, color=colors[location])
    
    edges = [
        ("Parking_B1-B4", "Gate_Top", 2), ("Parking_B5-B8", "Gate_MK", 2),
        ("Parking_B9-B12", "Gate_KFC", 2), ("Parking_C1-C5", "Gate_Top", 3),
        ("Parking_A", "Gate_PowerBy", 3), ("Parking_Motorcycle", "Gate_PowerBy", 1),
        ("Gate_Top", "MK", 1), ("Gate_MK", "MK", 1), ("Gate_MK", "Santafe", 1),
        ("Gate_KFC", "KFC", 1), ("Gate_PowerBy", "Annie Ann", 2),
        ("MK", "Dairy Queen", 2), ("MK", "Mister Donut", 2), ("MK", "Pizza Company", 3),
        ("Santafe", "Dairy Queen", 2), ("Yayoi", "Mister Donut", 2),
        ("Mister Donut", "Swensen", 2), ("Mister Donut", "Dairy Queen", 2),
        ("Swensen", "Pizza Company", 2), ("Swensen", "Potato Corner", 2),
        ("Potato Corner", "Annie Ann", 2), ("Tummua", "Swensen", 2),
        
        # เพิ่มเส้นทางที่ระบุ
        ("MK", "Santafe", 1),  # MK ไป Santafe
        ("Santafe", "Yayoi", 1),  # Santafe ไป Yayoi
        ("Yayoi", "Shabushi", 1),  # Yayoi ไป Shabushi
        ("Shabushi", "Oishi", 1),  # Shabushi ไป Oishi
        ("Oishi", "Tummua", 1),  # Oishi ไป Tummua
        ("Tummua", "KFC", 1)  # Tummua ไป KFC
    ]
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    return G, parking_locations, gate_locations, restaurant_locations, colors

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
        total_distance = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
        return path, total_distance
    except nx.NetworkXNoPath:
        print("No path found.")
        return None, None

if __name__ == "__main__":
    G, parking_locations, gate_locations, restaurant_locations, colors = create_graph()
    
    print("Available Parking Locations:")
    for idx, loc in enumerate(parking_locations.keys(), 1):
        print(f"{idx}. {loc}")
    
    parking_choice = int(input("Select parking number: "))
    parking_list = list(parking_locations.keys())
    start = parking_list[parking_choice - 1]
    
    print("Available Restaurants:")
    for idx, loc in enumerate(restaurant_locations.keys(), 1):
        print(f"{idx}. {loc}")
    
    restaurant_choice = int(input("Select restaurant number: "))
    restaurant_list = list(restaurant_locations.keys())
    end = restaurant_list[restaurant_choice - 1]
    
    if start in parking_locations and end in restaurant_locations:
        path, total_distance = find_shortest_path(G, start, end)
        if path:
            print("Shortest path:", " -> ".join(path))
            print(f"Total distance: {total_distance} units")
            draw_graph(G, {**parking_locations, **gate_locations, **restaurant_locations}, colors, path)
    else:
        print("Invalid input. Please check the location names.")