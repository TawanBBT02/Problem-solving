def find_multiples_of_three(start:int, end:int) -> list:
    result = []
    for i in range(start,end):
        if i%3 == 0:
            result.append(i)
    
    return result

print(find_multiples_of_three(10,25))