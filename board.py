import tkinter
import random
from tkinter import messagebox
from scoreboard import Score

TEXT = "#f2e8cf"
BACKGROUND = "#028391"
FONT = "Courier"


class Board(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic tac toe")
        self.resizable(False, False)
        self.config(padx=20, pady=20, background=BACKGROUND)
        self.score = Score()

        # Players image:
        self.player1_img = tkinter.PhotoImage(file="player1.png")
        self.player2_img = tkinter.PhotoImage(file="player2.png")

        # Control de posiciones totales
        self.remove_pos = []
        # Control de juego:
        self.end_game = False # False: juego continua | True: fin de la partida
        self.player1_pos = [] # Almacena los número asignados a cada posición de las fichas del jugador 1 (máquina)
        self.player2_pos = [] # Almacena los número asignados a cada posición de las fichas del jugador 2

        # Crea el tablero
        self.canvas = tkinter.Canvas(width=500, height=500, background=BACKGROUND, highlightthickness=False)
        self.board_img = tkinter.PhotoImage(file="board.png")
        self.canvas.create_image(250, 250, image=self.board_img)
        self.title = self.canvas.create_text(260, 10, text="TIC TAC TOE", fill=TEXT, font=(FONT, 15, "bold"))
        self.buttons()

        # Inicia la partida la máquina (player 1)
        self.draw_move()

    def buttons(self):
        """
        Función que crea los botones del tablero. Cada botón corresponde a una posición dónde los jugadores
        pueden poner su ficha.
        También se crean las puntuaciones de los jugadores y la máxima alcanzada por el player 2.
        """
        # Fila 0
        self.button_00 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_00, (120, 120, 1), "player2"))
        self.button_00.place(x=60, y=60)
        self.button_01 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_01, (260, 120, 2), "player2"))
        self.button_01.place(x=200, y=60)
        self.button_02 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_02, (400, 120, 3), "player2"))
        self.button_02.place(x=340, y=60)

        # Fila 1
        self.button_10 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_10, (120, 260, 4), "player2"))
        self.button_10.place(x=60, y=200)
        self.button_11 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_11, (260, 260, 5), "player2"))
        self.button_11.place(x=200, y=200)
        self.button_12 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_12, (400, 260, 6), "player2"))
        self.button_12.place(x=340, y=200)

        # Fila 2
        self.button_20 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_20, (120, 400, 7), "player2"))
        self.button_20.place(x=60, y=340)
        self.button_21 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_21, (260, 400, 8), "player2"))
        self.button_21.place(x=200, y=340)
        self.button_22 = tkinter.Button(self, width=16, height=8, background=BACKGROUND,
                                        activebackground=BACKGROUND, relief="flat", border=False,
                                        command=lambda: self.player_move(self.button_22, (400, 400, 9), "player2"))
        self.button_22.place(x=340, y=340)

        # Scores: max, player 1, player 2 y título
        self.canvas.create_text(401, 475, text="Score: ", fill=TEXT, font=(FONT, 15, "bold"))
        self.p1_score = self.canvas.create_text(380, 495, text=f"P1: {self.score.p1_score}", fill=TEXT, font=(FONT, 10, "normal"))
        self.p2_score = self.canvas.create_text(450, 495, text=f"P2: {self.score.p2_score}", fill=TEXT, font=(FONT, 10, "normal"))
        self.max_score = self.canvas.create_text(440, 10, text=f"High Score: {self.score.high_score}", fill=TEXT, font=(FONT, 10, "bold"))
        self.canvas.create_text(40, 495, text="arena", fill=TEXT, font=(FONT, 7, "normal"))
        self.canvas.pack()

    def draw_move(self):
        """
        Controla la jugada de la máquina. Asigna una posición aleatoria que se encuentre vacía.
        """
        init_pos = self.remaining_position(self.remove_pos)
        button, pos = random.choice(list(init_pos.items()))
        self.player_move(button, pos, "player1")
        self.remaining_position(self.remove_pos)

    def player_move(self, button, position, player):
        """
        Actualiza las listas con las posiciones de los jugadores, pone la imagen correspondiente y comprueba si hay
        ganador.
        :param button: botón pulsado que será sustituido por la ficha del jugador. El botón se borra.
        :param position: coordenadas x e y de dónde se encuentra el botón.
        :param player: jugador que está realizando la jugada.
        """
        button.place_forget()
        self.remove_pos.append(button)
        if player == "player2":
            self.canvas.create_image(position[0], position[1], image=self.player2_img, anchor="center",
                                     tag="player2")
            self.player2_pos.append(position[2])
            if self.check_winner(self.player2_pos, player) == False:
                self.draw_move() # Si no hay ganador pasa el turno a la máquina
        if player == "player1":
            self.canvas.create_image(position[0], position[1], image=self.player1_img, anchor="center",
                                     tag="player1")
            self.player1_pos.append(position[2])
            self.check_winner(self.player1_pos, player)

        self.remaining_position(self.remove_pos)

    def check_winner(self, player_list, win):
        """
        Comprueba si hay ganador o empate. En caso afirmativo, muestra un mensaje por pantalla, en caso contrario la
        partida continua.
        :param player_list: lista que contiene las posiciones del jugador actual.
        :param win: jugador actual (player1 o player2).
        """
        if ((1 in player_list and 2 in player_list and 3 in player_list) or
                (4 in player_list and 5 in player_list and 6 in player_list) or
                (7 in player_list and 8 in player_list and 9 in player_list) or
                (1 in player_list and 4 in player_list and 7 in player_list) or
                (2 in player_list and 5 in player_list and 8 in player_list) or
                (3 in player_list and 6 in player_list and 9 in player_list) or
                (1 in player_list and 5 in player_list and 9 in player_list) or
                (3 in player_list and 5 in player_list and 7 in player_list)
        ):
            messagebox.showinfo("Tic Tac Toe", f"¡{win.capitalize()} ha ganado la partida!")
            print(f"Ganador: {win}")
            self.score.add_score(win)
            print(f"Player 1: {self.score.p1_score} ptos | Player 2: {self.score.p2_score} ptos")
            # Actualiza la puntuación máxima
            self.canvas.itemconfig(self.max_score, text=f"High Score: {self.score.high_score}")
            self.disabled_buttons()

        elif len(self.remove_pos) == 9:
            print("**** EMPATE ******")
            messagebox.showinfo("Tic Tac Toe", "¡EMPATE! Fin de la partida.")
            self.disabled_buttons()
        else:
            return False

    def remaining_position(self, less_pos):
        """
        Posiciones que quedan vacías.
        :param less_pos: lista con todos los números de las posiciones ocupadas.
        :return: devuelve un diccionario con los botones, sus coordenadas y el número asignado a los botones que será
        utilizado en las listas.
        """
        dict_pos = {
            self.button_00: (120, 120, 1),
            self.button_01: (260, 120, 2),
            self.button_02: (400, 120, 3),
            self.button_10: (120, 260, 4),
            self.button_11: (260, 260, 5),
            self.button_12: (400, 260, 6),
            self.button_20: (120, 400, 7),
            self.button_21: (260, 400, 8),
            self.button_22: (400, 400, 9),
        }
        for free_pos in less_pos:
            if free_pos in dict_pos.keys():
                del dict_pos[free_pos]
        return dict_pos

    def disabled_buttons(self):
        """
        Fin de partida, oculta todos los botones que no fueron ocupados por ningún jugador
        """
        disable_buttons = self.remaining_position(self.remove_pos)
        for button in disable_buttons:
            button.place_forget()
        self.game_continue()

    def game_continue(self):
        """
        Fin de partida. Pregunta al usuario si quiere jugar otra vez.
        Si continua jugando, reestablece el tablero y las variables con las posiciones e inicia el primer movimiento
        de la máquina.
        Si no quiere continuar jugando, actualiza el tablero con las puntuaciones
        """
        question = messagebox.askquestion("Tic Tac Toe", "¿Quieres jugar otra partida?")

        if question == "yes":
            print("Continuar partida: Yes")
            # Reinicio de variables y widgets. Limpia el tablero
            self.canvas.delete("player1")
            self.canvas.delete("player2")
            self.canvas.delete(self.p1_score)
            self.canvas.delete(self.p2_score)
            self.canvas.delete(self.max_score)
            self.remove_pos = []
            self.end_game = False
            self.player1_pos = []
            self.player2_pos = []
            self.buttons()
            self.draw_move()
        else:
            print("Continuar partida: No")
            self.canvas.itemconfig(self.p1_score, text=f"P1: {self.score.p1_score}")
            self.canvas.itemconfig(self.p2_score, text=f"P2: {self.score.p2_score}")


if __name__ == "__main__":
    board = Board()
    board.mainloop()
