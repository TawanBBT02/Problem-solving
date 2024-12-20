def calculate_median(provinces:dict[str,int])->list[tuple[str,int]]:
    
    num_lst = []
    for i in provinces:
        num_lst.append(provinces[i])
    num_lst.sort()
    province_median = ''
    for i in provinces:
        if provinces[i] == num_lst[len(num_lst)//2]:
            province_median = i
    result = [province_median,num_lst[len(num_lst)//2]]
    # tuple(province_median, num_lst[len(num_lst)//2])

    return list(tuple(result))


province = {"Thailand":76,"Laos":17,"Vietnam":58,"Japan":47,"China":23}
print(calculate_median(province))