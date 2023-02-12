import customtkinter
import tkinter
import runpy

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk() # Création de la fenêtre racine

#personnalisation de la fenêtre racine
root.title("pyAsk") # Titre de la fenêtre
root.geometry("800x600") # Taille de la fenêtre
root.iconbitmap("couronne.ico") # Icone de la fenêtre


#Créer la frame
customtkinter.CTkFrame(root)


#ajouter un premier texte
Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk", font=("Courrier", 25))  # Création d'un widget Label (texte)
Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER) # Affichage du widget


#ajouter les boutons
button1 = customtkinter.CTkButton(root, width=15, text="Validation", font=("Courrier", 15), command=root.destroy)  # Création d'un widget Label (texte)
button1.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER) # Affichage du widget

button2 = customtkinter.CTkButton(root, width=15, text="Annulation", font=("Courrier", 15), command=root.destroy)  # Création d'un widget Label (texte)
button2.place(relx=0.21, rely=0.9, anchor=tkinter.CENTER) # Affichage du widget

back_button = customtkinter.CTkButton(root, text="Back", font=("Courrier", 15), command=lambda : [root.destroy(), runpy.run_path('IntStart.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

root.mainloop() # Lancement de la boucle principale

