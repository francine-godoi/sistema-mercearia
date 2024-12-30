import csv
import os

project_root = os.path.dirname(os.path.dirname(__file__))
caminho = os.path.join(project_root, 'db')

class DbBase:    
    
    @classmethod
    def salvar_na_db(cls, nome_bd: str, dados: list, criar_id: bool = True) -> None:
        if criar_id:
            dados.insert(0, cls.gerar_id(nome_bd))

        with open(f"{caminho}/{nome_bd}.csv", "a", newline="", encoding="utf-8") as csvfile:
            csv.writer(csvfile).writerow(dados) 

        
    @classmethod
    def pegar_todos_dados_db(cls, nome_bd: str) -> list: 
        dados = []
        with open(f"{caminho}/{nome_bd}.csv", encoding="utf-8") as csvfile:
            for linha in csv.reader(csvfile):
                dados.append(linha)
        return dados
    
    
    @classmethod
    def pegar_dados_por_codigo_db(cls, nome_bd: str, codigo: int) -> list:         
        with open(f"{caminho}/{nome_bd}.csv", encoding="utf-8") as csvfile:
            return next((linha for linha in csv.reader(csvfile) if linha[0] == str(codigo)))

    @classmethod
    def gerar_id(cls, nome_bd: str) -> int:        
        # pega a proxima id caso já exista dados cadastrados, senão retorna id 1        
        if os.path.isfile(f"{caminho}/{nome_bd}.csv"):
            dados = cls.pegar_todos_dados_db(nome_bd)
            return sum(1 for x in dados) + 1
        return 1





