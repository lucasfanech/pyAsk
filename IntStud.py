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


#ajouter les boutons
button1 = customtkinter.CTkButton(root, width=100, text="Validation", font=("Courrier", 15), command=root.destroy)  # Création d'un widget Label (texte)
button1.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER) # Affichage du widget

button2 = customtkinter.CTkButton(root, width=100, text="Aide", font=("Courrier", 15), command=root.destroy)  # Création d'un widget Label (texte)
button2.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER) # Affichage du widget

button3 = customtkinter.CTkButton(root, width=100, text="Annuler", font=("Courrier", 15), command=root.destroy)  # Création d'un widget Label (texte)
button3.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER) # Affichage du widget


back_button = customtkinter.CTkButton(root, text="Back",font=("Courrier", 15), command=lambda : [root.destroy(), runpy.run_path('IntStart.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)





# Scrollable frame with fixed size
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=200, height=300)
scrollable_frame.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)


# Create Label + Button on same line inside scrollable frame
for i in range(30):
    customtkinter.CTkLabel(scrollable_frame, text="Label").grid(row=i, column=0)
    customtkinter.CTkButton(scrollable_frame, text="Button").grid(row=i, column=1)



root.mainloop() # Lancement de la boucle principale

