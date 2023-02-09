from tkinter import * # Importation de la bibliothèque Tkinter
import runpy
import subprocess

# valeurs par défaut
ipServeur = "localhost"
portServeur = 1111
numTable = 0

root = Tk() # Création de la fenêtre racine

#personnalisation de la fenêtre racine
root.title("pyAsk") # Titre de la fenêtre
root.geometry("720x480") # Taille de la fenêtre
root.minsize(800, 600) # Taille minimum de la fenêtre
root.iconbitmap("couronne.ico") # Icone de la fenêtre
root.config(background='#B6F0E6') # Couleur de fond de la fenêtre

#Créer la frame
frame = Frame(root, bg='#B6F0E6')

#ajouter un premier texte
Label_title = Label(frame, text="Bienvenue sur pyAsk", font=("Courrier", 25), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
Label_title.pack() # Affichage du widget

#ajouter un deuxième texte
Label_subtitle = Label(frame, text="L'aide à la gestion des TP", font=("Courrier", 15), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
Label_subtitle.pack(pady=20) # Affichage du widget


#Soumettre l'adresse IP
def enregistrer_InfoConnexion():
    global ipServeur
    global portServeur
    global numTable
    ipServeur = entree1.get()
    portServeur = entree2.get()
    numTable = entree3.get()
    print("Info connexion : ", ipServeur, portServeur, numTable)


entree1 = Entry(frame, text="IP serveur")
entree1.pack(pady=2)
entree2 = Entry(frame, text="Port serveur")
entree2.pack(pady=2)
entree3 = Entry(frame, text="Numéro de la table")
entree3.pack(pady=2)

#ajouter des valeurs par défaut
entree1.insert(0, ipServeur)
entree2.insert(0, portServeur)
entree3.insert(0, numTable)




bouton = Button(frame, text="Soumettre", font=("Courrier", 10), bg='#B6F0E6', fg='black', command=enregistrer_InfoConnexion)
bouton.pack(pady=15)

#Ajouter
frame.pack(expand=YES)

#ajouter un bouton
yt_button = Button(frame, text="Commencer", font=("Courrier", 15), bg='#B6F0E6', fg='black', command=lambda : [root.destroy(),  subprocess.run(['python', 'client_interface.py', str(ipServeur), str(portServeur), str(numTable)])])  # Création d'un widget Label (texte)
yt_button.pack(pady=20, fill=X) # Affichage du widget

admin_button = Button(root, text="Admin", bg='#B6F0E6', command=lambda : [root.destroy(), runpy.run_path('IntProf.py')])
admin_button.pack(side=BOTTOM, anchor=SE)

root.mainloop() # Lancement de la boucle principale

