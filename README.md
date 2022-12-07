# pyAsk
#Le client :
-	GUI pour se connecter au serveur :
o	IP / PORT
o	Numéro de table
-	Si connexion réussie :
o	Affichage d’un nouveau GUI avec 3 boutons :
 - Question -> Demande pour une question
 - Validation -> Demande pour une validation
 - Annulation -> Annule la demande
Remarque : Le serveur envoie une réponse lors de la connexion et lors d’un clic sur un bouton afin de mettre à jour l’état des boutons.
Etat des boutons : 
Par défaut aucun bouton n’est sélectionné,
Question ou Validation cliqué, les boutons sont bloqués, seul le bouton annulation est activable

#Le serveur :
-	Gère les threads clients
-	Lorsqu’un client clique, il reçoit une demande et interroge la BDD
-	Fonction CheckDemand : Vérifie si une demande est déjà en cours ou non
-	Fonction SetState : Change l’etat des boutons du client
-	Fonction SendInBDD : Envoie l’info à la bdd
-	Retour au client

