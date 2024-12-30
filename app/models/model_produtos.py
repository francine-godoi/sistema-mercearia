from models.model_db_base import DbBase

class Produto(DbBase):
    
    NOME_BD = "produtos"

    @classmethod
    def cadastrar_produto(cls, nome: str, preco: float) -> None:
        """ Realiza o armazenamento dos dados dos produtos em DB (.csv)
                Como ficará armazenado:
                'id_produto', 'nome', 'preco_unit' 
        """       
        cls.salvar_na_db(cls.NOME_BD, [nome, preco])

    @classmethod
    def listar_produtos(cls) -> list:
        """ Retorna uma lista com todos os produtos """        
        return cls.pegar_todos_dados_db(cls.NOME_BD)
 
    @classmethod
    def listar_produto_por_codigo(cls, codigo: int) -> list: 
        """ Retorna uma lista com dados do produto filtrado pelo código(int) """                
        return cls.pegar_dados_por_codigo_db(cls.NOME_BD, codigo)              
        
    
