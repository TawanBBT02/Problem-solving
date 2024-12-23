def find_divisors(n:int) ->list[int]:
    result = []
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)
    return result

inp = int(input("Input : "))
print(find_divisors(inp))