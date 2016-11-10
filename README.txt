Compilei o programa em FORTRAN para Linux, com diferentes sementes aleat�rias para cada vez que o programa � rodado.
Realizei 200 simula��es com condi��o inicial em formato de tri�ngulo e mais 200 com condi��o inical de quadrado. 
Para automatizar isso eu acabei usando uma fun��o do Fortran 2003 (que a querida Jheniffer disponibilizou), 
mas tudo funciona perfeitamente como antes.

Os arquivos zipados cont�m todos os execut�veis e arquivos gerados por essas simula��es. Todos os disparos por camada, 
figuras, camadas de sa�da etc, tal qual o programa original do Leonel produzia. Eu usei todas as condi��es iniciais 
que estavam por padr�o no dia que Leonel nos levou ao NeuroLab a �ltima vez (e nos mostrou as imagens dos neur�nios disparando).

Acredito que o dado que temos usado para estudar o sinal produzido � o "total_PA_Saida_V2.txt". 
Para facilizar a an�lise dessa quantidade de dados (que eu n�o sei exatamente como ser� feita)
eu aglutinei todos os arquivos com esse nome de cada uma dessas 400 simula��es. 
O resultado s�o dois arquivos de nomes "triangles.dat" e "squares.dat". 
Assim, a primeira simula��o (S1) feita com C.I. de quadrado comp�e as 2000 primeiras 
linhas do arquivo "squares.dat". A segunda simula��o (S2) comp�e as 2000 linhas seguintes, e assim por diante.
O mesmo foi feito com o arquivo "triangles.dat"

Agora posso fazer quantas simula��es forem necess�rias, e com quaisquer condi��es iniciais. Se precisar de 
mais dados, ou se esses n�o servirem, basta avisar :)


--- Germano --- 20/10/16
 