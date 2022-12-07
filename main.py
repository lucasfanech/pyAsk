
# create a modern GUI with three buttons vertically aligned in the center of the screen with title "Modern GUI"
# Path: main.py
from tkinter import *
main = Tk()
main.title("Call Me Maybe")
main.geometry("600x600")
main.configure(bg="white")
# create a label with the text "Call Me Maybe" and font "Helvetica 20 bold"
# Path: main.py
label = Label(main, text="Call Me Maybe", font="Helvetica 20 bold")
label.pack()

bouton1 = Button(main, text="Question", bg="green", fg="white")
bouton2 = Button(main, text="Validation", bg="blue", fg="white")
bouton3 = Button(main, text="Annulation", bg="red", fg="white")

# Place les boutons au centre de la fenêtre
bouton1.pack(side=TOP, anchor=CENTER)
bouton2.pack(side=TOP, anchor=CENTER)
bouton3.pack(side=TOP, anchor=CENTER)
main.mainloop()

# create 3 buttons with tkinter