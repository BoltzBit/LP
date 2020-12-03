#calculo do imc peso/altura^2

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso/pow(2,altura)
msg = 'Seu imc é {0}'

print(msg.format(imc))
