from views.view_produtos import ViewProdutos
from models.model_produtos import Produto

class ControllerProdutos:

    def __init__(self) -> None:        
        self.produto = Produto()
        self.tela_produtos = ViewProdutos()

    def cadastrar_produto(self) -> None:
        """ Cadastra um produto no 'bd'
            :raise: ValueError: Valor inválido
        """     
        nome, preco = self.tela_produtos.exibir_form_cadastro_produto()

        # Inicio validação de dados
        if nome == "":
            print("Nome do produto não pode ser em branco.\n")
            return self.cadastrar_produto()
        
        if not self.preco_valido(preco):
            return self.cadastrar_produto()    
        # Fim validação Dados

        preco = float(preco.replace(',','.'))
        self.produto.cadastrar_produto(nome, preco)
        print("Cadastrado com sucesso! \n")            

    def preco_valido(self, preco):
        if preco == "":
            print("Preço não pode ficar em branco.\n")
            return False
        
        try:
            preco = float(preco.replace(',','.'))                
        except ValueError:
            print("Preço deve ser em números.\n")
            return False
        
        if preco <= 0:
            print("Valor deve ser maior que zero.\n")
            return False  

        return True
        
    def listar_produtos(self) -> None:
        """ Lista todos os produtos """
        produtos = self.produto.listar_produtos()
        self.tela_produtos.exibir_lista_produtos(produtos)
