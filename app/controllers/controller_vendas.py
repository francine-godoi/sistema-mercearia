from models.model_produtos import Produto
from models.model_vendas import Venda
from models.model_carrinho import Carrinho
from views.view_vendas import ViewVendas

from datetime import datetime

class ControllerVendas:

    def __init__(self) -> None:        
        self.produto = Produto()
        self.venda = Venda()
        self.carrinho = Carrinho()                     
        self.tela_vendas = ViewVendas()     
        

    def cadastrar_venda(self) -> None:
        """ Cadastra as informações da venda
            :raise: ValueError: Código ou quantidade inválida
            :raise: IndexError: Código do produto inválido
            :raise: StopIteration: Código do produto não encontrado.
        """        
        lista_produtos = self.produto.listar_produtos()        
        adicionar_mais_produtos = 's'

        while adicionar_mais_produtos == 's':
            codigo_produto, quantidade, adicionar_mais_produtos = self.tela_vendas.exibir_form_cadastro_venda(lista_produtos)

            # Inicio Validação de dados            
            if not self.codigo_valido(codigo_produto) or not self.quantidade_valida(quantidade):
                return self.cadastrar_venda()           
            # Fim Validação de dados

            # Começo processo de vendas
            codigo_produto = int(codigo_produto)
            quantidade = int(quantidade)
            item_comprado = self.produto.listar_produto_por_codigo(codigo_produto)

            # verifica se já tenha o mesmo item no carrinho e pega sua quantidade      
            qtde_no_carrinho = self.quantidade_item_duplicado(item_comprado) 

            self.carrinho.adicionar_item(item_comprado, (quantidade + qtde_no_carrinho))            
            total_venda = self.calcular_total()
            self.tela_vendas.exibir_itens_carrinho(self.carrinho.listar_itens(), total_venda)
        
        if self.carrinho: # se montou um carrinho com sucesso, salva a venda           
           self.venda.finalizar_venda(self.carrinho, total_venda)
           self.carrinho.limpar_carrinho()
           print(f"Vendas finalizada com sucesso! Pedido nº {self.venda.pegar_ultimo_id()}\n\n")


    def quantidade_item_duplicado(self, item_comprado) -> int:
        """ Se existe um carrinho, verifica se já tenha o mesmo item e soma suas quantidades """
        qtde_no_carrinho = 0            
        if self.carrinho:
            # item_comprado = ['código', 'nome', 'preco_unit']                
            for item in self.carrinho.listar_itens():                                       
                if item["codigo"] == item_comprado[0]: # caso o produto já está no carrinho
                    qtde_no_carrinho = item["quantidade"] # pega a quantidade
                    self.carrinho.remover_item(item) # remove item para evitar duplicidade  
                    print("Produto já se encontra no carrinho. Sua quantidade será atualizada!")
                    break        
        return qtde_no_carrinho
    

    def calcular_total(self) -> float:
        """ Calcula o valor total da compra"""

        return sum(item["subtotal"] for item in self.carrinho.listar_itens())


    def codigo_valido(self, codigo_produto) -> bool:
        """ Validação de código """

        if codigo_produto == "":
            print("Código não pode ficar em branco.\n")
            return False
        
        try:
            codigo_produto = int(codigo_produto)
        except ValueError:
            print("Código deve ser um número.\n")
            return False
                                
        try:                
            self.produto.listar_produto_por_codigo(codigo_produto)
        except StopIteration:
            print("Código do produto não encontrado. Consulte a lista de produtos.\n")
            return False
        
        return True

    
    def quantidade_valida(self, quantidade) -> bool:
        """ Validação de quantidade """

        if quantidade == "":
            print("Quantidade não pode ficar em branco.\n")
            return False
        
        try:
            quantidade = int(quantidade)
        except ValueError:
            print("Quantidade deve ser um número.\n")
            return False
                                
        if quantidade < 1:
            print("Quantidade não pode ser menor que 1.\n")
            return False

        return True


    def relatorio_vendas(self) -> None:
        """ Gera um relatório com todas as vendas realizadas """        
        vendas = self.venda.listar_vendas()
        produtos_vendidos = self.venda.listar_produtos_vendidos()
        self.tela_vendas.exibir_relatorio_vendas(vendas, produtos_vendidos)


    def relatorio_venda_data(self) -> None:
        """ Gera um relatório com as vendas filtradas por data """
        formato_data = "%d/%m/%Y"
        data_inicial = input("Data Inicial: dd/mm/aaaa: ")
        data_final = input("Data Inicial: dd/mm/aaaa: ")

        try:
            data_inicial = datetime.strptime(data_inicial, formato_data)
            data_final = datetime.strptime(data_final, formato_data)
        except ValueError:
            print("Data no formato errado. Tente novamente.\n")
            return self.relatorio_venda_data()

        # id_venda, 'dd/mm/yyyy HH:MM', 'total' 
        vendas = []
        for item in self.venda.listar_vendas():
            data_venda = item[1].split(" ")
            data_venda = datetime.strptime(data_venda[0], formato_data) 
            if data_inicial <= data_venda <= data_final:
                vendas.append(item)

        produtos_vendidos = self.venda.listar_produtos_vendidos()
        self.tela_vendas.exibir_relatorio_vendas(vendas, produtos_vendidos)


    def consultar_venda_codigo(self) -> None:
        """ Exibe as informações de uma Venda especifica """

        codigo_venda = input("Número do pedido: ")
        if codigo_venda == "":
            print("Código não pode ficar em branco.\n")
            return self.consultar_venda_codigo()
        
        try:
            codigo_venda = int(codigo_venda)
        except ValueError:
            print("Código deve ser um número.\n")
            return self.consultar_venda_codigo()
        
        try:
            vendas = self.venda.listar_vendas_codigo(codigo_venda)
        except StopIteration:
            print(f"Pedido nº {codigo_venda} não encontrado.\n")
            return
        
        produtos_vendidos = self.venda.listar_produtos_por_venda(codigo_venda)
        self.tela_vendas.exibir_venda(vendas, produtos_vendidos)