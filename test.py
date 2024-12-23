def fibonacci(n):
    print(n)
    if n==1:

        return 0
    elif n==2:

        return 1
    elif n==3:

        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2) + fibonacci(n-3)) 
    
    


print(fibonacci(5))
