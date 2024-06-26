num = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
for i in range(num):
    print(a, end=" ")
    a = b, a + b


Output:
Enter the number of terms:  10
Fibonacci series: 0 1 1 2 3 5 8 13 21 34 
