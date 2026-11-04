
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Construa um jogo da Forca em que o jogador adivinha letras para revelar uma palavra oculta. Pratique manipulação de strings, listas, loops, condicionais e seleção aleatória em Python.

## 📝 Tasks

### 🛠️ Preparar a palavra e o estado do jogo

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher uma palavra secreta e preparar as variáveis que acompanharão o andamento da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida
- Inicializar uma coleção para registrar as letras adivinhadas
- Definir e acompanhar o limite de palpites incorretos
- Exibir o progresso da palavra oculta, mostrando as letras ainda não adivinhadas como `_`

### 🛠️ Implementar os palpites e o fim da partida

#### Descrição
Implemente o loop principal para receber palpites, atualizar o progresso e encerrar a partida quando o jogador vencer ou atingir o limite de erros.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra a cada rodada
- Atualizar e exibir o progresso quando o palpite corresponder a uma letra da palavra
- Contabilizar e informar os palpites incorretos restantes
- Encerrar quando todas as letras da palavra forem reveladas ou o limite de erros for atingido
- Exibir uma mensagem indicando vitória ou derrota e revelar a palavra secreta ao final