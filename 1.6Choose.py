n = int(input("Please choose a number, n:\n"))
choice = input("Would you like to calculate the:\n\
    1. Sum of 1, ..., n?\n\
    2. Product of 1, ..., n?\n\n\
    Please choose '1' or '2'.\n")

if int(choice) == 1:
    step = 0
    x = 0
    while step < n:
        step = step + 1
        x = x + step
    
    print(f"Sum is {x}")

elif int(choice) == 2:
    product = 1
    for i in range(1, n+1):
       product = product*i

    print(f"Product is {product}") 

else: 
    print("Invalid option.")
    


