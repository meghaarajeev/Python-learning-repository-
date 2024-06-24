1)
n = int(input("Enter limit:"))
for i in range(0,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

Output :
Enter Limit : 6
*
* *
* * *
* * * *
* * * * *
* * * * * *

2)
for i in range(0,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

Output:
1 
1 2 
1 2 3 
1 2 3 4 

3)
for i in range(0,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

Output:
1 
2 2 
3 3 3 
4 4 4 4
