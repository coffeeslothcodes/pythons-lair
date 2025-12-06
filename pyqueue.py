queue = []

def addqueue():
    addvalue = input("Enter the element of the queue: ")
    queue.insert(0,addvalue)
    print(queue)
    print(f"{addvalue} inserted successfully!")

def popqueue():
    if len(queue) == 0:
        print("Cannot pop elements from an empty queue!")
    else:
        queue.pop(-1)
        print(queue)
        print("First element removed successfully!")
while True:
    print("Queues")
    choice = int(input("Choose the option: 1. Add 2. Remove  3. View 4. Quit : "))
    if choice == 1:
        addqueue()
    elif choice == 2:
        popqueue()
    elif choice == 3:
        print(queue)
    elif choice == 4:
        print("You have quit!")
        break
    else:
        ("Wrong option selected... Try again!")
