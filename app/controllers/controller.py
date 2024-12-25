from models.model_produtos import Produto
from models.model_vendas import Venda
from views.view import View
from datetime import datetime
import sys

class Controller:

    def __init__(self) -> None:        
        self.model_produto = Produto()
        self.model_venda = Venda()
        self.view = View()


    def mostrar_menu(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """
        self.view.mostrar_menu()


    def cadastrar_produto(self, nome: str, preco: str) -> None:
        """ Cadastra um produto no 'bd'
            :param nome: nome do produto
            :param type: string

            :param preco: preço do produto
            :param type: str

            :raise: ValueError: Valor inválido
        """        
        try:
            preco = float(preco.replace(',','.'))
            self.model_produto.cadastro_produto(nome, preco)
        except ValueError:
            print("Valor inválido. Dica: Não coloque pontos para separar os milhares.")
        else:
            print("Cadastrado com sucesso! \n")


    def listar_produtos(self) -> None:
        """ Lista todos os produtos """
        produtos = self.model_produto.lista_produtos()
        self.view.visualizar_produtos(produtos)


    def cadastrar_venda(self) -> None:
        """ Cadastra as informações da venda
            :raise: ValueError: Código ou quantidade inválida
            :raise: IndexError: Código do produto inválido
        """
        produtos = self.model_produto.lista_produtos()
        carrinho = []
        adicionar_mais_produtos = 's'

        while adicionar_mais_produtos == 's':
            try:
                codigo_produto, quantidade, adicionar_mais_produtos = self.view.tela_vendas(produtos)
                item_comprado = self.model_produto.listar_produto_por_codigo(int(codigo_produto))                
                pedido = self.montar_pedido(item_comprado, quantidade)           
                carrinho.append(pedido)
                total = self.calcular_total(carrinho)
                self.view.mostrar_carrinho(carrinho, total)
            except ValueError:
                print("Código ou quantidade invalidos. Por favor verifique e tente novamente.")
            except IndexError:
                print("Código do produto não encontrado. Consulte a lista de produtos.")
        
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


    def calcular_subtotal(self, quantidade: int, valor: float) -> float:
        """ Retorna o subtotal de uma compra
            :param quantidade: quantidade comprada
            :param type: int

            :param valor: valor do produto
            :param type: float

            :return: subtotal da compra de um produto
            :rtype: float
        """
        return int(quantidade) * float(valor)    


    def calcular_total(self, carrinho: list) -> float:
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
        self.view.gerar_relatorio_vendas(vendas)


    def tratar_opcao(self, opcao: str) -> None:
        """ Verifica a opção selecionada no menu e aciona para a função correspondente 
            :param opcao: opção selecionada no menu
            :param type: str
        """
        match opcao:
            case '1':
                nome, preco = self.view.tela_cadastro_produto()
                self.cadastrar_produto(nome, preco)
            case '2':
                self.listar_produtos()
            case '3':
                self.cadastrar_venda()
            case '4':
                self.relatorio_vendas()
            case '5':
                print("Obrigado pela preferencia")    
                exit()        
            case _:
                print("Opção Indisponível")


    def main(self) -> None:
        """ Inicia a aplicação abrindo o menu """
        while True:
            self.mostrar_menu()
            opcao = input()
            self.tratar_opcao(opcao)

    if __name__ == "__main__":
        main()