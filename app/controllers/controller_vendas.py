from models.model_produtos import Produto
from models.model_vendas import Venda
from models.model_produtos_vendidos import ProdutosVendidos
from views.view_vendas import ViewVendas

from datetime import datetime

class ControllerVendas:

    def __init__(self) -> None:        
        self.model_produto = Produto()                
        self.view_vendas = ViewVendas()   
        self.carrinho = ProdutosVendidos()            
        

    def cadastrar_venda(self) -> None:
        """ Cadastra as informações da venda
            :raise: ValueError: Código ou quantidade inválida
            :raise: IndexError: Código do produto inválido
            :raise: StopIteration: Código do produto não encontrado.
        """        
        lista_produtos = self.model_produto.lista_produtos()        
        adicionar_mais_produtos = 's'

        while adicionar_mais_produtos == 's':
            codigo_produto, quantidade, adicionar_mais_produtos = self.view_vendas.tela_vendas(lista_produtos)

            # Inicio Validação de dados

            if codigo_produto == "" or quantidade == "":
                print("Informações em branco. Por favor verifique e tente novamente")
                return
            
            try:
                codigo_produto = int(codigo_produto)
                quantidade = int(quantidade)
            except ValueError:
                print("Código ou quantidade inválidos. Por favor verifique e tente novamente.")
                return
                                    
            if quantidade < 1:
                print("Quantidade não pode ser menor que 1. Por favor verifique e tente novamente")
                return

            try:                
                item_comprado = self.model_produto.listar_produto_por_codigo(codigo_produto)
            except StopIteration:
                print("Código do produto não encontrado. Consulte a lista de produtos.\n")
                return            
            
            # Fim Validação de dados


            # Começo processo de vendas

            # Se existe um carrinho, verifica se já tenha o mesmo item e soma suas quantidades          
            qtde_no_carrinho = 0            
            if self.carrinho:
                # item_comprado = ['código', 'nome', 'preco_unit']                
                for item in self.carrinho.listar_itens():                                       
                    if item["codigo"] == item_comprado[0]: # caso o produto já está no carrinho
                        qtde_no_carrinho = item["quantidade"] # pega a quantidade
                        self.carrinho.remover_item(item) # remove item para evitar duplicidade  
                        print("Produto já se encontra no carrinho. Sua quantidade será atualizada!")

            self.carrinho.adicionar_item(item_comprado, (quantidade + qtde_no_carrinho))            
            total_venda = self.calcular_total()
            self.view_vendas.mostrar_carrinho(self.carrinho.listar_itens(), total_venda)
        
        if self.carrinho: # se montou um carrinho com sucesso, salva a venda           
           data = datetime.now().strftime("%d/%m/%Y %H:%M")  
           venda = Venda()                   
           id_venda = venda.cadastrar_venda(data, total_venda)
           
           self.carrinho.salvar_carrinho(id_venda)
           self.carrinho.limpar_carrinho()
           
    
    def calcular_total(self) -> float:
        """ Calcula o valor total da compra"""
        return sum(item["subtotal"] for item in self.carrinho.listar_itens())


    def relatorio_vendas(self) -> None:
        """ Gera um relatório com todas as vendas realizadas """
        vendas = Venda().listar_vendas()
        produtos_vendidos = ProdutosVendidos().listar_produtos_vendidos()
        self.view_vendas.gerar_relatorio_vendas(vendas, produtos_vendidos)
