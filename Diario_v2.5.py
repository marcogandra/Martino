#coding=Utf-8
import os
import re
from datetime import date

usuario = {}
conteudo = {}

conteudo['data'] = date.today()
conteudo['Dia'] = date.today().day
conteudo['Mes'] = date.today().month
conteudo['Ano'] = date.today().year

def linha():
	print('=-='*20)

def arquivo():
	'''
	Confere se há algo dentro do arquivo onde ficam guardados os dados do usuário
	'''
	return os.stat('logs.txt').st_size >= 1

def registro():
	'''
	Adiciona um novo usuário e uma nova senha ao arquivo de registro de usuário
	'''
	with open('logs.txt', 'w') as registro:
		registro.write(f'{usuario["Login"]}')
		registro.write(f'\n')
		registro.write(f'{usuario["Senha"]}')
		print('Parabens por ter adicionado um novo usuario!')
		print(f'Seu usuário é {usuario["Login"]} e sua senha é {usuario["Senha"]}.\n\nGuarde com atenção!')

	
def novo_usu():
	'''
	Função para cadastrar um novo usuário.
	Chama a função login() e guarda o 'login' e a 'senha'
	Pergunta se quer registrar o usuário, com esse login e senha
	Repete o procedimento enquanto a pessoa digitar 'N'
	Se digitar 'S', abre o método registro()
	'''
	novo = login()
	res = ''
	while True:
		try:
			res = str(input('Gostaria de guardar esse usuário e senha [S/N]? ')).upper().strip()[0]
		except:
			print('Coloque uma entrada válida!')
			continue
		if res == 'N':
			novo = login()
		else:
			if res == 'S':
				usuario['Login'] = novo[0]
				usuario['Senha'] = novo[1]
				registro()
				break
		
def login():
	'''
	Define um nome para o usuário e uma senha
	'''
	while True:
		try:
			nome = str(input('Digite o nome de um usuário: ')).strip()
		except:
			print('Escreva um login compatível.')
			continue
		try:
			senha = input('Digite uma senha: ')
		except:
			print('Escreva uma senha válida.')
		if (nome and senha) != "":
			print('Válidação de login e senha completos')
			break
	return nome, senha

def abertura():
	'''
	Com essa função, podemos ler o arquivo onde nós guardamos o login e a senha.
	E também adicionar esses dados para a variável 'usuario'
	A função retorna um dicionário com 'Login' e 'Senha' como chaves
	'''
	with open('logs.txt', 'r') as leitura:
		for index, words in enumerate(leitura):
			word = words.split()[0]
			if index == 0:
				usuario['Login'] = word
			if index == 1:
				usuario['Senha'] = word
		return usuario

def conferencia(dado_sis, dado_conferir):
	'''
	Puxa os dados e faz a conferência para saber se o login e a senha estão batendo.
	Se bater tudo, retorna True. Caso contrário retorna False
	'''
	# Utilizano o método match para bater os dados de login e senha
	m_login = re.match(dado_conferir[0], dado_sis['Login'])
	m_senha = re.match(dado_conferir[1], dado_sis['Senha'])
	
	#Confere se lo
	if m_login and m_senha:
		print('\nTudo ok! Sua entrada para escrever está liberada.\n')
		return True
	else:
		print("login e/ou senha incorreto(s)")
		return False

def bem_vindo():
	'''
	Essa função dá boas vindas ao usuário cadastrado.
	E inicia a função diario() enquanto o usuário quiser escrever.
	Quanto o usuario retornar False de diario(), entao a função retorna False também.
	'''
	linha()
	print(f'Bem vindo ao seu diário particular, {usuario["Login"]}. Somente você terá acesso a ele. Ninguem mais poderá se cadastrar.')
	linha()
	while True:
		escrever = diario()
		if escrever == False:
			return False

def diario():
	'''
	Essa função é responsável por gravar o conteúdo do diário.
	Pergunta pro usuário se ele quer permanecer escrevendo ou quer sair.
	Quando o usuário digita 'N' para saída, a função retorna False e volta para bem_vindo()
	'''
	conteudo['Registro'] = str(input('O que quer me falar? '))
	with open("arquivo.txt", "r+") as arquivo:
		arquivo.write(f'{conteudo["data"]} ou ')
		arquivo.write(f'{conteudo["Dia"]}/')
		arquivo.write(f'{conteudo["Mes"]}/')
		arquivo.write(f'{conteudo["Ano"]}\n')
		arquivo.write(f'{conteudo["Registro"]}\n')
		arquivo.readlines()
	continuar = ' '
	while True:
		continuar = str(input('Quer continuar escrevendo [S/N]? ')).strip().upper()
		if continuar == "" or continuar == "S":
			break
		else:
			if continuar == 'N':
				print('\nObrigado por participar!\n')
		return False


# Confere se tem algo no arquivo
tem_arquivo = arquivo()

# Se falso, chama a função de um novo usuário
if tem_arquivo == False:
	novo_usu()

# Se tiver dados no arquivo, o programa começa a rodar
if tem_arquivo == True:
	# inicio do procedimento, chamando os dados que estão no arquivo
	dados = abertura()
	# Começa o loopig para a conferencia de login. Caso o login ou senha estejam incorretos, a função retorna.
	while True:	
		# chama a função login() para depois fazer conferencia com os dados gravados
		conferir = login()
		# agora iremos bater os dados com o login
		res_conf = conferencia(dados, conferir)
		# se a conferência bater, inicia um novo procedimento.
		if res_conf == True:
			# chama a função de inicio do diario, com a funcao bem_vindo()
			saudacao = bem_vindo()
			if saudacao == False:
				break
	