def Factorial(N):
    if N > 1:
        Factorial = N * Factorial(N-1)
    else:
        Factorial = 1
n = int(input("N : "))
NFactorial =Factorial(n)
print(NFactorial)
