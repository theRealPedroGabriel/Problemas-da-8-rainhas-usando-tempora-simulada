import statistics
import time

import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()

def f(x):

  numero_ataques = 0


  for i in range(len(x)):
    for j in range(i + 1, len(x)):

      if x[i] == x[j] or   abs((x[i]) - (x[j]))==(j - i):
        numero_ataques += 1


  # Penalização por par de rainhas

  #print("pena",penalizacao)
  # Retorno de um número real
  return  numero_ataques


#x_axis = np.random.permutation(np.arange(1, 9))#Cria um array x1 contendo 1000 valores espaçados linearmente entre -1 e 2.
#print("xaxis",x_axis)

#Z = f(x_axis)
def gerar_candidato(x):

  i, j = np.random.randint(0, 8, size=2)
  #print(x)
  x_cand = x.copy()
  x_cand[i], x_cand[j] = x_cand[j], x_cand[i]
  #print(x_cand)
  return x_cand

x_l = np.array([1, 1, 1, 1, 1, 1, 1, 1]) #Define os limites inferior (x_l) e superior (x_u) para a busca do mínimo. Valores fora desses limites serão ajustados.
x_u = np.array([8, 8, 8, 8, 8, 8, 8, 8])



#x_opt = np.random.uniform(np.arange(1, 9))
x_opt = np.random.uniform(1, 9, size=(8,))
x_opt = np.round(x_opt)
x_opt = np.clip(x_opt, 1, 8)
#print("xopt",x_opt)
f_opt = f(x_opt)
#print("fopt",f_opt)

 #Desvio padrão do ruído gaussiano usado para gerar candidatos vizinhos
heuristicas = []
solucoes = []

contador_indices = []
solucao_otima_encontrada = False
#for p in range(10):
while not solucao_otima_encontrada:
    contador = 0

    t = 20
    T = 2000 #Temperatura inicial do Simulated Annealing (alto para maior aceitação de novos candidatos).
    sigma = .5
    for i in range(5000):

        n = np.random.normal(0, scale=sigma, size=(8,))
        n = np.round(n)  # Arredonda para o número inteiro mais próximo
        n = np.clip(n, -1, 1)  # Garante que os valores estejam no intervalo [-1, 1]
        x_cand = x_opt + n
        #print("xcand", x_cand)
        for j in range(x_cand.shape[0]):
            if (x_cand[j] < x_l[j]):
                x_cand[j] = x_l[j]
            if (x_cand[j] > x_u[j]):
                x_cand[j] = x_u[j]


        f_cand = f(x_cand)
        P_ij = np.exp(-(f_cand - f_opt) / T)
        heuristicas.append(f_opt)

        if f_cand < f_opt or P_ij >= np.random.uniform(0, 1):
            x_opt = x_cand
            f_opt = f_cand
            contador = 0
            #print("fopt", f_opt)
        if (f_cand >= f_opt ):
           contador += 1
           if (contador >= t):
              # print("contador maior q t")
               teste = gerar_candidato(x_cand)
               teste2 = f(teste)
               indice = len(heuristicas)
               if indice < 10000:
                   contador_indices.append(indice)


               if(teste2<f_opt):
                    x_opt = teste
                    f_opt = teste2
                    print("fopt", f_opt)



        numeros_inteiros = [round(numero) for numero in x_cand]
        if f_cand == 0 and tuple(numeros_inteiros) not in solucoes:
            # A solução é ótima e não está na lista
            solucoes.append(tuple(numeros_inteiros))  # Converte para tupla para comparação eficiente
            print("Solução ótima encontrada:", numeros_inteiros, f"(Quantidade de lugares: {len(solucoes)})")
            break

        if(len(solucoes)==92):solucao_otima_encontrada = True

        if T <= 0:
            print("T atinge um valor mínimo")
            break  # Sai do loop interno
        T = T * .99

    if solucao_otima_encontrada:
            break  # Sai do loop externo se uma solução ótima foi encontrada


end_time = time.time()
execution_time = end_time - start_time

print("Tempo de execução:", execution_time, "segundos")

plt.plot(heuristicas[0:10000])
vetor_limitado = contador_indices[:10000]
print(len(vetor_limitado))
plt.scatter(vetor_limitado, [heuristicas[idx] for idx in vetor_limitado], color='red')

for idx, valor in enumerate(heuristicas[0:10000]):
    if valor == 0 :
        plt.scatter(idx, valor, color='green', marker='o', s=100)


plt.show()


num_solucoes = len(solucoes)
plt.table(cellText=solucoes, colLabels=['1', '2', '3','4', '5', '6','7', '8'], loc='center')
plt.axis('off')
plt.title('Soluções: '+str(num_solucoes))
plt.show()

