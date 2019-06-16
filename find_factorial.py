def FirstFactorial(num):
    fact = 1
    i = 1
    if num == 1:
        return 1
    elif num > 1:
        while i <= num:
            fact = fact * i
            i += 1
    print(fact)

FirstFactorial(int(input()))
