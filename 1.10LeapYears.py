#Write a program that prints the next 20 leap years

year = int(input("What year is it?\n"))
leapYear = year
counter = 1
print("Next 20 leap years:\n")

while counter < 21:
    if (year%4 == 0 and year%100 !=0) or (year%100 == 0 and year%400 == 0):
        print(f"{counter}: {year}\n")
        counter = counter + 1
        year = year + 1
    else:
        year = year + 1
           