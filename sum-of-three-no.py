def sum_of_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    # Ask the user to input three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calculate the sum
    result = sum_of_three_numbers(num1, num2, num3)

    # Output the result
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
