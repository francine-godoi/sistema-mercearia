from views.view_produtos import ViewProdutos

class ViewVendas:

    def __init__(self):
         self.view_produtos = ViewProdutos()
  
    def tela_vendas(self, produtos: list) -> list:
            """ Mostra a tela de vendas
                :param produtos: lista com todos os produtos
                :param type: list

                :return: código e quantidade do produto vendido e uma flag (str: 's' ou 'n') avisando se o cliente deseja adicionar novo produto ao carrinho de compras
                :rtype: list
            """
            print("--------------- Vendas ---------------\n")
                        
            self.view_produtos.visualizar_produtos(produtos)
            codigo = input("Código do produto que deseja comprar: ")
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

        print("\n--------------- Seu Carrinho ---------------")

        for item in carrinho:
            descricao = f'Produto: {item["produto"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["valor"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
            print(descricao.replace(".",","))
            
        print("-----------------------------------------------")
        print(f"Total: R${float(total):.2f}")
        print("\n")


    def gerar_relatorio_vendas(self, vendas: list) -> None:  
        """ Mostra o relatório de todas as vendas realizadas
            :param vendas: lista com todas as vendas
            :param type: list
        """      
        
        #TODO: arrumar um  jeito de pegar os dados do banco para mostrar aqui
        print("\n--Relatório de Vendas--")
        print("---------------------------------------------------------------")
        for venda in vendas:
            print(f"\nPedido nº{venda[0]} - Data do pedido: {venda[1]}")
            print("---------------------------------------------------------------")
            a = str(venda[2]).strip("[]")
            
           # for item in venda[2]:
            #    print(item)
               # descricao = f'Produto: {item["produto"]} - Qtde: {item["quantidade"]} - Valor UN - R${float(item["valor"]):.2f} - Sub-Total: R${float(item["subtotal"]):.2f}'
               # print(descricao.replace(".",","))
            
            print("---------------------------------------------------------------")   
            print(f'Total do Pedido: R${venda["total"]:.2f}\n')
            print("---------------------------------------------------------------")            
        
        print(f"\nTotal das vendas: R$ {sum([venda["total"] for venda in vendas]):.2f}\n")
        print("---------------------------------------------------------------\n\n")            