# 🚀 Exercício: Lista de Compras
# 📌 Objetivo
# Crie uma classe ListaDeCompras que permita gerenciar uma lista de itens de supermercado.

# 📌 Atributo:
# itens: uma lista vazia que armazenará os itens adicionados.
# 📌 Métodos:
# adicionar_item(item): adiciona um item à lista.
# remover_item(item): remove um item da lista, se ele existir.
# exibir_lista(): exibe todos os itens da lista.

# class ListasDeCompras:
#     def __init__(self):
#         self.itens = []

#     def adicionar_item(self,item):
#         self.itens.append(item)
#         print(f'Item {item} adicionado a lista')

        
#     def remover_item(self, item):
#         if item in self.itens:
#             self.itens.remove(item)
#             print(f'Item {item} removido da lista')
#         else:
#             print(f'O item "{item}" não se encontra na lista')

            
#     def exibir_lista(self):
#         if self.itens:
#             print(f'Lista de compras')
#             for item in self.itens:
#                 print(f'- {item}')
#         else:
#             print('A lista esta vazia')

# minha_lista = ListasDeCompras()
# minha_lista.adicionar_item('pão')
# minha_lista.adicionar_item('arroz')
# minha_lista.adicionar_item('feijão')
# minha_lista.adicionar_item('café')
# minha_lista.adicionar_item('queijo')

# minha_lista.exibir_lista()
        
                
# ---------------------------------------------------------------------------------------------------------------------------

class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self,item):
        self.itens.append(item)
        print(f'Item {item} adicionado a lista de compras')
        
    def remover_item(self,item):
        if item in self.itens:
            self.itens.remove(item)
            print(f'Item {item} removido da Lista de compras')
        else:
            print(f'O item {item}, não se encontra na lista')

    def exibir_lista(self):
        if self.itens:
            print('Lista de Compras')
            for item in self.itens:
                print(f'- {item}')
        else:
            print('A lista esta vazia')
            
            


lista01 = ListaDeCompras()
    
lista01.adicionar_item('arroz')
lista01.adicionar_item('macarão')
lista01.adicionar_item('café')
lista01.adicionar_item('Produtop de limpeza')
lista01.exibir_lista()
lista01.remover_item('arroz')
lista01.exibir_lista()