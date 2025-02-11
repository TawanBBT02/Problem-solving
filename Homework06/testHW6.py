from prettytable import PrettyTable

Thailand = {
    'Northern': ['Chiang Mai', 'Lamphun', 'Lampang', 'Uttaradit', 'Phrae', 'Nan', 'Phayao', 'Chiang Rai', 'Mae Hong Son'],
    'Southern': ['Chumphon', 'Nakhon Si Thammarat', 'Narathiwat', 'Pattani', 'Phatthalung', 'Songkhla', 'Surat Thani',
                 'Yala', 'Krabi', 'Phang Nga', 'Phuket', 'Ranong', 'Satun', 'Trang'],
    'Central': ['Bangkok', 'Nonthaburi', 'Samut Prakan', 'Pathum Thani', 'Samut Sakhon', 'Nakhon Pathom',
                'Kamphaeng Phet', 'Chai Nat', 'Nakhon Nayok', 'Nakhon Sawan', 'Phra Nakhon Si Ayutthaya', 'Phichit',
                'Phitsanulok', 'Phetchabun', 'Lop Buri', 'Samut Songkhram', 'Saraburi', 'Sing Buri', 'Sukhothai', 'Suphan Buri',
                'Ang Thong', 'Uthai Thani'],
    'Northeastern': ['Kalasin', 'Khon Kaen', 'Chaiyaphum', 'Nakhon Phanom', 'Nakhon Ratchasima', 'Bueng Kan', 'Buri Ram', 'Maha Sarakham',
                     'Mukdahan', 'Yasothon', 'Roi Et', 'Loei', 'Si Sa Ket', 'Sakon Nakhon', 'Surin', 'Nong Khai', 'Nong Bua Lam Phu',
                     'Amnat Charoen', 'Udon Thani', 'Ubon Ratchathani'],
    'Eastern': ['Chanthaburi', 'Chachoengsao', 'Chonburi', 'Trat', 'Prachinburi', 'Rayong', 'Sakaeo'],
    'Western': ['Kanchanaburi', 'Tak', 'Prachuap Khiri Khan', 'Phetchaburi', 'Ratchaburi'],
}

def view_all_data():
    if Thailand:
        table = PrettyTable()
        table.field_names = ["Region", "Provinces"]
        
        for region, provinces in Thailand.items():
            table.add_row([region, ', '.join(provinces)])
        
        print(table)
    else:
        print("ไม่มีข้อมูล!\n")
