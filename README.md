# GG4F - Guessing Game For Friends

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

O Guessing Game For Friends (GG4F) é um guessing game - jogo de adivinhação - para amigos, como o nome já diz. Porém, as motivações de criação do jogo foram as seguintes:
  - Distância geografica entre amigos (muitos em outras cidades, estados ou países);
  - Falta de meio de transporte para se locomover (trânsito interferindo, por exemplo);
  - Falta de coragem de sair de casa.

## O que faz o GG4F diferente de outro Guessing Game?
Diferente dos outros guessing games, quem acerta o número certo é quem perde. O GG4F tem o intuito de ser um drinking game, ou seja, ao acertar o número que inicialmente está numa escala de 0 a 100, o usuário tem que beber uma dose de alguma bebida.
A cada palpite errado, o intervalo da escala vai diminuindo de acordo com o palpite, com isso, a dificuldade vai aumentando, pois a chance de acertar o número é maior.

## Tecnologias utilizadas
Para a implementação, foram utilizadas as seguintes tecnologias:
  - Python 3.6.1 - Como a linguagem de programação para o desenvolvimento;
  - Pycharm - Como IDE;
  - Socket
  - Dillinger - Como plataforma para edição de texto em Markdown.  

A arquitetura utilizada foi a cliente - servidor, e, para cada cliente, foi criado um socket e estabelecido uma conexão TCP com o servidor.

## Funcionamento
No servidor, o jogo é rodado e apenas são enviadas as mensagens do intervalo - se for a vez do jogador - e a mensagem se acertou ou não o número. 
No cliente, além de receber as mensagens, é enviada a mensagem com o valor que foi "chutado". 
No servidor cada vez que um cliente se conecta, é aberta uma nova thread com o jogo. 
Foram utilizadas variáveis globais para manter a consistência do jogo.

## Instalação

Para jogar, deve clonar o repositório em seu computador e rodar o código. É bem simples.
Os testes foram feitos apenas em MacBook para MacBook.


```sh
$ cd Diretorio_que_deseja_instalar
$ git clone https://github.com/vanessavieira/GuessingGamePython.git
```
#### Equipe
- Rubem Ferreira Santos Vasconcelos (Matrícula: 15111988)
- Vanessa Soares Vieira (Matrícula: 15112025)
