# client.py
import socket

HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 9000      # Port d'écoute du serveur

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Bonjour serveur !')
    data = s.recv(1024)

print('Reçu du serveur:', repr(data))