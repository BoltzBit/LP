#conversao de fahrenheit para kelvin

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

kelvin = ((fahrenheit-32)*(5/9))+273.15

msg = 'Temperatura em Kelvin: {}'

print(msg.format(kelvin))
