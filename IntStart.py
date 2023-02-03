from tkinter import * # Importation de la bibliothèque Tkinter
import runpy

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
    ipServeur = entree1.get()
    portServeur = entree2.get()
    ipbdd = entree3.get()
    portbdd = entree4.get()
    bddSelect = entree5.get()
    numTable = entree6.get()


entree1 = Entry(frame, text="IP serveur")
entree1.pack(pady=2)
entree2 = Entry(frame, text="Port serveur")
entree2.pack(pady=2)
entree3 = Entry(frame, text="IP base de données")
entree3.pack(pady=2)
entree4 = Entry(frame, text="Port base de données")
entree4.pack(pady=2)
entree5 = Entry(frame, text="Choix Base de données")
entree5.pack(pady=2)
entree6 = Entry(frame, text="Numéro de la table")
entree6.pack(pady=2)



bouton = Button(frame, text="Soumettre", font=("Courrier", 10), bg='#B6F0E6', fg='black', command=enregistrer_InfoConnexion)
bouton.pack(pady=15)

#Ajouter 
frame.pack(expand=YES)

#ajouter un bouton
yt_button = Button(frame, text="Commencer", font=("Courrier", 15), bg='#B6F0E6', fg='black', command=lambda : [root.destroy(), runpy.run_path('IntStud.py')])  # Création d'un widget Label (texte)
yt_button.pack(pady=20, fill=X) # Affichage du widget

admin_button = Button(root, text="Admin", bg='#B6F0E6', command=lambda : [root.destroy(), runpy.run_path('IntProf.py')])
admin_button.pack(side=BOTTOM, anchor=SE)

root.mainloop() # Lancement de la boucle principale

