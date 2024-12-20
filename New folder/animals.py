import struct

animal_struct_format = 'i20s10s10si20s10sf'
record_size = struct.calcsize(animal_struct_format)

def add_animal(file_path, animal):#Completed
    with open(file_path, 'ab') as f:
        f.write(struct.pack(animal_struct_format, *animal))

def display_animals(file_path):#80% (เรียงบรรทัดข้อมูล) 
    with open(file_path, 'rb') as f:
        print("ID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value ")
        while True:
            data = f.read(record_size)
            if not data:
                break
            
            animal = struct.unpack(animal_struct_format, data)
            animal = (animal[0],animal[1].decode().strip("\x00"),animal[2].decode().strip("\x00"),animal[3].decode().strip("\x00"),animal[4],
                      animal[5].decode().strip("\x00"),animal[6].decode().strip("\x00"),animal[7])
            print(animal[0]," "*(4 - len(str(animal[0]))),animal[1]," " * (16 - len(animal[1])),animal[2]," " * (8 - len(animal[2])),animal[3]," " * (10 - len(animal[3])),
                    animal[4]," " * (8 - len(str(animal[4]))),animal[5]," " * (10 - len(animal[5])),animal[6]," " * (11 - len(animal[6])),format(animal[7],".2f"),"฿")
           
def get_animal_by_category(file_path, category,category_value):
    with open(file_path, 'rb') as f:
        print("\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value ")
        while True:
            data = f.read(record_size)
            if not data:
                break
            animal = struct.unpack(animal_struct_format, data)
            animal = (animal[0],animal[1].decode().strip("\x00"),animal[2].decode().strip("\x00"),animal[3].decode().strip("\x00"),animal[4],animal[5].decode().strip("\x00"),animal[6].decode().strip("\x00"),animal[7])
            category.lower().replace(" ","")
            if category == "id":
                if animal[0] == category_value:
                    print(animal[0]," "*(4 - len(str(animal[0]))),animal[1]," " * (16 - len(animal[1])),animal[2]," " * (8 - len(animal[2])),animal[3]," " * (10 - len(animal[3])),animal[4]," " * (8 - len(str(animal[4]))),animal[5]," " * (10 - len(animal[5])),animal[6]," " * (11 - len(animal[6])),format(animal[7],".2f"),"฿")

            elif category == "category":
                if animal[1] == category_value:
                    print(animal[0]," "*(4 - len(str(animal[0]))),animal[1]," " * (16 - len(animal[1])),animal[2]," " * (8 - len(animal[2])),animal[3]," " * (10 - len(animal[3])),animal[4]," " * (8 - len(str(animal[4]))),animal[5]," " * (10 - len(animal[5])),animal[6]," " * (11 - len(animal[6])),format(animal[7],".2f"),"฿")

            elif category == "species":
                if animal[2] == category_value.capitalize()or category_value:
                    print(animal[0]," "*(4 - len(str(animal[0]))),animal[1]," " * (16 - len(animal[1])),animal[2]," " * (8 - len(animal[2])),animal[3]," " * (10 - len(animal[3])),animal[4]," " * (8 - len(str(animal[4]))),animal[5]," " * (10 - len(animal[5])),animal[6]," " * (11 - len(animal[6])),format(animal[7],".2f"),"฿")
                    
            elif category == "foodtype":
                if animal[6] == category_value:
                    print(animal[0]," "*(4 - len(str(animal[0]))),animal[1]," " * (16 - len(animal[1])),animal[2]," " * (8 - len(animal[2])),animal[3]," " * (10 - len(animal[3])),animal[4]," " * (8 - len(str(animal[4]))),animal[5]," " * (10 - len(animal[5])),animal[6]," " * (11 - len(animal[6])),format(animal[7],".2f"),"฿")
            else:
                print("No Values!!")
                break
        return ""
            
def update_animal(file_path, record_id, column, new_animal):
    animals = []
    cc = column - 1
    
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(record_size)
            if not data:
                break
            animal = struct.unpack(animal_struct_format, data)
            animal = (
                animal[0],
                animal[1].decode().strip("\x00"),
                animal[2].decode().strip("\x00"),
                animal[3].decode().strip("\x00"),
                animal[4],
                animal[5].decode().strip("\x00"),
                animal[6].decode().strip("\x00"),
                animal[7]
            )
            
            # อัปเดตข้อมูล
            if animal[0] == record_id:
                new_animal_tuple = list(animal)  # สร้างลิสต์จาก animal
                new_animal_tuple[cc] = new_animal  # แทนที่ค่า
                animals.append(tuple(new_animal_tuple))  # แปลงกลับเป็น tuple
            else:
                animals.append(animal)

    with open(file_path, 'wb') as f:
        for animal in animals:
            # แปลงค่าเป็น bytes ก่อนเขียนลงไฟล์
            animal_bytes = (
                animal[0], 
                animal[1].encode('utf-8').lower(), 
                animal[2].encode('utf-8').lower(), 
                animal[3].encode('utf-8').lower(), 
                animal[4], 
                animal[5].encode('utf-8').lower(), 
                animal[6].encode('utf-8').lower(), 
                animal[7]
            )
            f.write(struct.pack(animal_struct_format, *animal_bytes))

def delete_animal(file_path, record_id): #Completed // เพิ่มตัวเลือกการลบ
    animals = []
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(record_size)
            if not data:
                break
            animal = struct.unpack(animal_struct_format, data)
            if animal[0] != record_id:
                animals.append(animal)

    with open(file_path, 'wb') as f:
        for animal in animals:
            f.write(struct.pack(animal_struct_format, *animal))
            
    display_animals(file_path)
    print()
  
def generate_report(file_path): #90% (เรียงบรรทัด Reports)
    statistics = {
        'Mammals': 0,
        'Reptilia': 0,
        'Aquatic': 0,
        'Herbivore': 0,
        'Carnivore': 0,
        'Max Age': 0,
        'Min Age': float('inf'),
        'Earliest Birthdate': '31/12/9999',
        'Latest Birthdate': '01/01/1970',
        'Max Value': 0.0,
        'Min Value': float('inf')
    }

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(record_size)
            if not data:
                break
            animal = struct.unpack(animal_struct_format, data)
            # อัพเดตสถิติ
            age = animal[4]
            category = animal[2].decode('utf-8').strip()
            species = animal[6].decode('utf-8').strip()
            birthdate = animal[3].decode('utf-8').strip('\x00')
            value = animal[7]

            if "mammal" in category:
                statistics['Mammals'] += 1
            elif "reptilia" in category:
                statistics['Reptilia'] += 1
            elif "aquatic" in category:
                statistics['Aquatic'] += 1

            if 'herbivore' in species:
                statistics['Herbivore'] += 1
            elif 'carnivore' in species:
                statistics['Carnivore'] += 1

            statistics['Max Age'] = max(statistics['Max Age'], age)
            statistics['Min Age'] = min(statistics['Min Age'], age)
            
            current_max_value = float(statistics['Max Value']) if statistics['Max Value'] != '' else 0.0
            statistics['Max Value'] = format(max(current_max_value, value), '.2f')
            current_min_value = float(statistics['Min Value']) if statistics['Min Value'] != '' else float('inf')
            statistics['Min Value'] = format(min(current_min_value, value), '.2f')

            if birthdate < statistics['Earliest Birthdate']:
                statistics['Earliest Birthdate'] = birthdate
            if birthdate > statistics['Latest Birthdate']:
                statistics['Latest Birthdate'] = birthdate


    animals = []
    
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(record_size)
            if not data:
                break  # หากไม่มีข้อมูลให้หยุด
            animal = struct.unpack(animal_struct_format, data)
            
            # แปลงข้อมูลเป็นรูปแบบที่ต้องการ
            animal_data = (
                animal[0],                          # ID
                animal[1].decode('utf-8').strip('\x00'),  # ชื่อ
                animal[2].decode('utf-8').strip('\x00'),  # ประเภท
                animal[3].decode('utf-8').strip('\x00'),  # วันเกิด
                animal[4],                          # อายุ
                animal[5].decode('utf-8').strip('\x00'),  # ชื่อสัตว์
                animal[6].decode('utf-8').strip('\x00'),  # ประเภทอาหาร
                animal[7]                           # ค่า
            )
            animals.append(animal_data)           

    print(f"{'Category':<20} {'Value':<20}")
    print("="*40)
    for key, value in statistics.items():
        print(f"{key:<20} {value:<20}")
       
    with open("reports.txt", 'w') as f:
        # เขียนรายงานสถิติ
        f.write(f"{'Category':<20} {'Value':<20}\n")
        f.write("="*40 + "\n")
        for key, value in statistics.items():
            f.write(f"{key:<20} {value:<20}\n")
        f.write("="*40 + "\n")

        # เขียนข้อมูลสัตว์
        f.write("\nAll Animals\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        sum = 0.0
        for animal in animals:
            report_line = (
                f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                f"{format(animal[7], '.2f')}"
            )
            f.write(report_line + "\n")
            sum += animal[7]
        f.write("-"*100 + "\n")
        f.write(f"All Animals : {len(animals)}\n")
        f.write(f"Total Animals : {format(sum,".2f")}\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Mammals\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        count = 0
        sum = 0.0
        for animal in animals:
            if animal[2] == 'mammal':
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
                count += 1
                sum += animal[7]
        f.write("-"*100 + "\n")
        f.write(f"Total Mammal : {count}\n")
        f.write(f"Total Animals : {format(sum,".2f")}\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Reptilia\nAnimal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        count = 0
        for animal in animals:
            if animal[2] == 'reptilia':
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
                count+=1
        f.write("-"*100 + "\n")
        f.write(f"Total Reptilia : {count}\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Aquatic\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        count = 0
        for animal in animals:
            if animal[2] == 'aquatic':
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
                count += 1
        f.write("-"*100 + "\n")
        f.write(f"Total Aquatic : {count}\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Herbivore\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        count = 0
        for animal in animals:
            if animal[6] == 'herbivore':
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
                count += 1
        f.write("-"*100 + "\n")
        f.write(f"Total Herbivore : {count}\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Carnivore\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        count =0
        for animal in animals:
            if animal[6] == 'carnivore':
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
                count +=1
        f.write("-"*100 + "\n")
        f.write(f"Total Carnivore : {count}\n")
        f.write("-"*100 + "\n")
        
        f.write("\nCategory Max Age\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if animal[4] == statistics['Max Age']:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Min Age\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if animal[4] == statistics['Min Age']:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
        f.write("-"*100 + "\n")
        
        f.write("\nCategory Earliest Birthdate\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if animal[3] == statistics['Earliest Birthdate']:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")

        f.write("\nCategory Latest Birthdate\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if animal[3] == statistics['Latest Birthdate']:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
        f.write("-"*100 + "\n")
        
        f.write("\nCategory Max Value\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if format(animal[7],".2f") == statistics["Max Value"]:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
        f.write("-"*100 + "\n")

        f.write("\nCategory Min Value\nID | Animal Category | Species | Birthdate | Age |     Name     |  Food Type  | Value\n")
        f.write("="*100 + "\n")
        for animal in animals:
            if format(animal[7],".2f") == statistics["Min Value"]:
                report_line = (
                    f"{animal[0]}{' ' * (5 - len(str(animal[0])))}"
                    f"{animal[1].capitalize()}{' ' * (18 - len(animal[1]))}"
                    f"{animal[2].capitalize()}{' ' * (10 - len(animal[2]))}"
                    f"{animal[3]}{' ' * (12 - len(animal[3]))}"
                    f"{animal[4]}{' ' * (10 - len(str(animal[4])))}"
                    f"{animal[5].capitalize()}{' ' * (12 - len(animal[5]))}"
                    f"{animal[6].capitalize()}{' ' * (13 - len(animal[6]))}"
                    f"{format(animal[7], '.2f')}"
                )
                f.write(report_line + "\n")
        f.write("-"*100 + "\n")
    return ''

def show_id(file_path):
    with open(file_path, 'rb') as f:
                print("ID : ",end=" ")
                while True:
                    data = f.read(record_size)
                    if not data:
                        break
                    animal = struct.unpack(animal_struct_format, data)
                    print(animal[0],end=" ")
                print()

def check_no_id(file_path,record_id):
    with open(file_path, 'rb') as f:
                ani=[]
                while True:
                    data = f.read(record_size)
                    if not data:
                        break
                    animal = struct.unpack(animal_struct_format, data)
                    if animal[0] != record_id:
                        ani.append(animal[0])
                    else:
                        continue
    if ani != []:
        print("No data")
    
def id(file_path):
    with open(file_path, 'rb') as f:
                ani=[]
                while True:
                    data = f.read(record_size)
                    if not data:
                        break
                    animal = struct.unpack(animal_struct_format, data)
                    ani.append(animal[0])
    return ani

def menu(): #Completed
    print("Zoo Management System")
    print("1. Add Animal")
    print("2. Display All Animals")
    print("3. Get CATEGORY Animal")
    print("4. Update Animal")
    print("5. Delete Animal")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Choose an option: ")
    return choice

def main(): 
    file_path = "data_animal_project.bin"
    while True:
        choice = menu()
        invalid = "Your input is invalid! Try again!"
        if choice == '1':
            show_id(file_path)
            # เพิ่มข้อมูล
            try:
                record_id = int(input("Enter Record ID (Integers Only) : "))
                if record_id in id(file_path):
                    print("This ID is already exist! Try again!")
                    continue
            except ValueError:
                print(invalid)
                continue
            animal_category = input("Enter Animal Category: ").encode('utf-8').lower()
            species = input("Enter Species: ").encode('utf-8').lower()
            birthdate = input("Enter Birthdate (DD/MM/YYYY): ").encode('utf-8')
            try:
                age = int(input("Enter Age (Integers Only) : "))
            except ValueError:
                print(invalid)
                continue
            name = input("Enter Name: ").encode('utf-8').lower()
            food_types = input("Enter Food Types: ").encode('utf-8').lower()
            value = float(input("Enter Animal's Value (Floating Point numbers Only) : "))

            animal = (record_id, animal_category, species, birthdate, age, name, food_types,value)
            add_animal(file_path, animal)

        elif choice == '2':
            display_animals(file_path)

        elif choice == '3':
            print("ID , CATEGORY , SPECIES , FOOD TYPE")
            try:
                category = input("Enter Category : ").lower().replace(" ","")
            except ValueError:
                print(invalid)
                continue
            if category == "id":
                category_value = int(input(f"Enter Category {category.upper()} : "))
            elif category not in ['id','category','species','foodtype']:
                print("\nInvalid category. Please try again.\n")
                continue
            else:
                category_value = input(f"Enter Category {category.upper()} : ")

            animal = get_animal_by_category(file_path, category,category_value)
            print()

        elif choice == '4':
            show_id(file_path)

            try:
                record_id = int(input("Enter Record ID to Update: "))
                if record_id not in id(file_path):
                    print("This ID is not exist! Try again!")
                    continue
            except ValueError:
                print(invalid)
                continue

            print("\nID : 1 \nAnimal Category : 2 \nSpecies : 3 \nBirthdate : 4 \nAge : 5 \nName : 6 \nFood Type : 7 \nValue : 8")
            
            try:
                column = int(input("Enter Column to Update: "))
            except ValueError:
                print(invalid)
                continue
            if column in [1,5,8]:
                try:
                    new_animal = int(input("Enter Data to Update:"))
                except ValueError:
                    print(invalid)
                    continue
            else:
                new_animal = input("Enter Data to Update:")
            update_animal(file_path,record_id,column,new_animal)
            display_animals(file_path)
            print()
            # ดึงข้อมูลสัตว์ใหม่เพื่ออัปเดต
            # โค้ดเหมือนกับการเพิ่มข้อมูล
            # ...

        elif choice == '5':
            show_id(file_path)
            try:
                record_id = int(input("Enter Record ID to Delete: "))
                if record_id not in id(file_path):
                    print("\nThis ID is not exist! Try again!\n")
                    continue
            except ValueError:
                print(invalid)

            delete_animal(file_path, record_id)

        elif choice == '6':
            report = generate_report(file_path)
            print(report)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

main()
