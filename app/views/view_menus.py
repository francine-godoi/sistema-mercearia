class ViewMenus:

    def mostrar_menu_principal(self) -> None:
        """ Mostra o menu com as opções de serviços do sistema """        
        print("--------- Menu Principal ----------")        
        print("\nEscolha uma opção:")
        print("1 - Produtos\n2 - Vendas\n3 - Relatórios\n4 - Sair")

    def mostrar_submenu_produtos(self) -> None:
        """ Mostra o menu com as opções de relacionadas aos Produtos """ 
        print("--------- Menu Produtos ----------")        
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Voltar")

    def mostrar_submenu_vendas(self) -> None:
        """ Mostra o menu com as opções de relacionadas as Vendas """ 
        print("--------- Menu Vendas ----------")        
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Nova Venda\n2 - Consultar Pedido\n3 - Voltar")

    def mostrar_submenu_relatorio(self) -> None:
        """ Mostra o menu com as opções de relacionadas aos Relatórios """         
        print("--------- Menu - Relatórios ----------")        
        print("\nEscolha uma opção:")
        print("1 - Gerar relatório com todas as Vendas\n2 - Gerar relatório de vendas por data\n3 - Voltar")
