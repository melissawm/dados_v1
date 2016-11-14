# -*- coding: utf-8 -*-
"""
1) Ler dados de experimentos - lab. de neurociências
2) Aplicar random forest para classificar os dados.
"""
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# As linhas abaixo servem para que os gráficos sejam corretamente mostrados
# em monitores HiDPI; se este não for o seu caso, deixe-as comentadas.
rcParams['figure.dpi'] = 150
rcParams['lines.linewidth'] = 1
rcParams['lines.markersize'] = 2

with open("triangles.dat", "r") as arq1:
    with open("squares.dat", "r") as arq2:
        # A matriz de dados tem um experimento em cada linha; 
        # Primeiramente lemos os dados dos dois arquivos nas variáveis dados_tri 
        # e dados_qua.
        triangulos = []
        quadrados = []
        dados_tri = arq1.read().split("\n")
        dados_qua = arq2.read().split("\n")
        for line in dados_tri:
            linha = line.split(",")
            # Como a última linha do arquivo é um whitespace, eliminamos essa 
            # última linha da leitura dos dados.
            if len(linha) == 2:
                triangulos.append(float(linha[1]))
        for line in dados_qua:
            linha = line.split(",")
            # Como a última linha do arquivo é um whitespace, eliminamos essa 
            # última linha da leitura dos dados.
            if len(linha) == 2:
                quadrados.append(float(linha[1]))
            
# Transformamos os dados em nd-arrays (estrutura de dados do numpy)
triangulos = np.array(triangulos)
quadrados = np.array(quadrados)

# Agora os dados estão em matrizes em que cada linha representa um experimento,
# e cada coluna representa uma feature (um dos tempos em que houve medição)
triangulos = triangulos.reshape(200,2000)
quadrados = quadrados.reshape(200,2000)

# X é o conjunto completo de dados. Novamente, cada coluna representa uma feature,
# e cada linha representa um experimento.
X = np.concatenate((triangulos, quadrados))

# y é o conjunto dos rótulos; as 200 primeiras amostras, que são correspondentes aos 
# triângulos, terão rótulo 1; as outras 200 amostras tem rótulo 0 (quadrados)
y = np.zeros((400,))
y[0:200] = 1

model = RandomForestClassifier(n_estimators=30)
RANDOM_SEED = 142  # fix the seed on each iteration

# Shuffle: embaralhar os índices dos dados
idx = np.arange(X.shape[0])
np.random.seed(RANDOM_SEED)
np.random.shuffle(idx)

# Definimos o corte para o conjunto de treinamento como 75% do conjunto.
cut = int(np.floor(X.shape[0]*0.75))

# Xtrain e ytrain estão embaralhados, pois estamos tomando os elementos na
# ordem dada por idx, o vetor de índices embaralhados.
Xtrain = X[idx[0:cut],:]
ytrain = y[idx[0:cut]]

# Normalizar os dados - retornando a média e desvio padrao de cada coluna (feature)
mean = Xtrain.mean(axis=0)
std = Xtrain.std(axis=0)

Xtrain = (Xtrain - mean) 
# Como algumas features (alguns tempos de medição) tem resultado 0 para todos 
# os experimentos, excluimos esses elementos da normalização para evitar
# divisão por zero.
Xtrain[:,np.nonzero(std)] = Xtrain[:,np.nonzero(std)] / std[np.nonzero(std)]

# Treinamento
clf = model.fit(Xtrain, ytrain)

#
print("Score: ", clf.score(Xtrain,ytrain))

# Predição: relacionada aos 25% do conjunto de dados que ainda não foi considerado.
y_pred = model.predict(X[idx[cut:-1],:])
y_true = y[idx[cut:-1]]

# As linhas abaixo servem para que tenhamos uma ideia do conjunto de dados. 
# Cada gráfico representa um experimento.
#plt.plot(X[cut,:])
#plt.plot(X[cut+1,:])
#plt.plot(X[cut+2,:])
#plt.plot(X[cut+3,:])
#plt.plot(X[cut+4,:])
#plt.plot(X[cut+5,:])
#plt.plot(X[cut+6,:])
#print(y_true)
#print(y_pred)

diff = np.nonzero(y_true-y_pred)
print("Numero de rotulos errados: {}/100".format(len(diff[0])))

#print(np.nonzero(diff).shape)
#print(classification_report(y_true, y_pred, target_names=['triangulos', 'quadrados']))