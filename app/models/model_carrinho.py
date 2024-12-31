class Carrinho():

    def __init__(self):
        self.carrinho = []
    
    def adicionar_item(self, item_comprado: dict, quantidade: int) -> dict:
        """ Monta o pedido para adicionar ao carrinho de compras"""         
        codigo, nome_produto, preco_unit = item_comprado

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

    def limpar_carrinho(self) -> None:
            """ Limpa as informações do carrinho """
            self.carrinho = []      

      
  

        
