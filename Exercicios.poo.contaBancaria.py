# Exercício: Sistema de Gerenciamento de Contas Bancárias
# Crie uma classe chamada ContaBancaria que represente uma conta bancária. Ela deve ter os seguintes atributos e métodos:

# Atributos:
# titular: Nome do titular da conta.
# saldo: Saldo da conta (inicia em zero por padrão).
# Métodos:
# depositar(valor): Adiciona dinheiro à conta.
# sacar(valor): Remove dinheiro da conta se houver saldo suficiente.
# exibir_saldo(): Exibe o saldo atual da conta.
# Regras:
# Se o usuário tentar sacar mais dinheiro do que tem na conta, exibir a mensagem: "Saldo insuficiente!".
# Criar pelo menos dois objetos da classe ContaBancaria e testar os métodos.
# Desafio extra:
# Crie um método transferir(valor, destino) que transfere dinheiro de uma conta para outra, respeitando o saldo disponível.



class ContaBancaria:
   
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depositado {valor} na conta')
        else:
            print('Valor depositado inválido')
            
    def sacar(self,valor):
        if valor > 0:
            self.saldo -= valor
            print(f'Saue de {valor} realizado com sucesso')

        else:
            print('Saldo insuficiente') 
           
    def exibir_saldo(self):
        print(f'O saldo atual de {self.nome}: {self.saldo}')

    def trasferir(self,valor,destino):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                destino.saldo += self.saldo
                print(f'Tranferir de  R${valor} para {destino.nome}')
            else:
                print(f'Saldo insuficiente para trasferencia')
        else:
            print('Valor de trasferencia inválido')
                
cliente1 = ContaBancaria('Jorge')
cliente1.exibir_saldo()
cliente1.depositar(500)
cliente1.exibir_saldo()
cliente1.sacar(120)
cliente1.exibir_saldo()


# ------------------------------------------------------------------------------------------------------


# class ContaBancaria:
    
#     def __init__(self,titular):
#         self.titular = titular
#         self.saldo = 0

#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             print(f'Depósitado R${valor} realizado com sucesso')
#         else:
#             print('Valor depósitado inválido')
        
#     def sacar(self,valor):
#         if valor > 0:
#             if valor <= self.saldo:
#                 self.saldo -= valor
#                 print(f'Saque de R$ {valor} realizado con sucesso')
#             else:
#                 print('Saldo insuficiente')
#         else:
#             print('Valos de saque invalido')
                
#     def exibir_saldo(self):
#         print(f'O saldo atual de  {self.titular}: R${self.saldo}')
        
#     def transferir(self,valor,destino):
#         if valor > 0:
#             if valor <= self.saldo:
#                 self.saldo -= valor
#                 destino.saldo += valor
#                 print(f'Transferir de R${valor} para {destino.titular}')
#             else:
#                 print(f'Saldo insuficiente para transferência')
#         else:('Valor de transferência inválido')

    
# cliente1 = ContaBancaria('valdimarina')
# cliente2 = ContaBancaria('Mariazinha')

# cliente1.depositar(500)
# cliente1.sacar(200)
# cliente1.exibir_saldo()