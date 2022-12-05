from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == "localhost":
            host = "127.0.0.1"

        self.id = host, port
        self.address = None
        self.server = '127.0.0.1', 8888
        print(f"Working ID : {self.id}")


    def startProtocol(self):
        # when protocol start - write ready
        self.transport.write("ready".encode('utf-8'), self.server)


    def datagramRecieved(self, datagram, addr):
        if addr == self.server:
            datagram = datagram.decode('utf-8')
            print(f"Choose a client from \n {datagram}")
            self.address = input('Write host:'), int(input('Write port:'))
            reactor.callInThread(self.sendmessage)

        else:
            # print the addr (from where the data came) AND the data itself
            print(f"{addr} , : , {datagram}")

    def sendmessage(self):
        # send message to the address
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)


if __name__ == "__main__":
    port = randint(1000, 5000)
    # listen on "port" provided and the client is the listener
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()

