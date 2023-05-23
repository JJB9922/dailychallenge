n = int(input("Please input a number, n:\n"))

x=0
step = 0

while step < n:
    step = step + 1
    if float(step / 3).is_integer() or float(step / 5).is_integer():
        x = x + step

print(f"Sum is {x}")

