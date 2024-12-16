borrow = int(input("Enter the amount you want borrow:"))
if borrow <= 1000:
    result = borrow + (borrow * 0.1)
elif borrow <= 10000:
    result = borrow + (borrow * 0.05)
else:
    result = borrow + (borrow * 0.02)
print(f"The money you must return : {format(result,'.2f')}")