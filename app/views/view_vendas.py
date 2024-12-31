from views.view_produtos import ViewProdutos

class ViewVendas:

    def __init__(self):
         self.tela_produtos = ViewProdutos()
  
    def exibir_form_cadastro_venda(self, produtos: list) -> list:
            """ Mostra a tela de vendas """

            print("--------------- Vendas ---------------\n")
                        
            self.tela_produtos.exibir_lista_produtos(produtos)
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
    

    def exibir_itens_carrinho(self, carrinho: list, total: float) -> None:
        """ Mostra o carrinho de compras """

        print("\n--------------- Seu Carrinho ---------------")

        for item in carrinho:
            descricao = f'Produto: {item["produto"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["preco_unit"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
            print(descricao.replace(".",","))
            
        print("-----------------------------------------------")
        print(f"Total: R${float(total):.2f}")
        print("\n")


    def exibir_relatorio_vendas(self, vendas: list, carrinho: list) -> None:  
        """ Mostra o relatório de todas as vendas realizadas"""      

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


    def exibir_venda(self, vendas: list, carrinho: list) -> None: 
        """ Mostra os dados de uma venda consultada por código """    

        print("\n---------------------------Consulta Vendas------------------------------")
        
        # 'id_venda', 'data/hora', 'total'
        print(f"\nPedido nº{vendas[0]} - Data do pedido: {vendas[1]}")
        print("-------------------------------------------------------------------------")
            
        # 'codigo_produto', 'nome_produto', 'quantidade', 'valor_unit', 'subtotal', 'id_venda'
        for item in carrinho:
            descricao = f'Produto: {item[1]} - Qtde: {item[2]} - Valor UN - R${float(item[3]):.2f} - Sub-Total: R${float(item[4]):.2f}'
            print(descricao.replace(".",","))
        
        print("-------------------------------------------------------------------------")   
        print(f'Total do Pedido: R${float(vendas[2]):.2f}\n')
        print("-------------------------------------------------------------------------\n")           
 