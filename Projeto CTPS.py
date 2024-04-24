from datetime import datetime
dados = dict()
dados ['nome'] = str(input('nome: '))
nasc = int(input('Ano de Nascimento: '))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados ['ctps'] !=0:
    dados ['Contraração'] = int(input('Ano de Contratação: '))
    dados ['salário'] = float(input('Salário: R$ '))
    dados ['aposentadoria'] = dados['idade'] + ((dados ['Contraração'] + 45) - datetime.now().year)
print('***' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')