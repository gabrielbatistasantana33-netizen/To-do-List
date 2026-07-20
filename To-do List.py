import time
print('Welcome to our to-do system!')
time.sleep(0.5)
print("[1] Enter a task \n[2] View the tasks added \n[3] Remove a task \n[4] Quit the system")
tasks = []
while True:
    time.sleep(0.5)
    action = input('What do you want to do? ') 
    time.sleep(0.5)
    if action == '1':
        question = input('Enter a task: ')
        time.sleep(0.3)
        tasks.append(question)
       
       
    elif action == "2":
        time.sleep(0.5)
        print(f"Your current tasks are: {tasks}.")
        time.sleep(0.5)
    elif action == "3":
        time.sleep(0.5)
        remove = input('which task do you want to remove? ') 
        (tasks.remove(remove))
        time.sleep(0.5)
        print(f"Your current tasks are now: {tasks}.")
        time.sleep(0.5)
    elif action == "4":
        time.sleep(0.5)
        print('Logging out...')
        break