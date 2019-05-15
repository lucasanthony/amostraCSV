#coding: utf-8

def hello():
	return "helloworld"

def csvtolist(arquivo,separador):
	import csv
	lista = []
	arquivo = '%s.csv' %arquivo
	with open(arquivo) as csvfile:
   		dados = csv.reader(csvfile, delimiter=separador)
   		for linha in dados:
   			lista.append(linha)
	return lista


def randomLines(lista) :
	retorno = [];


def randomLines():
	import random
	saida = []
	fid = open("dados.csv", "r")
	dados = fid.readlines()
	fid.close()
	saida = []
	saida.append(dados[0])
	random.shuffle(dados)

	for i in range(10000):
		saida.append(dados[i])
	
	fid = open("amostra.csv", "w")
	fid.writelines(saida)
	fid.close()

randomLines()
