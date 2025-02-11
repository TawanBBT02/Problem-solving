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

def insert_data():
    print(f"-\n-".join(Thailand) + "\n")
    region = input("Enter region name: ")
    province = input("Enter province name: ")
    if region in Thailand:
        Thailand[region].append(province)
    else:
        Thailand[region] = [province]
    print("Data added successfully!\n")

def update_data():
    region = input("Enter the region name to update: ")
    if region.lower() in Thailand:
        print(f"Provinces in {region.capitalize()}:\n  - " + "\n  - ".join(Thailand[region]) + "\n")
        old_province = input("Enter the province name to update: ")
        if old_province in Thailand[region]:
            new_province = input("Enter the new province name: ")
            index = Thailand[region].index(old_province)
            Thailand[region][index] = new_province
            print("Data updated successfully!\n")
        else:
            print("Province not found!\n")
    else:
        print("Region not found!\n")

def search_data():
    print("=== Search Province Data ===")
    print("1. Search by Region")
    print("2. Search by Province")
    choice = input("Please select a menu (1-2): ")
    if choice == "1":
        region = input("Enter the region name: ")
        if region.lower() in Thailand:
            print(f"Provinces in {region}: {Thailand[region]}\n")
        else:
            print("Region data not found!\n")
    elif choice == "2":
        province = input("Enter province name: ")
        for region in Thailand:
            if province in Thailand[region]:
                print(f'Province {province} is in {region} region of Thailand')

def delete_data():
    region = input("Enter the region name to delete data: ")
    if region.lower() in Thailand:
        print(f"Provinces in {region}: {Thailand[region]}")
        province = input("Enter the province name to delete: ")
        if province in Thailand[region]:
            Thailand[region].remove(province)
            if not Thailand[region]:
                del Thailand[region]
            print("Data deleted successfully!\n")
        else:
            print("Province not found!\n")
    else:
        print("Region not found!\n")

def view_all_data():
    if Thailand:
        for region, provinces in Thailand.items():
            print(f"{region.capitalize()}:\n  - " + "\n  - ".join(provinces) + "\n")
    else:
        print("No data available!\n")

def main():
    while True:
        print("=== Province Data Management Menu ===")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Search Data")
        print("4. Delete Data")
        print("5. View All Data")
        print("6. Exit")
        print()
        
        choice = input("Please select a menu (1-6): ")
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
            print("Exiting the program...")
            break
        else:
            print("Please select a valid menu option (1-6)\n")

if __name__ == "__main__":
    main()
