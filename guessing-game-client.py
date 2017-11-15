from socket import *
import time

print ("Number Guessing Game V1.0\n\n")
print ("Connecting to server...\n")

# Set up the socket as an Internet facing streaming socket
clientsocket = socket(AF_INET, SOCK_STREAM)
# Connect to the server on port 4000
try:
    clientsocket.connect(('localhost', 4000))
except ConnectionRefusedError:
    print ("client:The connection was refused.")
    exit(0)
print("client:connected!\n")

running = True

while running:

    guessrange = clientsocket.recv(1024)
    response = guessrange.decode('ascii')

    if response == "Correct\r\n":
        print('You loose, you drink.')
        running = False
        break
    elif "server" not in response:
        print("response: "+response)
        # Ask for user to guess a number
        if response != "Correct\r\n" and response != "":
            guess = input("client: enter your guess: ")
        # Format the guess, ready to send to the server
            guessstring = str(guess)
        # Send the guess
            clientsocket.send(guessstring.encode('ascii'))
            time.sleep(0.1)
        elif response == "":
            print("Another player has lost, lucky you!")
            break
        else:
            break

    else:
        print('wait for your turn')

    #time.sleep(5)


clientsocket.close()