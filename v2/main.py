import os
import sys
import time

from core.tasks import tasks_manager
from storage.db_json import data_base

task_control = tasks_manager(data_base)

def screens_control():
    current = "main"

    while True:
        clear()
        current = screens[current]()

def main_screen():
    MENU_TEXT = (
        " Gerenciador de Tarefas - Tela Principal\n\n"
        f"{'...'*20}\n"
        " 1. Tarefas\n"
        " 2. Configurações\n"
        " 3. Limpar tela\n"
        " 4. Sair\n"
    )

    print(MENU_TEXT)
    choice = input(">>> ")
    match choice:
        case "1":
            return "task"
        case "2":
            return "config"
        case "3":
            clear()
            return "main"
        case "4":
            print(" Encerrando...")
            time.sleep(1)
            sys.exit()
        case _:
            print("opção invalida")
            return "main"
def tasks_screen():
    MENU_TEXT = (
        "Gerenciador de Tarefas - Tela de Tarefas\n\n"
        f"{'...'*20}\n"
        " 1. Ver todas as tarefas\n"
        " 2. Ver uma tarefa\n"
        " 3. Criar uma tarefa\n"
        " 4. Salvar tarefas\n"
        " 5. Limpar tela\n"
        " 6. Voltar\n"

    )
    print(MENU_TEXT)
    choice = input(">>> ")

    match choice:
        case "1":
            clear()
            task_control.view_all_tasks()
            return "task"
        case "2":
            clear()
            task_control.view_task()
            return "task"
        case "3":
            clear()
            task_control.add_task()
            return "task"
        case "4":
            clear()
            task_control.save_tasks(task_control.data)
            return "task"
        case "5":
            clear()
            return "task"
        case "6":
            print("retornando ao menu pricipal...")
            time.sleep(1)
            return "main"
        case _:
            print("Opção invalida")
            time.sleep(1)
            return "task"

def config_screen():
    MENU_TEXT = (
        " Gerenciador de tarefas - Tela de configuração\n\n"
        f"{'...'*20}\n"
        " 1. Banco de dados\n"
        " 2. Cores\n"
        " 3. Limpar tela\n"
        " 4. Voltar\n"
    )
    print(MENU_TEXT)
    choice = input(">>> ")
    match choice:
        case "1":
            print(" tudo ok com banco de dados")
            return "config"
        case "2":
            print(" tudo ok com as cores")
            return "config"
        case "3":
            clear()
            return "config"
        case "4":
            print(" retorando ao menu principal...")
            time.sleep(1)
            return "main"
        case _:
            print("opção invalida")
            time.sleep(1)
            return "config"
screens = {
    "task": tasks_screen,
    "config": config_screen,
    "main": main_screen
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

screens_control()
