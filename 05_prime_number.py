number = 18
counter = 0

for i in range(2,number):
    if(number%i == 0):
        counter = counter + 1

if(counter == 0):
    print(f"{number} is a prime number\n")
else:
    print(f"{number} is not a prime number\n")
