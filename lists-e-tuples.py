# colection(coleção) list(lista) tuple(tupla)




#lista(list)
compras = ['arroz', 'feijao', 'sardinha', 'macarrão', 'breja', 'queijo'];

print(compras[4]);

# trazendo os valores de tras pra frente
print(compras[-1]);

# do indice 1 pra frente,só mudar o numero do indice lembrando que ele nao pega o valor final
print(compras[1:4]);

#adicionando um novo elemento na posição zero
compras[0] = 'vinho';
print(compras);

#adicionar outra lista
compras.extend(['queijo', 'azeitona']);
print(compras);

#adicionar um elemento
compras.append('salame');
print(compras);

#adicionando no meio da lista, basta passar o numero do indice
compras.insert(1, 'wysky');
print(compras);

#remover só com o pop o ultimo valor 
compras.pop();
print(compras);

#remover pelo nome do indice
compras.remove('breja');
print(compras);

#limpar a lista
#compras.clear();
#print(compras);

#saber o numero do indice
print(compras.index('queijo'));

# quantos nome temos repetidos
print(compras.count('queijo'));

#ordenar tanto string, quanto numeros
compras.sort();
print(compras);

# de tras pra frente
compras.reverse();
print(compras);

# invertendo do z para o a
compras.reverse();
print(compras);

#copiar a lista
compras2 = compras;
print(compras2);

# copia
compras2 = compras.copy();
print(compras2);

## tuple(tupla) ela não pode ser alterada, nem adicionar e nem remover e usa se () ao inves de []
cordenadas = (100, -200);
cordenadas.pop();

