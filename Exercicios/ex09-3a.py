#calculo da área de um triângulo

altura = float(input('Insira a altura: '))
base = float(input('Insira o comprimento da base: '))

area = (base*altura)/2
msg = 'A àrea do triângulo é {}'

print(msg.format(area))
