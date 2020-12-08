#calculo do consumo de energia de um eletrodomestico

potencia = float(input('informe a potência do eletrodoméstico (kW): '))
horasLigadas = float(input('informe a quantidade de horas em funcionamento: '))

consumo = (potencia)*horasLigadas
valorConsumo = consumo*(0.51761)

consumo_mensal = valorConsumo * 20

msg = 'Valor do consumo mensal: {:.2f}'

print(msg.format(consumo_mensal))
