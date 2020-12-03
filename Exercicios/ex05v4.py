nome = input('Digite seu nome: ')
placa = input('Informe a placa do seu carro: ')
valor = input('Valor da pintura: ')
estacionamentoNumero = input('Numero do estacionamento: ')

msg = '{0}, seu carro placa {1} está pronto, o valor da pintura foi de {2}. Ele pode ser retirado no estacionamento numero {3}'

print(msg.format(nome,placa,valor,estacionamentoNumero))
