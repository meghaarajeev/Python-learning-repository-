def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return "Leap Year!"
    else:
        return "Not a Leap Year!"

year = int(input("Enter Year:"))
print(is_leap(year))

output:
Enter Year: 2020
Leap Year!
