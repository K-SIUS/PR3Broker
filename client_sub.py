import socket
import sys
import select
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

broker_address = ('localhost', 10000)
port = 10001
messageA = b'sub:id:%i'%port
messageB = b'sub:topic:game'

available = False



try:
    # Send data
    print('sending {!r}'.format(messageA))
    sent = sock.sendto(messageA, broker_address)
    print('sending {!r}'.format(messageB))
    sent = sock.sendto(messageB, broker_address)
finally:
    print('closing socket')
    sock.close()

#habrá que comprobar que el puerto esté libre

# Bind the socket to the port
while available == False:
    #con if y else no funciona, el error se genera igual y salta 
    #la ejecución. Por lo tanto he optado por meterlo en try catch
    # y en caso de que salte el error de socket, tratarlo
    #como un error de conexión por puerto ocupado, e incrementar su 
    #valor. 
    #de esta manera la programación no consiste en evitar el error
    #sino reaccionar a él. (Probablemente haya mejores soluciones)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', port)
        print('starting up on {} port {}'.format(*server_address))
        sock.bind(server_address)
        available = True
    except socket.error:
        print("unable to conect, trying with new port: ")
        port = port+ 1



while True:
    print('\nwaiting to receive message')
    rlist, _, _ = select.select([sock], [], []) 
    data, address = sock.recvfrom(1024)
    # Do stuff with data, fill this up with your code
    print('received {} bytes from {}'.format(len(data), address))
    print(data)
 

