#A quantidade de areas já esta definida

GMD_a = 0
GMD_b = 0
GMD_c = 0
GMD_d = 0
limite_animais = 15

animais = []
cont = 0
cont_2 = 0

print("Seja bem vindo ao sistema")
while cont == 0:
    
    print("1 - Mostrar dados" '\n'
          "2 - Definir GMD das areas" '\n'
          "3 - Definir animais" '\n'
          "4 - Definir movimentações e calcular" '\n'
          "5 - Apagar dados" '\n'
          "6 - Sair" '\n')
    menu = int(input("escolha uma opção"))
           
    if menu == 1:
        print("Suas areas são:" '\n'
        "Area A, com GMD de", GMD_a, '\n'
        "Area B, com GMD de", GMD_b, '\n'
        "Area C, com GMD de", GMD_c, '\n'
        "Area D, com GMD de", GMD_d, '\n')
        
        print("Segue o peso de cada animal:" '\n'
        , animais, '\n')
    
    elif menu == 2:
        if GMD_a == 0 and GMD_b == 0 and GMD_c == 0 and GMD_d == 0:
            var = (input("Nenhuma das suas areas tem GMD definido, gostaria de definir todas? (Sim ou nao)"))
            if var == "sim" or var == "Sim":
                GMD_a = float(input("Defina o GMD da area A"))
                GMD_b = float(input("Defina o GMD da area B"))
                GMD_c = float(input("Defina o GMD da area C"))
                GMD_d = float(input("Defina o GMD da area D"))
            else:
                var = (input("Qual das areas gostaria de definir o GMD? (escrever a letra que corresponde a area)"))
                if var == "a" or var == "A":
                    GMD_a = float(input("Defina o GMD da area A"))
                elif var == "b" or var == "B":
                    GMD_b = float(input("Defina o GMD da area B"))
                elif var == "c" or var == "C":
                    GMD_c = float(input("Defina o GMD da area C"))
                elif var == "d" or var == "D":
                    GMD_d = float(input("Defina o GMD da area D"))
        else:
            var = (input("Qual das areas gostaria de definir o GMD? (escrever a letra que corresponde a area)"))
            if var == "a" or var == "A":
                GMD_a = float(input("Defina o GMD da area A"))
            elif var == "b" or var == "B":
                GMD_b = float(input("Defina o GMD da area B"))
            elif var == "c" or var == "C":
                GMD_c = float(input("Defina o GMD da area C"))
            elif var == "d" or var == "D":
                GMD_d = float(input("Defina o GMD da area D"))
        
    elif menu == 3:
        var = float(input("Defina o peso do animal"))
        animais.append(var)
        cont_2 = cont_2 + 1
        
    elif menu ==4:
        cont_3 = 0
        ganho_peso = 0
        if cont_2 == 0:
            print("favor, criar algum animal antes de definir uma movimentação")
        elif cont_2 > 15:
            print("O numero de animais está acima do que as areas suportam")
        else:
            while cont_3 == 0:
                var = (input("Escolha uma das suas areas (escrever a letra que corresponde a area)"))
                dias = int(input("Quantos dias eles vão passar nessa area?"))
                if var == "a" or var == "A":
                    for i in range(dias):
                        for i in range(cont_2):
                            animais[i] = animais[i] + GMD_a
                        ganho_peso = ganho_peso + GMD_a
                
                elif var == "b" or var == "B":
                    for i in range(dias):
                        for i in range(cont_2):
                            animais[i] = animais[i] + GMD_b
                        ganho_peso = ganho_peso + GMD_b
                
                elif var == "c" or var == "C":
                    for i in range(dias):
                        for i in range(cont_2):
                            animais[i] = animais[i] + GMD_c
                        ganho_peso = ganho_peso + GMD_c
                            
                
                elif var == "d" or var == "D":
                    for i in range(dias):
                        for i in range(cont_2):
                            animais[i] = animais[i] + GMD_d
                        ganho_peso = ganho_peso + GMD_d
                    
                var = (input("Existe mais alguma movimentação? (sim ou nao)"))
                if var == "sim" or var == "Sim":
                    print("O ganho de peso atual é de", ganho_peso)
                else:
                    print("Novo peso dos animais:", animais)
                    cont_3 = cont_3 + 1
            print("O ganho de peso total de cada animal foi de", ganho_peso, '\n')  
            
    elif menu == 5:
        cont_4 = 0
        var = (input("gostaria de apagar todos os dados? (sim ou nao)"))
        if var == "sim" or var == "Sim":
            animais.clear()
            print("lista de animais apagada" '\n')
            cont_2 = 0
        else:
            while cont_4 == 0:
                var = int(input("qual animal você deseja apagar? (escreva o numero que corresponde a ele na lista)"))
                if var > cont_2 or var == 0:
                    print("favor, digitar um animal existente" '\n')
                else:
                    del(animais[var-1])
                    print("O", var,"º animal da lista foi apagado" '\n')
                    cont_2 = cont_2 - 1
                    cont_4 = cont_4 + 1
            
    elif menu == 6:
        print("Sistema encerrado, Tenha um bom dia ^^")
        cont = cont + 1
        
    else:    
        print("favor, selecionar uma opção valida" '\n')
