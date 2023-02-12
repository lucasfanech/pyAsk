import customtkinter
import tkinter
import runpy

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


#Soumettre l'adresse IP
def enregistrer_InfoConnexion():
    ipServeur = entree1.get()
    portServeur = entree2.get()
    numTable = entree6.get()

entree1 = customtkinter.CTkEntry(root, placeholder_text="IP serveur")
entree1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

entree2 = customtkinter.CTkEntry(root, placeholder_text="Port serveur")
entree2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

entree6 = customtkinter.CTkEntry(root, placeholder_text="Table")
entree6.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

bouton = customtkinter.CTkButton(root, text="Soumettre", font=("Courrier", 15), command=enregistrer_InfoConnexion)
bouton.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

admin_button = customtkinter.CTkButton(root, text="Admin",font=("Courrier", 15), command=lambda : [root.destroy(), runpy.run_path('IntProf.py')])
admin_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)


root.mainloop() # Lancement de la boucle principale