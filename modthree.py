def find_multiples_of_three(start:int, end:int) -> list:
    result = []
    for i in range(start+1,end):
        if i%3 == 0:
            result.append(i)
    
    return result

start = int(input("Enter Start : "))
end = int(input("Enter End : "))
print(find_multiples_of_three(start,end))