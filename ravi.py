class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

def main():
    calculator = Calculator()

    print("Welcome to the Basic Calculator Program!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calculator.add(num1, num2))
            elif choice == '2':
                print("Result:", calculator.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calculator.multiply(num1, num2))
            elif choice == '4':
                print("Result:", calculator.divide(num1, num2))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


########################################################################################################################################


class Calculator:
    def add(self, numbers):
        return sum(numbers)

    def subtract(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    def multiply(self, numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def divide(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num != 0:
                result /= num
            else:
                return "Cannot divide by zero"
        return result

def main():
    calculator = Calculator()

    print("Welcome to the Basic Calculator Program!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4'):
            numbers = [float(num) for num in input("Enter numbers separated by commas: ").split(',')]
            
            if choice == '1':
                print("Result:", calculator.add(numbers))
            elif choice == '2':
                print("Result:", calculator.subtract(numbers))
            elif choice == '3':
                print("Result:", calculator.multiply(numbers))
            elif choice == '4':
                print("Result:", calculator.divide(numbers))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


