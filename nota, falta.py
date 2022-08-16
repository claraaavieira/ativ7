




nome = str(input('digite o seu nome: '))
nota1 = float(input('escreva sua primeira nota: '))
nota2 = float(input('escreva sua segunda nota: '))
nota3 = float(input('escreva sua terceira nota: '))

falta = int(input('quantas vezes voce faltou? '))

media: float = (nota1 + nota2 + nota3) / 3
print(f'a media: {media:.1f}')

if media < 7.0 or falta > 3:
    print('infelizmente', nome, 'voce foi reprovado')
elif media >= 7:
    print('parabens,', nome, 'voce foi aprovado com sucesso!!')