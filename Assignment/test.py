# นาย วรานนท์ ใจตรง 6706025510433
# นาย วัชรากร ชูศรียิ่ง 6706022510051

import networkx as nx
import matplotlib.pyplot as plt

filename = "Data_Graph"

def create_graph(): 
    G = nx.Graph()
    locations = {}
    edges = []
    G, locations, edges = load_graph(filename,G, locations, edges)
    return G, locations, edges

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
    save_graph(filename,G, locations)
    print(f"Location {name} inserted successfully.")

def delete_node(G, locations, name):
    if name not in locations:
        print("Node does not exist.")
        return
    del locations[name]
    G.remove_node(name)
    save_graph(filename,G, locations)
    print(f"Location {name} deleted successfully.")

def save_graph(filename,G, locations):
    data = {
        "locations": locations,
        "edges": [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    }
    with open(filename, 'w') as file:
        file.write(str(data))
    print(f"Graph saved to {filename}")

def load_graph(filename, G, locations, edges):
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
    return G, locations, edges

if __name__ == "__main__":
    G, locations, edges = create_graph()
    
    print("Shortest route search system\n1.Show Graph\n2.Find Shortest Path\n3.Insert Location\n4.Delete Location\n5.Save Graph\n0.Exit")
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
        save_graph(filename,G, locations)

    elif choice == 0:
        exit()
    