FILEPATH =r"C:\унік\4 семестр\Розобка\lab1_2\list_tasks.txt"
FILEPATH2 =r"C:\унік\4 семестр\Розобка\lab1_2\done_tasks.txt"
def get_todos(filepath = FILEPATH):
         with open(filepath, 'r', encoding='utf-8') as f:
                 todos_local=f.readlines()
         return todos_local
def write_todos(todos_arg, filepath=FILEPATH):
         with open(filepath, 'w', encoding='utf-8') as file:
                 file.writelines(todos_arg)
def get_todos_done(filepath = FILEPATH2):
         with open(filepath, 'r', encoding='utf-8') as f:
                 todos_local=f.readlines()
         return todos_local
def write_todos_done(todos_arg, filepath=FILEPATH2):
         with open(filepath, 'w', encoding='utf-8') as file:
                 file.writelines(todos_arg)
def add_todo():
         task = input("Введіть назву завдання: ").strip()
         count = input("Введіть кількість: ").strip()
         date = input("Введіть дату дедлайну: ").strip()
         new_todo = f"{date} {task} 0/{count}\n"
         todos=get_todos()
         todos.append(new_todo)
         write_todos(todos)
def show_results():
         todos=get_todos_done()
         if not todos:
                  print("Список порожній")
         else:
                  for index, item in enumerate(todos):
                           row=f"{index+1}--{item.strip('\n')}"
                           print(row)
def show_todos():
         todos=get_todos()
         for index, item in enumerate(todos):
                  row=f"{index+1}--{item.strip('\n')}"
                  print(row)
def edit_todo(user_action):
         try:
                  number=int(user_action[5:])
                  number=number-1
                  todos = get_todos()
                  if number<0 or number>=len(todos):
                           raise IndexError
                  new_task = input("Введіть назву завдання: ").strip()
                  new_count = input("Введіть кількість: ").strip()
                  new_date = input("Введіть дату дедлайну: ").strip()
                  todos = f"{new_date} {new_task} 0/{new_count}\n"
                  write_todos(todos)
         except IndexError:
                  print("Невірний номер завдання")
def complate(user_action):
         try:
                  todos = get_todos()
                  number=int(user_action[9:])
                  number=number-1
                  if number<0 or number>= len(todos):
                           raise IndexError
                  todo = todos[number].strip()
                  parts = todo.rsplit(' ', 1)
                  task = parts[0]
                  counts = parts[1]
                  current, goal = counts.split('/')
                  new_current = int(current) + 1
                  int_goal = int(goal)
                  new_todo = f"{task} {new_current}/{int_goal}\n"

                  if new_current == int_goal:
                           message=f"\tЗавдання '{task}' було успішно виконане!"
                           print(message)
                           todos.pop(number)
                                

                           done_todos = get_todos_done()
                           done_todos.append(new_todo)
                           write_todos_done(done_todos)
                  else:
                           todos[number] = new_todo
                  write_todos(todos)

         except IndexError:
                  print("Невірний номер завдання")
                 
                              

         