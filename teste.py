#coding: utf-8

def randomLines():
	import random
	saida = []
	fid = open("dados.csv", "r")
	dados = fid.readlines()
	fid.close()
	dados.pop(0)

	random.shuffle(dados)

	for i in range(50000):
		saida.append(dados[i])
	
	fid = open("amostra.csv", "w")
	fid.writelines(saida)
	fid.close()

randomLines()
