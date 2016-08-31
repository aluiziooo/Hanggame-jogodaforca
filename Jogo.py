import pickle
import os
import random
facil = ["melhor","grande","claro","azul","vermelho","preto","branco","casa","tempo","felicidade","bondade","vida","caneta","cavalo","trem","golpe","cosmos"]
dificil = ["procrastinar","prolegômenos","vicissitudes","pernóstico","opróbrio","idiossincrasia","elucubrações","chistoso","acrimônia","combustível","concurso","protesto","governo","paquiderme","tamandaré"]
dificuldade = facil
vida = 5
partida = []
ranking = []

#DESCOBRIR SUA POSIÇÃO NO RANKING
def  posicaodocidadao(pont):
    x = 0
    z = 0
    if len(ranking) != 0:
        for p in range(len(ranking)):
            if pont > ranking[p]['pont']:
                x = p+1
                break
            z += 1
        if z == len(ranking):
            x = z + 1
    else:
        x = 1
    return x
#SALVA O RECORD DO CARA QUANDO TERMINA O JOGO
def salvarrecord(nome,pont):
    ranking = lerranking()
    posicao = posicaodocidadao(pont)
    z = 0
    jogador = {'nome':nome,'pont':pont}
    if len(ranking) != 0:
        posicao -= 1
        ranking.insert(posicao,jogador)
            
            
    else:
        ranking.append(jogador)
    arquivo = open("ranking.f","wb")
    pickle.dump(ranking,arquivo)
    arquivo.close()
#LIMPA A TELA
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
#LER O RANKING E JOGA TUDO O QUE TIVER NA MEMORIA SALVA PARA UMA LISTA
def lerranking():
    arquivo = open("ranking.f","rb")
    ranking = pickle.load(arquivo)
    arquivo.close()
    return ranking
#ORGANIZA A LISTA CASO TIVER MAIS PERDIDA DO QUE MUNDIAL DO PALMEIRAS OU O TORNEIRO DE VERÃ- - LIBERTADORES DE 2000 DO CORINTHIANS*
def organizarranking():
    for i in range(len(ranking)):
        j = 1
        for j in range(len(ranking)):
            if ranking[i]['pont'] > ranking[j]['pont']:
                aux = ranking[i]['pont']
                ranking[i]['pont'] = ranking[j]['pont']
                ranking[j]['pont'] = aux
            else:
                pass
    return ranking

#LER TODOS OS DADOS DA MINHA PARTIDA SALVA NA MEMORIA E JOGA NA FUNÇÃO "CONTINUAR JOGO"
def continuarpartida():
    arquivo = open("partidasalva","rb")
    partida = pickle.load(arquivo)
    arquivo.close()
    pontos = partida['pontos']
    acertos = partida['acertos']
    palavras  = partida['palavras']
    dificuldade = partida['dificuldade']
    vidas = partida['vidas']
    letras = partida['letras']
    palavra = partida['palavra']
    continuarjogo(pontos,acertos,palavras,dificuldade,vidas,palavra,letras)
def lerpartidassalvas():
    partidas =[]
    arquivo = open("partidasalva","rb")
    salvos = pickle.load(arquivo)
    arquivo.close()
    partidas.append(salvos)
    return partidas
    
#RETORNA O BOLEANO PARA A VISIBILIDADE CERTA DO MENU
def retornaboleanodobolado():
    arquivo = open("partidasalva","rb")
    eita = pickle.load(arquivo)
    if eita['dificuldade'] != "":
        continuar = True
    else:
        continuar = False
    arquivo.close()
    return continuar
def salvarpartida(pontos,acertos,palavras,dificuldade,vidas,palavra,letras):
    partida = {'pontos':pontos,'acertos':acertos,'palavras':palavras,'dificuldade':dificuldade,'vidas':vidas,'palavra':palavra,'letras':letras}
    arquivo = open("partidasalva","wb")
    pickle.dump(partida,arquivo)
    arquivo.close()
#DEFINIÇÕES COM OS TIPOS DE JOGOS, ACHEI MAIS FACIL FAZER ASSIM :P
def novojogo(dificuldade,vida):
        palavras = []
        while True:
            palavra = random.choice(dificuldade)
            if palavra not in palavras:
                palavras.append(palavra)
                break
        letras = ""
        x = 0
        acertos = []
        pontuacao = 0
        palavra = random.choice(dificuldade)
        clear()
        while True:
            subs = ""
            for l in palavra:
                subs += l if l in acertos else "_"
            if subs == palavra:
                if palavras == dificuldade:
                    pontuacao += (vida*100 + 1000*1) if dificuldade == facil else (vida*100 + 1000*2)
                    posicao = posicaodocidadao(pont)
                    while True:
                            print("É um novo recorde! Você está na posição",posicao,"do ranking. \nQual o seu nome?(5 caracteres são obrigatorios e so 5 mesmo >:) )")
                            nome = input(">")
                            if len(nome) == 5:
                                break
                            else:
                                clear()
                                print("SÃO 5 CARACTERES!!!")
                    break
                pontuacao += (vida*100 + 1000*1) if dificuldade == facil else (vida*100 + 1000*2)
                print("Parabéns, Você acertou. Seus pontos: ",pontuacao,end="")
                print(str(pontuacao))
                letras =""
                x =0
                acertos = []
                while True:
                        palavra = random.choice(dificuldade)
                        if palavra not in palavras:
                                palavras.append(palavra)
                                break
                subs = ""
                for l in palavra:
                        subs += l if l in acertos else "_"
                clear()
                    
                                

                            
            print("Letras já utilizadas:",letras,"     pontuação atual: ",str(pontuacao),"   Fase Atual: ",str(len(palavras)),"/",str(len(dificuldade)))
            print("Palavra:",subs,end='\n\n')
            print("Entre com uma letra(0 para sair). ",str(vida),"tentativas restantes")
            letra = input(">")
            if letra == "0":
                continuar = input("Quer salvar a partida?[n/s]")
                if continuar == "s":
                    clear()
                    salvarpartida(pontuacao,acertos,palavras,dificuldade,vida,palavra,letras)
                    print("partida gravada!!!")
                return 0
            if len(letra) > 1:
                        clear()
                        print("Oi! Isso não é uma letra.",end='\n\n')
            elif len(letra) == 1:
                if letra in letras:
                    clear()    
                    print("Letra '"+letra+"' já utilizada. Tente outra")
                else:
                    if letra in palavra:
                        clear()
                        print("Boa! A letra '",letra,"'existe na palavra :)",end='\n\n')

                        letras += " "+letra
                        acertos.append(letra)
                    else:
                        clear()
                        print("Essa letra não existe na palavra :(",end='\n\n')
                        vida = vida - 1
                        letras += " "+letra
            else:
                clear()
                print("Não pode ser espaço em branco!!!")
            if vida == 0:
                    print("Jogo encerrado. Você perdeu. A palavra era '",palavra,"'.Pressione enter para continuar...")
                    continuar = input()
                    clear()
                    if pontuacao > 0:
                        posicao = posicaodocidadao(pontuacao)
                        if posicao < 11:
                            while True:
                                print("É um novo recorde! Você está na posição",posicao,"do ranking. \nQual o seu nome?(5 caracteres são obrigatorios e so 5 mesmo >:) )")
                                nome = input(">")
                                if len(nome) == 5:
                                    break
                                else:
                                    clear()
                                    print("SÃO 5 CARACTERES!!!")
                        salvarrecord(nome,pontuacao)
                    clear()
                    break
                            
            else:
                x = 0
def continuarjogo(pontuacao,acertos,palavras,dificuldade,vida,palavra,letras):
        while True:
                subs = ""
                for l in palavra:
                        subs += l if l in acertos else "_"
                if subs == palavra:
                        if palavras == dificuldade:
                                 posicao = posicaodocidadao(pontuacao)
                                 if posicao < 11:
                                     while True:
                                        print("É um novo recorde! Você está na posição",posicao,"do ranking. \nQual o seu nome?(5 caracteres são obrigatorios e so 5 mesmo >:) )")
                                        nome = input(">")
                                        if len(nome) == 5:
                                            break
                                        else:
                                            clear()
                                            print("SÃO 5 CARACTERES!!!")
                                 return 0
                        print("Parabéns, Você acertou. Seus pontos: ",end="")
                        pontuacao += (vida*100 + 1000*1) if dificuldade == facil else (vida*100 + 1000*2)
                        print(str(pontuacao))
                        letras =""
                        acertos = []
                        x =0
                        while True:
                                palavra = random.choice(dificuldade)
                                if palavra not in palavras:
                                        palavras.append(palavra)
                                        break
                        subs = ""
                        for l in palavra:
                                subs += l if l in acertos else "_"
                print("Letras já utilizadas:",letras,"  pontuação atual: ",str(pontuacao),"   Fase Atual: ",str(len(palavras)),"/",str(len(dificuldade)))
                print("Palavra:",subs,end='\n\n')
                print("Entre com uma letra(0 para sair). ",str(vida),"tentativas restantes")
                letra = input(">")
                if letra == "0":
                        clear()
                        continuar = input("Quer salvar a partida?[n/s]")
                        if continuar == "s":
                                clear()
                                salvarpartida(pontuacao,acertos,palavras,dificuldade,vida,palavra,letras)
                                print("partida gravada!!!")
                                return 0
                        else:
                                salvarpartida(0,"","","",0,"","")
                                clear()
                                return 0
                if len(letra) > 1:
                        clear()
                        print("Oi! Isso não é uma letra.",end='\n\n')
                elif len(letra) == 1:
                        if letra in letras:
                                clear()
                                print("Letra '"+letra+"' já utilizada. Tente outra")
                        else:
                                if letra in palavra:
                                        clear()
                                        print("Boa! A letra '",letra,"'existe na palavra :)",end='\n\n')
                                        letras += " "+letra
                                        acertos.append(letra)
                                else:
                                        clear()
                                        print("Essa letra não existe na palavra :(",end='\n\n')
                                        vida = vida - 1
                                        letras += " "+letra
                else:
                    clear()
                    print("Não pode ser espaço em branco!!!")
                if vida == 0:
                        clear()
                        print("Jogo encerrado. Você perdeu. A palavra era '",palavra,"'.Pressione enter para continuar...")
                        continuar = input()
                        clear()
                        if pontuacao > 0:
                                posicao = posicaodocidadao(pontuacao)
                                if posicao < 11:
                                    while True:
                                        print("É um novo recorde! Você está na posição",posicao,"do ranking. \nQual o seu nome?(5 caracteres são obrigatorios e so 5 mesmo >:) )")
                                        nome = input(">")
                                        if len(nome) == 5:
                                            break
                                        else:
                                            clear()
                                            print("SÃO 5 CARACTERES!!!")
                                    salvarrecord(nome,pontuacao)
                        salvarpartida(0,"","","",0,"","")
                        break
                else:
                        x = 0
def doisjogadores():
        print("Entre com a palavra a ser utilizada nesta partida.")
        palavrachave = input(">")
        clear()
        acertos = []
        usadas = ""
        vida = 3
        letras = ""
        while True:
                subs = ""
                for letra in palavrachave:
                        subs += letra if letra in acertos else "_"
                if subs == palavrachave:
                        print("Parabéns, Você acertou!!!!")
                        con = input("Pressione qualquer tecla para continuar")
                        clear()
                        return 0
                print("Letras já utilizadas:",letras)
                print("Palavra:",subs,end='\n\n')
                print("Entre com uma letra(0 para sair). ",str(vida),"tentativas restantes")
                letra = input(">")
                if letra == "0":
                        break
                if len(letra) > 1:
                        clear()
                        print("Oi! Isso não é uma letra.",end='\n\n')
                elif len(letra) == 1:
                        if letra in letras:
                                clear()
                                print("Letra '"+letra+"' já utilizada. Tente outra")
                                vida = vida - 1
                        else:
                                if letra in palavrachave:
                                        clear()
                                        print("Boa! A letra '",letra,"'existe na palavra :)",end='\n\n')
                                        letras += " "+letra
                                        acertos.append(letra)
                                else:
                                        clear()
                                        print("Essa letra não existe na palavra :(",end='\n\n')
                                        vida = vida - 1
                                        letras += " "+letra
                if vida == 0:
                        clear()
                        print("Jogo encerrado. Você perdeu. A palavra era '",palavrachave,"'.Pressione enter para continuar...")
                        continuar = input()
                        break
                else:
                                x = 0




























        #AQUI COMEÇA THE FIGTH
#===========================================================================================================
#=====================================================================================================
while True:
    partidas = lerpartidassalvas()
    ranking = lerranking()
    continuar = retornaboleanodobolado()
#-------------------------------------------------------------------------------
    print("------------------------------")
    print("        JOGO DA FORCA")
    print("------------------------------")
    if continuar == True:
    #------------MENU COM PARTIDA SALVA-----------------------------------------------------
        print("1 - INICIAR NOVA PARTIDA")
        print("2 - CONTINUAR PARTIDA")
        print("3 - RANKING GERAL")
        print("4 - SAIR",end="\n\n")
        opcao = input("OPÇÃO DESEJADA: ")
        if opcao == "1":
            clear()
            while True:
            #----------------------------------------------------------------------------------
                print("------------------------------")
                print("        JOGO DA FORCA")
                print("------------------------------")
                print("1 - UM JOGADOR")
                print("2 - DOIS JOGADORES")
                print("3 - VOLTAR",end="\n\n")
                opcao = input("OPÇÃO DESEJADA: ")
                if opcao == "1":
                    clear()
                    while True:                  
                    #---------------------------------------------------------------------------
                        print("------------------------------")
                        print("        JOGO DA FORCA")
                        print("------------------------------")
                        print("FACIL")
                        print("DIFICIL",end="\n\n")
                        print("V - VOLTAR",end="\n\n")
                        escolha = input("OPCÃO DESEJADA: ")
                        if escolha == "F" or escolha == "f":
                            dificuldade = facil
                            vida = 5
                            letras = ""
                            novojogo(dificuldade,vida)
                        elif escolha == "D" or escolha == "d":
                            dificuldade = dificil
                            vida = 3
                            novojogo(dificuldade,vida)
                        elif escolha == "V" or escolha == "v":
                            clear()
                            break
                        else:
                            clear()
                            print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
                elif opcao == "2":
                    clear()
                    doisjogadores()
                    
                elif opcao =="3":
                    clear()
                    break
                else:
                    clear()
                    print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
        elif opcao == "2":
            clear()
            continuarpartida()
            """while True:
                print("---------------------")
                print("ESCOLHA SUA PARTIDA")
                print("---------------------",end="\n\n")
                print("Partidas em andamento:")
                qtddejogos=[]
                partidas = lerpartidassalvas()
                if len(partidas) > 0:
                    for joguinho in range(len(partidas)):
                        print(str(joguinho+1)+" - "+partidas[joguinho]['nome'])
                        qtddejogos.append(joguinho+1)
                    escolha = int(input("Escolha a sua partida(0 - para sair)"))
                    if escolha == 0:
                        clear()
                        break
                    continuarpartida(partidas,escolha,qtddejogos)
                else:
                    print("Nenhuma partida salva no momento!")
                    sair = input("S - para sair")
                    if sair == "S"or "s":
                        break"""
        elif opcao == "3":
            clear()
            #-------------------------------------------------------------------
            print("-----------------------")
            print("       RANKING")
            print("-----------------------")
            if len(ranking) != 0:
                ranking = organizarranking()
                for p in range(len(ranking)):
                    print("#"+str(p+1)+"º "+ranking[p]['nome']+"          "+str(ranking[p]['pont']))
            else:
                print("Nenhum resgistro salvo")
            con = input("Pressione enter para continuar")
            clear()
        elif opcao == "4":
            break
        else:
            clear()
            print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
#=================================================================================================================================================
#==================================================================================================================================================
    else:
        #MENU LIGHT KKK
        print("1 - INICIAR NOVA PARTIDA")
        print("2 - RANKING GERAL")
        print("3 - SAIR",end="\n\n")
        opcao = input("OPÇÃO DESEJADA: ")
        if opcao == "1":
            clear()
            while True:
            #----------------------------------------------------------------------------------
                print("------------------------------")
                print("        JOGO DA FORCA")
                print("------------------------------")
                print("1 - UM JOGADOR")
                print("2 - DOIS JOGADORES")
                print("3 - VOLTAR",end="\n\n")
                opcao = input("OPÇÃO DESEJADA: ")
                if opcao == "1":
                    clear()
                    while True:                  
                    #---------------------------------------------------------------------------
                        print("------------------------------")
                        print("        JOGO DA FORCA")
                        print("------------------------------")
                        print("FACIL")
                        print("DIFICIL",end="\n\n")
                        print("V - VOLTAR",end="\n\n")
                        escolha = input("OPCÃO DESEJADA: ")
                        if escolha == "F" or escolha == "f":
                            dificuldade = facil
                            vida = 5
                            letras = ""
                            novojogo(dificuldade,vida)
                        elif escolha == "D" or escolha == "d":
                            dificuldade = dificil
                            vida = 3
                            novojogo(dificuldade,vida)
                        elif escolha == "V" or escolha == "v":
                            clear()
                            break
                        else:
                            clear()
                            print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
                elif opcao == "2":
                    clear()
                    doisjogadores()
                elif opcao =="3":
                    clear()
                    break
                else:
                    clear()
                    print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
                
        elif opcao == "2":
            z = 0
            clear()
            print("-----------------------")
            print("       RANKING")
            print("-----------------------")
            if len(ranking) != 0:
                ranking = organizarranking()
                for p in range(len(ranking)):
                    print("#"+str(p+1)+"º "+ranking[p]['nome']+"          "+str(ranking[p]['pont']))
                    z += 1
                    if z == 10:
                        break
            else:
                print("Nenhum resgistro salvo")
            con = input("Pressione enter para continuar")
            clear()
                
        elif opcao == "3":
            break
        else:
            clear()
            print("DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.")
    
