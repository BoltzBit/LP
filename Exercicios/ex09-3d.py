#calculo da area do trapezio

base1 = float(input('Insira a primeira base: '))
base2 = float(input('Insira a segunda base: '))
altura = float(input('Insira a altura do trapezio: '))

area = (altura*(base1+base2))/2

msg = 'A area do trapezio é {}'

print(msg.format(area))
