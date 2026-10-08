name = input("What is your name")
print("Welcome to the Calculator " + name)
num1 = int(input ("Enter the first number: "))
num2 = int(input("Enter second number:"))
print("Choose one of the following:")
print("1. To add")
print("2. to subtract")
print("3. to multiply")
print("4. to divide")
print("5. exponent")
print("6. Exit")

choice = int(input())

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
elif choice == 5:
    print(num1 ** num2)
elif choice == 6:
    print("Goodbye")
else:
    print("Invalid entry")
    
match choice:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case _:
        print("invalid")
        

