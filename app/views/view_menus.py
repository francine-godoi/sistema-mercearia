import os

class ViewMenus:

    def mostrar_menu(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """        
        print("--------- Menu ----------")        
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Vendas\n4 - Relatório de Vendas\n5 - Sair")