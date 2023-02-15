import customtkinter
import tkinter
import runpy
import subprocess

# valeurs par défaut
ipServeur = "localhost"
portServeur = 1111
numTable = 0

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk() # Création de la fenêtre racine

#personnalisation de la fenêtre racine
root.title("pyAsk") # Titre de la fenêtre
root.geometry("720x480") # Taille de la fenêtre
root.minsize(800, 600) # Taille minimum de la fenêtre
root.iconbitmap("couronne.ico") # Icone de la fenêtre

#Créer la frame
customtkinter.CTkFrame(root)

#ajouter un premier texte
Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk", font=("Courrier", 25))  # Création d'un widget Label (texte)
Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER) # Affichage du widget

#ajouter un deuxième texte
Label_subtitle = customtkinter.CTkLabel(root, text="L'aide à la gestion des TP", font=("Courrier", 15))  # Création d'un widget Label (texte)
Label_subtitle.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER) # Affichage du widget


def enregistrer_Historique():
    global ipServeur
    global portServeur
    global numTable
    ipServeur = entree1.get()
    portServeur = entree2.get()
    numTable = entree3.get()
    print("Info connexion : ", ipServeur, portServeur, numTable)
    root.destroy()
    subprocess.run(['python', 'client_history.py', str(ipServeur), str(portServeur), str(numTable)])

#Soumettre l'adresse IP
def enregistrer_InfoConnexion():
    global ipServeur
    global portServeur
    global numTable
    ipServeur = entree1.get()
    portServeur = entree2.get()
    numTable = entree3.get()
    print("Info connexion : ", ipServeur, portServeur, numTable)
    root.destroy()
    subprocess.run(['python', 'client_interface.py', str(ipServeur), str(portServeur), str(numTable)])

def enregistrer_AdminConnexion():
    global ipServeur
    global portServeur
    global numTable
    ipServeur = entree1.get()
    portServeur = entree2.get()
    numTable = entree3.get()
    print("Info connexion : ", ipServeur, portServeur, numTable)
    root.destroy()
    subprocess.run(['python', 'client_teacher.py', str(ipServeur), str(portServeur), str(numTable)])

#Label pour l'adresse IP
Label_ip = customtkinter.CTkLabel(root, text="Adresse IP du serveur", font=("Courrier", 12))  # Création d'un widget Label (texte)
Label_ip.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER) # Affichage du widget
entree1 = customtkinter.CTkEntry(root, show="", placeholder_text="IP serveur")
entree1.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

#Label pour le port
Label_port = customtkinter.CTkLabel(root, text="Port du serveur", font=("Courrier", 12))  # Création d'un widget Label (texte)
Label_port.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER) # Affichage du widget
entree2 = customtkinter.CTkEntry(root, show="", placeholder_text="Port serveur")
entree2.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

#Label pour le numéro de table
Label_table = customtkinter.CTkLabel(root, text="Numéro de table", font=("Courrier", 12))  # Création d'un widget Label (texte)
Label_table.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # Affichage du widget
entree3 = customtkinter.CTkEntry(root, show="", placeholder_text="Numéro de table")
entree3.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

#ajouter des valeurs par défaut
entree1.insert(0, "localhost")
entree2.insert(0, "1111")
entree3.insert(0, "0")

#Bouton pour lancer le client
yt_button = customtkinter.CTkButton(root, text="Démarrer", font=("Courrier", 15), command=enregistrer_InfoConnexion)
yt_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

#Bouton pour lancer l'interface admin
admin_button = customtkinter.CTkButton(root, text="Admin",font=("Courrier", 15), command=enregistrer_AdminConnexion)
admin_button.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)

#Bouton pour afficher l'historique
historique_button = customtkinter.CTkButton(root, text="Historique",font=("Courrier", 15), command=enregistrer_Historique)
historique_button.place(relx=0.9, rely=0.85, anchor=tkinter.CENTER)

root.mainloop() # Lancement de la boucle principale

