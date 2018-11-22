# Exercício de Programação - Inteligência Artificial, USP ( EACH )

O intuito desse trabalho é aplicar o conhecimento de arvores de busca para resolver o problema de achar a comida do Packman.
Dado o labirinto do jogo, usou-se diversos algoritmos de busca para achar o melhor caminho entre o ponto inicial e a ponto destino.

Para a base do exercício utilizou-se parte do material/código livremente disponível do curso UC Berkeley CS188:
http://ai.berkeley.edu/project_overview.html

## Busca em Profundidade (DFS):

$ python pacman.py -l tinyMaze -p SearchAgent
$ python pacman.py -l mediumMaze -p SearchAgent
$ python pacman.py -l bigMaze -z .5 -p SearchAgent

## Busca em Largura (BFS)

$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

##  Variando a função custo - varia o peso de cada ação

$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

## Busca heurística - Busca em grafo A*

$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## Problema de busca dos 4 cantos

Nesse problema, acha-se o melhor caminho para que o packman coma a comida posicionada nos 4 cantos do labirinto

$ python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
