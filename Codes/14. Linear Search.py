l = []
n = int(input("Enter limit:"))
for i in range(0, n):
    a = int(input("Enter a number: "))
    l.append(a)

x = int(input("Enter the key:"))
f = 0
for i in range(len(l)):
    if x == l[i]:
        f = 1
        print("Element", x, "is present at position", i+1)  
        break
if f == 0:
    print("Element", x, "not present") 
