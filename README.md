# S16_a4_planilha_de_vendas

## Desafio
Construir um aplicativo simples que leia os dados, processe e exiba resultados organizados. O programa deve ser em Python e precisa:
*   declarar uma matriz 2D representando vendas;
*	calcular totais por vendedor;
*	calcular totais por mês;
*	calcular o total geral;
*	identificar o melhor vendedor.


Percorra a matriz e exiba os valores organizados por vendedor.
Analise e responda: 
*	Quantas linhas existem?
R: 3

*	Quantas colunas existem?
R: 3

## Etapa 2 – Total por vendedor
Calcule o total vendido por cada vendedor. Para isso:
*	utilize laços aninhados;
*	reinicie o acumulador para cada linha.

Ele deve exibir:
*	total vendedor 0;
*	total vendedor 1;
*	total vendedor 2.


## Etapa 3 – Total por mês
Agora, calcule o total vendido em cada mês. Para isso: 
*	inverta a lógica dos laços;
*	percorra colunas primeiro.

Ele deve exibir:
*	total mês 0;
*	total mês 1;
*	total mês 2.


## Etapa 4 – Total geral
Calcule o total geral da empresa.


## Etapa 5 – Melhor vendedor
Identifique qual vendedor obteve maior total de vendas. Ele deve exibir:
*	o melhor vendedor.


## Etapa 6 – Texto explicativo
Analise todos os passos realizados e responda:
*	Como os laços aninhados foram utilizados?
    R:Ele foi usado em todo o codigo, lendo matrizes usando o for

*	Como foi feito o controle de índices?
    R:Lendo, somando e comparando matrizes

*	Qual foi o resultado da análise?
    R:
    total vendedor 1; R$3800
    total vendedor 2; R$3700
    total vendedor 3; R$4200
    ----------------------------
    total vendido no mes 1; R$3100
    total vendido no mes 2; R$4500
    total vendido no mes 3; R$4100
    ----------------------------
    total da empresa; R$11700
    ----------------------------
    O melhor vendedor foi o 3º com R$4200 