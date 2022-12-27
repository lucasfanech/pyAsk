import mysql.connector

class DatabaseConnection:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(
                "Impossible de se connecter à la base de données. Vérifiez que le serveur MySQL est en cours d'exécution et que les informations de connexion sont correctes. Erreur:",
                e)
            exit(1)

    def disconnect(self):
        self.cursor.close()
        self.cnx.close()

    def detect_game(self):
        self.cursor.execute("SELECT id_session FROM `sessions` where active = 1")
        rows = self.cursor.fetchall()
        return rows

    def show_wait(self, userid, sessionId):
        self.cursor.execute("SELECT * FROM `waiting_line` where user_id = %s and session_id = %s and processing = 0", (userid, sessionId))
        rows = self.cursor.fetchall()
        return rows
