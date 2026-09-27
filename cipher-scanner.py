
import socket
import ssl
import sys

if len(sys.argv) < 2:
    print("Usage: cipher-scanner.py <website name> ")
    sys.exit(1)
website = sys.argv[1]

print(f"\nCipher Scanning initiated for {website}\n")

# list of ciphers 1.2
ciphers = [
           'ECDHE-RSA-AES128-GCM-SHA256', 
           'ECDHE-ECDSA-CHACHA20-POLY1305',
           'DES-CBC3-SHA']

# context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_default_certs()  
context.maximum_version = ssl.TLSVersion.TLSv1_2


for cipher in ciphers:
    client_socket = None
    try:
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.set_ciphers(f'{cipher}:@SECLEVEL=0')  
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((website, 443)) 

        tls_socket = context.wrap_socket(client_socket, server_hostname=website)

        print(cipher + ": TLS connection established!")
    except ssl.SSLError as e:
        print(f"{cipher}: Rejected by server ({e})")
    except OSError as e:
        print(f"{cipher}: Connection error ({e})")
    finally:
        if client_socket:
            try:
                client_socket.close()
            except OSError:
                    pass

