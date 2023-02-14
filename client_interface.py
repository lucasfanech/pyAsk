# coding: utf-8
import socket
import threading

import customtkinter
import tkinter
import runpy
import sys

ipServeur = None
portServeur = None
ipbdd = None
portbdd = None
bddSelect = None
numTable = None

if len(sys.argv) > 1:
    ipServeur = sys.argv[1]
    portServeur = sys.argv[2]
    numTable = sys.argv[3]

def send_list_command():
    # Envoie la commande "/list" au serveur en utilisant un socket
    clientsocket.send("/list".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Liste d'attente actuelle: ", response)
    # Affichage dans le tableau de la liste d'attente
    #empty scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    #Traitement de la réponse du serveur
    waitingList = []
    # Pour chaque entrée séparée par une virgule et accolade dans la réponse du serveur
    i = 0
    if response != "{}":
        for entry in response.split("},"):
            # chaque entrée est composée ainsi: {user: value_user, callType: value_callType}
            # on récupère le mot après le mot "user: " et avant la virgule
            user = entry.split("user: ")[1].split(",")[0]
            # on récupère le mot après le mot "callType: " et avant "}"
            callType = entry.split("callType: ")[1].split("}")[0]
            # on ajoute l'entrée à la liste d'attente
            #waitingList.append({"user": user, "callType": callType})
            print("user: ", user, " - callType: ", callType)
            customtkinter.CTkLabel(scrollable_frame, text="Table n° "+user+" ").grid(row=i,column=0)
            if callType == "0":
                customtkinter.CTkButton(scrollable_frame, text="Question").grid(row=i, column=1)
            elif callType == "1":
                customtkinter.CTkButton(scrollable_frame, text="Vérification").grid(row=i, column=1)

            i += 1




def send_ask_command():
    # Envoie la commande "/ask" au serveur en utilisant un socket
    clientsocket.send("/ask".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete("0.0", "end")  # delete all text
    T.insert("0.0", response)  # insert response
    send_list_command()


def send_verify_command():
    # Envoie la commande "/verify" au serveur en utilisant un socket
    clientsocket.send("/verify".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete("0.0", "end")  # delete all text
    T.insert("0.0", response)  # insert response
    send_list_command()

def send_cancel_command():
    # Envoie la commande "/cancel" au serveur en utilisant un socket
    clientsocket.send("/cancel".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete("0.0", "end")  # delete all text
    T.insert("0.0", response)  # insert response
    send_list_command()

def send_leave_command():
    # Envoie la commande "/leave" au serveur en utilisant un socket
    clientsocket.send("/leave".encode())
    root.destroy()
    runpy.run_path('client_start.py')


# Crée une connexion socket avec le seveur en localhost sur le port 1111
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connexion au serveur
if ipServeur and portServeur and numTable:
    # Code à exécuter si toutes les variables sont définies
    # Connecion au serveur
    print("Connexion au serveur: ", ipServeur, ":", portServeur, " - Table: ", numTable)
    try:
        clientsocket.connect((ipServeur, int(portServeur)))
    except:
        print("Erreur de connexion au serveur")
        sys.exit()
else:
    # Code à exécuter si au moins une variable n'est pas définie
    print("Erreur: Une variable n'est pas définie")
    # terminer le programme
    exit()

# numéro d'identification (table)
r = numTable
# envoie le numéro d'identification au serveur
clientsocket.send(r.encode())
# affiche la réponse du serveur
response = clientsocket.recv(2048).decode()
print(response)
# Si la réponse est "Vous êtes connecté" alors on affiche "Connexion réussie" et on attend une entrée utilisateur infinie
if response == "Vous êtes connecté":
    print("Connexion réussie")

    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    root = customtkinter.CTk()  # Création de la fenêtre racine

    # personnalisation de la fenêtre racine
    root.title("pyAsk")  # Titre de la fenêtre
    root.geometry("720x480")  # Taille de la fenêtre
    root.minsize(800, 600)  # Taille minimum de la fenêtre
    root.iconbitmap("couronne.ico")  # Icone de la fenêtre

    # Créer la frame
    customtkinter.CTkFrame(root)

    # ajouter un premier texte
    Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk",font=("Courrier", 25))  # Création d'un widget Label (texte)
    Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)  # Affichage du widget

    # ajouter les boutons
    button1 = customtkinter.CTkButton(root, width=100, text="Validation", font=("Courrier", 15),command=send_verify_command)  # Création d'un widget Label (texte)
    button1.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)  # Affichage du widget

    button2 = customtkinter.CTkButton(root, width=100, text="Aide", font=("Courrier", 15),command=send_ask_command)  # Création d'un widget Label (texte)
    button2.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)  # Affichage du widget

    button3 = customtkinter.CTkButton(root, width=100, text="Annuler", font=("Courrier", 15),command=send_cancel_command)  # Création d'un widget Label (texte)
    button3.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)  # Affichage du widget

    back_button = customtkinter.CTkButton(root, text="Back", font=("Courrier", 15),command=send_leave_command)
    back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)


    # Create textbox widget and label
    T = customtkinter.CTkTextbox(root, height=50, width=400)
    T.grid(row=0, column=0)
    T.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    # Add test text
    T.insert("0.0", "Table n°" + numTable + " est connecté au serveur")

    # Scrollable frame with fixed size
    scrollable_frame = customtkinter.CTkScrollableFrame(root, width=200, height=300)
    scrollable_frame.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
    # Mise à jour de la liste d'attente
    send_list_command()

    #Button to refresh the frame
    refresh_button = customtkinter.CTkButton(root, text="Refresh", font=("Courrier", 15),command=send_list_command)
    refresh_button.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)


    root.mainloop() # Lancement de la boucle principale



# lorsque l'on ferme la fenêtre, on ferme la connexion
clientsocket.send("/leave".encode())
clientsocket.close()
runpy.run_path('client_start.py')











