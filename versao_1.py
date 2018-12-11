# coding=utf-8
modofacil = "Em CAM1 de marido e CAM2, CAM3 mete a CAM4"
modomedio = "Se CAM1 trouxesse CAM2, CAM3 nao puxava CAM4"
mododificil = "CAM1 nao quer ser CAM2 nao lhe CAM3 a CAM4"

respfa = ["BRIGA", "MULHER", "NINGUEM", "COLHER"]
respme = ["FERRADURA", "SORTE", "BURRO", "CARROCA"]
respdi = ['QUEM', 'LOBO', 'VISTA', 'PELE']

niveis = ['facil', 'medio', 'dificil']
modo  = [modofacil, modomedio, mododificil]
respostas = [respfa, respme, respdi]
campos = ['CAM1', 'CAM2', 'CAM3', 'CAM4']

def boas_vindas():
	print('Seja bem vindo ao jogo das perguntas!')
boas_vindas()

def nivel():
	nivel_escolhido = input("Escolha um nivel: ( Facil | Medio | Dificil ): ").lower()
	print('Você escolheu o modo {}.'.format(nivel_escolhido))
	nivel_escolhido = niveis.index(nivel_escolhido)
	return nivel_escolhido
index_nivel = nivel()
print(index_nivel)
def jogar():
	jogando_nivel = niveis[index_nivel]
	frase_nivel = modo[index_nivel]
	print('jogando_nivel {}'.format(jogando_nivel))
	print('\n {}'.format(frase_nivel))
	print('\n Escolha as palavras que substiruirão os campos de 1 a 4: ')
jogar()

def resp_nivel():
	acertos = []
	indice = 0
	frase_nivel = modo[index_nivel]
	for local in campos:
		entrada = input('Substitua a {} palavra: '.format(local)).upper()
		resposta = entrada
		resp_modo = respostas[index_nivel]
		resp1 = resp_modo[indice]
		#imprime a entrada do usuário
		print(resposta)
		#imprime a resposta necessária para acertar
		print(resp1)
		while resposta != resp1:
			print('Você errou! Tente novamente!')
			entrada = input('Substitua a {} palavra: '.format(local)).upper()
			resposta = entrada
			resp_modo = respostas[index_nivel]
			resp1 = resp_modo[indice]
			#imprime a entrada do usuário
			print(resposta)
			#imprime a resposta necessária para acertar
			print(resp1)
		if resposta == resp1:
			print('Você acertou')
			indice += 1
	print('Parabens, você finalizou o jogo!')
resp_nivel()