class ViewProdutos:
  
    def exibir_form_cadastro_produto(self) -> list:
            """ Mostra a tela de cadastro de um novo produto
                :return: nome e preço do produto
                :rtype: list
            """
            print("--------- Cadastrar Novo Produto ---------")
            nome = input("Produto: ")
            preco = input("Preço: ")
            return [nome, preco]
    

    def exibir_lista_produtos(self, produtos: list) -> None:
        """ Mostra uma lista com todos os produtos
            :param produtos: lista com todos os produtos
            :param type: list 
        """        
        
        print("--------- Lista de Produtos ---------")       
        print("Cód - Nome do Produto - Preço")
        print("-------------------------------------")
                
        for produto in produtos:
            # 0 = código | 1 = nome produto | 2 = preço
            item = f'{produto[0]} - {produto[1]} - R$ {float(produto[2]):.2f}'
            print(item.replace(".",","))

        print("\n")