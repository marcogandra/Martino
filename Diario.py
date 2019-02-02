#coding=Utf-8
from datetime import date
logins = []
senhas = []
conteudo = {}
def linha():
	print('=-='*30)

def teusu(usu):
	"""
	Esta funcao testa se o usuário está cadastrado
	"""
	global logins
	if len(logins) == 0:
		return True
	else:
		if usu not in logins[0][0]:
			print('Usuário não cadastrado')
			return False

def tesen(sen):
	"""
	Esta função confere se a senha está correta!
	"""
	global logins
	if len(logins) == 0:
		return True
	else:
		if sen not in logins[1][0]:
			print('Senha invalida')
			return False

def login():
	global logins
	global usuario
	global senha
	linha()
	escolha = ' '
	while escolha not in 'SN':
		escolha = str(input('Nenhum usuário cadastrado. Gostaria de cadastrar esse nome [S/N]? ')).strip().upper()[0]
		linha()
		if escolha == 'S':
			logins.append([usuario])
			logins.append([senha])
			with open('logs.txt', 'w') as registro:
				registro.write(f'{logins[0][0]}')
				registro.write(f'\n')
				registro.write(f'{logins[1][0]}')
			print(f'Parabens por ter cadastrado o usuário: {usuario}.')
			linha()
		else:
			if escolha == 'N':
				break

def diario():
	global conteudo
	linha()
	print(f'Bem vindo ao seu diário particular, {logins[0][0]}. Somente você terá acesso a ele. Ninguem mais poderá se cadastrar.')
	linha()
	while True:	
		conteudo['data'] = date.today()
		conteudo['Dia'] = date.today().day
		conteudo['Mes'] = date.today().month
		conteudo['Ano'] = date.today().year
		conteudo['Registro'] = str(input('O que quer me falar? '))
		with open("arquivo.txt", "r+") as arquivo:
			arquivo.write(f'{conteudo["data"]} ou ')
			arquivo.write(f'{conteudo["Dia"]}/')
			arquivo.write(f'{conteudo["Mes"]}/')
			arquivo.write(f'{conteudo["Ano"]}\n')
			arquivo.write(f'{conteudo["Registro"]}\n')
			arquivo.readlines()
		continuar = ' '
		while continuar not in 'SN':
			continuar = str(input('Quer continuar escrevendo [S/N]? ')).strip().upper()[0]
			if continuar == 'S':
				continue
			else:
				if continuar == 'N':
					break
		if continuar == 'N':
			break


# PROGRAMA PRINCIPAL

with open('logs.txt') as registro:
	for item in registro:
		valores = item.split()
		logins.append(valores)
contador = 0
while True:
	if contador == 0:
		usuario = str(input('Login: '))
		if teusu(usuario) == False:
			break
		senha = input('Senha: ')
		if tesen(senha) == False:
			break
	contador += 1
	if len(logins) == 0:
		login()
	else:
		diario()
		break
