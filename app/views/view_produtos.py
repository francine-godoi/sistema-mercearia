class ViewProdutos:
  
    def tela_cadastro_produto(self) -> list:
            """ Mostra a tela de cadastro de um novo produto
                :return: nome e preço do produto
                :rtype: list
            """
            print("--------- Cadastrar Novo Produto ---------")
            nome = input("Produto: ")
            preco = input("Preço: ")
            return [nome, preco]
    

    def visualizar_produtos(self, produtos: list) -> None:
        """ Mostra uma lista com todos os produtos
            :param produtos: lista com todos os produtos
            :param type: list 
        """        
        
        print("--------- Lista de Produtos ---------")       
        print("Cód - Nome do Produto - Preço")
        print("-------------------------------------")
                
        for produto in produtos:
            item = f'{produto["codigo"]} - {produto["nome"]} - R$ {float(produto["preco"]):.2f}'
            print(item.replace(".",","))

        print("\n")