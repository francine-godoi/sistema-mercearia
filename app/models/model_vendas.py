from datetime import datetime
from utils.auxiliar_db import AuxiliarDB

class Venda(AuxiliarDB):
    
    NOME_BD = "vendas"

    def cadastrar_venda(self, data: datetime, total: float) -> None:
        """ Armazena uma venda no 'bd'           

        Como ficará armazenado:
        id_venda, 'dd/mm/yyyy HH:MM', 'total'              
        """ 
        self.salvar_na_db(self.NOME_BD, [data, total])
        return self.pegar_ultimo_id()
 

    def listar_vendas(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_todos_dados_db(self.NOME_BD)
        

    def pegar_ultimo_id(self) -> int:
        dados = self.listar_vendas()
        return sum(1 for x in dados)
    
