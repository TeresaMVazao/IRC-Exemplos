# udp-client.py
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SERVER_BUFFER_SIZE = 100

client_msg = " Hello world"

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_sock.sendto(client_msg, (UDP_IP, UDP_PORT))
print "Message to server: ", client_msg
(server_msg, (server_ipxs, server_port)) = client_sock.recvfrom (SERVER_BUFFER_SIZE)
print "Message from server: ", server_msg

client_sock.close()
