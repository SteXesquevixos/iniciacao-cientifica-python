import random
import numpy as np
import matplotlib.pyplot as plt

estados = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

ansiog_prob = np.array([1.0, 0.36, 0.47, 0.48, 0.45, 0.29, 0.47, 0.48, 0.50, 0.57, 1.0])
ansiol_prob = np.array([1.0, 0.37, 0.49, 0.50, 0.49, 0.44, 0.48, 0.49, 0.49, 0.60, 1.0])
controle_prob = np.array([1.0, 0.32, 0.46, 0.45, 0.46, 0.30, 0.42, 0.48, 0.49, 0.55, 1.0])

iteracoes = 100

ansiog_passos = np.zeros((11, iteracoes))
ansiol_passos = np.zeros((11, iteracoes))
controle_passos = np.zeros((11, iteracoes))

for j in range(iteracoes):

    #Ansiogenico:

    ansiog_random = []
    ansiog_trajetoria = [6]

    i = 5
    s = 0
    ansiog_contador = 0
    parar1 = 1
    parar2 = 1

    while parar1 + parar2 > 0:
        ansiog_random.append(float("%.3f" % random.random()))
        n = estados[i]
        p = ansiog_prob[i]
        aux = 1

        while aux == 1:

            ansiog_contador += 1

            if i != 0 and i != 10 and aux == 1:
                if ansiog_random[s] <= p and aux == 1:
                    n = estados[i - 1]
                    ansiog_trajetoria.append(n)
                    p = ansiog_prob[i - 1]
                    aux = 0
                    if ansiog_passos[i-1][j] == 0:
                        ansiog_passos[i-1][j] = ansiog_contador
                    i = i - 1

                elif ansiog_random[s] > p and aux == 1:
                    n = estados[i + 1]
                    ansiog_trajetoria.append(n)
                    p = ansiog_prob[i + 1]
                    aux = 0
                    if ansiog_passos[i+1][j] == 0:
                        ansiog_passos[i+1][j] = ansiog_contador
                    i = i + 1

            elif i == 0 and ansiog_random[s] <= p and aux == 1:
                n = estados[i+1]
                ansiog_trajetoria.append(n)
                p = ansiog_prob[i+1]
                aux = 0
                parar1 = 0
                if ansiog_passos[i][j] == 0:
                    ansiog_passos[i][j] = ansiog_contador
                i = i + 1

            elif i == 10 and ansiog_random[s] <= p and aux == 1:
                n = estados[i-1]
                ansiog_trajetoria.append(n)
                p = ansiog_prob[i-1]
                aux = 0
                parar2 = 0
                if ansiog_passos[i][j] == 0:
                    ansiog_passos[i][j] = ansiog_contador
                i = i - 1

        s += 1

    print(ansiog_trajetoria)

    ansiog_tempo = [np.mean(ansiog_passos[0]),np.mean(ansiog_passos[1]),np.mean(ansiog_passos[2]),
                    np.mean(ansiog_passos[3]),np.mean(ansiog_passos[4]),0,np.mean(ansiog_passos[6]),
                    np.mean(ansiog_passos[7]),np.mean(ansiog_passos[8]),np.mean(ansiog_passos[9]),
                    np.mean(ansiog_passos[10])]

    ansiog_desvpad = [np.std(ansiog_passos[0]),np.std(ansiog_passos[1]),np.std(ansiog_passos[2]),
                      np.std(ansiog_passos[3]),np.std(ansiog_passos[4]),0, np.std(ansiog_passos[6]),
                      np.std(ansiog_passos[7]),np.std(ansiog_passos[8]),np.std(ansiog_passos[9]),
                      np.std(ansiog_passos[10])]

    #Ansiolitico:

    ansiol_random = []
    ansiol_trajetoria = [6]

    i = 5
    s = 0
    ansiol_contador = 0
    parar1 = 1
    parar2 = 1

    while parar1 + parar2 > 0:
        ansiol_random.append(float("%.3f" % random.random()))
        n = estados[i]
        p = ansiol_prob[i]
        aux = 1

        while aux == 1:

            ansiol_contador += 1

            if i != 0 and i != 10 and aux == 1:
                if ansiol_random[s] <= p and aux == 1:
                    n = estados[i - 1]
                    ansiol_trajetoria.append(n)
                    p = ansiol_prob[i - 1]
                    aux = 0
                    if ansiol_passos[i-1][j] == 0:
                        ansiol_passos[i-1][j] = ansiol_contador
                    i = i - 1

                elif ansiol_random[s] > p and aux == 1:
                    n = estados[i + 1]
                    ansiol_trajetoria.append(n)
                    p = ansiol_prob[i + 1]
                    aux = 0
                    if ansiol_passos[i+1][j] == 0:
                        ansiol_passos[i+1][j] = ansiol_contador
                    i = i + 1

            elif i == 0 and ansiol_random[s] <= p and aux == 1:
                n = estados[i+1]
                ansiol_trajetoria.append(n)
                p = ansiol_prob[i+1]
                aux = 0
                parar1 = 0
                if ansiol_passos[i][j] == 0:
                    ansiol_passos[i][j] = ansiol_contador
                i = i + 1

            elif i == 10 and ansiol_random[s] <= p and aux == 1:
                n = estados[i-1]
                ansiol_trajetoria.append(n)
                p = ansiol_prob[i-1]
                aux = 0
                parar2 = 0
                if ansiol_passos[i][j] == 0:
                    ansiol_passos[i][j] = ansiol_contador
                i = i - 1

        s += 1

    ansiol_tempo = [np.mean(ansiol_passos[0]),np.mean(ansiol_passos[1]),np.mean(ansiol_passos[2]),
                    np.mean(ansiol_passos[3]),np.mean(ansiol_passos[4]),0,np.mean(ansiol_passos[6]),
                    np.mean(ansiol_passos[7]),np.mean(ansiol_passos[8]),np.mean(ansiol_passos[9]),
                    np.mean(ansiol_passos[10])]

    ansiol_desvpad = [np.std(ansiol_passos[0]),np.std(ansiol_passos[1]),np.std(ansiol_passos[2]),
                      np.std(ansiol_passos[3]),np.std(ansiol_passos[4]),0,np.std(ansiol_passos[6]),
                      np.std(ansiol_passos[7]),np.std(ansiol_passos[8]),np.std(ansiol_passos[9]),
                      np.std(ansiol_passos[10])]

    #Controle:

    controle_random = []
    controle_trajetoria = [6]

    i = 5
    s = 0
    controle_contador = 0
    parar1 = 1
    parar2 = 1

    while parar1 + parar2 > 0:
        controle_random.append(float("%.3f" % random.random()))
        n = estados[i]
        p = controle_prob[i]
        aux = 1

        while aux == 1:

            controle_contador += 1

            if i != 0 and i != 10 and aux == 1:
                if controle_random[s] <= p and aux == 1:
                    n = estados[i-1]
                    controle_trajetoria.append(n)
                    p = controle_prob[i-1]
                    aux = 0
                    if controle_passos[i-1][j] == 0:
                        controle_passos[i-1][j] = controle_contador
                    i = i - 1

                elif controle_random[s] > p and aux == 1:
                    n = estados[i+1]
                    controle_trajetoria.append(n)
                    p = controle_prob[i+1]
                    aux = 0
                    if controle_passos[i+1][j] == 0:
                        controle_passos[i+1][j] = controle_contador
                    i = i + 1

            elif i == 0 and controle_random[s] <= p and aux == 1:
                n = estados[i+1]
                controle_trajetoria.append(n)
                p = controle_prob[i+1]
                aux = 0
                parar1 = 0
                if controle_passos[i][j] == 0:
                    controle_passos[i][j] = controle_contador
                i = i + 1

            elif i == 10 and controle_random[s] <= p and aux == 1:
                n = estados[i-1]
                controle_trajetoria.append(n)
                p = controle_prob[i-1]
                aux = 0
                parar2 = 0
                if controle_passos[i][j] == 0:
                    controle_passos[i][j] = controle_contador
                i = i - 1

        s += 1

    controle_tempo = [np.mean(controle_passos[0]),np.mean(controle_passos[1]),np.mean(controle_passos[2]),
                      np.mean(controle_passos[3]),np.mean(controle_passos[4]),0,np.mean(controle_passos[6]),
                      np.mean(controle_passos[7]),np.mean(controle_passos[8]),np.mean(controle_passos[9]),
                      np.mean(controle_passos[10])]

    controle_desvpad = [np.std(controle_passos[0]), np.std(controle_passos[1]), np.std(controle_passos[2]),
                        np.std(controle_passos[3]), np.std(controle_passos[4]), 0, np.std(controle_passos[6]),
                        np.std(controle_passos[7]), np.std(controle_passos[8]), np.std(controle_passos[9]),
                        np.std(controle_passos[10])]

#Grafico:
plt.plot(estados, ansiog_tempo, '--', marker='o', color='red', markersize=3, linewidth=1, label='Ansiogenico')
plt.plot(estados, ansiol_tempo, ':', marker='^', color='blue', markersize=3, linewidth=1, label='Ansiolitico')
plt.plot(estados, controle_tempo, '-', marker='s', color='black', markersize=3, linewidth=1, label='Controle')

plt.errorbar(estados, ansiog_tempo, ansiog_desvpad, linestyle='None', linewidth=0.5)
plt.errorbar(estados, ansiol_tempo, ansiol_desvpad, linestyle='None', linewidth=0.5)
plt.errorbar(estados, controle_tempo, controle_desvpad, linestyle='None', linewidth=0.5)

plt.legend(loc=0)
plt.xlabel('Estado')
plt.ylabel('Tempo Medio de Primeira Visita')
plt.gca().yaxis.grid()
plt.ylim(0)
plt.xticks(range(1, 12))
plt.show()