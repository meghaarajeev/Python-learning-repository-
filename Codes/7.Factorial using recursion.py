def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

x=int(input("Enter number:"))
if x < 0:
    print("Enter positive number")
elif x == 0:
    print("Factorial is 1")
else:
    print("The Factorial of",x,"is",fact(x))

