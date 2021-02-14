# FOR, RANGE
# em python tudo é um objeto

# repetição, mais usado para percorrer listas
lista =['arroz', 'carne', 'feijao', 'azeitona', 'cerveja']
#for i in range(5):
    #print(1+i) # vai começar de 1 a 5, caso queira começar do zero basta colocar só a variavel(i)

for i in lista:
    print(i,len(i))
#antes do len tem que ter uma (,) len é o lenght para saber a quantidade de caracteres
# for i in lista.copy(): retorna um espelho ou copia da lista
# break , serve para quebrar ou parar a repetição
   
 # if -> condicional
#senha = 'admin'

#if(senha == 'adm123'):
 #   print('Olá, Administrador')
#else:
 #   print('acesso negador')

a = 3

if a != 3:
    print('é diferente')
elif a == 3:
    print('é igual')
else:
    print('nem um, nem outro')



## while é o faça enquanto

while True:
    pass
#pass não faz nada é como se fosse um "null"
