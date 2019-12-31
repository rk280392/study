def fibo(n):
    if n<0:
        print("Please put only positive numbers")
    elif n==1:
        return 0 

    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    

print(fibo(9))

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))
