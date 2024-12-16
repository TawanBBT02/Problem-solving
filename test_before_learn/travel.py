dis = int(input("Enter distance (KM) : "))
car = str(input("Enter car type (ev/standard) : "))
if car.lower() == "ev":
    total = dis * 1
elif car.lower() == "standard" : 
    total = dis * 4
else:
    print("Error!!!!!!")

print(f"Total : {total}")