#calculo de média de 4 notas

numeroNotas = int(input('Insira a quantidade de notas: '))
somaNotas = 0

for nota in range(numeroNotas):
    nota_aluno = int(input('Insira a {0}ª nota do aluno: '.format(nota+1)))
    somaNotas += nota_aluno
    
mediaNotas = somaNotas/numeroNotas

msg = 'A media do aluno é {0}'

print(msg.format(mediaNotas))
