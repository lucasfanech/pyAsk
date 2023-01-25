from tkinter import * # Importation de la bibliothèque Tkinter
import runpy    

root = Tk() # Création de la fenêtre racine

#personnalisation de la fenêtre racine
root.title("Interface professeur") # Titre de la fenêtre
root.geometry("720x480") # Taille de la fenêtre
root.minsize(480, 360) # Taille minimum de la fenêtre
root.iconbitmap("couronne.ico") # Icone de la fenêtre
root.config(background='#B6F0E6') # Couleur de fond de la fenêtre

#Créer la frame
frame = Frame(root, bg='#B6F0E6')

#ajouter un premier texte
Label_title = Label(root, text="Bienvenue sur pyAsk", font=("Courrier", 25), bg='#B6F0E6', fg='black')  # Création d'un widget Label (texte)
Label_title.pack(pady=50) # Affichage du widget


#Ajouter 
frame.pack(expand=YES)

#ajouter les boutons
button1 = Button(root, width=15, text="Validation", font=("Courrier", 15), bg='#37BF39', fg='black', command=root.destroy)  # Création d'un widget Label (texte)
button1.pack(pady=15,padx=15, fill=Y, side=LEFT) # Affichage du widget

button2 = Button(root, width=15, text="Annulation", font=("Courrier", 15), bg='#E84130', fg='black', command=root.destroy)  # Création d'un widget Label (texte)
button2.pack(pady=15, padx=15, fill=Y, side=LEFT) # Affichage du widget

back_button = Button(root, text="Back", bg='#B6F0E6', command=lambda : [root.destroy(), runpy.run_path('IntStart.py')])
back_button.pack(side=BOTTOM, anchor=SE)

root.mainloop() # Lancement de la boucle principale

