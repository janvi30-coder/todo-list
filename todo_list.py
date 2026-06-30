tasks = ["Study Python","Drink Water","Exercise"]
while True :
    print("1.Add Task ")
    print("2.View Tasks ")
    print("3.Remove Task")
    print("4.Exit")
    choice = int(input("Enter your choice in number :"))
    if choice == 1 :
       task=input("Enter a task :")
       tasks.append(task)
       print(tasks)
    elif choice == 2 :
       print("Your Tasks :\n     ")
       for task in tasks :
         print(task)
    elif choice == 3 :      
        number = int(input("Enter the task index number to remove :"))
        tasks.pop(number)
        print(tasks)
    elif choice == 4:
        print("The Program ends")
        break
    else:
       print("invalid choice")