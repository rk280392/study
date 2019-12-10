a = int(input("please enter first value : "))
b = int(input("please enter second value: "))
c = int(input("please enter thrid value: "))

def main(a,b,c):
    if a > b and a > c:
        print(f"greatest number is {a}")
    elif b > a and b > c:
        print(f"greatest number is {b}")
    elif c > a and c > b:
        print(f"greatest number is {c}")
        
main(a,b,c)
