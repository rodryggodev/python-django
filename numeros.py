# NUMEROS EM PYTHON

# importando a bliblioteca de matematica
import math

num1 = 4;
num2 = 7;



#convertendo numero int para float

#a = float(5);
#print(a);

#convertendo de float para inteiro
#b = int(5.4);
#print(b)



 #operadores
 # + adição
 # - subtração
 # * multiplicação
 # / divisão
 # % mode
 # ** esponenciação
 # // for division que faz arredondamento


print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 // num2)

#ordem de precedencia
print((5 + 5) * (3+5))

#abs() -> retorna um numero absoluto
print(abs(-16))


#pow() -> power faz esponenciação
print(pow(3,3))

#max() e min() numero maior entre valores e numero menor
print(max(1, 10))
print(min(100, 1))

# arendondamento em aproximação round() tanto pra cima quanto para baixo, depende do valor passado em float
print(round(7.6))

# aredondamento para cima e para baixo floor, lembrando que para usar o floot precisamos importar o math
print(math.floor(8.8)) # pra baixo
print(math.ceil(8.8)) # pra cima
print(math.sqrt(8.9)) # raiz quadrada
