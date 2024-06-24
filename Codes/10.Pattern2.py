1)
n = int(input("limit:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


Output

limit: 6
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

2)
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

output:
1 2 3 4 
1 2 3 
1 2 
1 

3)
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

output:
4 4 4 4 
3 3 3 
2 2 
1
