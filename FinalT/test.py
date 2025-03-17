import matplotlib.pyplot as plt
import networkx as nx

# ฟังก์ชันสำหรับสร้างกราฟ
def create_graph(): # สร้างกราฟ
    G = nx.Graph() 
    # กำหนดโหนดและขอบของกราฟ
    node = [1,2,3,5,4,6,7,8,9,10] # โหนด
    edges = [(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(4,6),(4,7),(5,7),(5,8),(6,7),(6,9),(7,8),(7,9),(7,10),(8,10),(9,10)] # การเชื่อมกันของแต่ละโหนด
    colors = ['pink','red','green','blue','yellow','orange','purple','brown','silver','gray'] # สีของโหนด ต้องมีเท่ากับจำนวนโหนด

    # เพิ่มโหนด
    for i in node:
        G.add_node(i)
    # เพิ่มเส้นเชื่อมในกราฟ
    for u, v in edges:
        G.add_edge(u, v)
    return G, node, colors

# ฟังก์ชันสำหรับวาดกราฟ
def draw_graph(G, node, colors, shortest_path=None):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    # วาดกราฟด้วยสีและขนาดที่กำหนด
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color=colors, edge_color="gray", font_size=8)
    if shortest_path:
        # วาดเส้นทางที่สั้นที่สุดถ้ามี
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw(G, pos, edgelist=path_edges, edge_color="red", width=3)

    plt.show()

# ฟังก์ชันสำหรับหาทางที่สั้นที่สุด
def find_shortest_path(G, start, end):
    try:
        path = nx.shortest_path(G, source=start, target=end)
        distance = nx.shortest_path_length(G, source=start, target=end)
        return path, distance
    except nx.NetworkXNoPath:
        return None

# ฟังก์ชันสำหรับเพิ่มโหนด
def insert_node(G, node, colors, locate_add_edge):
    if name in node: # ตรวจโหนดมีอยู่แล้วหรือไม่
        print("Node already exists.")
        return
    
    node.append(name) # เพิ่มโหนด
    colors.append(color) # เพิ่มสีของโหนด
    G.add_node(name) # เพิ่มโหนดในกราฟ
    G.add_edge(name, locate_add_edge) # เพิ่มเส้นเชื่อมในกราฟ
    print(f"Location {name} inserted successfully.")

# ฟังก์ชันสำหรับลบโหนด
def delete_node(G, node, name):
    if name not in node: # ตรวจโหนดมีอยู่หรือไม่
        print("Node does not exist.")
        return
    
    G.remove_node(name) # ลบโหนดในกราฟ
    node.remove(name) # ลบโหนด
    colors.pop() # ลบสีของโหนด
    print(f"Location {name} deleted successfully.")

if __name__ == "__main__":
    G, node, colors = create_graph() 

    while True:  
        # แสดงเมนูให้ผู้ใช้เลือก
        menu = int(input("1. Show graph\n2. Find shortest path\n3. Insert\n4. Delete\n0. Exit\nPlease select a menu : ")) # รับค่าเมนู
        if menu == 1:
            draw_graph(G, node, colors) # แสดงกราฟ  
        elif menu == 2:
            start = int(input("Enter start Node : ")) # รับค่าโหนดเริ่มต้น
            end = int(input("Enter end Node : ")) # รับค่าโหนดปลายทาง
            shortest_path, distance = find_shortest_path(G, start, end) # หาทางที่สั้นที่สุด
            if shortest_path: # ถ้ามีทางที่สั้นที่สุด
                print(f"Shortest path: {shortest_path}") # แสดงทางที่สั้นที่สุด
                print(f"Distance: {distance}") # แสดงระยะทางที่สั้นที่สุด 
                draw_graph(G, node, colors, shortest_path) # วาดกราฟ
            else:
                print("No path found.")

        elif menu == 3:
            name = int(input("Enter name of the node : ")) # รับค่าชื่อของโหนด
            locate_add_edge = int(input("Enter location to add edge : ")) # รับค่าโหนดที่ต้องการเชื่อม
            color = input("Enter color of the node : ") # รับค่าสีของโหนด
            insert_node(G, node, colors, locate_add_edge) # เพิ่มโหนด

        elif menu == 4:
            name = int(input("Enter name of the node : "))  # รับค่าชื่อของโหนด
            delete_node(G, node, name) # ลบโหนด

        elif menu == 0:
            break # ออกจากโปรแกรม

        else:
            print("Invalid menu.")
