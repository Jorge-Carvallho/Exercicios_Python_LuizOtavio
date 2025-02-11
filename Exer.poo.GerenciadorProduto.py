# Exercício: Gerenciador de Produtos
# Objetivo: Criar um sistema simples de gerenciamento de produtos usando um dicionário.

# Atributos da Classe GerenciadorProdutos
# produtos: Dicionário que armazena os produtos no formato {codigo: {'nome': nome, 'preco': preco, 'quantidade': quantidade}}.
# Métodos da Classe
# adicionar_produto(codigo, nome, preco, quantidade): Adiciona um produto ao dicionário.
# remover_produto(codigo): Remove um produto do dicionário pelo código.
# atualizar_preco(codigo, novo_preco): Atualiza o preço de um produto.
# atualizar_quantidade(codigo, nova_quantidade): Atualiza a quantidade de um produto.
# exibir_produtos(): Exibe todos os produtos cadastrados.


# class GerenciadorProdutos:
#     def __init__(self):
#         self.produto  = dict()

#     def adicionar_produtos(self,codigo, nome,preco,quantidade):
#         if codigo in self.produto:
#             print(f'O priduto com código { codigo} já existe')
#         else:
#             self.produto[codigo] = {'Nome': nome, 'Preço': preco, 'Quantidade': quantidade}
            
#     def remover_produto(self,codigo):
#         if codigo in self.produto:
#             del self.produto[codigo]
#         else: 
#             print(f'Produto código {codigo} não encontrado')

#     def atualizar_estoque(self, quantidade):
        
        








class GerenciadorProduto:
    def __init__(self):
        self.produto = {}

    def adicionar_produto(self,codigo,nome,preco, quantidade):
        if codigo in self.produto:
            print(f'Produto com código {codigo} já existe')
        else:
            self.produto[codigo] = {'Nome': nome, 'Preço': preco, 'Quantidade': quantidade}        
            print(f'Produto {nome} adicionado com sucesso!')

    def remover_produto(self, codigo):
        if codigo in self.produto:
            del self.produto[codigo]
        else: 
            print(f'Produto código {codigo} não encontrado')
            
    def atualizar_preco(self,preco):
        pass

    def atualizar_estoque(self, codigo,nova_quantidade):
        if codigo in self.produto:
            self.produto[codigo]['Quantidade'] = nova_quantidade
            print(f'Estoque atualizado com {nova_quantidade} unidades')
        else:
            print(f'Produto com código {codigo} não encontrado')
        
    def exibir_produto(self):
        if not self.produto:
            print('Nenhum produto cadastrado')

        else:
            for codigo, info in self.produto.items():
                print(f"Código: {codigo} | Nome: {info['Nome']} | Preço: {info['Preço']:.2f} | Quantidade: {info['Quantidade']}")
                
                
        
loja01 = GerenciadorProduto()
loja01.adicionar_produto(100 ,'Erva doce', 4.20, 20)
loja01.exibir_produto()
loja01.adicionar_produto(102,'Vinho', 80, 60)
loja01.adicionar_produto(103,'fermento', 80, 35)
loja01.adicionar_produto(104,'limão', 80, 30)
loja01.atualizar_estoque(100, 40)
loja01.exibir_produto()

# -------------------------------------------------------------------------------------------------------------------------------




