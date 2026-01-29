import os
import copy
import string
import time as t
import random as rd
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
 
configPadrao = {
 'N de Jogadores' : 2,
 'N de pares de cartas' : 10,
 'Icone carregamento' : '@',
 'Ciclos de carregamento' : 1
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
			t.sleep(0.05)
		for j in range(limite):
			clear()
			linha.pop()
			print('\n\n\t',*linha)
			t.sleep(0.05)

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
			menuConfiguracao()
			
		elif opc == 3:
			creditos()
		
		elif opc == 4:
			exit()
			
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
	
	# Exibir placar
	print('\t','-'*20)
	for k,v in pontuacao.items():
		print('\t',k,' --> ',v)
	print('\t','-'*20)
		
	nome = list(pontuacao.items())[vez][0]
	print(f'\n\n Vez do :  {nome}')
	print('\n\n',auxast)

def jogo():
	global cartas, config, pontuacao, vez
	while True:
		exibirCartas()
		
		# verificar termino da partida
		soma = 0
		for i in range(config[listConfig[0]]):
			num = list(pontuacao.items())[i][1]
			soma += num
		if soma == config[listConfig[1]]:
			print('\n\t Fim !!! ')
			t.sleep(2)
			break
			
		try:
			v1 = int(input(' ~> '))
			if v1 == -1: break # retornar ao menu
			auxiliar[v1-1] = cartas[v1-1]
			exibirCartas()
			v2 = int(input(' ~> '))
			if v2 == -1: break # retornar ao menu
			auxiliar[v2-1] = cartas[v2-1]
			exibirCartas()
			t.sleep(2)

			if cartas[v1-1] == cartas[v2-1]:
				# player marca 1 ponto
				pontuacao[f'Player{vez+1}'] += 1
				# Jogar novamente
				vez -= 1
			else:
				#esconder cartas
				auxiliar[v1-1] = '{:02d}'.format(v1)
				auxiliar[v2-1] = '{:02d}'.format(v2)
		except:
			print('\n\t [ ERROR ] - Caractere incorreto')
			t.sleep(1)
			vez -=1
			
		# verificar vez
		if vez + 1 >= config[listConfig[0]]:
			vez = 0
		else:
			vez += 1

def creditos():
	load = ['/','-','\\','|']
	linha = ['\t\t .']
	
	for i in range(5):
		for y in range(2):
			for y in load:
				clear()
				for x in linha:
					print(x)
				print('\n\t\t',y)
				t.sleep(0.1)
		linha.append('\t\t .')
	
	clear()
	print('''
	
	.___________________________.
	|.  \t\t    <[0_0]3     
	|   - - - Redes Sociais - - - 
	|.  \t                                          
	|.       GITHUB : CLedsonB        
	|.   YOUTUBE : @cledsonbds  
	|.  \t 
	|__________________________
	''')
	t.sleep(5)

def menuConfiguracao():
	global configPadrao, config, listConfig, pontuacao
	
	while True:
		clear()
		
		print('\n Configuracoes')
		
		i = 0
		for key in listConfig:
			print(f'\t[{i+1}]. ',key)
			i += 1
		print(f'\t[{i+1}]. Redefinir')
		print(f'\t[{i+2}]. Sair e salvar')
		
		try:
			opc = int(input(' ~> '))

			if opc == 1:
				print('\n Digite o numero de jogadores : ')
				print(f' Valor atual : {config[listConfig[opc-1]]} --> {list(pontuacao.keys())}\n')
				aux = int(input(' ~> '))
				pontuacao = {}
				config[listConfig[opc-1]] = aux
			
				for i in range(aux):
					nome = input(f'\n Insira o nome do jogador {i+1}\n --> ')
					pontuacao[nome] = 0
			
			elif opc == 2:
				print('\n Digite a quantidade de pares de cartas : ')
				print(f' Valor atual --> {config[listConfig[opc-1]]} ( max. 26) ')
				
				aux = int(input(' ~> '))
				
				if aux > 26 or aux < 1:
					print('Opcao invalida !!!')
				else:
					config[listConfig[opc-1]] = aux
					
			elif opc == 3:
				print('\n Icone da barra de carregamento : ')
				print(f' Valor atual --> {config[listConfig[opc-1]]}')
				aux = input(' ~> ')
				config[listConfig[opc-1]] = aux
			elif opc == 4:
				print('\n Ciclos da barra de carregamento : ')
				print(f' Valor atual --> {config[listConfig[opc-1]]}')
				aux = int(input(' ~> '))
				config[listConfig[opc-1]] = aux
			elif opc == 5:
				print(' Redefinir Configuracoes : ')
				i = 0
				for k in range(len(configPadrao)):
					print(f' {listConfig[k]} : {config[listConfig[k]]} --> {configPadrao[listConfig[k]]} ')
					i += 1
				aux = input('\n Deseja redefinir todas as configuracoes ? ( s / n )\n ~> ')
				
				if aux == 's':
					pontuacao = {}
					for i in range(len(configPadrao)):
						config[listConfig[i]] = configPadrao[listConfig[i]]
					for i in range(config[listConfig[0]]):
						pontuacao[f'Player{i+1}'] = 0
				elif aux == 'n':
					print('\n Operacao cancelada')
				else:
					print('\n Caractere invalido !!!')
					
			elif opc == 6:
				print('\n Configuracoes atualizadas !!!')
				t.sleep(1)
				break
			else:
				print('\n Numero invalido !!!')
				
		except:
			print('\n Caractere invalido\n Tente Novamente')
			t.sleep(1)
	
	
# inicio do programa
menuInicial()