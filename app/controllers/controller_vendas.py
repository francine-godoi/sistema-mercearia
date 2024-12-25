from models.model_produtos import Produto
from models.model_vendas import Venda
from views.view_vendas import ViewVendas
from datetime import datetime


class ControllerVendas:

    def __init__(self) -> None:        
        self.model_produto = Produto()
        self.model_venda = Venda()
        self.view_vendas = ViewVendas()
        

    def cadastrar_venda(self) -> None:
        """ Cadastra as informações da venda
            :raise: ValueError: Código ou quantidade inválida
            :raise: IndexError: Código do produto inválido
        """
        produtos = self.model_produto.lista_produtos()        
        carrinho = []
        adicionar_mais_produtos = 's'

        #FIXME: erro ao selecionar código de produto inválido, parando app
        #TODO: caso tente adicionar o mesmo produto no carrinho, soma a quantidade ao invés de adicionar novamente
        while adicionar_mais_produtos == 's':
            try:
                codigo_produto, quantidade, adicionar_mais_produtos = self.view_vendas.tela_vendas(produtos)
                item_comprado = self.model_produto.listar_produto_por_codigo(int(codigo_produto))                
                pedido = self.montar_pedido(item_comprado, quantidade)           
                carrinho.append(pedido)
                total = self.calcular_total(carrinho)
                self.view_vendas.mostrar_carrinho(carrinho, total)
            except ValueError:
                print("Código ou quantidade inválidos. Por favor verifique e tente novamente.")
            except IndexError:
                print("Código do produto não encontrado. Consulte a lista de produtos.\n")
        
        if carrinho:
           data = datetime.now().strftime("%d/%m/%Y %H:%M")
           self.model_venda.cadastrar_venda(data, carrinho, total)


    def montar_pedido(self, item_comprado: dict, quantidade: int) -> dict:
        """ Monta o pedido para adicionar ao carrinho de compras
            :param item: lista com as informações do produto adicionado ao carrinho
            :param type: list

            :param quantidade: quantidade do produto
            :param type: int

            :return: dicionário com as informações da venda
            :rtype: dict
        """ 
        nome, valor = item_comprado["nome"], item_comprado["preco"]        

        subtotal = self.calcular_subtotal(quantidade, valor)
        pedido = {"nome": nome,
                  "quantidade": quantidade,
                  "valor": valor,
                  "subtotal": subtotal}
        return pedido

    @classmethod
    def calcular_subtotal(cls, quantidade: int, valor: float) -> float:
        """ Retorna o subtotal de uma compra
            :param quantidade: quantidade comprada
            :param type: int

            :param valor: valor do produto
            :param type: float

            :return: subtotal da compra de um produto
            :rtype: float
        """
        return int(quantidade) * float(valor)    

    @classmethod
    def calcular_total(cls, carrinho: list) -> float:
        """ Calcula o valor total da compra
         
            :param carrinho: todos os item comprados
            :param type: list

            :return: soma de totos os subtotais
            :rtype: float     
        """
        return sum(item["subtotal"] for item in carrinho)


    def relatorio_vendas(self) -> None:
        """ Gera um relatório com todas as vendas realizadas """
        vendas = self.model_venda.listar_vendas()
        self.view_vendas.gerar_relatorio_vendas(vendas)
