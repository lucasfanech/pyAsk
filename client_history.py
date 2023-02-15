import customtkinter
import tkinter
import runpy
import socket
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

#Fonctions:
def send_history_command():
    # Envoie la commande "/history" au serveur en utilisant un socket
    clientsocket.send("/history".encode())
    # affiche la réponse du serveur taille indéfinie
    response = clientsocket.recv(81920).decode()
    print("Historique: ", response)
    # Affichage dans le tableau de l'historique
    #empty scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    #Traitement de la réponse du serveur
    historyList = []
    # Pour chaque entrée séparée par une virgule et accolade dans la réponse du serveur
    i = 0
    if response != "{}":
        for entry in response.split("},"):
            # chaque entrée est composée ainsi: {user: value_user, callType: value_callType, solved: value_solved, mark: value_mark, comment: value_comment}
            # on récupère le mot après le mot "user: " et avant la virgule
            user = entry.split("user: ")[1].split(",")[0]
            # on récupère le mot après le mot "callType: " et avant la virgule
            callType = entry.split("callType: ")[1].split(",")[0]
            # on récupère le mot après le mot "solved: " et avant la virgule
            solved = entry.split("solved: ")[1].split(",")[0]
            # on récupère le mot après le mot "mark: " et avant la virgule
            mark = entry.split("mark: ")[1].split(",")[0]
            # on récupère le mot après le mot "comment: " et avant "}"
            comment = entry.split("comment: ")[1].split("}")[0]
            # on ajoute l'entrée à la liste d'attente
            print("user: ", user, " - callType: ", callType, " - solved: ", solved, " - mark: ", mark, " - comment: ", comment)
            customtkinter.CTkLabel(scrollable_frame, text="Table n° "+user+" ").grid(row=i,column=0)
            if callType == "0":
                customtkinter.CTkButton(scrollable_frame, text="Question").grid(row=i, column=1)
            elif callType == "1":
                customtkinter.CTkButton(scrollable_frame, text="Vérification").grid(row=i, column=1)
            customtkinter.CTkLabel(scrollable_frame, text="     "+mark+"/5").grid(row=i, column=3)
            customtkinter.CTkLabel(scrollable_frame, text="     "+comment).grid(row=i, column=5)
            customtkinter.CTkLabel(scrollable_frame, text="     "+solved).grid(row=i,column=7)



            i += 1



#Connect admin socket
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

#Interface
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
Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk",
                                     font=("Courrier", 25))  # Création d'un widget Label (texte)
Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)  # Affichage du widget

# Scrollable frame with fixed size
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=600, height=350)
scrollable_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

send_history_command()

# refresh button
refresh_button = customtkinter.CTkButton(root, text="Refresh", font=("Courrier", 15), command=send_history_command)
refresh_button.place(relx=0.9, rely=0.85, anchor=tkinter.CENTER)
# back button
back_button = customtkinter.CTkButton(root, text="Back", font=("Courrier", 15), command=lambda: [root.destroy(),clientsocket.send("/leave".encode()),clientsocket.close(), runpy.run_path('client_start.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

root.mainloop()  # Lancement de la boucle principale
clientsocket.send("/leave".encode())
clientsocket.close()
runpy.run_path('client_start.py')