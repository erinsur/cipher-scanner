import socket
import ssl
import sys

if len(sys.argv) < 2:
    print("Usage: cipher-scanner.py <website name> ")
    sys.exit(1)
website = sys.argv[1]

# list of ciphers
ciphers = ['TLS_AES_128_GCM_SHA256',
           'TLS_AES_256_GCM_SHA384',
           'TLS_CHACHA20_POLY1305_SHA256',
           'ECDHE-RSA-AES128-GCM-SHA256', 
           'ECDHE-ECDSA-CHACHA20-POLY1305',
           'TLS_RSA_WITH_AES_128_CBC_SHA']

# context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_default_certs()    

for cipher in ciphers:
    
    try:
        context.set_ciphers(cipher)
        # tcp connection (AF_INET -> IPV4 and SOCK_STREAM -> TCP)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((website, 443)) 

        tls_socket = context.wrap_socket(client_socket, server_hostname=website)

        print(cipher + ": TLS connection established!")
    except Exception as e:
        print(cipher + ": Not able to connect")



