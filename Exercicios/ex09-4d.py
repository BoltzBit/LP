#conversao de fahrenheit para celsius
fahrenheit = float(input('Informe a temperatura em fahrenheit: '))

celsius = (fahrenheit-32)*(5/9)

msg = 'Temperatura em Celsius: {}'

print(msg.format(celsius))
