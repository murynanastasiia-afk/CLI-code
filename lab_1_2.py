import time
import functions_lab1
import os

os.makedirs("Python", exist_ok=True)
todos_path=os.path.join("Python", "todos.txt")

if not os.path.exists(todos_path):
         with open(todos_path, 'w') as f:
                 pass
now=time.strftime("%b %d %Y %H:%M:%S")
print(now)
while True:
        user_action=input("Type add, show, edit, complete, show results or exit: ")
        user_action=user_action.strip()

        if user_action.lower().startswith('add'):
                functions_lab1.add_todo()
        elif user_action.lower().startswith('show results'):
                functions_lab1.show_results()
        elif user_action.lower().startswith('show'):
                functions_lab1.show_todos()
        elif user_action.lower().startswith('edit'):
                functions_lab1.edit_todo(user_action)
        elif user_action.lower().startswith('complete'):
                functions_lab1.complate(user_action)

        elif user_action.lower().startswith('exit'):
                break
        else:
                print('invalid input')
        print("Успішне виконання команди")