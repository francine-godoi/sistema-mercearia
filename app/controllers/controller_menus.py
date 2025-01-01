from views.view_menus import ViewMenus
from controllers.controller_produtos import ControllerProdutos
from controllers.controller_vendas import ControllerVendas

class ControllerMenus:

    def __init__(self) -> None:                
        self.tela_menu = ViewMenus()
        self.controller_produtos = ControllerProdutos()
        self.controller_vendas = ControllerVendas()


    def mostrar_menu_principal(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """
        self.tela_menu.mostrar_menu_principal()


    def tratar_opcao(self, opcao: str) -> None:
        """ Verifica a opção selecionada no menu e aciona para a função correspondente """
        match opcao:
            case '1':
                self.tela_menu.mostrar_submenu_produtos()
                sub_opcao = input()
                self.tratar_subopcao('1.' + sub_opcao)
            case '2':                
                self.tela_menu.mostrar_submenu_vendas()
                sub_opcao = input()
                self.tratar_subopcao('2.' + sub_opcao)
            case '3':
                self.tela_menu.mostrar_submenu_relatorio()
                sub_opcao = input()
                self.tratar_subopcao('3.' + sub_opcao)
            case '4':
                print("Obrigado pela preferencia")    
                exit()        
            case _:
                print("Opção Indisponível\n")


    def tratar_subopcao(self, subopcao: str) -> None:
        """ Verifica a opção selecionada no menu principal e aciona para a função correspondente """
        match subopcao:
            case '1.1':
                self.controller_produtos.cadastrar_produto()
            case '1.2':
                self.controller_produtos.listar_produtos()
            case '1.3':
                return self.mostrar_menu_principal()
            case '2.1':
                self.controller_vendas.cadastrar_venda()
            case '2.2':
                self.controller_vendas.consultar_venda_codigo()
            case '2.3':
                return self.mostrar_menu_principal()
            case '3.1':
                self.controller_vendas.relatorio_vendas()
            case '3.2':
                self.controller_vendas.relatorio_venda_data()
            case '3.3':
                return self.mostrar_menu_principal()
            case _:
                print("Opção Indisponível\n")


    def main(self) -> None:
        """ Inicia a aplicação abrindo o menu """
        while True:
            self.mostrar_menu_principal()
            opcao = input()
            self.tratar_opcao(opcao)

    if __name__ == "__main__":
        main()