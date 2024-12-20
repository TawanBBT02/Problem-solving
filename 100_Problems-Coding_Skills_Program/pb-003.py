def find_multiples_of_three_and_four(start:int, end:int) -> list:
    result = []
    for i in range(start,end):
        if i%3 == 0 or i%2 == 0 or i%5 == 0:
            continue
        else:
            result.append(i)
    return result

print(find_multiples_of_three_and_four(10,25))