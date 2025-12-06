stack = []

def addstack():
    stkvalue = input("Enter the element of the stack: ")
    stack.append(stkvalue)
    print(stack)
    print(f"{stkvalue} inserted successfully!")

def popstack():
    if len(stack) == 0:
        print("Cannot pop elements from an empty stack!")
    else:
        stack.pop()
        print(stack)
        print("Last element removed successfully!")
while True:
    choice = int(input("Choose the option: 1. Add 2. Remove  3. View 4. : "))
    if choice == 1:
        addstack()
    elif choice == 2:
        popstack()
    elif choice == 3:
        print(stack)
    elif choice == 4:
        print("You have quit!")
        break
    else:
        ("Wrong option selected... Try again!")
