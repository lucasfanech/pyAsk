# serveur.py
import socket

HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 9000        # Port d'écoute du serveur

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connecté par', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
