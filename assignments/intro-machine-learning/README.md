# 📘 Atividade: Introdução ao Aprendizado de Máquina

## 🎯 Objetivo

Construir e avaliar um classificador em Python usando o conjunto Iris. Você vai distinguir características de rótulos, separar dados de treino e teste e comparar resultados de modelos de árvore de decisão.

## 📝 Tarefas

### 🛠️ Explore o conjunto de dados

#### Descrição

Prepare o ambiente e explore o conjunto Iris carregado pelo código inicial. Identifique quais informações serão usadas para fazer previsões e quais resultados o modelo deverá prever.

#### Requisitos

O programa concluído deve:

- Instalar o scikit-learn com `python -m pip install scikit-learn`
- Identificar as quatro características (features) e os nomes das classes (rótulos) do conjunto Iris
- Dividir os dados em conjuntos de treino e teste, mantendo a proporção entre as classes
- Informar quantas amostras ficaram em cada conjunto e explicar por que o teste deve usar dados que não treinaram o modelo

### 🛠️ Treine e avalie um classificador

#### Descrição

Treine uma árvore de decisão com os dados de treino e avalie suas previsões usando os dados de teste. Em seguida, compare árvores com limites diferentes de profundidade.

#### Requisitos

O programa concluído deve:

- Treinar o modelo sem usar os dados de teste
- Exibir a acurácia e a matriz de confusão, identificando a ordem dos nomes das classes
- Comparar os resultados de árvores com profundidades máximas de 1, 2 e 3 usando a mesma divisão de dados
- Indicar qual profundidade escolheria e justificar a resposta com base nos resultados, mencionando uma limitação da acurácia como única métrica
