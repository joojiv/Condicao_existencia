#Condição de existencia
from collections import OrderedDict

triang = []
while len(triang) < 3:
    add = float(input('Insira a medida do lado: '))
    triang.append(add)

maior = max(triang)
menor = min(triang)
triang.insert(0, maior)
triang.insert(1, menor)
triang_final = list(OrderedDict.fromkeys(triang))

existe = triang_final[2] - triang_final[1] < triang_final[0] < triang_final[1] + triang_final[2]

if existe == True:
    print('O triângulo existe!')
else:
    print('O triângulo não existe!')

