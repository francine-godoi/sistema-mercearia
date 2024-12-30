from views.view_menus import ViewMenus
from controllers.controller_produtos import ControllerProdutos
from controllers.controller_vendas import ControllerVendas

class ControllerMenus:

    def __init__(self) -> None:                
        self.tela_menu = ViewMenus()
        self.controller_produtos = ControllerProdutos()
        self.controller_vendas = ControllerVendas()


    def mostrar_menu(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """
        self.tela_menu.mostrar_menu()


    def tratar_opcao(self, opcao: str) -> None:
        """ Verifica a opção selecionada no menu e aciona para a função correspondente 
            :param opcao: opção selecionada no menu
            :param type: str
        """
        match opcao:
            case '1':
                self.controller_produtos.cadastrar_produto()
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