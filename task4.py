i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if (i + j) % 2 == 0:
            print((i, j))
        j += 1
    i += 1
    
    
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