# Clase que actualiza las puntuaciones.
# Guarda en un fichero si el player 2 (jugador) tiene la puntuación más alta que la que está almacenada actuamente

class Score:
    def __init__(self):
        # Los jugadores inicia con 0 puntos
        self.p1_score = 0
        self.p2_score = 0
        # Actualiza el ítem con la puntuación más alta guardada
        try:
            with open("data.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("data.txt", "w") as file:
                file.write("0")
                self.high_score = 0

    def add_score(self, player):
        """
        Suma 1 a la puntuación actual del jugador.
        Llama a la función que comprueba si hay nuevo récord de puntuación: highest_score()
        :param player: jugador que va a sumar un punto
        """
        if player == "player1":
            self.p1_score += 1
        if player == "player2":
            self.p2_score += 1
            self.highest_score()

    def highest_score(self):
        """
        Función que comprueba si hay nuevo récord de puntuación.
        En caso de que así sea, actualiza el fichero "data.txt" con la nueva puntuación
        """
        if self.p2_score > self.high_score:
            self.high_score = self.p2_score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

