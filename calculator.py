def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

while True:
    print("Options:")
    print("Enter '1' to add")
    print("Enter '2' to subtract")
    print("Enter '3' to multiply")
    print("Enter '4' to divide")
    print("Enter '5' to exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '5':
        print("Exiting the calculator.")
        break
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid option.")
        continue
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        try:
            print("Result:", divide(num1, num2))
        except ValueError as ve:
            print(ve)
