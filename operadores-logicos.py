# or(ou) ou um ou outro true(verdade), se tiver um true e outro falso, sempre vai ser verdadeiro

# and(e) as duas tem que ser verdadeiras true, se um for verdadeira e outra false, ele vai da false

# and not (e não)

# not (nao) se for verdadeiro e passar pelo not, ele retorna como negação(false), e se for false ele retornar true(verdadeiro)

tenho_sede = True;
tenho_fome = False;

#### OPERADORES LOGIGOS #####
# or->ou
# and-> e
# not() -> não
    
if tenho_sede or tenho_fome:
    print('vou na cozinha');
else:
    print('nao vou');
    
if tenho_sede and tenho_fome:
    print('fazer um mexido');
else:
    print('nao tenho cede');
