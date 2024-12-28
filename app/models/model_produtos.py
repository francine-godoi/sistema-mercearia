from utils.auxiliar_db import AuxiliarDB

class Produto(AuxiliarDB):

    #_produtos = []
    NOME_BD = "produtos"

    def __init__(self) -> None:
    #    self.produtos = self._produtos
        self.nome_bd = self.NOME_BD


    def cadastro_produto(self, nome: str, preco: float) -> None:
        """ Realiza o armazenamento de um dicionário com os dados dos produtos no 'bd'
            :param nome: nome do produto
            :param type: str

            :param preco: preço do produto
            :param type: float
        """
        # codigo = self.get_codigo(self.produtos)
        # self.produtos.append({"codigo": codigo + 1,
        #                       "nome": nome,
        #                       "preco": preco})

        codigo = self.get_codigo(self.lista_produtos())
        dados = [codigo, nome, preco]
        self.salvar_na_db(self.NOME_BD, dados)


    def lista_produtos(self) -> list:
        """ Retorna uma lista com todos os produtos """
        #return self.produtos
        return self.pegar_todos_dados_db(self.NOME_BD)
 
    #TODO resolver como fica essa função usando DB
    def listar_produto_por_codigo(self, codigo: int) -> dict: 
        """ Retorna um dicionario com um produto filtrado pelo código
            :param codigo: código do produto
            :param type: int

            :return: Dicionário com um produto
            :rtype: dict
        """            
        #return next(produto for produto in self.produtos if produto["codigo"] == codigo)
        return self.pegar_dados_por_codigo(self.NOME_BD, codigo)              
        
    
    @staticmethod
    def get_codigo(produtos: list) -> int: 
        """ Pega a quantidade de produtos na lista para determinar o código do próximo
            :param produtos:  todos os produtos cadastrados
            :param type: list

            :return: quantidade de produtos armazenados
            :rtype: int
        """          
        return sum(1 for item in produtos) + 1
    
