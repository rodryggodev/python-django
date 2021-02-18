# if, else, statemensts, operadores logicos e compração
# or(ou) ou um ou outro true(verdade), se tiver um true e outro falso, sempre vai ser verdadeiro

# and(e) as duas tem que ser verdadeiras true, se um for verdadeira e outra false, ele vai da false

# and not (e não)

# not (nao) se for verdadeiro e passar pelo not, ele retorna como negação(false), e se for false ele retornar true(verdadeiro)

tenho_sede = True;
tenho_fome = False;

if tenho_sede:
    print('tenho sede');
else:
    print('bucho cheio');

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



if tenho_sede or tenho_fome:
    print('vou na cozinha');
elif tenho_sede and not (tenho_fome):
    print('Tomar agua');
elif not(tenho_sede) and tenho_fome:
    print('linguiça')
else:
    print('nao vou');    


######### COMPARAÇÃO ###########
# < menor
# <= menor igual
# > maior
# >= maior igual
# == igual
# != diferente

num1 = 3;
num2 = 10;
num3 = '11';
if num1 < num2:
    print('sim');
elif num1 > num2:
    print('talvez');
else:
    print('Noooops');

if num1 == num2:
    print('sim');
elif num1 != num3:
    print('Yes');
else:
    print('Noooops');
