Compilei o programa em FORTRAN para Linux, com diferentes sementes aleatórias para cada vez que o programa é rodado.
Realizei 200 simulações com condição inicial em formato de triângulo e mais 200 com condição inical de quadrado. 
Para automatizar isso eu acabei usando uma função do Fortran 2003 (que a querida Jheniffer disponibilizou), 
mas tudo funciona perfeitamente como antes.

Os arquivos zipados contém todos os executáveis e arquivos gerados por essas simulações. Todos os disparos por camada, 
figuras, camadas de saída etc, tal qual o programa original do Leonel produzia. Eu usei todas as condições iniciais 
que estavam por padrão no dia que Leonel nos levou ao NeuroLab a última vez (e nos mostrou as imagens dos neurônios disparando).

Acredito que o dado que temos usado para estudar o sinal produzido é o "total_PA_Saida_V2.txt". 
Para facilizar a análise dessa quantidade de dados (que eu não sei exatamente como será feita)
eu aglutinei todos os arquivos com esse nome de cada uma dessas 400 simulações. 
O resultado são dois arquivos de nomes "triangles.dat" e "squares.dat". 
Assim, a primeira simulação (S1) feita com C.I. de quadrado compõe as 2000 primeiras 
linhas do arquivo "squares.dat". A segunda simulação (S2) compõe as 2000 linhas seguintes, e assim por diante.
O mesmo foi feito com o arquivo "triangles.dat"

Agora posso fazer quantas simulações forem necessárias, e com quaisquer condições iniciais. Se precisar de 
mais dados, ou se esses não servirem, basta avisar :)


--- Germano --- 20/10/16
 