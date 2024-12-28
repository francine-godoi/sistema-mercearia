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
            :raise: StopIteration: Código do produto não encontrado.
        """
        produtos = self.model_produto.lista_produtos()        
        carrinho = []
        adicionar_mais_produtos = 's'

        while adicionar_mais_produtos == 's':
            codigo_produto, quantidade, adicionar_mais_produtos = self.view_vendas.tela_vendas(produtos)

            if codigo_produto == "" or quantidade == "":
                print("Informações em branco. Por favor verifique e tente novamente")
                return
            
            try:
                codigo_produto = int(codigo_produto)
                quantidade = int(quantidade)
            except ValueError:
                print("Código ou quantidade inválidos. Por favor verifique e tente novamente.")
                return

            try:                
                item_comprado = self.model_produto.listar_produto_por_codigo(codigo_produto)
            except StopIteration:
                print("Código do produto não encontrado. Consulte a lista de produtos.\n")
                return            
            
            qtde_no_carrinho = 0
            if carrinho: # Caso já tenha o mesmo item no carrinho, soma suas quantidades
                
                # item_comprado = ['código', 'nome', 'valor']                

                qtde_no_carrinho = sum([item["quantidade"] for item in carrinho if item["produto"] == item_comprado[1]])
                try:  # remove item para evitar duplicidade            
                    item_duplicado = [item for item in carrinho if item["produto"] == item_comprado[1]]                
                    carrinho.remove(item_duplicado[0]) 
                except IndexError: # não achou duplicados
                    pass
                else:
                    print("Produto já se encontra no carrinho. Sua quantidade será atualizada!")

            pedido = self.montar_pedido(item_comprado, (quantidade + qtde_no_carrinho))
            carrinho.append(pedido)
            total = self.calcular_total(carrinho)
            self.view_vendas.mostrar_carrinho(carrinho, total)
        
        if carrinho: # se montou um carrinho com sucesso, salva a venda
           data = datetime.now().strftime("%d/%m/%Y %H:%M")
           self.model_venda.cadastrar_venda(data, carrinho, total)

    @staticmethod
    def montar_pedido(item_comprado: dict, quantidade: int) -> dict:
        """ Monta o pedido para adicionar ao carrinho de compras""" 
        
        codigo, nome, valor = item_comprado

        subtotal = int(quantidade) * float(valor)
        pedido = {"codigo": codigo,
                  "produto": nome,
                  "quantidade": quantidade,
                  "valor": valor,
                  "subtotal": subtotal}
        return pedido

    @staticmethod
    def calcular_total(carrinho: list) -> float:
        """ Calcula o valor total da compra"""
        return sum(item["subtotal"] for item in carrinho)


    def relatorio_vendas(self) -> None:
        """ Gera um relatório com todas as vendas realizadas """
        vendas = self.model_venda.listar_vendas()
        self.view_vendas.gerar_relatorio_vendas(vendas)
