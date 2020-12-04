#Calculo de Salário
salarioHora = float(input('Informe o valor da hora trabalhada: '))
horasTrabalhadas = float(input('informe as horas trabalhadas: '))

salarioBruto = salarioHora*horasTrabalhadas

inss = salarioBruto*0.11

contribuicaoSindical = salarioBruto*0.05

salarioLiquido = salarioBruto - contribuicaoSindical - inss

msg = 'O salario do colaborador é: {}'

print(msg.format(salarioLiquido))
