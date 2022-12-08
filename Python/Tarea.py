import random

def play():
    user = input("Escribe tu nombre: ")
    playera = ""
    
    if user == "Félix":
        playera = "Te toca la 27"
    if user == "Marcelo":
        playera = "Te toca la 10"
    elif user == "Marcelo":
          playera = "Ya veremos cual te toca"
    else:
        playera = "Sigue participando"
        
    return playera

print ("El resultado es: " + play())
