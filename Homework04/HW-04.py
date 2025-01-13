numbers = [21, 34, 51, 23, 37, 44, 60, 11, 94, 99]
result = []
result2 = {}
for i in range(0,len(numbers)):
    group =[]
    for j in range(0,len(numbers)):
        if numbers[j]%10 == i:
            group.append(numbers[j])
    result.append(group)
    result2[i] = group
group_most = [[]]
result3 = {}
for i in result2:
    if len(result2[i]) > len(group_most[0]):
        group_most.clear()
        group_most.append(result2[i])
        result3.clear()
        result3[i] = result2[i]
    elif len(result2[i]) == len(group_most[0]):
        group_most.append(result2[i])
        result3[i] = result2[i]
        
print(result2)
print(result3)