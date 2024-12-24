from datetime import datetime
class Venda:
    
    def __init__(self) -> None:        
        self.vendas = []


    def cadastrar_venda(self, data: datetime, carrinho: list, total: float) -> None:
        """ Armazena uma venda no 'bd'
        :param data: data da venda
        :param type: datetime

        :param carrinho: carrinho de compras
        :param type: lista de dicionários
        
        :param total: valor total da venda
        :param type: float      

        Como ficará armazenado na lista:
            >[{"data": 'dd/mm/yyyy HH:MM',\n
            >"pedido": [{'nome': 'nome_produto', 'quantidade': int, 'valor': float, 'subtotal': float}],\n
            >"total": float}]              
        """ 
        self.vendas.append({"data": data, "pedido":carrinho, "total":total}) 
  

    def listar_vendas(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.vendas
        
