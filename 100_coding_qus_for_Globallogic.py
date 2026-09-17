# Check if a number is prime
for i in range(2, 12):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, "Prime number")
    else:
        print(i, "Not a prime number")

# Check if a number is palindrome
num = "456"
if num[::-1] == num:
    print(num,"is a palindrome number")
else:
    print("Not a palindrome")

# Reverse a number
num = "456"
print(num[::-1])

# Find factorial of a number
num=10
fact = 1
for i in range(1,num+1):
    facte=fact*i
print(fact)


# Find Power of a Number (Without Using pow())
num = int(input("Enter number: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * num

print("Result =", result)

