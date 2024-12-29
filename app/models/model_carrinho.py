from utils.auxiliar_db import AuxiliarDB

class Carrinho(AuxiliarDB):
    
    NOME_BD = "carrinhos"

    def salvar_carrinho(self, id_venda: int, carrinho: list) -> None:
        """ Armazena o carrinho no 'bd' vinculado a venda          

        Como ficará armazenado:
        'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'                 
        """                
        for item in carrinho:
            item["fk_id"] = id_venda
            self.salvar_na_db(self.NOME_BD, item.values(), criar_id=False)        
  

    def listar_carrinho(self, cod_venda) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_dados_por_codigo(self.NOME_BD, cod_venda)
    
    
    def listar_todos_carrinhos(self) -> list:
        """ Retorna uma lista com todas as vendas """
        return self.pegar_todos_dados_db(self.NOME_BD)
        