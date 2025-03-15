data = [25,27,14,48,37,30,26,41,31,43,54,40]
for i in  data:
    print(i%len(data),end=" ")
print()
    
result = []
for i in range(len(data)):
    res = []
    for j in data:
        
        if j%len(data) == i:
            res.append(j)
    result.append(res)
    
print(result)