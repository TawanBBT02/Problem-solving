def print_rectangle_pattern(rows:int,columns:int)->None:
    for i in range(rows):
        for j in range(columns):
            print("*",end="")
        print()
    return ''
row = int(input("Rows :"))
column = int(input("Columns :"))
print(print_rectangle_pattern(row,column))