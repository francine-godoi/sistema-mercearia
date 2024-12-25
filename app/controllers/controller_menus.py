from views.view_menus import ViewMenus
from views.view_produtos import ViewProdutos
from controllers.controller_produtos import ControllerProdutos
from controllers.controller_vendas import ControllerVendas

class ControllerMenus:

    def __init__(self) -> None:                
        self.view_menu = ViewMenus()
        self.view_produtos = ViewProdutos()
        self.controller_produtos = ControllerProdutos()
        self.controller_vendas = ControllerVendas()


    def mostrar_menu(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """
        self.view_menu.mostrar_menu()


    def tratar_opcao(self, opcao: str) -> None:
        """ Verifica a opção selecionada no menu e aciona para a função correspondente 
            :param opcao: opção selecionada no menu
            :param type: str
        """
        match opcao:
            case '1':
                nome, preco = self.view_produtos.tela_cadastro_produto()
                self.controller_produtos.cadastrar_produto(nome, preco)
            case '2':
                self.controller_produtos.listar_produtos()
            case '3':
                self.controller_vendas.cadastrar_venda()
            case '4':
                self.controller_vendas.relatorio_vendas()
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