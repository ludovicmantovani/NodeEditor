from graphics.node_graphics_socket import GraphicsSocket

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4

SOCKET_TYPE_INPUT = 0
SOCKET_TYPE_OUTPUT = 1

class Socket:
    def __init__(self, node, index=0, position=LEFT_TOP, socket_type=SOCKET_TYPE_OUTPUT):
        self.position = position
        self.index = index
        self.node = node
        self.socket_type = socket_type

        self.grSocket = GraphicsSocket(self, self.socket_type)

        self.grSocket.setPos(
            *self.node.getSocketPosition(
                self.index,
                self.position
            )
        )

        self.edge = None

    def __str__(self):
        return "<Socket {}..{}>".format(
            hex(id(self))[2:5],
            hex(id(self))[-3:]
        )

    def getSocketPosition(self):
        return self.node.getSocketPosition(self.index, self.position)

    def setConnectedEdge(self, edge=None):
        self.edge = edge

    def hasEdge(self):
        return self.edge is not None
