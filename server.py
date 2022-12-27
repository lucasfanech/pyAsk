import socket
import threading
#import de la classe DatabaseConnection du fichier bdd.py
from bdd import DatabaseConnection

#fonction qui affiche les threads de la liste threads et les sépare par des virgules
def print_threads():
    print("Threads actifs: ", end="")
    for thread in threads:
        print(thread, end=", ")
    print()

#fonction check_demande qui vérifie si une demande est présente dans la table waiting_line
def check_demand(userid, sessionId):
    # Créer une instance de la classe DatabaseConnection
    db = DatabaseConnection("localhost", 3306, "cmm", "root", "")

    # Établir la connexion à la base de données
    db.connect()

    # Vérifie si une demande est présente dans la table waiting_line
    demand = db.show_wait(userid, sessionId)
    print("demande: " + str(demand))
    # fermes la connexion à la base de données
    db.disconnect()
    # Si une demande est présente, on retourne True
    if demand:
        return True
    # TO DO: Return de l'etat de la demande au lieu de true


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048)
        print("Connexion du client n°: ", r.decode(), "...")
        self.idClient = r.decode()
        # ajoute le numéro d'identification du client à la liste des threads
        threads.append(r.decode())
        # affiche la liste des threads
        print_threads()

        self.clientsocket.send("Vous êtes connecté".encode())
        # check_demand()
        r_demand = check_demand(self.idClient, num_session)
        self.state = r_demand

        # écoute les messages du client et les affiche
        while True:
            r = self.clientsocket.recv(2048)
            print("Client "+self.idClient+" :", r.decode())
            # Si la réponse est "/call" alors on affiche "Appel en cours"
            if r.decode() == "/ask":
                print("Appel pour une question")
            if r.decode() == "/verify":
                print("Appel pour une vérification")
            if r.decode() == "/cancel":
                print("Annule l'appel")


            if r.decode() == "/leave":
                print("Connexion terminée")
                self.clientsocket.close()
                # supprime le numéro d'identification du client de la liste des threads
                threads.remove(self.idClient)
                # affiche la liste des threads
                print_threads()
                break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

# crée un tableau de threads
threads = []

while True:
    # Créer une instance de la classe DatabaseConnection
    db = DatabaseConnection("localhost", 3306, "cmm", "root", "")

    # Établir la connexion à la base de données
    db.connect()

    # Appeler la méthode detect_game
    results = db.detect_game()

    # Afficher les résultats
    if results[0][0] is not None:
        print("Session n°"+ str(results[0][0]))
        num_session = results[0][0]

    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()


