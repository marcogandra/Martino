#coding=Utf-8
# Importando biblioteca pandas
import pandas as pd
# Criando DataFrame
data = {}
df = pd.DataFrame(data)

#coding=Utf-8
# Dicionário com produtos a serem cadastrados e seus respectivos valores
produtos = {}
# Lista para definir indice nos produtos
index_list = []
q_list = []

def cadastrar():
	'''
	Função responsável por cadastrar produtos.
	Pede que seja digitado nome e valor e então guarda em 'produtos'
	'''
	produto = str(input('Digite o nome de um produto: ')).strip()
	valor = float(input('Digite o valor do produto: '))
	quant = int(input('Digite a quantidade do produto: '))
	q_list.append(valor)
	q_list.append(quant)
	produtos[produto] = q_list.copy()
	q_list.clear()

def listar():
	'''
	Lista os produtos a serem mostrados, quando necessário
	'''
	print(f'{"Index":<8} {"Produto ":<9}{"":-<20} {"Preço"}')
	index = 0
	for key, value in produtos.items():
		print(f'{index:<8} {key:<9}{"":-<20} {value}')
		index += 1

def buscar():
	'''
	Função que busca um produto em 'produtos'. Basicamente essa função retorna o valor do produto buscado.
	'''
	listar()
	while True:
		item = str(input('Digite o nome do produto procurado: ')).strip()
		if item in produtos:
			print(f'Valor do produto buscado: {produtos[item]}.')
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
	O que está guardado ainda não está incluso nessa versão.
	'''
	listar()
	index = 0
	for produto in produtos:
		index_list.append(index)
		index += 1
	while True:
		escolha = int(input('Digite o número do produto que quer editar: '))
		if escolha in index_list:
			break
	for index, value in enumerate(produtos):
		if index == escolha:
			n_prod = str(input('Digite o novo nome para o produto: ')).strip()
			n_valor = float(input('Digite o novo valor para o produto: '))
			produtos[n_prod] = produtos.pop(value)
			produtos[n_prod] = n_valor

def vender():
	'''
	Função em construção.
	'''
	listar()
	p_venda = input('Digite o número ou nome do produto vendido:').strip()

def sair():
	'''
	Essa função termina o programa. Porém, antes de fechar, o programa pega o que ficou na memória, aloca no dataframe e depois guarda no arquivo.
	'''
	for prod in produtos.items():
		print(produtos)
		print(produtos.keys())
		print(produtos.values())
		df['PRODUTO'] = produtos.keys()
		for l in produtos.values():
			for ind in l:
				df['VALOR'] = l[0]
				df['QUANTIDADE'] = l[1]
	print(df)
	df.to_csv('produtos_loja.csv', index=False)
	return quit()

def menu(esc):	
	'''
	Função do menu inicial. Conforme a escolha do usuário recebida, puxa a função desejada.
	'''
	if esc == 0:
		cadastro = cadastrar()
	elif esc == 1:
		busca = buscar()
	elif esc == 2:
		edicao = editar()
	elif esc == 3:
		venda = vender()
	else:
		if esc == 4:
			sair()


#total_venda = soma_vendas()
frase = 'Bem vindo ao mercadinho virtual' 
print('='*len(frase))
print(frase)
print('='*len(frase))
print(f'\n{"MENU":=^31}')
index_menu, lista_menu = [], ['Cadastro', 'Busca', 'Edicao', 'Venda', 'Sair']
print(f'\nINDEX ---------------- MODULOS')
for i, v in enumerate(lista_menu):
	index_menu.append(i)
	print(f'{i} -------------------- {v.upper()}')
while True:
	esc = input('\nEscolha um item do menu pelo número do índice: ')
	if esc.isnumeric():
		esc = int(esc)
		if esc in index_menu:
			menu(esc)