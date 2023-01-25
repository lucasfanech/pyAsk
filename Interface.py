from tkinter import * # Importation de la bibliothèque Tkinter

root = Tk() # Création de la fenêtre racine

#personnalisation de la fenêtre racine
root.title("pyAsk") # Titre de la fenêtre
root.geometry("720x480") # Taille de la fenêtre
root.minsize(480, 360) # Taille minimum de la fenêtre
root.iconbitmap("couronne.ico") # Icone de la fenêtre
root.config(background='#B6F0E6') # Couleur de fond de la fenêtre

#Créer la frame
frame = Frame(root, bg='#B6F0E6')

#ajouter un premier texte
Label_title = Label(frame, text="Bienvenue sur pyAsk", font=("Courrier", 25), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
Label_title.pack() # Affichage du widget

#ajouter un deuxième texte
Label_subtitle = Label(frame, text="L'aide à la gestion des TP", font=("Courrier", 15), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
Label_subtitle.pack() # Affichage du widget

#Ajouter 
frame.pack(expand=YES)

#ajouter un bouton
yt_button = Button(frame, text="Commencer", font=("Courrier", 15), bg='#B6F0E6', fg='black', command=root.destroy)  # Création d'un widget Label (texte)
yt_button.pack(pady=25, fill=X) # Affichage du widget

root.mainloop() # Lancement de la boucle principale

