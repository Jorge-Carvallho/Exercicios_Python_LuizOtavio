"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

# entrada = input('Digite um numero inteiro: ')
# if entrada.isdigit():
#     numero_int = int(entrada)
#     if numero_int % 2 == 0:
#         print('número é par')
#     else:
#         print('Número impar')
# else:
#     print('Entrada inválida, digite um número inteiro')
        

#  ==========================================================   
    

# entrada = input('Digite um número ')
# if entrada.isdigit():
#     numero_int = int(entrada)
#     if numero_int % 2 == 0:
#         print('número par')
#     else:
#         print('número impar')
        
# else:
#     print('Entrda inválida, digite um entrada válida')
            
        
# ==========================================================        


"""
Faça um programa que exiba a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Informe a Hora e receba sua saudação(0-24) ')

# if hora.isdigit():
#     hora_int = int(hora)
#     if 0 <= hora_int < 24: # tipo de verificar se valor esta dentro de algum intervalo intervalo
#         if 0 <= hora_int <12:
#             print('Bom dia')
#         elif 12 <= hora_int <18:
#             print('Boa tarde')
#         else:
#             print('Boa noite')

# else:
#     print('Entrada inválida, digite uma hora valida')
    
# ---------------------------------------------------------------------------------------------------
    # usando try, except
    
# entrada =  input('Digite a hora: ')

# try: 
#     hora =  int(entrada)
#     if 0 <= hora <12:
#         print('Bom dia')
#     elif 12 <= hora < 18:
#         print('Boa tarde')
#     else:
#         print('Boa noite ')
    
    
# except:
#     print('Digite a hora correta')
    
    
    
# --------------------------------------------------------------------------------------------------------    
    
# hora = input('Digite a Hora (0-24): ')
# if hora.isdigit():
#     hora_int = int(hora)
#     if 0 <= hora_int < 24:
#         if 0 <= hora_int < 12:
#             print('bom dia')
#         elif 12 <= hora_int < 18:
#             print('Boa tarde')
#         else:
#             print('boa noite')
#     else:
#         print('digite uma hora válida')
# else:
#     print('Entrada inválida, digite um número correto')

# --------------------------------------------------------------------------------------------------
# codigo 2


# entrada_hora = input('Informe a hora (0:24) ')
# entrada_hora = int(entrada_hora)
# if entrada_hora > 0 and entrada_hora < 24:
#     if entrada_hora >= 0  and entrada_hora <= 12:
#         print('Bom dia')
#     elif entrada_hora > 12 and entrada_hora < 18:
#         print('Boa tarde')
#     else:
#         print('Boa noite')

# else:
#     print('Hora inválida')
        

#codigo3

# entrada = input('Digite a hora em número ')

# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <=12:
#         print('Bom dia')
#     elif hora > 12 and hora <=18:
#         print('Boa tarde')
#     elif hora  > 18 and hora <= 24:
#         print('Boa noite')
#     else:
#         print('Digite apenas entre 0 a 24 horas')

 
# except:
#     print('Digite número inteiro')
 


"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

# nome = input('Digite seu nome: ')

# if len(nome) < 4:
#     print('Seu nome é curto')
# elif 4 <= len(nome) < 6:
#     print('Seu nome é médio')
# elif len(nome ) > 6:
#     print('Seu nome é grande')

# ------------------------------------------------------------------------
# nome = input('Digite seu nome: ')
# nome = len(nome)# retorna um valor int( pos é o tamanho da string)

# if nome == 0: # verifica se usuario digitou correto
#     print('Digite um valor válido')
# else:
#     if nome < 4:
#         print('Seu nome é curto')
#     elif 4 <= nome < 7:
#         print('Seu nome é médio')
#     elif nome > 6:
#         print('Seu nome é grande')


# ========== melhor forma de fazer ===============
# nome = input('Digite um nome: ')

# if not nome.isalpha():
#     print('Digite um valor válido')
    
# else:
#     nome = len(nome)
#     if nome < 4:
#         print('Seu nome é curto')
#     elif 4<= nome < 7:
#         print('Seu nome é médio')
#     elif nome > 7:
#         print('Seu nome é grande')










# nome = input('Digite seu nome: ')
# nome = len(nome)
# if nome < 4:
#     print('Nome curto')
# elif nome > 4 and nome <= 6:
#     print('Nome médio')
# else:
#     print('Nome muito grande')
