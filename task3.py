age = int(input("Enter age: "))
count = 0

while age != -1:
    if age < 1 or age > 120:
        age = int(input("Enter age: "))
        continue

    count += 1
    age = int(input("Enter age: "))

print("Valid ages count:", count)


number = int(input("Enter number: "))
total = 0

while number != 0:
    if number % 5 != 0:
        number = int(input("Enter number: "))
        continue

    total += number
    number = int(input("Enter number: "))

print("Sum:", total)


text = "PyTHon ProGRAM"
count = 0

for char in text:
    if not ('A' <= char <= 'Z'):
        continue

    count += 1

print("Uppercase letters count:", count)

sales = [500, 0, 1200, 0, 700]
total = 0

for amount in sales:
    if amount == 0:
        continue

    total += amount

print("Total sales amount:", total)