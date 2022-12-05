from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        # decodes datagram from bytes to string
        datagram = datagram.decode('utf-8')
        if datagram == "ready":
            addresses = "\n".join([str[x] for x in self.clients])
            # the next line does -> [a,b,c,d] ---> "a/nb/nc/nd/n" (as a string)
            self.transport.write(addresses.encode('utf-8'), addr)
            self.clients.add(addr)


if __name__ == '__main__':
    reactor.listenUDP(8888, Server())
    reactor.run()