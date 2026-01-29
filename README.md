# Jogo da Memória

## Descrição
Este é um jogo da memória desenvolvido em Python, onde os jogadores podem competir uns contra os outros.

## Configuração
O jogo permite configurar o número de jogadores e o número de pares de cartas.

* Número de jogadores: pode ser configurado para 2 ou mais jogadores.
* Número de pares de cartas: pode ser configurado para qualquer número inteiro entre 1 e 26 considerando o limite alfabético.
* Ícone de carregamento: é possível escolher qualquer caractere para ser exibido durante o carregamento do jogo
* Ciclos de carregamento: é possível escolher o tempo em ciclos que o carregamento vai durar.

## Como jogar
1. Execute o arquivo `jogo.py` em um terminal.
2. Configure o número de jogadores e o número de pares de cartas, destacando que antes de cada configuração é calculado se o número de jogadores não é maior que o número de cartas disponíveis, se sim vai gerar um erro, portanto aumente o número de cartas antes de aumentar o número de jogadores
3. Clique em "Iniciar Jogo" para começar.
4. Será exibida todas as cartas de forma númerica e o placar atual da partida
5. O jogo prosseguirá de acordo com as regras definidas.

## Regras do jogo
- Cada jogador  deve escolher dois números inteiro disponíveis segundo a tela do jogo
- O objetivo é encontrar todos os pares de cartas.
- O jogador que encontrar mais pares de cartas vence o jogo.
- Se um jogador não encontrar um par de cartas, ele perde a vez.
- O jogo termina quando não houver mais pares de carta
- Você pode retornar para a tela inicial se digitar durante a partida "-1"

## Licença
* Este jogo é de código aberto e pode ser modificado e distribuído livremente.

### Observações
* O jogo não inclui uma interface gráfica, é jogado no terminal.
* O jogo não inclui uma opção de salvar o jogo, é necessário jogar de uma vez só.

Na natureza nada se cria e nada se perde, tudo se transforma, estou adaptando o modelo do uno para esse projeto, tenho muita coisa para mudar no código-fonte desse projeto ainda...