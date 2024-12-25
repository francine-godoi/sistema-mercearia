class Produto:

    _produtos = []

    def __init__(self) -> None:
        self.produtos = self._produtos


    def cadastro_produto(self, nome: str, preco: float) -> None:
        """ Realiza o armazenamento de um dicionário com os dados dos produtos no 'bd'
            :param nome: nome do produto
            :param type: str

            :param preco: preço do produto
            :param type: float
        """
        codigo = self.get_codigo(self.produtos)
        self.produtos.append({"codigo": codigo + 1,
                              "nome": nome,
                              "preco": preco})


    def lista_produtos(self) -> list:
        """ Retorna uma lista com todos os produtos """
        return self.produtos
 
    
    def listar_produto_por_codigo(self, codigo: int) -> dict: 
        """ Retorna um dicionario com um produto filtrado pelo código
            :param codigo: código do produto
            :param type: int

            :return: Dicionário com um produto
            :rtype: dict
        """       
        
        return next(produto for produto in self.produtos if produto["codigo"] == codigo)       
        
    
    @classmethod
    def get_codigo(cls, produtos: list) -> int: 
        """ Pega a quantidade de produtos na lista para determinar o código do próximo
            :param produtos:  todos os produtos cadastrados
            :param type: list

            :return: quantidade de produtos armazenados
            :rtype: int
        """  
        return sum(1 for item in produtos)
    
