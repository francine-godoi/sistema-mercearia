class View:

    def mostrar_menu(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """
        print("\nEscolha uma opção:\n\
               1 - Cadastrar Produto\n\
               2 - Listar Produtos\n\
               3 - Vendas\n\
               4 - Relatório de Vendas\n\
               5 - Sair")

  
    def tela_cadastro_produto(self) -> list:
            """ Mostra a tela de cadastro de um novo produto
                :return: nome e preço do produto
                :rtype: list
            """
            print("\nCadastrar Novo Produto")
            nome = input("Produto: ")
            preco = input("Preço: ")
            return [nome, preco]
    

    def visualizar_produtos(self, produtos: list) -> None:
        """ Mostra uma lista com todos os produtos
            :param produtos: lista com todos os produtos
            :param type: list 
        """

        print("\n--Lista de Produtos--")
        print("---------------------")
        print("Cód - Nome do Produto - Preço")
        print("---------------------")
        
        for produto in produtos:
            item = f'{produto["codigo"]} - {produto["nome"]} - R$ {float(produto["preco"]):.2f}'
            print(item.replace(".",","))

    
    def tela_vendas(self, produtos: list) -> list:
            """ Mostra a tela de vendas
                :param produtos: lista com todos os produtos
                :param type: list

                :return: código e quantidade do produto vendido e uma flag (str: 's' ou 'n') avisando se o cliente deseja adicionar novo produto ao carrinho de compras
                :rtype: list
            """
            print("\nVendas")
            print("---------------------")
            self.visualizar_produtos(produtos)
            codigo = input("\nCódigo do produto que deseja comprar: ")
            quantidade = input("Quantidade: ")
            continuar = ''
            while continuar != 's' and continuar != 'n':
                continuar = input("Adicionar mais produtos? s/n ").lower()
            return [codigo, quantidade, continuar]
    

    def mostrar_carrinho(self, carrinho: list, total: float) -> None:
        """ Mostra o carrinho de compras
            :param carrinho: lista com todos os produtos comprados
            :param type: list

            :param total: total do carrinho
            :param type: float 
        """

        print("\n--Seu Carrinho--")
        print("---------------------")

        for item in carrinho:
            descricao = f'Produto: {item["nome"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["valor"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
            print(descricao.replace(".",","))
            
        print("---------------------")
        print(f"Total: {float(total):.2f}")


    def gerar_relatorio_vendas(self, vendas: list) -> None:  
        """ Mostra o relatório de todas as vendas realizadas
            :param vendas: lista com todas as vendas
            :param type: list
        """      

        print("\n--Relatório de Vendas--")
        print("---------------------")
        for num_pedido, venda in enumerate(vendas):
            print(f"\nPedido nº{num_pedido + 1} - Data do pedido: {venda["data"]}")
            print("---------------------")

            for item in venda["pedido"]:
                descricao = f'Produto: {item["nome"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["valor"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
                print(descricao.replace(".",","))
            
            print(f'Total do Pedido: {venda["total"]:.2f}\n')
            print("---------------------")            
        
        print("\n--Total das vendas--")
        print("---------------------")
        print(f'R$ {sum([venda["total"] for venda in vendas]):.2f}')
        print("---------------------")
        