def check_prime(n:int) ->str:
    result = []
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)

    if len(result) > 2:
        return "is not prime",result
    else:
        return "is prime",result

inp = int(input("Input : "))
print(check_prime(inp))