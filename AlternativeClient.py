from twisted.application.service import Application, Service
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.internet.protocol import DatagramProtocol

SERVER_IP = '127.0.0.1'; SERVER_PORT = 43278; BEAT_PERIOD = 5

class HeartbeatClient(Service):
    def startService(self):
        self._call = LoopingCall(self._heartbeat)
        self._call.start(BEAT_PERIOD)

    def stopService(self):
        self._call.stop()

    def _heartbeat(self):
        port = reactor.listenUDP(0, DatagramProtocol())
        port.write('PyHB', (SERVER_IP, SERVER_PORT))
        port.stopListening()

application = Application("PyHB")
HeartbeatClient().setServiceParent(application)