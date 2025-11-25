#funções das tasks
import time


class tasks_manager:

    def __init__(self, database):
        self.db = database
        self.data = self.db.get_data()

    def add_task(self):
        print(" Gerenciador de Tarefas - Adicionar Tarefa")
        MENU_TEXT = (
            "Gerenciador de Tarefas - Adicionar Tarefa\n\n"
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
        else:
            print(" Erro:\n Tarefa sem nome não pode ser adicionada")
            time.sleep(1)
        return "task"


    def remove_task(self):
        print(" remove uma tarefa")

    def update_task(self, task):
        MENU_TEXT = (
            " Gerenciador de Tarefas - Editor de Tarefas\n\n"
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

    def view_task(self):
        print(" Gerenciador de Tarefas - Vizualizador de Tarefas\n\n")
        print(" Para ver uma tarefa, faça a busca pelo id.")
        matched_task = self.get_task()
        if matched_task:
            TASK_TEXT = (
                f" | {matched_task['name']} |\n\n"
                f" | Description: \n"
                f" {matched_task['description']}\n\n"
                f" 1. Editar tarefa \n"
                f" 2. Excluir tarefa\n"
                f" 3. sair\n"
            )
            print(TASK_TEXT)

            choice = input(">>> ")
            match choice:
                case "1":
                    self.update_task(matched_task)
                case "3":
                    return "task"
                case _:
                    print("Opção invalida")
                    time.sleep(1)
        else:
            print(" Tarefa não encontrada, verifique o id e tente novamente")
            time.sleep(1)


    def view_all_tasks(self):
        print(" Gerenciador de tarefas - vizualizador de tarefas (todas)\n\n")
        for task in self.data:
            print(f" | {task['name']} | {task['id']}")
        input("pressione qualquer tecla para retornar")

    def save_tasks(self, new_data):
        self.db.save(new_data)
    #method extras

    def get_task(self):
        target = int(input(" ID: "))
        matched_task = next((task for task in self.data if task['id'] == target), None)
        return matched_task
