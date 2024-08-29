def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Can't divide by zero"
    else:
        return 'Invalid operation.'


print('Calculator')
while True:
    print('\n---------------------')
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # tuple of valid operations
    valid_ops = ('1', '2', '3', '4')
    operation = input("Enter your choice: ").strip()
    if operation == '5':
        break
    elif operation in valid_ops:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = calculate(num1, num2, operation)

        print(f'The result is: {result}')
    else:
        print('Invalid command, try again.')

print('The calculator is closed')