from models.model_db_base import DbBase

class Produto(DbBase):
    
    NOME_BD = "produtos"

    def cadastro_produto(self, nome: str, preco: float) -> None:
        """ Realiza o armazenamento dos dados dos produtos em DB (.csv)
                Como ficará armazenado:
                'id_produto', 'nome', 'preco_unit' 
        """       
        self.salvar_na_db(self.NOME_BD, [nome, preco])


    def lista_produtos(self) -> list:
        """ Retorna uma lista com todos os produtos """        
        return self.pegar_todos_dados_db(self.NOME_BD)
 
    
    def listar_produto_por_codigo(self, codigo: int) -> list: 
        """ Retorna uma lista com dados do produto filtrado pelo código(int) """                
        return self.pegar_dados_por_codigo(self.NOME_BD, codigo)              
        
    
