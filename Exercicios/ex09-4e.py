#Conversao de Kelvin para fahrenheit

kelvin = float(input('Informe a temperatura em Kelvin: '))

fahrenheit = ((kelvin - 273.15)*(9/5)) + 32

msg = 'Temperatura em Fahrenheit: {}'

print(msg.format(fahrenheit))
