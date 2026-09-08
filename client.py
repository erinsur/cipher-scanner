import socket
import ssl

# context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_default_certs()

# tcp connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("example.com", 443)) 


tls_socket = context.wrap_socket(client_socket, server_hostname="example.com")

print("TLS connection established!")
print(tls_socket.cipher())


