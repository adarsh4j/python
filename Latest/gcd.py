def gcd_number(a,b):
    while b:
        a,b=b,a%b
    return a

a=int(input("Enter the first number : "))
b=int(input("Enter the second number: "))
gcd=gcd_number(a,b)
print(f"GCD of {a} and {b} is {gcd}")
