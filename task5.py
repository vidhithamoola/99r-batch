i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if (i + j) % 2 == 0:
            print("(", i, ",", j, ")")
        j += 1
    i += 1
    
i = 1
count = 0
while i <= 10:
    j = 1
    while j <= 10:
        if i * j > 30:
            print("(", i, ",", j, ")")
            count += 1
        j += 1
    i += 1
print("Total pairs:", count)

num = int(input("Enter number: "))
while num != 0:
    total = 0
    print("Factors:", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            total += i
    print()
    print("Sum:", total)
    num = int(input("Enter number: "))
    
numbers = [12, 7, 20, 9]
for num in numbers:
    i = 1
    count = 0
    while i <= num:
        if i % 2 == 0:
            count += 1
        i += 1
    print(num, "→ Even count:", count)