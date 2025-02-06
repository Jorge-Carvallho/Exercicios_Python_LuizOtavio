
frase = 'aaaaaoooo'

i = 0

qtd_apareceu_mas_vezes = 0
letra_apareceu_mas_vezes = ''

while i < len(frase):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
    continue

qtd_apareceu_mas_vezes_atual = frase.count(letra_atual)


if qtd_apareceu_mas_vezes < qtd_apareceu_mas_vezes_atual:
        qtd_apareceu_mas_vezes = qtd_apareceu_mas_vezes_atual
letra_apareceu_mas_vezes = letra_atual

i += 1


print('A letra que apareceu mas vezes foi '
      f'*{letra_apareceu_mas_vezes}* que apareceu '
      f'{qtd_apareceu_mas_vezes} x ')
