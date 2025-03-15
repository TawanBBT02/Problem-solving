# นาย วรานนท์ ใจตรง 6706025510433
# นาย วัชรากร ชูศรียิ่ง 6706022510051

import networkx as nx
import matplotlib.pyplot as plt
import json

def create_graph():
    G = nx.Graph()
    
    locations = {
        "Modern One Dorm": (-4, 3), "Thipai Dorm": (-3, 4), "Baan Kasem Dorm": (-3, 2), "Baan Puen Apartment": (-2, 3),
        "Chanchao Mansion": (-5, 5), "Saowalak Dorm": (-5, 3), "Buakhao Dorm": (-5, 1), "Chamnongjit Dorm": (-4, 0),
        "Waramon Grand Place": (-2, 5), "Wanasaya Grand": (-2, 1), "Baan Khun Yai Serm Dorm": (-1, 2),
        "Baan Nicha Prachinburi": (1, 5), "Sommee Threep House": (1, 1), "Baan Thanomkhwan": (2, 2),
        "Mangkornthong Mansion": (3, 5), "The Brick Place": (3, 3), "Khao Yai Modern Place": (3, 1),
        "Gray Dorm": (4, 4), "White Lion Dorm": (4, 2), "Wannaporn Dorm": (5, 5),
        "Saengtawan Dorm": (5, 3), "Baan Khun Yai Apartment": (5, 1), "KMUTNB Male Dorm": (6, 4), "KMUTNB Female Dorm": (6, 2),
        "University": (0, 3)
    }
    
    edges = [
        ("University", "Modern One Dorm", 1.5),
        ("University", "Thipai Dorm", 1.3),
        ("University", "Baan Kasem Dorm", 1.4),
        ("University", "Baan Puen Apartment", 1.0),
        ("University", "Chanchao Mansion", 2.5),
        ("University", "Saowalak Dorm", 2.5),
        ("University", "Buakhao Dorm", 2.4),
        ("University", "Chamnongjit Dorm", 2.4),
        ("University", "Waramon Grand Place", 1.6),
        ("University", "Wanasaya Grand", 1.4),
        ("University", "Baan Khun Yai Serm Dorm", 1.4),
        ("University", "Baan Nicha Prachinburi", 1.2),
        ("University", "Sommee Threep House", 1.2),
        ("University", "Baan Thanomkhwan", 1.1),
        ("University", "Mangkornthong Mansion", 0.95),
        ("University", "The Brick Place", 0.7),
        ("University", "Khao Yai Modern Place", 0.7),
        ("University", "Gray Dorm", 0.6),
        ("University", "White Lion Dorm", 0.55),
        ("University", "Wannaporn Dorm", 0.45),
        ("University", "Saengtawan Dorm", 0.4),
        ("University", "Baan Khun Yai Apartment", 0.4),
        ("University", "KMUTNB Male Dorm", 0),
        ("University", "KMUTNB Female Dorm", 0),
        ("Modern One Dorm", "Thipai Dorm", 1.3),
        ("Thipai Dorm", "Baan Kasem Dorm", 1.3),
        ("Baan Kasem Dorm", "Baan Puen Apartment", 1.4),
        ("Baan Puen Apartment", "Chanchao Mansion", 1.0),
        ("Chanchao Mansion", "Saowalak Dorm", 2.5),
        ("Saowalak Dorm", "Buakhao Dorm", 2.5),
        ("Buakhao Dorm", "Chamnongjit Dorm", 2.4),
        ("Chamnongjit Dorm", "Waramon Grand Place", 2.4),
        ("Waramon Grand Place", "Wanasaya Grand", 1.6),
        ("Wanasaya Grand", "Baan Khun Yai Serm Dorm", 1.4),
        ("Baan Khun Yai Serm Dorm", "Baan Nicha Prachinburi", 1.4),
        ("Baan Nicha Prachinburi", "Sommee Threep House", 1.2),
        ("Sommee Threep House", "Baan Thanomkhwan", 1.2),
        ("Baan Thanomkhwan", "Mangkornthong Mansion", 1.1),
        ("Mangkornthong Mansion", "The Brick Place", 0.95),
        ("The Brick Place", "Khao Yai Modern Place", 0.7),
        ("Khao Yai Modern Place", "Gray Dorm", 0.7),
        ("Gray Dorm", "White Lion Dorm", 0.6),
        
    ]
    
    for location, pos in locations.items():
        G.add_node(location, pos=pos)
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    return G, locations

def draw_graph(G, locations, shortest_path=None):
    pos = nx.spring_layout(G, seed=42)  # Use spring layout for better visualization
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", edge_color="gray", font_size=8)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color="red", width=3)
    
    plt.show()

def find_shortest_path(G, start):
    try:
        path = nx.shortest_path(G, source=start, target="University", weight='weight')
        return path
    except nx.NetworkXNoPath:
        print("No path found.")
        return None

def insert_node(G, locations, name, pos, distance):
    if name in locations:
        print("Node already exists.")
        return
    locations[name] = pos
    G.add_node(name, pos=pos)
    G.add_edge(name, "University", weight=distance)
    print(f"Node {name} added successfully.")

def delete_node(G, locations, name):
    if name not in locations:
        print("Node does not exist.")
        return
    G.remove_node(name)
    del locations[name]
    print(f"Node {name} deleted successfully.")

def save_graph(G, locations, filename):
    data = {
        "locations": locations,
        "edges": [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    }
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Graph saved to {filename}")

def load_graph(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    G = nx.Graph()
    locations = data["locations"]
    for location, pos in locations.items():
        G.add_node(location, pos=pos)
    
    for u, v, weight in data["edges"]:
        G.add_edge(u, v, weight=weight)
    
    print(f"Graph loaded from {filename}")
    return G, locations

if __name__ == "__main__":
    G, locations = create_graph()
    
    print("Available dorms:")
    for loc in locations.keys():
        print(loc)
    
    action = input("Enter 'search' to find a path, 'insert' to add a dorm, 'delete' to remove a dorm, 'save' to save the graph, or 'load' to load a graph: ")
    
    if action == "search":
        start = input("Enter dorm name: ")
        if start in locations:
            path = find_shortest_path(G, start)
            if path:
                print("Shortest path:", " -> ".join(path))
                draw_graph(G, locations, path)
        else:
            print("Invalid input. Please check the dorm name.")
    elif action == "insert":
        name = input("Enter new dorm name: ")
        x = float(input("Enter x position: "))
        y = float(input("Enter y position: "))
        distance = float(input("Enter distance to University: "))
        insert_node(G, locations, name, (x, y), distance)
        draw_graph(G, locations)
    elif action == "delete":
        name = input("Enter dorm name to delete: ")
        delete_node(G, locations, name)
        draw_graph(G, locations)
    elif action == "save":
        filename = input("Enter filename to save the graph: ")
        save_graph(G, locations, filename)
    elif action == "load":
        filename = input("Enter filename to load the graph: ")
        G, locations = load_graph(filename)
        draw_graph(G, locations)
    elif action == "show":
        draw_graph(G, locations)
    else:
        print("Invalid action.")
