# -*- coding: utf-8 -*-
"""
1) Ler dados de experimentos - lab. de neurociências
2) Aplicar random forest para classificar os dados.
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier

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
            
triangulos = np.array(triangulos)
quadrados = np.array(quadrados)

triangulos = triangulos.reshape(200,2000)
quadrados = quadrados.reshape(200,2000)

# X é o conjunto completo de dados
X = np.concatenate((triangulos, quadrados))

# y é o conjunto dos rótulos; as 200 primeiras amostras, que são correspondentes aos 
# triângulos, terão rótulo 1; as outras 200 amostras tem rótulo 0 (quadrados)
y = np.zeros((400,1))
y[0:200] = 1

model = RandomForestClassifier(n_estimators=30)
RANDOM_SEED = 42  # fix the seed on each iteration

# Shuffle: embaralhar os índices dos dados
idx = np.arange(X.shape[0])
np.random.seed(RANDOM_SEED)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# Normalizar (?) os dados 
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std

# Train - NAO ESTA FUNCIONANDO. TALVEZ FALTE LIMPAR OS DADOS
#clf = model.fit(X, y)
#scores = clf.score(X, y)