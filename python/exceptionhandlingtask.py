##1 syntax error check
try
    print("Attempting risky operation...")
except:
    print("Something went wrong!")

##fixed version
try:
    print("Attempting risky operation...")
except:
    print("Something went wrong!")


##2 zero division error
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    print (numerator / denominator)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


##3 value error
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Error: Please enter a valid number for age.")


##4 type error
try:
    num = 10
    text = "20"
    result = num + text
    print("Result:", result)
except TypeError:
    print("Error: Cannot add integer and string together.")


# 5 finally block
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Error: That was not an integer.")
finally:
    print("Program Completed")


## 6 multiple exception
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")


# ## 7 file handling error
try:
    with open("student_data.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error: The file 'student_data.txt' does not exist.")


## 8 catch all exception
try:
    num = float(input("Enter a number: "))
    print("Square:", num ** 2)
except Exception as error:
    print("An unexpected error occurred:", error)


## 9 custom message error
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is:", age)
except ValueError as error:
    print("Error:", error)



## 10 safe calculator
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            print("Result:", num1 / num2)
        else:
            print("Error: Invalid operation.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as error:
        print("Unexpected error:", error)
calculator()
