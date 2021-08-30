#coding utf-8
def lista_so_com_oposto(lista):
	i=0
	excluidos=[]
	def procura_oposto(l,e, ind):
		for j in range(len(l)):
			num = l[j]
			if j != ind and num+e==0: return True
		return False
	
	def tira_elementos(l, ex):
		for i in range(len(l)-1, -1,-1):
			e=l[i]
			for el in ex:
				if e == el:
					for c in range(i, len(l)-1):
							l[c],l[c+1]=l[c+1],l[c]
					l.pop()
					break
					

#armazena os elementos a serem excluídos numa lista
	for i in range(len(lista)):
		elemento = lista[i]		
		op=False
		op = procura_oposto(lista,elemento,i)
		if not op: excluidos.append(elemento)
	#print(excluidos)
	tira_elementos(lista, excluidos)
	

	return None
	




lista = [int(n) for n in input().split()]
print(lista_so_com_oposto(lista))
print(lista)
