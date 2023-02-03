# coding: utf-8
import socket
from tkinter import * # Importation de la bibliothèque Tkinter
import runpy
def send_ask_command():
    # Envoie la commande "/ask" au serveur en utilisant un socket
    clientsocket.send("/ask".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete(1.0, END)
    T.insert(END, response)


def send_verify_command():
    # Envoie la commande "/verify" au serveur en utilisant un socket
    clientsocket.send("/verify".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete(1.0, END)
    T.insert(END, response)

def send_cancel_command():
    # Envoie la commande "/cancel" au serveur en utilisant un socket
    clientsocket.send("/cancel".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Réponse du serveur: ", response)
    T.delete(1.0, END)
    T.insert(END, response)

def send_leave_command():
    # Envoie la commande "/leave" au serveur en utilisant un socket
    clientsocket.send("/leave".encode())
    root.destroy()
    runpy.run_path('IntStart.py')


# Crée une connexion socket avec le seveur en localhost sur le port 1111
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#Connecion au serveur
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
    root = Tk() # Création de la fenêtre racine
    #personnalisation de la fenêtre racine
    root.title("Interface etudiants") # Titre de la fenêtre
    root.geometry("720x480") # Taille de la fenêtre
    root.minsize(880, 600) # Taille minimum de la fenêtre
    #root.iconbitmap("couronne.ico") # Icone de la fenêtre
    root.config(background='#B6F0E6') # Couleur de fond de la fenêtre
    #Créer la frame
    frame = Frame(root, bg='#B6F0E6')
    #ajouter un premier texte
    Label_title = Label(root, text="Bienvenue sur pyAsk", font=("Courrier", 25), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
    Label_title.pack(pady=50) # Affichage du widget
    #Ajouter
    frame.pack(expand=YES)
    #ajouter les boutons
    button1 = Button(frame, width=25, text="Validation", font=("Courrier", 15), bg='#37BF39', fg='black', command=send_verify_command)  # Création d'un widget Label (texte)
    button1.pack(pady=15, fill=X) # Affichage du widget
    button2 = Button(frame, width=25, text="Aide", font=("Courrier", 15), bg='#F1FF00', fg='black', command=send_ask_command)  # Création d'un widget Label (texte)
    button2.pack(pady=15, fill=X) # Affichage du widget
    button3 = Button(frame, width=25, text="Annuler", font=("Courrier", 15), bg='#E84130', fg='black', command=send_cancel_command)  # Création d'un widget Label (texte)
    button3.pack(pady=15, fill=X) # Affichage du widget
    back_button = Button(root, text="Back", bg='#B6F0E6', command=send_leave_command)  # Création d'un widget Label (texte)
    back_button.pack(side=BOTTOM, anchor=SE)
    # Create text widget and label
    Label_response = Label(frame, text="Réponse du serveur", font=("Courrier", 15), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
    Label_response.pack(pady=50) # Affichage du widget
    T = Text(frame, height=2, width=30)
    T.pack()
    T.insert(END, "Connecté au serveur.")
    root.mainloop() # Lancement de la boucle principale



# lorsque l'on ferme la fenêtre, on ferme la connexion
clientsocket.send("/leave".encode())
clientsocket.close()
runpy.run_path('IntStart.py')










