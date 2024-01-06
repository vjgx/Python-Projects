todo = []
print("--------Welcome to your to do list--------")
          
def add_todo():
    item=input("Enter the item you want to add:")
    todo.append(item)
    print(item + " has been added to your to-do list.")
    
def remove_todo():
    item = input("Enter the item you want to remove: ")
    if item in todo:
        todo.remove(item)
        print(item + " has been removed from your to-do list.")
    else:
        print(item + " is not in your to-do list.")
def display_todo():
    if len(todo)==0:
        print("Your to do is empty.")
    else:
        print("your to do list is:")
        for item in todo:
            print(item)    

while True:
    print("\nMenu:")
    print("1.Add a task")
    print("2.Remove a task.")
    print("3.Display the tasks.")
    print("4.Quit")
    
    choice=input("Enter your choice(1-4):")

    if choice=='1':
       add_todo()
    elif choice=='2':
       remove_todo()
    elif choice=='3':
       display_todo()
    elif choice=='4':
       print("Goodbye!!!")
       break
    else:
        print("Invalid choice.plz enter a valid choice.")
    

            