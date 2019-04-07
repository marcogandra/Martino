#coding=Utf-8

# Importando biblioteca pandas
import pandas as pd

# Data frame com produtos existentes
try:
	df_arquivo = pd.read_csv('produtos_loja.csv')
	tem_ar = True
except:
	print('\nArquivo vazio!\n')
	tem_ar = False

# Dicionário que vai guardar os produtos existentes
produtos = {}

# Lista para definir indice nos produtos, indice de menu, lista de produtos e valores
index_menu = []
index_list = []
q_list = []
nomes = []
valores = []

def resgate():
	for line in df_arquivo:
		count = df_arquivo[line].count()
		for index, value in enumerate(df_arquivo[line]):
			if line == 'PRODUTO':
				nomes.append(value)
			if line == 'VALOR':
				valores.append([value])
			if line == 'QUANTIDADE':
				valores[index].append(value)
	
	for i, v in enumerate(nomes):
		produtos[v] = valores[i]
		
	nomes.clear()
	valores.clear()

def inc():
	'''
	Apenas define quando uma entrada está incorreta e deve ser digitado novamente.
	'''
	print('Entrada incorreta. Digite novamente')

def bem_vindo():
	'''
	Um bem vindo bonito para nossos usuários!
	'''
	frase = 'Bem vindo ao mercadinho virtual' 
	print('='*len(frase))
	print(frase)
	print('='*len(frase))

def nav():
	'''
	Apresentação visual do menu.
	'''
	print(f'\n{"MENU":=^31}')
	lista_menu = ['Listar', 'Cadastro', 'Busca', 'Edicao', 'Venda', 'Sair']
	print(f'\nINDEX ---------------- MODULOS')
	for i, v in enumerate(lista_menu):
		index_menu.append(i)
		print(f'{i} -------------------- {v.upper()}')
	return index_menu

def cadastrar():
	'''
	Função responsável por cadastrar produtos.
	Pede que seja digitado nome e valor e então guarda em 'produtos'.
	'''
	while True:
		try:
			produto = input('Digite o nome de um produto: ').strip()
			if produto.isalpha():
				break
			else:
				inc()
				continue
		except:
			continue

	while True:
		try:
			valor = input('Digite o valor do produto: ')
			if valor:
				valor = float(valor)
				break
		except:
			inc()
			continue
	while True:
		try:
			quant = input('Digite a quantidade do produto: ')
			if quant.isnumeric():
				quant = int(quant)
				break
		except:
			inc()
			continue
	q_list.append(valor)
	q_list.append(quant)
	produtos[produto] = q_list.copy()
	q_list.clear()

def listar():
	'''
	Lista os produtos a cadastrados na memória ativa.
	'''
	print(f'{"Index":<8} {"Produto ":<9}{"":-<20} {"Preço"} {"Quantidade":>12}')
	index = 0
	for key, value in produtos.items():
		print(f'{index:<8} {key:<9}{"":-<20} {value[0]:<6.2f} {value[1]:>6}')
		index += 1

def buscar():
	'''
	Função que busca um produto em 'produtos'. Basicamente essa função retorna o valor e quantidade do produto buscado.
	'''
	listar()
	while True:
		item = str(input('Digite o nome do produto procurado: ')).strip()
		if item in produtos:
			print(f'Valor do produto buscado: R$ {produtos[item][0]:.2f} - Quantidade do produto buscado: {produtos[item][1]} unidades.')
			while True:
				nova_busca = str(input('Gostaria de buscar por outro produto [S/N]? ')).strip().upper()
				if nova_busca == '':
					continue
				if nova_busca in 'SN':
					break
			if nova_busca == 'N':
				break
			elif nova_busca == 'S':
				continue

def editar():
	'''
	Função responsável por editar algo que está na memória ativa do programa.
	'''
	listar()
	index = 0
	for produto in produtos:
		index_list.append(index)
		index += 1
	while True:
		try:
			escolha = int(input('Digite o número do produto que quer editar: '))
			if escolha in index_list:
				break
		except:
			inc()
			continue
	for index, value in enumerate(produtos):
		for k, v in produtos.items():	
			if index == escolha:
				while True:
					try:
						n_prod = str(input('Digite o novo nome para o produto: ')).strip()
						break
					except:
						int()
						continue
				while True:
					try:
						n_valor = float(input('Digite o novo valor para o produto: '))
						break
					except:
						int()
						continue
				while True:
					try:
						n_quant = int(input('Digite a nova quantidade para o produto: '))
						break
					except:
						int()
						continue
				produtos[n_prod] = produtos.pop(value)
				produtos[n_prod] = [n_valor, n_quant]
				break

def vender():
	'''
	Módulo de venda. Elimina uma unidade em relação ao produto digitado pelo usuário.
	'''
	listar()
	while True:
		try:
			p_venda = input('Digite o nome do produto vendido: ')
			if p_venda.isalpha():
				break
		except:
			print('Entrada inválida:')
			continue
	if p_venda in produtos:
		produtos[p_venda][1] -= 1
		print(f'\nProduto {p_venda} vendido com sucesso!\nAgora a quantidade do {p_venda} é de {produtos[p_venda][1]} unidades')

def sair():
	'''
	Essa função termina o programa. Porém, antes de fechar, o programa pega o que ficou na memória, aloca no dataframe e depois guarda no arquivo.
	'''
	# Criando DataFrame responsável pela manipulação dos arquivos
	df = pd.DataFrame(columns=['PRODUTO', 'VALOR', 'QUANTIDADE'])

	for k, v in produtos.items():
		df = df.append({'PRODUTO': k, 'VALOR': v[0], 'QUANTIDADE': v[1]}, ignore_index=True)

	# Salvando arquivos do DF em CSV
	df.to_csv('produtos_loja.csv', index=False)
	return quit()

def b_menu():
	while True:
		esc = input('\nEscolha um item do menu pelo número do índice: ')
		if esc.isnumeric():
			esc = int(esc)
			if esc in index_menu:
				menu(esc)

def menu(esc):	
	'''
	Função do menu inicial. Conforme a escolha do usuário, busca a função desejada.
	'''
	if esc == 0:
		listagem = listar()
	elif esc == 1:
		cadastro = cadastrar()
	elif esc == 2:
		busca = buscar()
	elif esc == 3:
		edicao = editar()
	elif esc == 4:
		venda = vender()
	else:
		if esc == 5:
			sair()


# INÍCIO DO PROGRAMA
#total_venda = soma_vendas()
bem_vindo()
if tem_ar:
	resgate()
nav()
b_menu()
