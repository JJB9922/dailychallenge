#8. Write a program that prints *all* prime numbers

x = 0

#in order to print ALL prime numbers... change to while True:
while x < 50000:
    for i in range(2, x-1):
        #print(f"i is {i}")
        if(x % i == 0):
            #print(f"{x} and {x%i}")
            break

    else: print(f"{x}")
    x = x+1
