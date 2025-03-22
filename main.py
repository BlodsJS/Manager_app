import json
import os

class ManagerDB:
    def __init__(self, db_path: str = "themes.json"):
        self.db_path = db_path
        self.data = None
        self.is_loaded = False
        self._connect()

    def _connect(self):
        """Tenta carregar o arquivo JSON ou cria um novo se houver falha"""
        try:
            # Tenta carregar o arquivo existente
            with open(self.db_path, 'r') as f:
                self.data = json.load(f)
            self.is_loaded = True
            
        except FileNotFoundError:
            print(f"Arquivo {self.db_path} não encontrado. Criando novo banco de dados.")
            self._create_new_db()
            
        except json.JSONDecodeError:
            print(f"Arquivo {self.db_path} corrompido. Criando novo banco de dados.")
            self._create_new_db()
            
        except Exception as e:
            print(f"Erro inesperado ao carregar o banco de dados: {str(e)}")
            self.is_loaded = False

    def _create_new_db(self):
        """Cria uma nova estrutura de banco de dados vazia"""
        self.data = {
        	"themes": [],
        	"Id": "black",
        	"desc": "blue",
        	"date": "yellow",
        	"nodate": "red"
        }  # Exemplo de estrutura inicial
        self.is_loaded = self.save()

    def save(self):
        """Salva os dados no arquivo JSON"""
        try:
            with open(self.db_path, 'w') as f:
                json.dump(self.data, f, indent=4)
            return True
        except Exception as e:
            print(f"Erro ao salvar o banco de dados: {str(e)}")
            return False

    # Exemplo de método adicional para manipulação de dados
    def add_theme(self, theme_data: dict):
        if self.is_loaded:
            self.data["themes"].append(theme_data)
            return self.save()
        return False
        
        
db = ManagerDB()

print(db.data)
for i in db.data:
    print(f"{i}: {db.data[i]}")
