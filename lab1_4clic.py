import time
import functions_lab1_4
import click

COMMANDS = {
        "add": functions_lab1_4.add_todo,
        "show": functions_lab1_4.show_todos,
        "edit":  functions_lab1_4.edit_todo,
        "complate": functions_lab1_4.complate,
        "results": functions_lab1_4.show_results,
        "exit": functions_lab1_4.do_exit,
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
                if should_continue:
                        return should_continue

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

@click.group(help="Todo CLI start")
def click_cli():
        "Todo click"
        pass


@click_cli.command("add")
def click_add():
        functions_lab1_4.add_todo()
        print("Успішно виконано!")

@click_cli.command("show")
def click_show():
        functions_lab1_4.show_todos()
        print("Успішно виконано!")

@click_cli.command("edit")
@click.argument("number", type=int)
def click_edit(number):
        functions_lab1_4.edit_todo(number)
        print("Успішно виконано!")

@click_cli.command("complete")
@click.argument("number", type=int)
def click_complete(number):
        functions_lab1_4.complate(number)
        print("Успішно виконано!")

@click_cli.command("results")
def click_results():
       functions_lab1_4.show_results()
       print("Успішно виконано!")
       

@click_cli.command("repl")
def click_repl():
        repl()

if __name__=="__main__":
        click_cli()


