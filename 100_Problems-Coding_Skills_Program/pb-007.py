def prime_numbers_in_range(start:int, end:int) ->tuple:
    result = []
    for i in range(start,end+1):
        wi = []
        for ii in range(1,i+1):
            if i%ii == 0:
                wi.append(i)

        if len(wi) > 2:
            continue
        else:
            result.append(i)
            
    sum_result = 0
    for sum in result:
        sum_result+=sum

    return result,sum_result

print(prime_numbers_in_range(10,20))