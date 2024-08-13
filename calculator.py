import math

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square root")
        print("6. Exponent")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("0. Exit")

        choice = input("Enter choice(0-10): ")

        if choice == '0':
            break

        if choice in ('1', '2', '3', '4'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        else:
            num1 = int(input("Enter number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            if num2 == 0:
                print("Division by zero!")
            else:
                print(num1, "/", num2, "=", num1 / num2)

        elif choice == '5':
            print("Square root of", num1, "=", math.sqrt(num1))

        elif choice == '6':
            exp = int(input("Enter exponent: "))
            print(num1, "^", exp, "=", math.pow(num1, exp))

        elif choice == '7':
            print("Sine of", num1, "=", math.sin(math.radians(num1)))

        elif choice == '8':
            print("Cosine of", num1, "=", math.cos(math.radians(num1)))

        elif choice == '9':
            print("Tangent of", num1, "=", math.tan(math.radians(num1)))

        elif choice == '10':
            base = int(input("Enter base: "))
            print("Logarithm of", num1, "base", base, "=", math.log(num1, base))

        else:
            print("Invalid input")

calculator()
