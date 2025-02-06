"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade antes digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite sue nome: ')
idade = input('Digite sua idade: ')
# nome = 'Jorge Carvalho'
# idade = 34


if nome == nome and idade == idade:
    print(f'Seu nome digitado é {nome}')
    print(f'Seu nome digitado de ao contrario é: {nome[::-1]}')

    if ' ' in nome:
        print('Meu nome contem espaços')
    else:
        print('Meu nome não contem espaços')
        
    print(f'Meu nome contem {len(nome)} letras')
    print(f'A primeira letra do meu nome é: {nome[0]}')
    print(f'A ultima letra do meu nome é: {nome[-1]}')
else:
    print('Você deixou campos vazios')




# nome = input('Digite seu nome ')
# idade = input('Digite sua idade ')
# nome = 'jorge Carvalho'
# idade = 34


# if nome and idade:
#     print(f'Seu nome é {nome} e idade é {idade}')
#     print(f'Meu nome invertido é {nome[::-1]}')
#     if ' ' in nome:
#         print('Meu nome comtem espacos')
#     else:
#         print('Meu nome nao cotem espaços')
        
#     print(f'Meu nome contem {len(nome)} letras')
#     print(f' A primeira letra do meu nome é {nome[0]}')
#     print(f'A última letra do meu nome é {nome[-1]} ')
# else:
#     print('Voce deixou campos vazios')