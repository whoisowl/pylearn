def divide(a, b):
    result = a / b
    return result


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("Result:", divide(num1, num2))

        break

    except ZeroDivisionError:
        print("Can't be divided by zero!")

    except ValueError:
        print("Can't put a string here!")

    finally:
        print("App successfully completed!")
