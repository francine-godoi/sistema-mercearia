from views.view_produtos import ViewProdutos
from models.model_produtos import Produto

class ControllerProdutos:

    def __init__(self) -> None:        
        self.model_produto = Produto()
        self.view_produtos = ViewProdutos()

    def cadastrar_produto(self, nome: str, preco: str) -> None:
        """ Cadastra um produto no 'bd'
            :raise: ValueError: Valor inválido
        """     
        # Inicio validação de dados

        if nome == "" or preco == "":
            print("Valores em branco. Verifique e tente novamente.\n")
            return
        try:
            preco = float(preco.replace(',','.'))                
        except ValueError:
            print("Valor inválido. Dica: Não coloque pontos para separar os milhares.")
            return
        
        if preco <= 0:
            print("Valor inválido. Não pode ser menor ou igual a zero")
            return
        
        # Fim validação Dados
        
        self.model_produto.cadastro_produto(nome, preco)
        print("Cadastrado com sucesso! \n")            


    def listar_produtos(self) -> None:
        """ Lista todos os produtos """
        produtos = self.model_produto.lista_produtos()
        self.view_produtos.visualizar_produtos(produtos)
