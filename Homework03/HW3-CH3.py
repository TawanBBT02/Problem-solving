import time #BigO = 1
n = int(input("N : "))
start = time.time()
even = (n*(n + 2))/4
odd = ((n)/2)**2

print("Sum of odd number : ",odd,)
print("Sum of even number : ",even)
print("time : ",(time.time()-start)*1000)