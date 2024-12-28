from models.model_produtos import Produto
from models.model_vendas import Venda
from models.model_carrinho import Carrinho
from views.view_vendas import ViewVendas

from datetime import datetime

class ControllerVendas:

    def __init__(self) -> None:        
        self.model_produto = Produto()
        self.model_venda = Venda()
        self.model_carrinho = Carrinho()
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

            # Inicio de válidação de dados
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
            
            # Com dados ok, inicia o processo de vendas

            # Se existe um carrinho, verifica se já tenha o mesmo item e soma suas quantidades          
            qtde_no_carrinho = 0
            if carrinho:                 
                # item_comprado = ['código', 'nome', 'preco_unit']                
                qtde_no_carrinho = sum([item["quantidade"] for item in carrinho if item["codigo"] == item_comprado[0]])

                try:  # remove item para evitar duplicidade            
                    item_duplicado = [item for item in carrinho if item["codigo"] == item_comprado[0]]                
                    carrinho.remove(item_duplicado[0]) 
                except IndexError: # não achou duplicados
                    pass
                else:
                    print("Produto já se encontra no carrinho. Sua quantidade será atualizada!")

            pedido = self.montar_pedido(item_comprado, (quantidade + qtde_no_carrinho))
            carrinho.append(pedido)
            total_venda = self.calcular_total(carrinho)
            self.view_vendas.mostrar_carrinho(carrinho, total_venda)
        
        if carrinho: # se montou um carrinho com sucesso, salva a venda           
           data = datetime.now().strftime("%d/%m/%Y %H:%M")           
           self.model_venda.cadastrar_venda(data, total_venda)
           id_venda = self.model_venda.pegar_ultimo_id()          
           self.model_carrinho.salvar_carrinho(id_venda, carrinho)

    @staticmethod
    def montar_pedido(item_comprado: dict, quantidade: int) -> dict:
        """ Monta o pedido para adicionar ao carrinho de compras""" 
        
        codigo, nome_produto, preco_unit = item_comprado

        subtotal = int(quantidade) * float(preco_unit)
        pedido = {"codigo": codigo,
                  "produto": nome_produto,
                  "quantidade": quantidade,
                  "preco_unit": preco_unit,
                  "subtotal": subtotal}
        return pedido

    @staticmethod
    def calcular_total(carrinho: list) -> float:
        """ Calcula o valor total da compra"""
        return sum(item["subtotal"] for item in carrinho)


    def relatorio_vendas(self) -> None:
        """ Gera um relatório com todas as vendas realizadas """
        vendas = self.model_venda.listar_vendas()
        carrinhos = self.model_carrinho.listar_todos_carrinhos()
        self.view_vendas.gerar_relatorio_vendas(vendas, carrinhos)
