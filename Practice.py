count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")






def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "Fizzbuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15)) 






num = int(input("Enter a number: "))
message = "Even" if num % 2 == 0 else "Odd"
print(message)





for num in range(1, 11):
    print(num)




num = int(input("Enter a number: "))
for divisor in range(2, num):
    if num % divisor == 0:
        print(divisor)




num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break


if is_prime:
    print("%d It is a prime number"%num)
else:
    print("%d It is not a prime number"%num)


    

num = int(input("Enter a number: "))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("%d Is a prime number"%num)
else:
    print("%d Is not a prime number"%num)
