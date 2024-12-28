import csv
import os

project_root = os.path.dirname(os.path.dirname(__file__))
caminho = os.path.join(project_root, 'db')

class AuxiliarDB:    
    
    @staticmethod
    def salvar_na_db(nome_bd: str, dados: list) -> None:
        with open(f"{caminho}/{nome_bd}.csv", "a", newline="", encoding="utf-8") as csvfile:
            csv.writer(csvfile).writerow(dados)

    @staticmethod
    def pegar_todos_dados_db(nome_bd: str) -> list: 
        dados = []
        with open(f"{caminho}/{nome_bd}.csv", encoding="utf-8") as csvfile:
            for linha in csv.reader(csvfile):
                dados.append(linha)
        return dados
    
    @staticmethod
    def pegar_dados_por_codigo(nome_bd: str, codigo: int) -> list:         
        with open(f"{caminho}/{nome_bd}.csv", encoding="utf-8") as csvfile:
            return next((linha for linha in csv.reader(csvfile) if linha[0] == str(codigo)))


if __name__ == "__main__":
    aux = AuxiliarDB()
    dados = aux.pegar_todos_dados_db("produtos")
    print(dados)
    print(sum(1 for x in dados))
    print(aux.pegar_dados_por_codigo("produtos", 6))




