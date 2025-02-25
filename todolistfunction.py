tasks = []
def menu():
    print("""

        TO-DO LIST MANAGER
        -—-------------------
        
        1. Add a task
        2. View tasks
        3. Mark task as complete
	4. Delete a task
        5. Exit
        
        """)

def add_a_task():
		
	if add_task.startswith(" "):
		print("Invalid")

	if add_task.isdigit():
		print("Invalid")

	tasks.append({'task': task})
	return "Task added!"

def view_tasks():
	
	print("Tasks: ")
	for task in tasks:
		print(f"{tasks['task']}")  
	if not tasks:
		print("No tasks recorded yet.\n")

def mark_task_as_complete():
       
	for count, task in range(tasks):
		mark = "✓" if task["done"] else " "
		print(f"[{mark}] {count + 1}. {task['task']}")

def delete_task():
        if task in tasks:
            tasks.remove(task)

def main():

	menu()
	while True:
		print(" ")
	choice = int(input("Enter your choice: "))
	if choice == 1:
            
		task = input("Enter the task: ")
           
		tasks.append({'task': task})
		print("Task added!\n")
		add_a_task()            
      
	elif choice == 2:
		view_tasks()
	elif choice == 3:
		mark_task_as_complete()                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	elif choice == 4:
		delete_task()
	elif choice == 5:
		Exit()
	break
	else:
		print("Invalid option. Please try again.")

	


	
	print(menu())
main()


	
