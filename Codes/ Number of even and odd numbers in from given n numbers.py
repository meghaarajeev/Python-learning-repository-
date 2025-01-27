l=[]
n=int(input("Enter Limit:"))
e=0
o=0
for i in range(n):
    a=int(input("Enter numbers:"))
    l.append(a)
print(l)
for i in l:
    if i%2==0 :
        e += 1
        
    else :
        o += 1
print(f"Their are {e} even numbers and {o} odd numbers")

# output:
# Enter Limit: 6
# Enter numbers: 1
# Enter numbers: 3
# Enter numbers: 6
# Enter numbers: 4
# Enter numbers: 2
# Enter numbers: 2
# [1, 3, 6, 4, 2, 2]
# Their are 4 even numbers and 2 odd numbers
