from views.view_produtos import ViewProdutos

class ViewVendas:

    def __init__(self):
         self.view_produtos = ViewProdutos()
  
    def cadastrar_nova_venda(self, produtos: list) -> list:
            """ Mostra a tela de vendas
                :param produtos: lista com todos os produtos
                :param type: list

                :return: código e quantidade do produto vendido e uma flag (str: 's' ou 'n') avisando se o cliente deseja adicionar novo produto ao carrinho de compras
                :rtype: list
            """
            print("--------------- Vendas ---------------\n")
                        
            self.view_produtos.visualizar_produtos(produtos)
            codigo = input("Código do produto que deseja comprar: ")

            # produtos = 'id_produto', 'nome', 'preco_unit'
            if codigo: 
                try:                
                    print(f"Produto: {next(produto[1] for produto in produtos if produto[0] == codigo)}")
                except StopIteration:
                    pass 

            quantidade = input("Quantidade: ")
            continuar = ''

            while continuar != 's' and continuar != 'n':
                continuar = input("Adicionar mais produtos? s/n ").lower()
            return [codigo, quantidade, continuar]
    

    def mostrar_carrinho(self, carrinho: list, total: float) -> None:
        """ Mostra o carrinho de compras """

        print("\n--------------- Seu Carrinho ---------------")

        for item in carrinho:
            descricao = f'Produto: {item["produto"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["preco_unit"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
            print(descricao.replace(".",","))
            
        print("-----------------------------------------------")
        print(f"Total: R${float(total):.2f}")
        print("\n")


    def gerar_relatorio_vendas(self, vendas: list, carrinho: list) -> None:  
        """ Mostra o relatório de todas as vendas realizadas
            :param vendas: lista com todas as vendas
            :param type: list

            :param carrinho: lista com todas os carrinhos
            :param type: list
        """      
        print("\n---------------------------Relatório de Vendas---------------------------")
        
        # 'id_venda', 'data/hora', 'total'
        for venda in vendas:
            print(f"\nPedido nº{venda[0]} - Data do pedido: {venda[1]}")
            print("-------------------------------------------------------------------------")
             
            # 'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'
            for item in carrinho:
                if item[5] == venda[0]: # FK do carrinho é o mesma ID da venda
                    descricao = f'Produto: {item[1]} - Qtde: {item[2]} - Valor UN - R${float(item[3]):.2f} - Sub-Total: R${float(item[4]):.2f}'
                    print(descricao.replace(".",","))
            
            print("-------------------------------------------------------------------------")   
            print(f'Total do Pedido: R${float(venda[2]):.2f}\n')
            print("-------------------------------------------------------------------------")            
        
        print(f"\nTotal das vendas: R$ {sum([float(venda[2]) for venda in vendas]):.2f}\n")
        print("-------------------------------------------------------------------------\n\n")            