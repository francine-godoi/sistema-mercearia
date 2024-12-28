from datetime import datetime
from utils.auxiliar_db import AuxiliarDB

class Venda(AuxiliarDB):
    
    NOME_BD = "vendas"

    def __init__(self) -> None:    
        self.nome_bd = self.NOME_BD


    def cadastrar_venda(self, data: datetime, carrinho: list, total: float) -> None:
        """ Armazena uma venda no 'bd'           

        Como ficará armazenado na lista:
        ['dd/mm/yyyy HH:MM', [{'nome': 'nome_produto', 'quantidade': int, 'valor': float, 'subtotal': float}],'total']              
        """ 
        self.salvar_na_db(self.nome_bd, [data, carrinho, total])
        #self.vendas.append({"data": data, "pedido":carrinho, "total":total}) 
  

    def listar_vendas(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_todos_dados_db(self.nome_bd)
        
