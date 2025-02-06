"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_enviado_pelo_usuario = '014.150.535-45' # cpf string recebido pelo usuário

cpf_limpo_enviado_pelo_usuario = cpf_enviado_pelo_usuario.replace('.','').replace('-','') # cpf retirado . e - 
cpf_int = int(cpf_limpo_enviado_pelo_usuario) # cpf limpo convertido de string para número inteiro


nove_digitos = cpf_limpo_enviado_pelo_usuario[:9] #pegando apenas os 9 primeiros digitos para calculo
contador_regressivo_1 = 10 # contador usado a frente para a multiplicação
resultado_digito_1 = 0 # resultado sera gerado depis do calculo multiplicado e somado

for digitos in nove_digitos:
    # print(f'{digitos} {contador_regressivo}' ) 
    resultado_digito_1 += (int(digitos) * contador_regressivo_1) # aqui é gerado o primeiro digito do calculo digitos * contador regressivo em ordem decrecente e ja somado cada resultado da multiplicacao mas soma dos resultados 1 a 1 ex... 1* 10 = 10 | 2*10 = 20 mas 10 =30
    print(f'{digitos} * {contador_regressivo_1} += {resultado_digito_1}  ')
    digito_1 = (resultado_digito_1 * 10) % 11
    contador_regressivo_1 -= 1
    
    digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'Primeiro digito gerado é {digito_1}')
print('---------------------------')

# -------------------------------------------------calculo 2 digito-------

print('CPF calculo de validacão 2 digito')
    
    
    
dez_digitos =  nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado__digito_2 = 0
print(f' CPF com 1 digito validado -> {dez_digitos}')

for digitos in dez_digitos:
    resultado__digito_2 += (int(digitos) * contador_regressivo_2)
    print(f'{digitos} * {contador_regressivo_2} += {resultado__digito_2}')
    digito_2 = (resultado__digito_2 *10) % 11
    contador_regressivo_2 -=1
    
    digito_2 = digito_2 if digito_2 <= 9 else 0
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(f'Segundo digito gerado é {digito_2}')


print(cpf_gerado_pelo_calculo, cpf_limpo_enviado_pelo_usuario)
cpf_gerado_convertido = f'{cpf_int:011}'
cpf_gerado_convertido = f'{cpf_gerado_convertido[:3]}.{cpf_gerado_convertido[3:6]}.'\
                        f'{cpf_gerado_convertido[6:9]}-{cpf_gerado_convertido[9:]}'
            
            
print(f'{cpf_enviado_pelo_usuario} 1')           
print(f'{cpf_gerado_pelo_calculo}    2') 
print(f'{cpf_limpo_enviado_pelo_usuario}    3')
print(f'{cpf_gerado_convertido} 4')

if cpf_gerado_pelo_calculo == cpf_limpo_enviado_pelo_usuario:
    print('--------------------------')
    print(' é valido')
else:
    print('cpf invalido')
    
print('----------------------------')

        


















# -------- Contado do 1 digito abaixo------------------------------
# cpf = '746.824.890-70 '
# cpf_limpo = cpf.replace('.', '')
# cpf_int = int(cpf_limpo)
# nove_digitos = cpf_limpo[:9]

# contador_regresivo_1 = 10
# resultado_1 = 0

# # print(cpf)
# # print(cpf_limpo)
# # print(cpf_int)
# for digitos in nove_digitos:
#     # print(nove_digitos)
#     resultado_1 += int(digitos) * contador_regresivo_1
#     print(digitos, contador_regresivo_1, ' = ', resultado_1)
#     contador_regresivo_1 -=1
# print(resultado_1)
    
# digito_1 = (resultado_1 * 10) % 11
# print()
# digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)
