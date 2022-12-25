import mysql.connector

class DatabaseConnection:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.cnx.cursor()

    def disconnect(self):
        self.cursor.close()
        self.cnx.close()

    def detect_game(self):
        self.cursor.execute("SELECT id_session FROM `sessions` where active = 1")
        rows = self.cursor.fetchall()
        return rows

    def show_wait(self, userid, sessionId):
        self.cursor.execute("SELECT * FROM `waiting_line` where user_id = %s and session_id = %s and processing = 1", (userid, sessionId))
        rows = self.cursor.fetchall()
        return rows
