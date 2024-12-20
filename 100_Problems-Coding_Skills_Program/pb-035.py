# จำนวนแถวของรูปทรงที่ต้องการ
rows = 5

# สร้างรูปแบบรูปทรง
for i in range(1, rows + 1):
    print('*' * i,'#')

for i in range(rows - 1, 0, -1):
    print('*' * i)