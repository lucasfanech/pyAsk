import socket
import threading
#import de la classe DatabaseConnection du fichier bdd.py
from bdd import DatabaseConnection

#Paramètres par défaut:
ipBdd = "localhost"
portBdd = 3306
userBdd = "root"
passwordBdd = ""
bddName = "cmm"
#fonction qui affiche les threads de la liste threads et les sépare par des virgules
def print_threads():
    print("Threads actifs: ", end="")
    for thread in threads:
        print(thread, end=", ")
    print()

#fonction qui affiche les clients de la liste d'attente et les sépare par des virgules
def get_waiting_list():
    global ipBdd
    global portBdd
    global userBdd
    global passwordBdd
    global bddName
    # Créer une instance de la classe DatabaseConnection
    db = DatabaseConnection(ipBdd, portBdd, bddName, userBdd, passwordBdd)
    # Établir la connexion à la base de données
    db.connect()
    # Récupère la liste des clients en attente
    waiting_list = db.show_waitingline(num_session)
    # ferme la connexion à la base de données
    db.disconnect()
    # affiche la liste des clients en attente
    liste = ""
    print("Liste d'attente: ", end="")
    for client in waiting_list:
        liste += "{ user: "+str(client[2]) + ", callType: " + str(client[4]) + "}, "

    return liste


#fonction check_demande qui vérifie si une demande est présente dans la table waiting_line
def check_demand(client, sessionId):
    global ipBdd
    global portBdd
    global userBdd
    global passwordBdd
    global bddName
    # Créer une instance de la classe DatabaseConnection
    db = DatabaseConnection(ipBdd, portBdd, bddName, userBdd, passwordBdd)

    # Établir la connexion à la base de données
    db.connect()

    # Vérifie si une demande est présente dans la table waiting_line
    demand = db.show_wait(client.idClient, sessionId)
    # fermes la connexion à la base de données
    db.disconnect()
    # Si une demande est présente, on retourne True
    if demand != None:
        if len(demand) > 0:
            # get the superclass of userid
            if (demand[0][4] == 0):
                client.state = "question pending"
            elif (demand[0][4] == 1):
                client.state = "verify pending"
            else:
                client.state = "error"
            print("client.state: " + client.state)
            return True
        else:
            client.state = "free"
            print("client.state: " + client.state)
            return False
    else:
        client.state = "free"
        print("client.state: " + client.state)
        return False


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.state = None
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
        r_demand = check_demand(self, num_session)

        # écoute les messages du client et les affiche
        while True:
            r = self.clientsocket.recv(2048)
            print("Client "+self.idClient+" :", r.decode())
            # check_demand()
            r_demand = check_demand(self, num_session)

            # Si la réponse est "/call" alors on affiche "Appel en cours"
            if r.decode() == "/ask":
                print("Appel pour une question")
                if self.state == "free":
                    self.clientsocket.send("Question envoyée".encode())
                    db.ask(self.idClient, num_session)
                else:
                    self.clientsocket.send("ERREUR: Vous avez déjà une demande en cours".encode())
            elif r.decode() == "/verify":
                print("Appel pour une vérification")
                if self.state == "free":
                    self.clientsocket.send("Vérification envoyée".encode())
                    db.verify(self.idClient, num_session)
                else:
                    self.clientsocket.send("ERREUR: Vous avez déjà une demande en cours".encode())
            elif r.decode() == "/cancel":
                print("Annule l'appel")
                if self.state == "question pending":
                    self.clientsocket.send("Question annulée".encode())
                    db.cancel(self.idClient, num_session)
                elif self.state == "verify pending":
                    self.clientsocket.send("Vérification annulée".encode())
                    db.cancel(self.idClient, num_session)
                else:
                    self.clientsocket.send("ERREUR: Vous n'avez pas de demande en cours".encode())
            elif r.decode() == "/leave":
                print("Connexion terminée")
                self.clientsocket.close()
                # supprime le numéro d'identification du client de la liste des threads
                threads.remove(self.idClient)
                # affiche la liste des threads
                print_threads()
                break
            elif r.decode() == "/list":
                print("Liste d'attente")
                waiting_list = get_waiting_list()
                self.clientsocket.send(waiting_list.encode())
            else:
                self.clientsocket.send("ERREUR: Commande inconnue".encode())


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

# crée un tableau de threads
threads = []


#Paramétrage de la base de données:
ipBdd = input("Entrez l'adresse IP de la base de données: (localhost par défaut) ")
if ipBdd == "":
    ipBdd = "localhost"
portBdd = input("Entrez le port de la base de données: (3306 par défaut) ")
if portBdd == "":
    portBdd = 3306
else:
    portBdd = int(portBdd)
userBdd = input("Entrez le nom d'utilisateur de la base de données: (root par défaut) ")
if userBdd == "":
    userBdd = "root"
passwordBdd = input("Entrez le mot de passe de la base de données: (vide par défaut) ")
if passwordBdd == "":
    passwordBdd = ""
nomBdd = input("Entrez le nom de la base de données: (cmm par défaut) ")
if nomBdd == "":
    nomBdd = "cmm"


while True:
    # Créer une instance de la classe DatabaseConnection
    db = DatabaseConnection(ipBdd, portBdd, nomBdd, userBdd, passwordBdd)

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


