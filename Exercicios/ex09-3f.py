#calculo da area do circulo
import math

raio = float(input('Insira o valor do raio: '))

area = math.pi*pow(raio,2)

msg = 'Area do circulo é {}'

print(msg.format(area))

