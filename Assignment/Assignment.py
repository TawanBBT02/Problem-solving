# นาย วรานนท์ ใจตรง 6706025510433
# นาย วัชรากร ชูศรียิ่ง 6706022510051

from fileinput import filename
import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    locations = {
        #zone 1.
        "Modern One Dorm": (-3, 5), "Thipai Dorm": (-4, 4.5), "Baan Kasem Dorm": (-5, 4), "Baan Puen Apartment": (-2.7, 3.7),
        #zone 2.
        "The Brick Place": (1.4, 2.9), "Khao Yai Modern Place": (3.9, 2.8),"Gray Dorm": (2.8, 3.4),
        "White Lion Dorm": (3.6, 3.7), "Wannaporn Dorm": (2, 4),"Saengtawan Dorm": (0.6, 4),
        #zone 3.
        "Wanasaya Grand": (-3.5, 1.4),"Baan Nicha Prachinburi": (-2.5, 1.1),"Mee Suk House": (-2.5, 1.7), 
        "Baan Thanomkhwan": (-1.5, 1.3),"Mangkornthong Mansion": (-0.8, 2),
        #zone 4.
        "Waramon Grand Place": (0.8, 1.5),
        #zone 5.
        "Chanchao Mansion": (3.5, 0.5), "Saowalak Dorm": (-1.6, 0.5), "Buakhao Dorm": (-0.1, 0.5), "Chamnongjit Dorm": (2, 0.5),
        #zone 6.
        "KMUTNB Male Dorm": (-2.9, 2.1),"KMUTNB Female Dorm": (-3.5, 2.6),"University": (-1.6, 3)
    }
    
    edges = [
        #zone 1.
        ("University", "Modern One Dorm", 1.4),
        ("University", "Baan Puen Apartment", 1),
        ("Baan Puen Apartment", "Baan Kasem Dorm", 0.4),
        ("Baan Puen Apartment", "Thipai Dorm", 0.3),
        ("Modern One Dorm", "Thipai Dorm", 0.45),
        ("Thipai Dorm", "Baan Kasem Dorm", 0.45),
        #zone 2.
        ("University", "The Brick Place", 0.7),
        ("University", "Saengtawan Dorm", 0.4),
        ("Saengtawan Dorm","Wannaporn Dorm", 0.05),
        ("Wannaporn Dorm","Gray Dorm", 0.13),
        ("Wannaporn Dorm","White Lion Dorm", 0.13),
        ("Gray Dorm","White Lion Dorm", 0.013),
        ("Khao Yai Modern Place", "White Lion Dorm", 0.12),
        ("Khao Yai Modern Place","Gray Dorm", 0.12),
        ("Khao Yai Modern Place","The Brick Place", 0.25),
        #zone 3.
        ("University", "Mangkornthong Mansion", 0.95),
        ("Mangkornthong Mansion", "Baan Thanomkhwan", 0.18),
        ("Baan Thanomkhwan", "Mee Suk House", 0.11),
        ("Baan Thanomkhwan", "Baan Nicha Prachinburi", 0.11),
        ("Mee Suk House", "Baan Nicha Prachinburi", 0),
        ("Wanasaya Grand","Mee Suk House", 0.2),
        ("Wanasaya Grand", "Baan Nicha Prachinburi", 0.2),
        #zone 4.
        ("Waramon Grand Place", "Mangkornthong Mansion", 0.65),
        ("Waramon Grand Place", "Chamnongjit Dorm", 1.1),
        ("Waramon Grand Place", "Buakhao Dorm", 1.1),
        #zone 5.
        ("Buakhao Dorm", "Chamnongjit Dorm", 0.45),
        ("Buakhao Dorm", "Saowalak Dorm", 0.13),
        ("Chamnongjit Dorm", "Chanchao Mansion", 0.26),
        #zone 6.
        ("University", "KMUTNB Male Dorm", 0),
        ("University", "KMUTNB Female Dorm", 0),        
    ]
    for location, pos in locations.items():
        G.add_node(location, pos=pos)
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
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

def find_shortest_path(G, start, end):
    try:
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        distance = nx.shortest_path_length(G, source=start, target=end, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None

def insert_node(G, locations, name, pos, locate_add_edge, distance):
    if name in locations:
        print("Node already exists.")
        return
    locations[name] = pos
    G.add_node(name, pos=pos)
    G.add_edge(name, locate_add_edge, weight=distance)
    print(f"Location {name} inserted successfully.")

def delete_node(G, locations, name):
    if name not in locations:
        print("Node does not exist.")
        return
    del locations[name]
    G.remove_node(name)
    print(f"Location {name} deleted successfully.")
def save_graph(G, locations, filename):
    data = {
        "locations": locations,
        "edges": [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    }
    with open(filename, 'w') as file:
        file.write(str(data))
    print(f"Graph saved to {filename}")

def load_graph(filename):
    with open(filename, 'r') as file:
        data = eval(file.read())
    
    G = nx.Graph()
    locations = data["locations"]
    edges = data["edges"]
    for location, pos in locations.items():
        G.add_node(location, pos=pos)     
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
    print(f"Graph loaded from {filename}")
    return G, locations


if __name__ == "__main__":
    G, locations = create_graph()
    
    print("Shortest route search system\n1.Show Graph\n2.Find Shortest Path\n3.Insert Location\n4.Delete Location\n5.Save Graph\n6.Load Graph\n0.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        draw_graph(G, locations)
        
    elif choice == 2:
        print("Available Locations:")
        for idx, loc in enumerate(locations.keys(), 1):
            print(f"{idx}. {loc}")
        
        location_start = int(input("Select location start: "))
        location_list = list(locations.keys())
        selected_location_start = location_list[location_start - 1]

        location_end = int(input("Select location end: "))
        selected_location_end = location_list[location_end - 1]

        if selected_location_start and selected_location_end in locations:
            path, distance = find_shortest_path(G, selected_location_start, selected_location_end)
            if path:
                print(f"Shortest path to {selected_location_end}:")
                print(" -> ".join(path))
                print(f"Total distance: {format(distance,'.2f')} km")
                draw_graph(G, locations, path)
            else:
                print("No path found.")
        else:
            print("Invalid location selection.")
            
    elif choice == 3:
        name = input("Enter location name: ")
        pos = tuple(map(float, input("Enter location position (x, y): ").split(", ")))
        print("Available Locations:")
        for idx, loc in enumerate(locations.keys(), 1):
            print(f"{idx}. {loc}")
        
        location = int(input("Select location to insert distance : "))
        location_list = list(locations.keys())
        selected_location = location_list[location - 1]
        distance = float(input("Enter distance to selected location: "))
        insert_node(G, locations, name, pos, selected_location, distance)
        draw_graph(G, locations)
        
    elif choice == 4:
        name = input("Enter location name to delete: ")
        delete_node(G, locations, name)
        draw_graph(G, locations)

    elif choice == 5:
        filename = input("Enter filename to save the graph: ")
        save_graph(G, locations, filename)

    elif choice == 6:
        filename = input("Enter filename to load the graph: ")
        load_graph(filename)
        draw_graph(G, locations)

    elif choice == 0:
        exit()
    
