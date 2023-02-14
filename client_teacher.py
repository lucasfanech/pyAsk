import customtkinter
import tkinter
import socket
import runpy
import sys

ipServeur = None
portServeur = None
ipbdd = None
portbdd = None
bddSelect = None
numTable = None

selectedClient = None
selectedMark = None

if len(sys.argv) > 1:
    ipServeur = sys.argv[1]
    portServeur = sys.argv[2]
    numTable = sys.argv[3]

#Fonctions:
def reset_interface():
    send_list_command()
    global selectedClient
    global selectedMark
    selectedClient = None
    selectedMark = None
    entry1.delete("0.0", "end")
    check1.deselect()
    check2.deselect()
    check3.deselect()
    check4.deselect()
    check5.deselect()

def send_mark_command():
    global selectedClient
    global selectedMark
    # get comment entry1
    selectedComment = entry1.get("0.0", "end")

    #if selectedClient is not None and selectedMark is not None:
    if selectedClient is not None:
        if selectedMark is not None:
            print("Envoi de la commande /mark ", selectedClient, selectedMark, selectedComment)
            # Envoie la commande "/mark" au serveur en utilisant un socket
            clientsocket.send(("/mark "+selectedClient+" "+str(selectedMark)+" "+selectedComment).encode())
            # affiche la réponse du serveur
            response = clientsocket.recv(2048).decode()
            print("Réponse du serveur: ", response)
            #Reset interface
            reset_interface()
        else:
            print("Erreur: Aucune note sélectionnée")
    else:
        print("Erreur: Aucun client sélectionné")

def set_Client(i, client):
    global selectedClient
    if (selectedClient == client):
        selectedClient = None
        print("Client désélectionné")
        #activate all buttons
        for widget in scrollable_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.configure(state=tkinter.NORMAL)

    else:
        selectedClient = client
        print("Client sélectionné: ", selectedClient)
        #desactivate all buttons
        for widget in scrollable_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.configure(state=tkinter.DISABLED)
        #activate selected button
        scrollable_frame.winfo_children()[i*2+1].configure(state=tkinter.NORMAL)

def set_Mark(mark):
    global selectedMark
    if (selectedMark == -1):
        selectedMark = None
    else:
        selectedMark = mark
    print("Note selectionnée: ", selectedMark)




def send_list_command():
    global selectedClient
    selectedClient = None
    print("Client désélectionné")
    # Envoie la commande "/list" au serveur en utilisant un socket
    clientsocket.send("/list".encode())
    # affiche la réponse du serveur
    response = clientsocket.recv(2048).decode()
    print("Liste d'attente actuelle: ", response)
    # Affichage dans le tableau de la liste d'attente
    #empty scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    #Traitement de la réponse du serveur
    waitingList = []
    checkboxes = []
    if response != "{}":
        # Pour chaque entrée séparée par une virgule et accolade dans la réponse du serveur
        i = 0
        for entry in response.split("},"):
            # chaque entrée est composée ainsi: {user: value_user, callType: value_callType}
            # on récupère le mot après le mot "user: " et avant la virgule
            user = entry.split("user: ")[1].split(",")[0]
            # on récupère le mot après le mot "callType: " et avant "}"
            callType = entry.split("callType: ")[1].split("}")[0]
            # on ajoute l'entrée à la liste d'attente
            #waitingList.append({"user": user, "callType": callType})
            print("user: ", user, " - callType: ", callType)

            customtkinter.CTkLabel(scrollable_frame, text="Table n° "+user+" ").grid(row=i,column=0)
            if callType == "0":
                customtkinter.CTkButton(scrollable_frame, text="Question", command=lambda i=i, client=user: set_Client(i, client)).grid(row=i, column=1)
            elif callType == "1":
                customtkinter.CTkButton(scrollable_frame, text="Vérification", command=lambda i=i, client=user: set_Client(i, client)).grid(row=i, column=1)

            i += 1

#Connect admin socket
# Crée une connexion socket avec le seveur en localhost sur le port 1111
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connexion au serveur
if ipServeur and portServeur and numTable:
    # Code à exécuter si toutes les variables sont définies
    # Connecion au serveur
    print("Connexion au serveur: ", ipServeur, ":", portServeur, " - Table: ", numTable)
    try:
        clientsocket.connect((ipServeur, int(portServeur)))
    except:
        print("Erreur de connexion au serveur")
        sys.exit()
else:
    # Code à exécuter si au moins une variable n'est pas définie
    print("Erreur: Une variable n'est pas définie")
    # terminer le programme
    exit()

# numéro d'identification (table)
r = numTable
# envoie le numéro d'identification au serveur
clientsocket.send(r.encode())
# affiche la réponse du serveur
response = clientsocket.recv(2048).decode()
print(response)
# Si la réponse est "Vous êtes connecté" alors on affiche "Connexion réussie" et on attend une entrée utilisateur infinie
if response == "Vous êtes connecté":
    print("Connexion réussie")


#Start Interface


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
# On click on check1-2-3-4-5 -> uncheck others
check1.configure(command=lambda: [check2.deselect(), check3.deselect(), check4.deselect(), check5.deselect(), set_Mark(1)])
check2.configure(command=lambda: [check1.deselect(), check3.deselect(), check4.deselect(), check5.deselect(), set_Mark(2)])
check3.configure(command=lambda: [check1.deselect(), check2.deselect(), check4.deselect(), check5.deselect(), set_Mark(3)])
check4.configure(command=lambda: [check1.deselect(), check2.deselect(), check3.deselect(), check5.deselect(), set_Mark(4)])
check5.configure(command=lambda: [check1.deselect(), check2.deselect(), check3.deselect(), check4.deselect(), set_Mark(5)])
# ajouter une textbox user input
entry1 = customtkinter.CTkTextbox(root, width=250, height=270, font=("Courrier", 15), fg_color="#484f58")  # Création d'un widget Label (texte)
entry1.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)  # Affichage du widget

# ajouter les boutons
button1 = customtkinter.CTkButton(root, width=100, text="Validation", font=("Courrier", 15), command=send_mark_command)  # Création d'un widget Label (texte)
button1.place(relx=0.2, rely=0.85, anchor=tkinter.CENTER)  # Affichage du widget

button2 = customtkinter.CTkButton(root, width=100, text="Annuler", font=("Courrier", 15), command=reset_interface)  # Création d'un widget Label (texte)
button2.place(relx=0.35, rely=0.85, anchor=tkinter.CENTER)  # Affichage du widget

back_button = customtkinter.CTkButton(root, text="Back", font=("Courrier", 15), command=lambda: [root.destroy(), runpy.run_path('client_start.py')])
back_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

# Scrollable frame with fixed size
scrollable_frame = customtkinter.CTkScrollableFrame(root, width=250, height=300)
scrollable_frame.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

send_list_command()

# Refresh button
refresh_button = customtkinter.CTkButton(root, text="Refresh", font=("Courrier", 15), command=send_list_command)
refresh_button.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)


root.mainloop()  # Lancement de la boucle principale
clientsocket.send("/leave".encode())
clientsocket.close()
runpy.run_path('client_start.py')