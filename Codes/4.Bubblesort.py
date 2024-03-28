a=[]
n = int(input("Enter limit:"))
for i in range(0,n):
    x=int(input("Enter Numbers:"))
    a.append(x)
for i in range(0,n):
    for j in  range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)
