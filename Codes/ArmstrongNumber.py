n = input("Enter Number:")
k = int(n)

sum = 0
for i in n:
    sum += int(i) ** len(n)

if k == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")
