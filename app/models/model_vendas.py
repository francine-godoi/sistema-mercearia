from models.model_db_base import DbBase
from models.model_carrinho import Carrinho

from datetime import datetime

class Venda(DbBase):
    
    DB_VENDAS = "vendas"
    DB_PRODUTOS_VENDIDOS = "produtos_vendidos"

    def finalizar_venda(self, carrinho: Carrinho, total: float) -> None:
        """ Armazena uma venda no 'bd'
            Como ficará armazenado:
            id_venda, 'dd/mm/yyyy HH:MM', 'total'              
        """ 
        data = datetime.now().strftime("%d/%m/%Y %H:%M")  
        self.salvar_na_db(self.DB_VENDAS, [data, total])
        id_venda = self.pegar_ultimo_id()
        
        """ Armazena o carrinho no 'bd' vinculado a venda 
            Como ficará armazenado:
            'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'                 
        """                        
        for item in carrinho.listar_itens():
            item["id_venda"] = id_venda
            self.salvar_na_db(self.DB_PRODUTOS_VENDIDOS, item.values(), criar_id=False)   

    def listar_vendas(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_todos_dados_db(self.DB_VENDAS)    

    def listar_produtos_por_venda(self, id_venda) -> list:
        """ Retorna uma lista com todos os produtos de uma venda """
        produtos_da_venda = []        
        for item in self.listar_produtos_vendidos():
            #'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'   
            if int(item[5]) == id_venda:
                produtos_da_venda.append(item)
        return produtos_da_venda
    
    def listar_produtos_vendidos(self) -> list:
        """ Retorna uma lista com todas os produtos vendidos """
        return self.pegar_todos_dados_db(self.DB_PRODUTOS_VENDIDOS)       

    def pegar_ultimo_id(self) -> int:
        dados = self.listar_vendas()
        return sum(1 for x in dados)        

