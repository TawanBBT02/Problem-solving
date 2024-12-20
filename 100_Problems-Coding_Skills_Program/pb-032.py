def calculate_median(lst:list[int])->float:
    lst.sort()
    print(lst)
    return lst[len(lst)//2]

num = [8,4,7,4,6,2,10,9,3,7,1]
print(calculate_median(num))