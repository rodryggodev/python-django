# trabalhando strings no python

minha_string = 'blblblblblblblblbl';
stre = 'ABABABAB';
c = 'rodrigo'
## .upper() deixa tudo em maisculo
print(f'{minha_string.upper()}');

#lower() tudo em minusculo
print(f'{stre.lower()}');

#capitalize() -> deixa a primeira letra maiscula

print(f'{c.capitalize()}');

# isupper() -> retorna true ou false se caso queria saber se o texto tá em maisculo ou minusculo
print(f'{minha_string.isupper()}');

# strip() -> remove espaços

#replace(tem que passar parametro)-> substitui letra ou texto
#replace('a palavra atual', 'palavra nova')

# .len()-> diz quantos tamanho tem uma string

print(minha_string[3]) #-> ver indeice

# saber se tem uma palavra especifica na variavel true ou false
x = 'bl' in minha_string
print(x)
# print(f'{}') esse f e {} serve para concatenar variavel

