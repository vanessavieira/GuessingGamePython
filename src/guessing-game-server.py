import random
from socket import *
import threading
import time

numone = 0
numtwo = 100

running = True

# Set up the socket
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('localhost', 4000))
serversocket.listen(5)

players = []

# Generate a random number for the client to try and guess
numbertoguess = random.randrange(0, 100)

# Function definitions
def run():
    global numone, numtwo, running
    turnindex = 0

    # Main loop
    while running:
        clientsocket = players[turnindex]

        guessmessage = "play "+ str(numone) + " " + str(numtwo)
        clientsocket.send(guessmessage.encode('ascii'))
        time.sleep(0.1)

        guess = clientsocket.recv(1024).decode('ascii')

        answerisright, numone, numtwo = check(numone, numtwo, int(guess), numbertoguess)

        if (answerisright):
            messagetosend = ("Correct\r\n")
            clientsocket.send(messagetosend.encode('ascii'))
            time.sleep(0.1)
            running = False
            break
        else:
            messagetosend = ("server: you're safe now, but be careful\r\n")
            clientsocket.send(messagetosend.encode('ascii'))
            time.sleep(0.1)
            running = True

        turnindex = (turnindex + 1) % (len(players))


    for clientsocket in players:
        clientsocket.close()
        print("Connection closed.")


def check(numone, numtwo, guess, numtoguess):
    answerisright = False
    if (guess >= numtwo or guess <= numone):
        print("try again")
    elif (guess < numtwo and guess > numone):
        if (guess == numtoguess):
            answerisright = True
        elif (guess > numtoguess):
            numtwo = guess
        elif (guess < numtoguess):
            numone = guess

    return answerisright,numone, numtwo


# Main server loop
while 1:
    (clientsocket, clientaddress) = serversocket.accept()

    players.append(clientsocket)

    threading.Thread(target=run).start()

    print("server: Connection passed to new thread. Returning to listening.")
