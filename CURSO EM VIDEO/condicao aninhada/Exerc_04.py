from datetime import date

nasc = int(input(' Qual a data de nascimento? '))
ano_atual = date.today().year
sexo = input('''Qual seu genero: 
             [M] Masculino
             [F] Feminino:  ''')

idade = ano_atual - nasc

if sexo == 'M' and idade > 18:
    anos = idade - 18
    print(f'Você está com {idade} anos e já deveria ter se alistado há {anos} anos atrás, no ano de {ano_atual - anos}')


elif sexo == 'M' and idade == 18:
    anos = idade - 18
    print(f'Você está com {idade} anos e já deve se alistar esse ano de {ano_atual - anos}')

elif sexo == 'M' and idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print(f'Você está com {idade} anos e ainda falta {saldo} anos para vc se alistar, no ano de {ano}')    

else:
    print('Você é Mulher e não precisa de alistar')