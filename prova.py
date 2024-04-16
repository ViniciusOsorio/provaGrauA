import random

def game():
    #(N,L,S,O)
    dirs = (0,0,0,0)

    entrada = {'nome': 'Entrada', 'direções': dirs, 'msg': '', 'local': 'na'}
    salaEstar = {'nome': 'Sala de Estar', 'direções': dirs, 'msg': '', 'local': 'na'}
    cozinha = {'nome': 'Cozinha', 'direções': dirs, 'msg': '', 'local': 'na'}
    salaEstudos = {'nome': 'Sala de Estudos', 'direções': dirs, 'msg': '', 'local': 'na'}
    dormitorioM = {'nome': 'Dormitório Masculino', 'direções': dirs, 'msg': '', 'local': 'no'}
    dormitorioF = {'nome': 'Dormitório Feminino', 'direções': dirs, 'msg': '', 'local': 'no'}

    entrada['direções'] = (0,salaEstar,0,0)
    salaEstar['direções'] = (salaEstudos,dormitorioF,cozinha,entrada)
    cozinha['direções'] = (salaEstar,0,0,0)
    salaEstudos['direções'] = (0,0,salaEstar,dormitorioM)
    dormitorioM['direções'] = (0,0,dormitorioF,salaEstudos)
    dormitorioF['direções'] = (dormitorioM,0,0,salaEstar)

    salas = [cozinha, salaEstudos, dormitorioM, dormitorioF]

    localSabre = random.choice(salas)

    for sala in salas:
        if localSabre['nome'] == sala['nome']:
            sala['msg'] = 'Você encontrou seu sabre de luz!'
        else:
            sala['msg'] = 'Nada! Seu sabre de luz deve estar em outro lugar!'

    sabreEncontrado = False
    vaderd = False

    salaAtual = entrada

    turno = 0

    print("A localização do refúgio Jedi foi descoberta e o Lorde Sith, Darth Vader, está a caminho. Encontre seu sabre de luz e preparece para o que está por vir, Padawan. E que a Força esteja com você!")
    while (sabreEncontrado == False and vaderd == False):
        print(f"Turno {turno}")
        print(f"Você está {salaAtual['local']} {salaAtual['nome']}! Você pode ir para...")
        for x in range(4):
            if (salaAtual['direções'][x] != 0):
                print('\n','N' if x == 0 else 'L' if x == 1 else 'S' if x == 2 else 'O','-',salaAtual['direções'][x]['nome'],'\n')
        seMoveu = False
        while(seMoveu is False):
            direcao = input("Para onde deseja ir?\n")
            # print(direcao)
            match direcao:
                case "N","n":
                    if(salaAtual['direções'][0] != 0):
                        salaAtual = salaAtual['direções'][0]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "L","l":
                    if(salaAtual['direções'][1] != 0):
                        salaAtual = salaAtual['direções'][1]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "S","s":
                    if(salaAtual['direções'][2] != 0):
                        salaAtual = salaAtual['direções'][2]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case "O","o":
                    if(salaAtual['direções'[3]] != 0):
                        salaAtual = salaAtual['direções'][3]
                        seMoveu = True
                    else:
                        print('Não há nada nessa direção. Mantenha a calma. Confie na Força.')
                    break
                case _:
                    print('Opção inválida!')
        print(f"Você chegou {salaAtual['local']} {salaAtual['Nome']}! {salaAtual['msg']}")
        if(salaAtual['nome'] == localSabre['nome']):
            sabreEncontrado = True
            print("Com seu sabre de luz, você consegue abrir uma passagem pela parede mais próxima e escapar!")
        
        


game()