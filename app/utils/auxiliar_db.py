import csv
import os

project_root = os.path.dirname(os.path.dirname(__file__))
caminho = os.path.join(project_root, 'db')

class AuxiliarDB:    
    
    def salvar_na_db(self, nome_bd: str, dados: list) -> None:
        dados.insert(0, self.gerar_id(nome_bd))
        with open(f"{caminho}/{nome_bd}.csv", "a", newline="", encoding="utf-8") as csvfile:
            csv.writer(csvfile).writerow(dados) 

    def salvar_na_tabela_aux(self, nome_bd: str, fk_id: int, dados: list) -> None:        
        with open(f"{caminho}/{nome_bd}.csv", "a", newline="", encoding="utf-8") as csvfile:
            escrever = csv.writer(csvfile) 
            for dado in dados:
                dado["fk_id"] = fk_id
                escrever.writerow(dado.values())
        
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

    
    def gerar_id(self, nome_bd: str) -> int:        
        # pega a proxima id caso já exista dados cadastrados, senão retorna id 1        
        if os.path.isfile(f"{caminho}/{nome_bd}.csv"):
            dados = self.pegar_todos_dados_db(nome_bd)
            return sum(1 for x in dados) + 1
        return 1


if __name__ == "__main__":
    aux = AuxiliarDB()
    dados = aux.pegar_todos_dados_db("vendas")
   # for dado in dados:
   #     print(str(dado[2]).split(","))
    #print(sum(1 for x in dados))
    #print(aux.pegar_dados_por_codigo("vendas", 1))

    lista = [{'nome': 'nome_produto', 'quantidade': 1, 'valor': 1.1, 'subtotal': 1.0}, {'nome': 'nome_produto', 'quantidade': 1, 'valor': 1.1, 'subtotal': 1.0}]            
    aux.salvar_na_db_aux("carrinho", 1, lista)




