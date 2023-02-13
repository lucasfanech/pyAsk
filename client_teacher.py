import customtkinter
import tkinter
import runpy

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # Création de la fenêtre racine

# personnalisation de la fenêtre racine
root.title("pyAsk")  # Titre de la fenêtre
root.geometry("800x600")  # Taille de la fenêtre
root.iconbitmap("couronne.ico")  # Icone de la fenêtre

# Créer la frame
customtkinter.CTkFrame(root)

# ajouter un premier texte
Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk",
                                     font=("Courrier", 25))  # Création d'un widget Label (texte)
Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)  # Affichage du widget

# ajouter un deuxième texte
Label_subtitle = customtkinter.CTkLabel(root, text="Notez et commentez",
                                        font=("Courrier", 15))  # Création d'un widget Label (texte)
Label_subtitle.place(relx=0.3, rely=0.22, anchor=tkinter.CENTER)  # Affichage du widget

# Créer la frame
customtkinter.CTkFrame(root)

# ajouter un premier texte
Label_title = customtkinter.CTkLabel(root, text="Bienvenue sur pyAsk",
                                     font=("Courrier", 25))  # Création d'un widget Label (texte)
Label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)  # Affichage du widget

# ajouter des checkboxes
check1 = customtkinter.CTkCheckBox(root, text="*")  # Création d'un widget Label (texte)
check1.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)  # Affichage du widget
check2 = customtkinter.CTkCheckBox(root, text="**")  # Création d'un widget Label (texte)
check2.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)  # Affichage du widget
check3 = customtkinter.CTkCheckBox(root, text="***")  # Création d'un widget Label (texte)
check3.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)  # Affichage du widget
check4 = customtkinter.CTkCheckBox(root, text="****")  # Création d'un widget Label (texte)
check4.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)  # Affichage du widget
check5 = customtkinter.CTkCheckBox(root, text="*****")  # Création d'un widget Label (texte)
check5.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)  # Affichage du widget

# ajouter une textbox user input
entry1 = customtkinter.CTkTextbox(root, width=250, height=270, font=("Courrier", 15),
                                  fg_color="#484f58")  # Création d'un widget Label (texte)
entry1.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)  # Affichage du widget

# ajouter les boutons
button1 = customtkinter.CTkButton(root, width=100, text="Validation", font=("Courrier", 15),
                                  command=root.destroy)  # Création d'un widget Label (texte)
button1.place(relx=0.2, rely=0.85, anchor=tkinter.CENTER)  # Affichage du widget

button2 = customtkinter.CTkButton(root, width=100, text="Annuler", font=("Courrier", 15),
                                  command=root.destroy)  # Création d'un widget Label (texte)
button2.place(relx=0.35, rely=0.85, anchor=tkinter.CENTER)  # Affichage du widget

back_button = customtkinter.CTkButton(root, text="Back", font=("Courrier", 15),
                                      command=lambda: [root.destroy(), runpy.run_path('client_start.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

# Scrollable frame with fixed size
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=200, height=300)
scrollable_frame.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

# Create Label + Button on same line inside scrollable frame
for i in range(30):
    customtkinter.CTkCheckBox(scrollable_frame, text="").grid(row=i, column=0)
    customtkinter.CTkLabel(scrollable_frame, text="Label {}".format(i)).grid(row=i, column=1)

# Refresh button
refresh_button = customtkinter.CTkButton(root, text="Refresh", font=("Courrier", 15))
refresh_button.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)


root.mainloop()  # Lancement de la boucle principale
