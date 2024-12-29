from utils.auxiliar_db import AuxiliarDB

class ProdutosVendidos(AuxiliarDB):
    
    NOME_BD = "produtos_vendidos"

    def __init__(self):
        self.carrinho = []
    
    def adicionar_item(self, item_comprado: dict, quantidade: int) -> dict:
        """ Monta o pedido para adicionar ao carrinho de compras"""         
        codigo, nome_produto, preco_unit = item_comprado.values()

        subtotal = int(quantidade) * float(preco_unit)
        item = {"codigo": codigo,
                "produto": nome_produto,
                "quantidade": quantidade,
                "preco_unit": preco_unit,
                "subtotal": subtotal}
        self.carrinho.append(item)      
    
    def remover_item(self, item_duplicado) -> None:
        """ Remove item duplicado do carrinho """                
        self.carrinho.remove(item_duplicado) 

    def listar_itens(self) -> list:
        """ Retorna uma lista com todos os produtos """        
        return self.carrinho    

    def limpar_carrinho(self):
            self.carrinho = []      

    def salvar_carrinho(self, id_venda):
        """ Armazena o carrinho no 'bd' vinculado a venda          

        Como ficará armazenado:
        'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'                 
        """                        
        for item in self.carrinho:
            item["fk_id"] = id_venda
            self.salvar_na_db(self.NOME_BD, item.values(), criar_id=False)        
  

    def listar_produtos_por_venda(self, cod_venda) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_dados_por_codigo(self.NOME_BD, cod_venda)
    
    
    def listar_produtos_vendidos(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_todos_dados_db(self.NOME_BD)
        
