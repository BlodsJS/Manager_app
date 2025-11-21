from Extras.formatation_doc import *
import time
import os
import json

#db database
#carregando as informacoes/Arquivo
file_path = "data.json" #arquivo principal
db = []
# db = [{task}, {task2}, etc...]
#indice	  0        1      2    etc...
time.sleep(0.5)
try: #tenta carregar o banco de dados padrao
	with open(file_path, "r") as json_file:
		db = json.load(json_file)
except FileNotFoundError:
	pass
	#caso nao tenha um banco de dados padrao

def  load_data():
	global db
	#Seletor do banco de dados *Banco de dados padrão, é "data.json"
	print("digite o nome do banco de dados (db.json)")
	file_path = input("")
	time.sleep(0.5)
	try:
		with open(file_path, "r") as json_file:
			db = json.load(json_file)
	except FileNotFoundError:    #Tratamento de erro para caso o arquivo não seja encontrado
		print("arquivo não encontrado - Verifique o nome")

#Se o banco de dados possuir informações, vai pegar o último id(última tarefa)
if db:
	task_id = db[-1]["id"] #pegando o id pelo indice (para pegar o indice: db[idx]) (indice comeca em 0)
else:
	task_id = 0

#Tela principal
#Formatação de print para estilizar a tela principal
def show_table():
	time.sleep(0.7)
	print(forma.sub + " "*53 + forma.end)
	print(forma.sub + "     |       Gerenciador de Tarefas     |" + " "*12 + forma.end)
	header = "ID   |   Descrição da Tarefa   | Status | Data"
	print(colors.cyan + header + colors.end)
	print("-" * len(header)) #
	for i in db:
		idx = i["id"]
		task = i["task"]
		data = i["data"]
		stats = i["stats"]
		print(f"{idx:03} | {task:<20} | {stats:<10} | {data}")
	input("\ntecle enter para voltar")
	time.sleep(0.5)
	print("_"*60)
		
#Tela das tarefas
def show_task(id):
	time.sleep(0.7)
	print(forma.sub + " "*53 + forma.end)
	print(forma.sub + "     |       Gerenciador de Tarefas     |" + " "*12 + forma.end)
	header = "ID   |   Descrição da Tarefa   | Status | Data"
	print(colors.cyan + header + colors.end)
	print("-" * len(header))
	
	i = id["id"]
	task = id["task"]
	stats = id["stats"]
	data = id["data"]
	print(f"{i:03} | {task:<20} | {stats:<10} | {data}")
	print("_"*60, "\n")
	print("""1. Editar tarefa
2. Excluir tarefa
obs: tecle enter ou qualquer tecla para voltar ao menu principal""")
	quest = input(" ")
	time.sleep(0.5)
	print("_"*60)

	if quest == "1":
		edit_task(i)
	elif quest == "2":
		delet_task(i)
	else:
		pass

#seletor de tarefa (Selecionar tarefa específica)
def selector():
	quest = int(input("digite um id(não use zeros a esquerda): "))
	print("_"*60)
	time.sleep(0.5)
	for i in db:
		if i["id"] == quest:
			print("\n")
			show_task(i)

#Adicionar tarefa
def add_task(n):
	global task_id
	n += 1
	task_id = n
	task = input("Nome da tarefa: ")
	data = input("Data (dd/mm/yy): ")
	print("_"*60)
	time.sleep(0.5)
	print("\n")
	new_task = {"id": n, "task": task, "stats": "incompleto", "data": data}
	db.append(new_task)

def edit_task(n):
	for idx, i in enumerate(db): #para encontrar o indice da tarefa, pelo id
		if i["id"] == n:
			pass
	
	print("""o que deseja editar?
1. Nome da tarefa
2. Status da tarefa
3. Data da tarefa""")
	quest = input("")
	print("_"*60)
	time.sleep(0.5)
	print("\n")
	if quest == "1":
		name = input("Digite o novo nome da tarefa: ")
		db[idx]["task"] = name
		print("\n")
	elif quest == "2":
		name = input("Digite o novo status da tarefa: ")
		db[idx]["stats"] = name
		print("\n")
	elif quest == "3":
		name = input("Digite a nova data da tarefa: ")
		db[idx]["data"] = name
		print("\n")
	print("_"*60)

def delet_task(n):
	for idx, i in enumerate(db): #para encontrar o indice da tarefa, pelo id
		if i["id"] == n:
			pass
	db.pop(idx) #metodo de remover um elemento pelo seu indice
	print("tarefa deletada com sucesso!")
	time.sleep(0.5)
	print("_"*60)

#Salvar alteração (No json_file)
def save_data():
	with open(file_path, "w") as json_file:
		json.dump(db, json_file, indent=4)  # `indent` para formatação legível
	time.sleep(0.5)
	print("Alterações salvas com sucesso!")
	print("_"*60)

#menu principal 
main_menu = True
while main_menu == True: #Carrega o menu principal quando true
	print("""\n1. Carregar um arquivo
2. Mostrar todas as tarefas
3. Selecionar uma tarefa
4. Adicionar tarefa
5. Salvar alterações
6. Sair
\n obs: \num banco de dados padrão sera carregado em falta de escolha\n7 para limpar o terminal""")
	#uso das """serve para selecionar todo o bloco como string"""

	choice = input("Escolha uma opção: ")
	print("_"*30)
	print("\n")
  match choice:
    case 1:
      load_data()
    case 2:
      show_table()
    case 3:
      view = True
      selector()
    case 4:
      add_task(task_id)
    case 5:
      save_data()
    case 6:
      print("Encerrando...")
      main_menu = False
      time.sleep(1)
    case 7:
      os.system("clear")
    case _:
      print("Opção inválida. Tente novamente.")
