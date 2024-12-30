from models.model_db_base import DbBase
from models.model_carrinho import Carrinho

from datetime import datetime

class Venda(DbBase):
    
    DB_VENDAS = "vendas"
    DB_PRODUTOS_VENDIDOS = "produtos_vendidos"

    @classmethod
    def finalizar_venda(cls, carrinho: Carrinho, total: float) -> None:
        """ Armazena uma venda no 'bd'
            Como ficará armazenado:
            id_venda, 'dd/mm/yyyy HH:MM', 'total'              
        """ 
        data = datetime.now().strftime("%d/%m/%Y %H:%M")  
        cls.salvar_na_db(cls.DB_VENDAS, [data, total])
        id_venda = cls.pegar_ultimo_id()
        
        """ Armazena o carrinho no 'bd' vinculado a venda 
            Como ficará armazenado:
            'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'                 
        """                        
        for item in carrinho.listar_itens():
            item["id_venda"] = id_venda
            cls.salvar_na_db(cls.DB_PRODUTOS_VENDIDOS, item.values(), criar_id=False)   

    @classmethod
    def listar_vendas(cls) -> list:
        """ Retorna uma lista com todas as vendas """
        return cls.pegar_todos_dados_db(cls.DB_VENDAS)    

    @classmethod
    def listar_produtos_por_venda(cls, id_venda) -> list:
        """ Retorna uma lista com todos os produtos de uma venda """
        produtos_da_venda = []        
        for item in cls.listar_produtos_vendidos():
            #'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'   
            if int(item[5]) == id_venda:
                produtos_da_venda.append(item)
        return produtos_da_venda
    
    @classmethod
    def listar_produtos_vendidos(cls) -> list:
        """ Retorna uma lista com todas os produtos vendidos """
        return cls.pegar_todos_dados_db(cls.DB_PRODUTOS_VENDIDOS)       

    @classmethod
    def pegar_ultimo_id(cls) -> int:
        dados = cls.listar_vendas()
        return sum(1 for x in dados)        

