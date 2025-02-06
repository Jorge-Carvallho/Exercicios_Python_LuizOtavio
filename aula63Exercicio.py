'''
Possiveis problemas corrigidos de verificação de validação de CPF
Entrando com expressões regulares

IMPORT RE DE EXPRESSÕES REGULARES METODO 'R' QUE SUBISTITUI DODOS OS CARACTERES POR UMA REGRA IMPLEMENTA
'''
import re # importação de expressão regular
import sys # = sys.exit() método que sair do python e encerra o programa

# cpf_enviado_pelo_usuario = '014.150.535-45' # cpf string recebido pelo usuário

# cpf_limpo_enviado_pelo_usuario = cpf_enviado_pelo_usuario.\
#     replace('.','')\
#     .replace('-','') # cpf retirado . e - 
# cpf_int = int(cpf_limpo_enviado_pelo_usuario) # cpf limpo convertido de string para número inteiro
entrada_do_cpf = input('Digite um CPF ')


cpf_enviado_pelo_usuario = re.sub( r'[^0-9]', '', 
   entrada_do_cpf
  )# modulo 'r' imprtado acima qualquer caracter comocado entre 0 e 9 sera eliminado e validado apenas os números dentro da expressão
cpf_limpo_enviado_pelo_usuario = cpf_enviado_pelo_usuario

# Este bloco de código verifique se entrdada de usuario foi sequencial caso tenha sido o programa e encerrado na hora , métdod import.sys, e responsavel por esta finalização
entrada__sequencial = entrada_do_cpf == entrada_do_cpf[0] * len(entrada_do_cpf)
if entrada__sequencial:
    print('Você enviou dados sequencial, vamos tentar novamente')
    sys.exit()
 



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


# print(cpf_gerado_pelo_calculo, cpf_limpo_enviado_pelo_usuario)
# cpf_gerado_convertido = f'{cpf_int:011}'
# cpf_gerado_convertido = f'{cpf_gerado_convertido[:3]}.{cpf_gerado_convertido[3:6]}.'\
#                         f'{cpf_gerado_convertido[6:9]}-{cpf_gerado_convertido[9:]}'
            
      # ====^ acima ussando o modulo import não é necessario fazer essas verificações      
            
print(f'{cpf_enviado_pelo_usuario}    1')           
print(f'{cpf_gerado_pelo_calculo}    2') 
print(f'{cpf_limpo_enviado_pelo_usuario}    3')
# print(f'{cpf_gerado_convertido} 4')

if cpf_gerado_pelo_calculo == cpf_enviado_pelo_usuario:
    print('--------------------------')
    print(' é valido')
else:
    print('cpf invalido')
    
print('----------------------------')

        


















