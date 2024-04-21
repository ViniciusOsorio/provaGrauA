import random
import os

#(N,L,S,O)
dirs = (0,0,0,0)

entrada = {'nome': 'Entrada', 'direções': dirs, 'msg': '', 'local': 'na'}
salaEstar = {'nome': 'Sala de Estar', 'direções': dirs, 'msg': '', 'local': 'na'}
cozinha = {'nome': 'Cozinha', 'direções': dirs, 'msg': '', 'local': 'na'}
salaEstudos = {'nome': 'Sala de Estudos', 'direções': dirs, 'msg': '', 'local': 'na'}
dormitorioM = {'nome': 'Dormitório Masculino', 'direções': dirs, 'msg': '', 'local': 'no'}
dormitorioF = {'nome': 'Dormitório Feminino', 'direções': dirs, 'msg': '', 'local': 'no'}
#comodos extras
arquivos = {'nome': 'Arquivos', 'direções': dirs, 'msg': '', 'local': 'nos'} #N da Sala de Estudos
horta = {'nome': 'Horta', 'direções': dirs, 'msg': '', 'local': 'na'} #S da cozinha
salaoDaForca = {'nome': 'Salão da Força', 'direções': dirs, 'msg': '', 'local': 'no'} #L da Sala de Estar, E do Corredor Principal
corredor = {'nome': 'Corredor Principal', 'direções': dirs, 'msg': '', 'local': 'no'} #L do Salão da Força, S do Dormitório Masculino, N do Dormitório Feminino, E do Salão da Força
salaDeMeditação = {'nome': 'Sala de Meditação', 'direções': dirs, 'msg': '', 'local': 'na'} #L do Corredor


def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# def comodoGrafico(sala):
#     print(f"{sala['nome'] if sala else 'Teste'}",
#           "\n-----------",
#           "\n|         |",
#           "\n|         |",
#           "\n|         |",
#           "\n-----------")
    
# def montarMapa():
#     print('teste')
#     contX = 0
#     contY = 0
#     mapFinder = entrada
#     mapArray = [[entrada]]


def game():
    limparTela()
    tipoJogo = 0
    while (tipoJogo != 'R' and tipoJogo != 'r' and tipoJogo != 'L' and tipoJogo != 'l'):
        tipoJogo = input("Qual tipo de jogo gostaria de jogar?\nR - Jogo Rápido\nL - Jogo Longo\n")
        match tipoJogo:
            case 'R'|'r':
                print("Jogo Rápido\nNúmero de Cômodos: 6")
                input("Pressione ENTER para continuar...")
                tipoJogo = 'r'
            case 'L'|'l':
                print("Jogo Longo\nNúmero de Cômodos: 11")
                input("Pressione ENTER para continuar...")
            case _:
                print("Opção Inválida")
                input("Pressione ENTER para continuar...")
                limparTela()
    limparTela()

    #(N,L,S,O)
    #Mapa Longo
    #                  Arquivos                             Dormitório Masculino
    #                     |
    #               Sala de Estudos                                 |
    #                     |
    #Entrada    -   Sala de Estar   -   Salão da Força  -   Corredor Principal  -   Sala de Meditação
    #                     |
    #                  Cozinha                                      |
    #                     |
    #                   Horta                               Dormitório Feminino

    entrada['direções'] = (0,salaEstar,0,0)
    salaEstar['direções'] = (salaEstudos,dormitorioF,cozinha,entrada) if tipoJogo == 'r' else (salaEstudos,salaoDaForca,cozinha,entrada)
    cozinha['direções'] = (salaEstar,0,0,0) if tipoJogo == 'r' else (salaEstar,0,horta,0)
    salaEstudos['direções'] = (0,0,salaEstar,dormitorioM) if tipoJogo == 'r' else (arquivos,0,salaEstar,0)
    dormitorioM['direções'] = (0,0,dormitorioF,salaEstudos) if tipoJogo == 'r' else (0,0,corredor,0)
    dormitorioF['direções'] = (dormitorioM,0,0,salaEstar) if tipoJogo == 'r' else (corredor,0,0,0)
    #direções para comodos extras
    arquivos['direções'] = (0,0,salaEstudos,0) #N da Sala de Estudos
    horta['direções'] = (cozinha,0,0,0) #S da cozinha
    salaoDaForca['direções'] = (0,corredor,0,salaEstar) #L da Sala de Estar, E do Corredor Principal
    corredor['direções'] = (dormitorioM,salaDeMeditação,dormitorioF,salaoDaForca) #L do Salão da Força, S do Dormitório Masculino, N do Dormitório Feminino, E do Salão da Força
    salaDeMeditação['direções'] = (0,0,corredor,0) #L do Corredor


    salas = [cozinha, salaEstudos, dormitorioM, dormitorioF] if tipoJogo == 'r' else [salaEstar, cozinha, salaEstudos, dormitorioM, dormitorioF, horta, arquivos, salaDeMeditação, corredor,salaoDaForca]

    localSabre = random.choice(salas)

    salas = [salaEstar, cozinha, salaEstudos, dormitorioM, dormitorioF] if tipoJogo == 'r' else [salaEstar, cozinha, salaEstudos, dormitorioM, dormitorioF, horta, arquivos, salaDeMeditação, corredor,salaoDaForca]

    for sala in salas:
        if localSabre['nome'] == sala['nome']:
            sala['msg'] = 'Você encontrou seu sabre de luz!'
        else:
            sala['msg'] = 'Nada! Seu sabre de luz deve estar em outro lugar!'

    sabreEncontrado = False
    vaderd = False

    salaAtual = entrada

    localVader = entrada
    localDiferente = False

    turno = 1

    print("A localização do refúgio Jedi foi descoberta e o Lorde Sith, Darth Vader, está a caminho. Encontre seu sabre de luz e preparece para o que está por vir, Padawan. E que a Força esteja com você!\n")
    input("Pressione ENTER para começar")
    
    while (sabreEncontrado == False and vaderd == False):        
        limparTela()
        print(f"Turno {turno}")
        print(f"Você está {salaAtual['local']} {salaAtual['nome']}! Você pode ir para...")
        for x in range(4):
            if (salaAtual['direções'][x] != 0):
                print('\n','N' if x == 0 else 'L' if x == 1 else 'S' if x == 2 else 'O','-',salaAtual['direções'][x]['nome'],'\n')
        seMoveu = False
        while(seMoveu is False):
            direcao = input("Para onde deseja ir?\n")
            
            match direcao:
                case "N"|"n":
                    if(salaAtual['direções'][0] != 0):
                        salaAtual = salaAtual['direções'][0]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "L"|"l":
                    if(salaAtual['direções'][1] != 0):
                        salaAtual = salaAtual['direções'][1]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "S"|"s":
                    if(salaAtual['direções'][2] != 0):
                        salaAtual = salaAtual['direções'][2]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "O"|"o":
                    if(salaAtual['direções'][3] != 0):
                        salaAtual = salaAtual['direções'][3]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case _:
                    print('Opção inválida!')
        
        limparTela()
        print(f"Você chegou {salaAtual['local']} {salaAtual['nome']}!\n{salaAtual['msg']}")
        input("\n\nPressione ENTER para continuar...")
        if(salaAtual['nome'] == localSabre['nome']):
            sabreEncontrado = True
            print("\n\nCom seu sabre de luz, você consegue abrir uma passagem pela parede mais próxima e escapar!\n")
            break
        turno+=1
        if (turno == 3 and sabreEncontrado == False):            
            limparTela()
            while localDiferente is False:
                localVader = random.choice(salas)
                if (localVader['nome'] != salaAtual['nome']):
                    localDiferente = True
            print(f"\nDarth Vader encontrou o abrigo e conseguiu entrar!\nEle está {localVader['local']} {localVader['nome']} e irá começar a lhe procurar!",
                    "\nO corpo debilitado do Lorde Sith impede que ele se mova constantemente, precisando de um turno de descanso a cada turno de movimento.",
                    "\nPorém, o lado negro da Força é forte e permite que ele se mova 2 cômodos a cada turno.",
                    "\nCaso ele termine o movimento no mesmo cômodo que você, ele lhe encontrará e você estará acabado!",
                    "\nPlaneje seus movimentos de acordo!")
            input("\n\nPressione ENTER para continuar\n\n")
        elif turno%2 == 1:
            for y in range(2):
                vaderMoveu = False
                while (vaderMoveu == False):
                    vaderDestino = localVader['direções'][random.randint(0,3)]
                    if (vaderDestino!=0):
                        localVader = vaderDestino
                        vaderMoveu = True
                print(f"\n\nDarth Vader moveu-se e está procurando você {localVader['local']} {localVader['nome']}\n\n")
                input("Pressione ENTER para continuar")
            if (localVader['nome'] == salaAtual['nome']):
                vaderd = True
                limparTela()
                print("Darth Vader lhe encontrou.\nSua jornada como Jedi termina aqui...")

game()