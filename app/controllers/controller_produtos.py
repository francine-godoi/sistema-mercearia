from views.view_produtos import ViewProdutos
from models.model_produtos import Produto

class ControllerProdutos:

    def __init__(self) -> None:        
        self.model_produto = Produto()
        self.view_produtos = ViewProdutos()

    def cadastrar_produto(self, nome: str, preco: str) -> None:
        """ Cadastra um produto no 'bd'
            :param nome: nome do produto
            :param type: string

            :param preco: preço do produto
            :param type: string

            :raise: ValueError: Valor inválido
        """     
        #TODO: não permitir cadastro de produto sem nome
        try:
            preco = float(preco.replace(',','.'))
            self.model_produto.cadastro_produto(nome, preco)
        except ValueError:
            print("Valor inválido. Dica: Não coloque pontos para separar os milhares.")
        else:
            print("Cadastrado com sucesso! \n")            


    def listar_produtos(self) -> None:
        """ Lista todos os produtos """
        produtos = self.model_produto.lista_produtos()
        self.view_produtos.visualizar_produtos(produtos)
