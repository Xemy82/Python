import random

def main():
    # Obtiene la palabra aleatoria
    word = list(get_random_word())
    hidden = list()

    # Genera la lista con rayas para informar al usuario
    for char in word:
        hidden.append("_")

    # Variables a utilizar en el juego
    maxtries = 5 # Máximo de fallos
    tries = 0 # Fallos consumidos
    isgameover = False # Controla cuando se acaba el juego
    guess = "" # Almacena el string con la letra que introduce el usuario
    num_hits = 0 # Contador de letras acertadas
    isguess = False # Controla si la letra introducida por el usuario es válida.

    # Bucle infinito hasta que acabe el juego
    while isgameover == False:

        get_gameinfo(maxtries, tries, hidden)
        try:
            guess = set_guess()
        except ValueError:
            print("Introduce una letra")
            guess = set_guess()
        isguess = check_guess(guess,word,hidden)
        num_hits = get_hits(hidden)

        # Según el valor de la variable isguess la letra está o no en la palabra. Si falla debes incrementar el valor de una variable.

        # Condiciones de finalización del juego. Debes fijar isgameover a True cuando el usuario gane o pierda
        


# Genera una palabra aletoria y la devuelve en letras mayusculas
def get_random_word():
    candidates = ["Esqueleto","Amarillo","Cuerdas","Mural","Enhebrar","Cencerro","Escalera","Medicina","Planetas"]
    word = random.choice(candidates).upper()
    return word

# Informa al usuario del estado de la partida. Letras acertadas e intentos restantes.
def get_gameinfo(maxtries, tries, hidden):
    # IMPLEMENTA LA FUNCIÓN
    pass

# Devuelve la letra introducida por el usuario en mayúsculas. Deberá verificar que ha introducido una letra y no podrá continuar la ejecución hasta que lo haga. Si la letra introducida no es válida deberá lanzar la excepción ValueError
def set_guess():
    # IMPLEMENTA LA FUNCIÓN
    return ""

# Devuelve True si la letra está en la palabra, False si no.
# Además, modifica la lista hidden si la letra está en la palabra y el contador de aciertos
def check_guess(guess,word,hidden):
    # IMPLEMENTA LA FUNCIÓN
    return False

# Devuelve la cantidad de aciertos restando la longitud de la palabra de la cantidad de letras que siguen siendo guiones bajos.
def get_hits(hidden):
    hits = len(hidden) - hidden.count("_")
    return hits

# Main lanza la ejecución del programa
main()
