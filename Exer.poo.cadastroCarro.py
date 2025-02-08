
# Exercício: Cadastro de Carros
# Crie uma classe chamada Carro que representa um carro.

# Atributos:
# modelo: Nome do modelo do carro.
# ano: Ano de fabricação do carro.
# velocidade: Velocidade atual do carro (inicia em 0).
# Métodos:
# acelerar(valor): Aumenta a velocidade do carro em um valor específico.
# frear(valor): Diminui a velocidade do carro em um valor específico, sem deixar a velocidade negativa.
# exibir_informacoes(): Exibe o modelo, ano e velocidade atual do carro.

class Carro:
    def __init__(self, modelo, ano_de_fabricacao):
        self.modelo = modelo
        self.ano_de_fabricacao = ano_de_fabricacao
        self.velocidade = 0

    def acelerar(self,valor):
        if valor > 0:
            self.velocidade += valor
            print(f'O carro {self.modelo} está acelerando em {self.velocidade} km/h')
            if self.velocidade > 120:
                print('Carro em alta velocidade')
        else:
            print('O valor da aceleração deve ser maior que 0')
            

    def frear(self,valor):
        if self.velocidade <= 0:
            print('Carro já está parado')
            return
        if valor > 0:
            self.velocidade -= valor
            if self.velocidade < 0: 
                self.velocidade = 0
            print(f'O carro {self.modelo} reduziu para {self.velocidade} km/h, vamos estacionar')

        else:
            print(f'O valor da frenagem deve ser maior que zero')
        
    def parar(self,):
        if self.velocidade > 0:
            print(f'Reduza a velocidade atual de {self.velocidade} km/h para o carro parar')
            print('Carro parou, vamos estacionar')
            self.frear(self.velocidade)
        else:
            print('Carro já está parado')
                    
    def exibir_informacoes(self):
        print(f'O carro: {self.modelo}, Ano: {self.ano_de_fabricacao}, Velocidade atual: {self.velocidade}')
        
        
carro_de_Wesley = Carro('Audi Q3', 2020)

carro_de_Wesley.exibir_informacoes()
carro_de_Wesley.parar()
carro_de_Wesley.acelerar(125)
carro_de_Wesley.frear(50)
carro_de_Wesley.parar()
carro_de_Wesley.frear(20)
carro_de_Wesley.acelerar(23)
carro_de_Wesley.acelerar(40)
carro_de_Wesley.acelerar(80)
carro_de_Wesley.exibir_informacoes()
