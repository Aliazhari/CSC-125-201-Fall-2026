def menu():
    print("Welcome Calc")
    print("Choose one of the following:")
    print("1 : ADD")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")

def add(n1, n2):
    result = n1 + n2  
    print(result) 

def subtract(n1, n2):
    result = n1 - n2  
    print(result)   
    
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
menu()
choice = int(input("Enter a choice: "))
match choice:
    case 1:
        add(num1, num2)
    case 2:
        subtract(num1, num2)