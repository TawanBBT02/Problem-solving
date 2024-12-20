def find_multiples_of_three_and_four(start:int, end:int) -> list:
    result = []
    for i in range(start,end):
        if i%3 == 0 and i%4 == 0:
            result.append(i)
    return result

print(find_multiples_of_three_and_four(10,50))