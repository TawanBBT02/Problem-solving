print("***Calculate the sum between start and stop number***")
start = int(input("Enter the start number : "))
end = int(input("Enter the end number : "))
result = 0
for i in range(start,end+1):
    result += i
print(f"The sum from {start} to {end} is : {result}")