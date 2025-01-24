def Factorial(N):
    # if N > 1:
    #     Factorial = N * Factorial(N-1)
    # else:
    #     Factorial = 1
    if N == 1:
        return 1
    for i in range(0,N):
        return N * Factorial(N - 1)
n = int(input("N : "))
NFactorial =Factorial(n)
print(NFactorial)
