print("***Multiplication Table***")
num = float(input("Enter the multiplication table number : "))
print(f"Multiplication Table for {num}")
for i in range(1,13):
    print(f"{num} * {i} = {format(num*i,'.2f')}")