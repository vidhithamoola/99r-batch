number = 1
while number <= 10:
    print(number)
    number += 1

number = 1
while number <= 10:
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1
    
number = 1
while number <= 10:
    if number == 8:
        break
    print(number)
    number += 1
    
number = 1
while number <= 10:
    if number == 8:
        break
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1
    
number = 1
while number <= 10:
    if number == 8:
        break
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    number += 1