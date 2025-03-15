import networkx as nx
import matplotlib.pyplot as plt

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
    
    distances = {
        "Modern One Dorm": 1.5, "Thipai Dorm": 1.3, "Baan Kasem Dorm": 1.4, "Baan Puen Apartment": 1.0,
        "Chanchao Mansion": 2.5, "Saowalak Dorm": 2.5, "Buakhao Dorm": 2.4, "Chamnongjit Dorm": 2.4,
        "Waramon Grand Place": 1.6, "Wanasaya Grand": 1.4, "Baan Khun Yai Serm Dorm": 1.4,
        "Baan Nicha Prachinburi": 1.2, "Sommee Threep House": 1.2, "Baan Thanomkhwan": 1.1,
        "Mangkornthong Mansion": 0.95, "The Brick Place": 0.7, "Khao Yai Modern Place": 0.7,
        "Gray Dorm": 0.6, "White Lion Dorm": 0.55, "Wannaporn Dorm": 0.45,
        "Saengtawan Dorm": 0.4, "Baan Khun Yai Apartment": 0.4, "KMUTNB Male Dorm": 0,
        "KMUTNB Female Dorm": 0
    }
    
    for location, pos in locations.items():
        G.add_node(location, pos=pos)
    
    for location, distance in distances.items():
        G.add_edge(location, "University", weight=distance)
    
    return G, locations

def draw_graph(G, locations, shortest_path=None):
    pos = nx.get_node_attributes(G, 'pos')
    
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

if __name__ == "__main__":
    G, locations = create_graph()
    
    print("Available dorms:")
    for loc in locations.keys():
        print(loc)
    
    action = input("Enter 'search' to find a path, 'insert' to add a dorm, or 'delete' to remove a dorm: ")
    
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
    else:
        print("Invalid action.")
