prime_numbers = 0
number = 2
while(prime_numbers <= 25):
    counter = 0
    for i in range(2,number):
        if(number%i == 0):
            counter = counter + 1
    
    if(counter == 0):
        prime_numbers = prime_numbers + 1
        print(number)
    number = number + 1