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

    def cancel(self, userid, sessionId):
        self.cursor.execute("UPDATE `waiting_line` SET processing = 1 WHERE user_id = %s and session_id = %s", (userid, sessionId))
        self.cnx.commit()
        return True

    def ask(self, userid, sessionId):
        # exemple: INSERT INTO `waiting_line` (`id_waiting`, `session_id`, `user_id`, `waiting_time`, `call_type`, `processing`, `rate`, `solved_date`, `comment`) VALUES (NULL, '4', '11', CURRENT_TIMESTAMP, '0', '0', NULL, NULL, NULL);
        self.cursor.execute("INSERT INTO `waiting_line` (`id_waiting`, `session_id`, `user_id`, `waiting_time`, `call_type`, `processing`, `rate`, `solved_date`, `comment`) VALUES (NULL, %s, %s, CURRENT_TIMESTAMP, '0', '0', NULL, NULL, NULL)", (sessionId, userid))
        self.cnx.commit()
        return True

    def verify(self, userid, sessionId):
        # exemple: INSERT INTO `waiting_line` (`id_waiting`, `session_id`, `user_id`, `waiting_time`, `call_type`, `processing`, `rate`, `solved_date`, `comment`) VALUES (NULL, '4', '11', CURRENT_TIMESTAMP, '1', '0', NULL, NULL, NULL);
        self.cursor.execute("INSERT INTO `waiting_line` (`id_waiting`, `session_id`, `user_id`, `waiting_time`, `call_type`, `processing`, `rate`, `solved_date`, `comment`) VALUES (NULL, %s, %s, CURRENT_TIMESTAMP, '1', '0', NULL, NULL, NULL)", (sessionId, userid))
        self.cnx.commit()
        return True

    def show_waitingline(self, sessionId):
        self.cursor.execute("SELECT * FROM `waiting_line` where session_id = %s and processing = 0 ORDER BY waiting_time", (sessionId,) )
        rows = self.cursor.fetchall()
        return rows

