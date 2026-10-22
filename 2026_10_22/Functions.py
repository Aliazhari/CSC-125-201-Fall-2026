def menu():
    print("Welcome Calc")
    print("Choose one of the following:")
    print("1 : Balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Exit")

balance = 1000
menu()
choice = int(input())
match(choice):
    case 1:
        print("Your blance is ", balance )
    case 2:
        print("Enter the amount")
        amount = int(input())
        balance = balance + amount
        print("Your balance now is ", balance)
    case 3:
        print("Enter the amount")
        amount = int(input())
        balance = balance - amount
        print("Your balance now is ", balance)
    case 4:
        print("Thank you! goodbye")