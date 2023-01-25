# coding: utf-8

import socket

# Crée une connexion socket avec le seveur en localhost sur le port 1111
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 1111))

# demande un numéro d'identification au client via la fonction input()
r = input("Entrez votre numéro d'identification: ")
# envoie le numéro d'identification au serveur
clientsocket.send(r.encode())
# affiche la réponse du serveur
response = clientsocket.recv(2048).decode()
print(response)
# Si la réponse est "Vous êtes connecté" alors on affiche "Connexion réussie" et on attend une entrée utilisateur infinie
if response == "Vous êtes connecté":
    print("Connexion réussie")
    while True:
        userInput = input("Entrée utilisateur: ")
        # envoie l'entrée utilisateur au serveur
        print("Envoi de l'entrée utilisateur au serveur...")
        clientsocket.send(userInput.encode())
        # affiche la réponse du serveur
        response = clientsocket.recv(2048).decode()
        print("Réponse du serveur: ", response)
        # Si la réponse est "/server-stop" alors on affiche "Connexion terminée" et on ferme la connexion
        if userInput == "/leave":
            print("Connexion terminée")
            clientsocket.close()
            break


# lorsque l'on ferme la fenêtre, on ferme la connexion
clientsocket.close()






