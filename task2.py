while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

number = int(input("Enter a positive integer: "))

while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter a positive integer: "))

total = 0
i = 1

while i <= number:
    total += i
    i += 1

print("Sum:", total)

while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            break
        print("Invalid input. Enter a positive integer.")
    except ValueError:
        print("Invalid input. Enter an integer.")

total = 0
i = 1

while i <= number:
    total += i
    i += 1

print("Sum:", total)

while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number > 0:
            break
        else:
            print("Error: Please enter a positive integer.")

    except ValueError:
        print("Error: Please enter a valid integer.")

total = 0
i = 1

while i <= number:
    total += i
    i += 1

print("Sum of numbers from 1 to", number, "is:", total)