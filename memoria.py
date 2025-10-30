import os
import copy
import string
import time as t
import random as rd
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
 
configPadrao = {
 'N de Jogadores' : 2,
 'N de pares de cartas' : 5,
 'Icone carregamento' : '@',
 'Ciclos de carregamento' : 5
}
config = copy.deepcopy(configPadrao)

listConfig = []
for key in config.keys():
	listConfig.append(key)

pontuacao = {}
for i in range(config[listConfig[0]]):
	pontuacao[f'Player{i+1}'] = 0

vez = 0
def carregamento():
	global config, listConfig
	
	caractere = config[listConfig[2]]
	limite = 15
	volta = config[listConfig[3]]
	linha = []
	
	for i in range(volta):
		for j in range(limite):
			clear()
			linha.append(caractere)
			print('\n\n\t',*linha)
		for j in range(limite):
			clear()
			linha.pop()
			print('\n\n\t',*linha)

def menuInicial():
	carregamento()
	while True:
		clear()
		print('''
		°°°Jogo da Memoria °°°
		
		[1] - Novo Jogo
		[2] - Configuracoes
		[3] - Creditos
		[4] - Sair
''')
		try:
			opc = int(input(' ~> '))
		except:
			opc = 0
			
		if opc == 1:
			cartas, auxiliar = prepararCartas()
			carregamento()
			jogo()
			
		elif opc == 2:
			# menuConfiguracao()
			print('Em construcao')
			
		elif opc == 3:
			# creditos()
			print('Em construcao')
		
		else:
			print('\n Caractere invalido !!! ')
			t.sleep(1)
			
	
abc = string.ascii_uppercase
cartas, auxiliar = [], []
def prepararCartas():
	global cartas, config, auxiliar
	auxiliar = [f"{i:02d}" for i in range(1, 53)]
	for i in range(config[listConfig[1]]):
		cartas.append(abc[i])
		cartas.append(abc[i])
	rd.shuffle(cartas)
	return cartas, auxiliar

def exibirCartas():
	global cartas, auxiliar, config, pontuacao, vez
	aux, auxast, x,y = '', '', 0, 0
	for i in range(len(cartas)):
		if i % 5 == 0:
			aux += f'\n\n\t {cartas[i]} '
			auxast += f'\n\n\t {auxiliar[i]} '
			y += 1
		else:
			aux += f'  {cartas[i]} '
			auxast += f'  {auxiliar[i]} '
	clear()
	nome = list(pontuacao.items())[vez][0]
	ponto = list(pontuacao.items())[vez][1]
	print(f'\n\n {nome} : {ponto}')
	print('\n\n',auxast)

def jogo():
	global cartas, config, pontuacao, vez
	while True:
		exibirCartas()
		v1 = int(input(' ~> '))
		auxiliar[v1-1] = cartas[v1-1]
		exibirCartas()
		v2 = int(input(' ~> '))
		auxiliar[v2-1] = cartas[v2-1]
		exibirCartas()
		t.sleep(2)
	
		if cartas[v1-1] == cartas[v2-1]:
			# player marca 1 ponto
			print(' + 1 ponto')
			pontuacao[f'Player{vez+1}'] += 1
			t.sleep(1)
		else:
			#esconder cartas
			auxiliar[v1-1] = '{:02d}'.format(v1)
			auxiliar[v2-1] = '{:02d}'.format(v2)
		
		if vez + 1 >= config[listConfig[0]]:
			vez = 0
		else:
			vez += 1

menuInicial()