
import time
import sys
import typer
import functions_1_5

COMMANDS = {
        "add": functions_1_5.add_todo,
        "show": functions_1_5.show_todos,
        "edit":  functions_1_5.edit_todo,
        "complate": functions_1_5.complate,
        "results": functions_1_5.show_results,
        "exit": functions_1_5.do_exit,
}

def dispanch(user_action):
         user_action=user_action.strip()
         if not user_action:
                print("invalid input")
                return True
         
         parts = user_action.split(maxsplit=1)
         cmd = parts[0].lower()
         handler = COMMANDS.get(cmd)

         if handler is None:
                print("invalid input")
                return True

         if len(parts)>1:
                args_to_pass=parts[1]
         else:
                args_to_pass = None

         try:
                should_continue = handler(args_to_pass)
                if should_continue is False:
                           return False
                return True
         except ValueError:
                print("Ваша команда не зовсім зрозуміла")
                return True
         except IndexError:
                print("Не вірний номер тудушки")
                return True

def repl():
         now = time.strftime("%b %d %Y %H:%M:%S")
         print(now)
         while True:
                user_action=input("Type add, show, edit, complate, results or exit: ")
                if not dispanch(user_action):
                        break

typer_app = typer.Typer(help="Todo CLI через typer (альтернатива argparse і click).")


@typer_app.command()
def add(text: list[str] = typer.Argument(None)):
    functions_1_5.add_todo(" ".join(text))
    print("Успішно виконано!")


@typer_app.command()
def show():
    functions_1_5.show_todos()


@typer_app.command()
def edit(number: int):
    try:
        functions_1_5.edit_todo(number=number)
        print("Успішно виконано!")
        
    except IndexError:
        print("Не вірний номер тудушки")
        raise typer.Exit()


@typer_app.command()
def complete(number: int):
        functions_1_5.complate(number=number)
        print("Успішно виконано!")

@typer_app.command()
def data():
       now = time.strftime("%Y %B %d - %H:%M:%S")
       print(now)

@typer_app.command()
def results():
         functions_1_5.show_results()



def main():
    if len(sys.argv) == 1:
        repl()
        return
    else:
        typer_app()
        return



if __name__ == '__main__':
    main()
