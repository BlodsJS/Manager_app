#funções das tasks
import time


class tasks_manager:

    def __init__(self, database):
        self.db = database
        self.data = self.db.get_data()

    def add_task(self):
        MENU_TEXT = (
            "Gerenciador de Tarefas - Adicionar Tarefa\n\n"
            f"{'...'*20}\n"
            " Para criar uma nova tarefa, serão pedidas algumas informações leia atentamente e complete\n"
            " * obrigatorias\n"
            " 1. Nome da tarefa*\n"
            " 2. Descrição da tarefa\n"
        )
        print(MENU_TEXT)
        input(" Pressione enter para prosseguir...\n")
        name = input(" Nome: ")
        description = input(" Descrição (de enter para descrição padrão): ")
        if name:
            self.db.id_current +=1
            new_id = self.db.id_current

            if description:
                pass
            else:
                description = " Tarefa sem descrição própria, para adicionar descrição, edite a tarefa na tela de tarefas\n"

            new_task = {
                "name": name,
                "description": description,
                "id": new_id
            }
            self.data.append(new_task)
            self.db.save(self.data)
        else:
            print(" Erro:\n Tarefa sem nome não pode ser adicionada")
            time.sleep(1)
        return "task"

    def remove_task(self, task):
        MENU_TEXT = (
            " Gerenciador de Tarefas - Editor de Tarefas\n\n"
            f"{'...'*20}\n"
            " Antes de excluir, confira o titulo e a exclusão da tarefa\n"
            f" Tarefa: {task['name']}\n\n"
            " apos a confirmação, yes (y) para continuar a exclusão ou no (n) para cancelar\n"
        )
        print(MENU_TEXT)
        choice = input(">>> ")
        match choice:
            case "yes":
                task['_delete'] = True
            case "y":
                task['_delete'] = True
            case _:
                print(" Exclusão cancelada, Retornando a tela anterior por segurança...")
                time.sleep(1)
                return "task"
        print(" Exclusão confirmada, Retornando a tela anterior...")
        time.sleep(1)

    def update_task(self, task):
        MENU_TEXT = (
            " Gerenciador de Tarefas - Editor de Tarefas\n\n"
            f"{'...'*20}\n"
            " 1. Titulo\n"
            " 2. Descrição\n"
            " 3. Sair\n"
        )
        print(MENU_TEXT)
        choice = input(">>> ")
        match choice:
            case "1":
                new_title = input(" Novo titulo: ")
                if new_title:
                    task['name'] = new_title
            case "2":
                new_description = input(" Nova descrição: ")
                if new_description:
                    task['description'] = new_description
            case _:
                print(" Opção invalida, retornando ao menu anterior por segurança")
                time.sleep(1)
                return "task"
        print(" Tarefa editada com sucesso!")
        print(" Retornando ao menu anterior...")
        time.sleep(1)

    def view_task(self):
        print(f" Gerenciador de Tarefas - Vizualizador de Tarefas\n\n{'...'*20}\n")
        print(" Para ver uma tarefa, faça a busca pelo id.")
        matched_task = self.get_task()
        if matched_task:
            MENU_TEXT = (
                f" | {matched_task['name']} |\n\n"
                f"{'...'*20}\n"
                f" | Descrição: \n"
                f" {matched_task['description']}\n\n"
                f"{'...'*20}\n"
                f" 1. Editar tarefa \n"
                f" 2. Excluir tarefa\n"
                f" 3. sair\n"
            )
            print(MENU_TEXT)

            choice = input(">>> ")
            match choice:
                case "1":
                    self.update_task(matched_task)
                    self.db.save(self.data)
                case "2":
                    self.remove_task(matched_task)
                    self.db.save(self.data)
                case "3":
                    print(" Retornando a tela anterior...")
                    time.sleep(1)
                case _:
                    print("Opção invalida")
                    time.sleep(1)
        else:
            print(" Tarefa não encontrada, verifique o id e tente novamente")
            time.sleep(1)


    def view_all_tasks(self):
        print(f" Gerenciador de tarefas - vizualizador de tarefas (todas)\n\n{'...'*20}\n")
        for task in self.data:
            short = self.shorten(task["name"])
            print(f" | {short:<21} | {task['id']}")
        input("pressione qualquer tecla para retornar")
        print(" Retornando a tela anterior...")
        time.sleep(1)

    def save_tasks(self, new_data):
        self.db.save(new_data)
    #method extras

    def get_task(self):
        target = int(input(" ID: "))
        matched_task = next((task for task in self.data if task['id'] == target), None)
        return matched_task

    def shorten(self, text, limit=20):
        return text if len(text) <= limit else text[:limit-3] + "..."
