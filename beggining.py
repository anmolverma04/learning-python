def calculator():
    while True:
        print("\nBasic Calculator")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        elif choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()