#นายวรานนท์ ใจตรง 6706022510433
#นายวัชรากร ชูศรียิ่ง 6706022510051

# Dictionary สำหรับเก็บข้อมูลจังหวัดของแต่ละภาค
Thailand = {
    'northern': ['chiang mai', 'lamphun', 'lampang', 'uttaradit', 'phrae', 'nan', 'phayao', 'chiang rai', 'mae hong son'],
    'southern': ['chumphon', 'nakhon si thammarat', 'narathiwat', 'pattani', 'phatthalung', 'songkhla', 'surat thani',
                 'yala', 'krabi', 'phang nga', 'phuket', 'ranong', 'satun', 'trang'],
    'central': ['bangkok', 'nonthaburi', 'samut prakan', 'pathum thani', 'samut sakhon', 'nakhon pathom',
                'kamphaeng phet', 'chai nat', 'nakhon nayok', 'nakhon sawan', 'phra nakhon si ayutthaya', 'phichit',
                'phitsanulok', 'phetchabun', 'lop buri', 'samut songkhram', 'saraburi', 'sing buri', 'sukhothai', 'suphan buri',
                'ang thong', 'uthai thani'],
    'northeastern': ['kalasin', 'khon kaen', 'chaiyaphum', 'nakhon phanom', 'nakhon ratchasima', 'bueng kan', 'buri ram', 'maha sarakham',
                     'mukdahan', 'yasothon', 'roi et', 'loei', 'si sa ket', 'sakon nakhon', 'surin', 'nong khai', 'nong bua lam phu',
                     'amnat charoen', 'udon thani', 'ubon ratchathani'],
    'eastern': ['chanthaburi', 'chachoengsao', 'chonburi', 'trat', 'prachinburi', 'rayong', 'sakaeo'],
    'western': ['kanchanaburi', 'tak', 'prachuap khiri khan', 'phetchaburi', 'ratchaburi'],


}

# ฟังก์ชันเพิ่มข้อมูล
def insert_data():
    print(f"-"+"\n-".join(Thailand) + "\n")
    region = input("ป้อนชื่อภาค: ")
    province = input("ป้อนชื่อจังหวัด: ")
    if region in Thailand:
        Thailand[region].append(province)
    else:
        Thailand[region] = [province]
    print("เพิ่มข้อมูลเรียบร้อย!\n")

# ฟังก์ชันแก้ไขข้อมูล
def update_data():
    region = input("ป้อนชื่อภาคที่ต้องการแก้ไข: ")
    if region.lower() in Thailand:
        print(f"Provinces in {region.capitalize()}:\n  - " + "\n  - ".join(Thailand[region]) + "\n")
        print(f"จังหวัดในภาค {region.capitalize()}: {Thailand[region]}")
        old_province = input("ป้อนชื่อจังหวัดที่ต้องการแก้ไข: ")
        if old_province in Thailand[region]:
            new_province = input("ป้อนชื่อจังหวัดใหม่: ")
            index = Thailand[region].index(old_province)
            Thailand[region][index] = new_province
            print("แก้ไขข้อมูลเรียบร้อย!\n")
        else:
            print("ไม่พบจังหวัดที่ต้องการแก้ไข!\n")
    else:
        print("ไม่พบภาคที่ระบุ!\n")

# ฟังก์ชันค้นหาข้อมูล
def search_data():
    print("=== ค้นหาข้อมูลจังหวัด ===")
    print("1. ค้นหาจากภูมิภาค")
    print("2. ค้นหาจากจังหวัด")
    choice = input("กรุณาเลือกเมนู (1-2) : ")
    if choice == "1":
        region = input("ป้อนชื่อภาคที่ต้องการค้นหา: ")
        if region.lower() in Thailand:
            print(f"จังหวัดในภาค {region}: {Thailand[region]}\n")
        else:
            print("ไม่พบข้อมูลของภาคนี้!\n")
    elif choice == "2":
        province = input(" : ")
        for i in Thailand:
            if province in Thailand[i]:
                print(f'จังหวัด {province} อยู่ในภาค {i} ของประเทศไทย')
        
# ฟังก์ชันลบข้อมูล
def delete_data():
    region = input("ป้อนชื่อภาคที่ต้องการลบข้อมูล: ")
    if region.lower() in Thailand:
        print(f"จังหวัดในภาค {region}: {Thailand[region]}")
        province = input("ป้อนชื่อจังหวัดที่ต้องการลบ: ")
        if province in Thailand[region]:
            Thailand[region].remove(province)
            if not Thailand[region]:  # ถ้าภาคไม่มีจังหวัดเหลือ ให้ลบภาคออก
                del Thailand[region]
            print("ลบข้อมูลเรียบร้อย!\n")
        else:
            print("ไม่พบจังหวัดที่ต้องการลบ!\n")
    else:
        print("ไม่พบภาคที่ระบุ!\n")

# ฟังก์ชันแสดงข้อมูลทั้งหมด
def view_all_data():
    if Thailand:
        for region, provinces in Thailand.items():
            print(f"{region.capitalize()}:\n  - " + "\n  - ".join(provinces) + "\n")
    else:
        print("ไม่มีข้อมูล!\n")

# เมนูหลัก
def main():
    while True:
        print("=== เมนูจัดการข้อมูลจังหวัด ===")
        print("1. เพิ่มข้อมูล (InsertData)")
        print("2. แก้ไขข้อมูล (UpdateData)")
        print("3. ค้นหาข้อมูล (SearchData)")
        print("4. ลบข้อมูล (DeleteData)")
        print("5. แสดงข้อมูลทั้งหมด (ViewAllData)")
        print("6. ออกจากโปรแกรม")
        print()
        
        choice = input("กรุณาเลือกเมนู (1-6): ")
        print()

        if choice == "1":
            insert_data()
        elif choice == "2":
            update_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            view_all_data()
        elif choice == "6":
            print("ออกจากโปรแกรม...")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง (1-6)\n")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()