# 🏫 Desafio: Criar uma Classe Aluno
# Requisitos:
# 1️⃣ A classe deve ter os seguintes atributos:

# nome (nome do aluno)
# nota (começa como None, ou seja, sem nota)
# 2️⃣ Métodos:

# atribuir_nota(valor): Define a nota do aluno (entre 0 e 10).
# verificar_aprovacao(): Mostra se o aluno foi aprovado.
# Se a nota for maior ou igual a 6, exibir "Aprovado!"
# Se for menor que 6, exibir "Reprovado!"
# exibir_informacoes(): Mostra o nome do aluno e sua nota.

# class Aluno:
#     def __init__(self, nome_aluno):
#         self.nome_aluno = nome_aluno
#         self.nota = 0
#         self.situacao = 'Cursando'
        
#     def atribuir_nota(self, valor):
#         if 0 <= valor <= 10:
#             self.nota = valor
#             print(f'Nota {valor} atribuida com sucesso ')
#         else:
#             print('ERRO: insira uma nota entre 0 e 10')
        
#     def verificar_aprovacao(self):
       
#         if self.nota >= 6:
#             print(f'Aluno {self.nome_aluno} Aprovado na matéria')
#             self.situacao = 'Aprovado na matéria'
#         else:
#             print(f'Aluno { self.nome_aluno} esta Reprovado')
#             self.situacao = 'Reprovado na matéria'
            
        
#     def exibir_informacoes(self):
#         print(f'Nome do aluno: {self.nome_aluno}: Nota do aluno: {self.nota} Situação: {self.situacao}')
    
    
    
# aluno01 = Aluno('Jorge')
# aluno01.atribuir_nota(3)
# aluno01.verificar_aprovacao()
# aluno01.exibir_informacoes()

# print()

# aluno02 = Aluno('Lais')
# aluno02.atribuir_nota(8)
# aluno02.verificar_aprovacao()
# aluno02.exibir_informacoes()


# --------------------------------------------------------------------------------------------------------------------------


class Aluno:
    def __init__(self, nome_aluno):
        self.nome_aluno = nome_aluno
        self.nota = None
        self.situação = 'Cursando'

    def atribuir_nota(self,valor):
        if 0<= valor <= 10:
            self.nota = valor
            print(f'Nota {valor} atribuida com sucesso.')
        else: 
            print('Erro: Nota ainda não atribuida')

    def verificar_aprovacao(self):
        if self.nota is None:
            print('Erro: Nota ainda não atribuida')
            return
        
        if self.nota >= 6:
            self.situação = 'Aprovado na matéria'
        else:
            self.situação = 'Reprovado na matéria'
        

        
        print(f'O aluno {self.nome_aluno} está {self.situação}')

            
    def exibir_informaçao(self):
        print(f'Nome do aluno: {self.nome_aluno}, Nota do Aluno: {self.nota}, Situação do Aluno: {self.situação}')



aluno1 = Aluno('Elis')
aluno1.atribuir_nota(6.5)
aluno1.verificar_aprovacao()
aluno1.exibir_informaçao()


        