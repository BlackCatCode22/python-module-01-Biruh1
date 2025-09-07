def describe_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        largest = num1
        var_name = "num1"
    elif num2 >= num1 and num2 >= num3:
        largest = num2
        var_name = "num2"
    else:
        largest = num3
        var_name = "num3"

    message = (
        f"Message to User: You entered three numbers, {num1}, {num2}, and {num3}. "
        f"The first whole number you entered was assigned to a variable named num1, "
        f"the second ({num2}) to num2, and finally the third ({num3}) was assigned to num3. "
        f"Your input was processed and the largest number you entered was {largest}, "
        f"which belonged to an integer variable named {var_name}."
    )
    return message

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(describe_largest(num1, num2, num3))
