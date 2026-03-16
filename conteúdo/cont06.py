#Podemos escrever um resultado na quantidade de caracteres específica ao colocar o valor dentro da mácara após escrever

nome = input ('Qual é o seu nome?')

print('prazer em conhece-lo {:20}!'.format(nome))

Qual é o seu nome? Gustavo

prazer em conhece-lo Gustavo
#LINHAMENTO DE MASCARA

#Podemos alinhar o nome dentro do número de caracteres que desejamos

A#linhamento para direita
nome = input ('Qual é o seu nome?')
print('prazer em conhece-lo {:>20}!'.format(nome))

#Alinhamento para a esquerda
nome = input ('Qual é o seu nome?')
print('prazer em conhece-lo {:<20}!'.format(nome))

#Alinhamento no centro
nome = input ('Qual é o seu nome?')
print('prazer em conhece-lo {:^20}!'.format(nome))
