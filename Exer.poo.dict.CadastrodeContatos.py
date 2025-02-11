# Exercício: Cadastro de Contatos
# Objetivo: Criar uma classe para gerenciar uma agenda de contatos. A agenda será um dicionário onde a chave é o nome do contato e o valor é um outro dicionário com o número de telefone e o email do contato.

# Atributos:
# contatos: Dicionário vazio, onde as chaves serão os nomes dos contatos e os valores serão dicionários com as informações de telefone e email.

# Métodos:
# adicionar_contato(nome, telefone, email):
# Adiciona um novo contato à agenda. O nome será a chave, e o valor será um dicionário com o telefone e o email do contato.


# remover_contato(nome):
# Remove o contato da agenda pelo nome.
# exibir_contatos():

# Exibe todos os contatos registrados na agenda.
# buscar_contato(nome):

# Busca um contato pelo nome e exibe as informações (telefone e email) do contato.

class CadastroDeContados:
    def __init__(self):
        self.contatos = {}
        
    
    def adicionar_contatos(self, nome, telefone, email):
        self.contatos[nome] = {'Telefone': telefone, 'email': email}
        print(f'Contato de `{nome} adicionado com sucesso')
        
    def remover_contatos(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f'Contado de {nome} removido com sucesso')
        else:
            print(f'Contado de {nome} não encontrado')

    def exibir_contatos(self):
        if not self.contatos:
            print('Agenda vazia')
        else:
            for nome, info in self.contatos.items():
                print(f"{nome}: Telefone - {info['Telefone']}, Email - {info['email']}")

    def buscar_contato(self,nome):
        if nome in self.contatos:
            info = self.contatos[nome]
            print(f'Contato encotrado: {nome}: -Telefone: {info['Telefone']}, Email: {info['email']}')
        else:
            print(f'Contato {nome} não encontrado')
        

        
contatoComando = CadastroDeContados()
contatoComando.adicionar_contatos('jorge', '1991432033', 'Jorge.carvalor0309@hotmail.com')
contatoComando. exibir_contatos()
contatoComando.buscar_contato('jorge')
contatoComando.adicionar_contatos('Tais','972398423', 'Taismmsj@hotmail.com')
contatoComando.adicionar_contatos('Lais', '0832-39842','laai.curvello@hotmail.com')
contatoComando.exibir_contatos()
contatoComando.buscar_contato('Lais')