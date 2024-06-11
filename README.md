# TIC TAC TOE

![banner_tictactoe](https://github.com/arenaf/tic-tac-toe/assets/169451601/286c7b58-495c-4aa8-baed-7baefa62bbfe)


## Sobre el desarrollo
Este proyecto se desarrolló con Python y se utilizó Tkinter como entorno gráfico.

#### Archivos contenidos
- Archivo principal ***main.py*** desde el cuál se debe ejecutar la aplicación.
- Módulo ***board.py*** que contiene la clase *Board* que crea el tablero y todos sus componentes.
  Desde esta clase se controla la partida: movimientos de los jugadores y reinicio de partida.
- Módulo ***scoreboard.py*** que contiene la clase *Score* que comprueba las puntuaciones de los jugadores y las actualiza.
- Fichero ***data.txt*** dónde se almacena la puntuación más alta alcanzada por player 2. Si no existe se crea automáticamente
  en la primera partida. Sólo se tiene en cuenta la puntuación de player 2, si player 2 consigue un nuevo récord,
  sobreescribe el fichero con la nueva puntuación.
- Imagen ***board.png***: imagen del tablero.
- Imagen ***player1.png***: imagen que corresponde a las fichas del jugador 1 (máquina).
- Imagen ***player2.png***: imagen asignada a las fichas del jugador 2.


## Cómo se juega
Juego también conocido como "Tres en raya". 
Cada jugador, en su turno, coloca una ficha sobre un tablero de 3x3, el primero que consiga poner tres fichas consecutivas en horizontal, vertical o diagonal, gana la partida.
Se mueve una ficha por turno, al finalizar el movimiento pasa el turno al siguiente jugador.

La máquina (player1) juega con ficha "o", el jugador "player2" con la ficha "x". La máquina siempre mueve primero.

La partida finaliza cuando gana "player 1", "player 2" o con empate.

![ganador](https://github.com/arenaf/tic-tac-toe/assets/169451601/1d7cde75-c959-473d-a608-03eaf140a942)

Pregunta al usuario si quiere jugar otra partida y actualiza las puntuaciones de cada jugador y la puntución más alta (si procede):

  - *P1*: player 1
  - *P2*: player 2
  - *High Score*: puntuación más alta que ha obtenido player 2

![puntuacion-tictactoe](https://github.com/arenaf/tic-tac-toe/assets/169451601/64dd7344-4333-4e2c-95ab-e9b5ace687a6)



