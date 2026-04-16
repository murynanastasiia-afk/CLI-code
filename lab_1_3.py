import time
import functions_lab1_3
import os
import sys
import argparse

COMMANDS = {
        "add": functions_lab1_3.add_todo,
        "show": functions_lab1_3.show_todos,
        "edit":  functions_lab1_3.edit_todo,
        "complate": functions_lab1_3.complate,
        "results": functions_lab1_3.show_results,
        "exit": functions_lab1_3.do_exit,
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

        if len(parts) > 1:
                args_to_pass = parts[1] 
        else: args_to_pass = None

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
                

def build_parser():
        parser = argparse.ArgumentParser (
                prog = 'todo',
                description="Todo CLI App"
                )
        sub = parser.add_subparsers(dest="command")

        p_add = sub.add_parser("add", help="Додати завдання")
        p_add.add_argument("text", nargs="+", help="Текст завдання")

        sub.add_parser("show", help="Показати список")

        p_edit = sub.add_parser("edit", help="Редагувати")
        p_edit.add_argument("number", type=int, help="Номер завдання")

        p_complate = sub.add_parser("complate", help="Виконати")
        p_complate.add_argument("number", type=int, help="Номер завдання")

        sub.add_parser("results", help="Показати результати")

        sub.add_parser("repl", help="Запустити через repl")
        return parser

def run_args(args):
        if args.command == "add":
                task_text = " ".join(args.text)
                dispanch(f"add {task_text}")
        elif args.command == "show":
                dispanch("show")
        elif args.command == "edit":
                dispanch(f"edit {args.number}")
        elif args.command == "complate":
                dispanch(f"complate {args.number}")
        elif args.command == "results":
                dispanch("results")
        elif args.command == "repl":
                repl()

def main():
        if len(sys.argv) == 1:
                repl()
                return
        parser = build_parser()
        args = parser.parse_args()
        run_args(args)
               
if __name__ == '__main__':
        main()