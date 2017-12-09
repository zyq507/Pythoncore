from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class Echo(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,)
        )

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)


class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.quote + "\r\n")
        self.transport.loseconnection()


class QOTDFactory(Factory):

    protocol = QOTD

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'

    def buildProtocol(self, addr):
        return QOTD()


class Answer(LineReceiver):
    answers = {'How are you?': 'Fine', None: "I don't know what do you mean"}

    def lineReceived(self, line):
        if line in self.answers:
            self.sendLine(self.answers[line])
        else:
            self.sendLine(self.answers[None])


if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(QOTDFactory("configurable quote"))
    reactor.run()

