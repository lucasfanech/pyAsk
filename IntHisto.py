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


# Scrollable frame with fixed size
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=550, height=350)
scrollable_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Create Label + Button on same line inside scrollable frame
for i in range(30):
    customtkinter.CTkCheckBox(scrollable_frame, text="").grid(row=i, column=0) 
    customtkinter.CTkLabel(scrollable_frame, text="GroRuk".format(i)).grid(row=i, column=1) 
    

#back button
back_button = customtkinter.CTkButton(root, text="Back",font=("Courrier", 15), command=lambda : [root.destroy(), runpy.run_path('IntProf.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)


root.mainloop() # Lancement de la boucle principale