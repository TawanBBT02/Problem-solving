import array as arr
a = arr.array('i', [50, 87, 65, 39])
print(f"All data in array : {a}")
print("Max = ",max(a))
print("Min = ",min(a))
ave = sum(a)/4
print("Sum = ",sum(a))
print("Average = ",ave)
sort_a = sorted(a)
print("Sort Min to Max = ",sort_a)
sort_a.reverse()
print("Sort Max to Min = ",sort_a)
odd = []
even = []
for i in a :
    if i%2 != 0:
        odd.append(i)
    else:
        even.append(i)
print("Odd Number = ",odd)
print("Even Number = ",even)
search = int(input("Search a number : "))
if search in a :
    print(f"Number {search} in Array")
else:
    print(f"Number {search} not in Array")

delete = int(input("Delete a number : "))
if delete in a :
    a.remove(delete)
    print(f"Delete success!!")
    print(a)
else:
    print(f"Number {delete} not in Array")