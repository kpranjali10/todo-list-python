print("    ")
print("TO-DO LIST")
print("")
tasks_list = []
while True:
    print("====MENU====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark the task as completed")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Enter your choice(1-5): ")
    print("    ")

    if choice == "1":
        task = input("Enter the task:")
        time = input("enter the time required to complete the task:")
        description = input(" enter the description if any:")

        tasks = {"task": task, 
                 "time": time,
                 "description": description
                 }
        tasks_list.append(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks_list) == 0:
            print("No tasks available.")
            print("    ")
        else:
            print("your tasks are:")
            for eachtask in tasks_list:
                print("Task:", eachtask["task"])
                print("Time:", eachtask["time"])
                print("Description:", eachtask["description"])
                print("    ")

    elif choice == "3":
            task_to_mark = input("Enter the task to mark as completed:")
            for eachtask in tasks_list:
                if eachtask["task"] == task_to_mark:
                    tasks_list.remove(eachtask)
                    print("Task marked as completed and removed from the list.")
                else:
                    print("Task not found.")

    elif choice == "4":
        task_to_delete = input("Enter the task to delete:")
        found = False
        for eachtask in tasks_list:
            if eachtask["task"] == task_to_delete:
                tasks_list.remove(eachtask)
                print("Task deleted successfully.")
                found = True
                break
        if not found:
            print("Task not found.")

    elif choice == "5":
        print("Exiting the program.")
        print("thankyou for using the to-do list.")
        break

    else:
         print("Invalid choice. Please enter a number between 1 and 5.")
         print("")
        