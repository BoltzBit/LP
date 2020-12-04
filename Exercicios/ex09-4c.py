#conversao de celsius para fahrenheit

celsius = float(input('Insira a temperatura em Celsius: '))

fahrenheit = (celsius*(9/5))+32

msg = 'Temperatura em Fahrenheit: {}'

print(msg.format(fahrenheit))
