#Write a program that prints the multiplication table for numbers up to 12

print("Multiplication table for numbers 1-12: \n")

for i in range(1, 13):
    arr = []
    for x in range (1, 13):
        arr.append(i*x)
        if len(arr) == 12:
            [print(arr)]

