import numpy as np
import matplotlib.pyplot as plt
import statistics
import random

def perturb(x,e):
    return np.random.uniform(low=x-e,high=x+e) # Esta função recebe uma permutação x (representando a ordem de visitação das cidades) e troca aleatoriamente dois elementos para criar uma nova solução candidata.

def f(x1, x2):
    pi = np.pi
    return (x1 * np.sin(4*pi*x1) )- (x2 * np.sin(4*pi*x2 + pi) )+ 1

def calcular_moda(resultados):
    """Calcula a moda dos resultados."""
    resultados_tuplas = [(resultado['x1'], resultado['x2'], resultado['f']) for resultado in resultados]
    return statistics.mode(resultados_tuplas)
def verifica_restricao(x1, x2):
    """Verifica se x1 e x2 estão dentro dos limites x_l e x_u."""
    return limiin <= x1 <= limisu and limiin <= x2 <= limisu
limiin = -1
limisu = 3


x1 = np.linspace(limiin, limisu, 1000)
X1 , X2 = np.meshgrid(x1 , x1 ) #cria duas matrizes bidimensionais X1 e X2 usando os valores de x1. Imagine uma grade onde cada ponto representa um valor de x1 e x2.
Y = f(X1 , X2 )

x_otimo = limiin
x2_otimo = limiin
# x_otimo = np.random.uniform(low=-2,high=2)
f_otimo = f(x_otimo, x2_otimo)  #calcula o valor inicial da função no ponto inicial.

e = .1
max_it = 1000   #define o número máximo de iterações do algoritmo.
max_vizinhos = 20  #define o número máximo de candidatos a serem explorados por iteração.
i = 0
t = 8
R = 100
#fazendo o grafico 3d
fig = plt.figure()
ax = fig.add_subplot(projection ='3d')
ax.plot_surface(X1, X2, Y, rstride =10 , cstride =10 , alpha =0.6 , cmap ='jet') # plota a superfície 3D usando os valores de X1, X2, e Y

melhoria = True
#plt.plot(x1, f(x1)) # plota o gráfico da função f(x) usando os valores de x_axis.

ax.scatter(x_otimo,x2_otimo,f_otimo,color='red',s=90,marker='x')

#algoritimo de hill cabling

solucoes1 = []
for p in range(R):
    while i<max_it and melhoria:
        melhoria = False
        contador = 0
        for j in range(max_vizinhos):
            x_candidato = perturb(x_otimo,e)
            x2_candidato = perturb(x2_otimo,e)
            if verifica_restricao(x_candidato, x2_candidato):
                f_candidato = f(x_candidato, x2_candidato)
                if(f_candidato>f_otimo):
                    melhoria = True
                    x_otimo = x_candidato
                    x2_otimo = x2_candidato
                    f_otimo = f_candidato
                    ax.scatter(x_otimo,x2_otimo,f_otimo,color='blue',s=90,marker='x')
                    contador = 0
                    break
                else:
                    contador+=1
                    if(contador>=t):  #poss´ıvel parada antecipada
                        print("contador maior q t")
                        max_it = 1000
                        break
        i+=1
    novo_resultado = {'x_otimo': x_otimo, 'x2_otimo': x2_otimo, 'f_otimo': f_otimo}
    solucoes1.append(novo_resultado)
    ax.scatter(x_otimo, x2_otimo, f_otimo,color='green',s=90,marker='x',linewidth=3)

plt.pause(.5)
# Converte cada dicionário em uma tupla e adiciona à lista de resultados
resultados_tuplas = [(resultado['x_otimo'], resultado['x2_otimo'], resultado['f_otimo']) for resultado in solucoes1]

# Calcula a moda das tuplas de resultados
moda_resultados = statistics.mode(resultados_tuplas)

print("a moda do hillcabling é: ",moda_resultados)
x_moda = moda_resultados[0]
x2_moda = moda_resultados[1]
f_moda = moda_resultados[2]

ax.scatter(x_moda, x2_moda, f_moda, color='orange', s=90, marker='x', linewidth=3)

#busca local aleatoria



def verifica_restricao(x1, x2):
    """Verifica se x1 e x2 estão dentro dos limites x_l e x_u."""
    # Aqui você colocaria sua própria verificação de restrição
    return x_otimo <= x1 <= x2_otimo and x_otimo <= x2 <= x2_otimo



Nmax = 1000 # Passo 1: Definir uma quantidade máxima de iterações Nmax



sigma = 0.1
x_otimo = random.uniform(limiin, limisu)
x2_otimo = random.uniform(limiin, limisu)
f_otimo = f(x_otimo, x2_otimo)
i = 0
solucoes2 = []
for p in range(R):
    while i < Nmax:
        n = random.normalvariate(0, sigma)
        contador = 0
        x_candidato = x_otimo + n
        x2_candidato = x2_otimo + n
        if verifica_restricao(x_candidato, x2_candidato):
            fcand = f(x_candidato, x2_candidato)
            if fcand > f_otimo:
                x_otimo = x_candidato
                x2_otimo = x2_candidato
                f_otimo= fcand
                contador = 0
                break
            else:
                contador += 1
                if (contador >= t):
                    print("contador maior q t")
                    Nmax = 1000
                    break

        i += 1


    novo_resultado = {'x_otimo': x_otimo, 'x2_otimo': x2_otimo, 'f_otimo': f_otimo}
    solucoes2.append(novo_resultado)
    ax.scatter(x_otimo, x2_otimo, f_otimo, color='purple', s=90, marker='x', linewidth=3)
# Exemplo de saída
plt.pause(.5)
# Converte cada dicionário em uma tupla e adiciona à lista de resultados
resultados_tuplas = [(resultado['x_otimo'], resultado['x2_otimo'], resultado['f_otimo']) for resultado in solucoes2]

# Calcula a moda das tuplas de resultados
moda_resultados2 = statistics.mode(resultados_tuplas)

print("a moda de busca local aleatorio é: ",moda_resultados2)
x_moda = moda_resultados2[0]
x2_moda = moda_resultados2[1]
f_moda = moda_resultados2[2]

ax.scatter(x_moda, x2_moda, f_moda, color='gray', s=90, marker='x', linewidth=3)

#busca aleatoria global



Nmax = 1000 # Passo 1: Definir uma quantidade máxima de iterações Nmax

i = 0
solucoes3 = []
for p in range(R):
    while i < Nmax:
        contador = 0
        x_candidato = random.uniform(limiin, limisu)
        x2_candidato = random.uniform(limiin, limisu)
        if verifica_restricao(x_candidato, x2_candidato):
            fcand = f(x_candidato, x2_candidato)

            if fcand > f_otimo:
                x_otimo = x_candidato
                x2_otimo = x2_candidato
                f_otimo = fcand
                contador = 0
                break
            else:
                contador += 1
                if (contador >= t):
                    print("contador maior q t")
                    Nmax = 1000
                    break


        i += 1


    novo_resultado = {'x_otimo': x_otimo, 'x2_otimo': x2_otimo, 'f_otimo': f_otimo}
    solucoes3.append(novo_resultado)
    ax.scatter(x_otimo, x2_otimo, f_otimo, color='yellow', s=90, marker='x', linewidth=3)
# Exemplo de saída
plt.pause(.5)
# Converte cada dicionário em uma tupla e adiciona à lista de resultados
resultados_tuplas = [(resultado['x_otimo'], resultado['x2_otimo'], resultado['f_otimo']) for resultado in solucoes3]

# Calcula a moda das tuplas de resultados
moda_resultados3 = statistics.mode(resultados_tuplas)

print("a moda de busca GLOBAL aleatorio é: ",moda_resultados3)
x_moda = moda_resultados3[0]
x2_moda = moda_resultados3[1]
f_moda = moda_resultados3[2]

ax.scatter(x_moda, x2_moda, f_moda, color='pink', s=90, marker='x', linewidth=3)


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x1 ,x2)')
plt.tight_layout()
plt.show()



# Cria uma tabela com as modas dos diferentes algoritmos
algoritmos = ['Hill Climbing', 'Busca Local Aleatorio', 'Busca Global Aleatorio']
modas = [moda_resultados, moda_resultados2, moda_resultados3]
plt.figure(figsize=(14, 4))
plt.table(cellText=modas, colLabels=['Moda de x1', 'Moda de x2', 'Moda de f'], rowLabels=algoritmos, loc='center')
plt.axis('off')
plt.title('Moda das Soluções de Diferentes Algoritmos de Otimização')
plt.show()
