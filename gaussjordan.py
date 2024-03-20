import numpy as np

a=np.array([[3.03,-12.1,14,-119],
	[-3.03,12.1,-7,120],
	[6.11,-14.2,21,-139]])

fila,colmn=a.shape
orden=max(fila,colmn)
matriz=np.zeros((orden,orden))
matriz[:fila,:colmn]=a
for j in range(min(fila,colmn)):
	if matriz[j][j]==0:
		for i in range(j+1,fila):
			if matriz[i][j]!=0:
				for k in range(orden):
					matriz[j][k],matriz[i][k]=matriz[i][k],matriz[j][k]
				break
	for i in range(orden):
		if i!=j:
			if matriz[i][j]!=0:
				if matriz[j][j]!=0:
					aux=matriz[i][j]/matriz[j][j]
				for k in range(orden):
					matriz[i][k]-=matriz[j][k]*aux
print(matriz[:fila,:colmn])