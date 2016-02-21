# udp-server.py
import socket

UDP_PORT = 5005
ANY_ADDR = ""
SERVER_BUFFER_SIZE = 100
server_msg = "Nice to meet you :) "

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_sock.bind((ANY_ADDR, UDP_PORT))

(client_msg, (client_ip, client_port)) = server_sock.recvfrom (SERVER_BUFFER_SIZE)
server_sock.sendto(server_msg, (client_ip, client_port)) 

server_sock.close()
