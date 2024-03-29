from node_content_widget import NodeContentWidget
from graphics.node_graphics_node import NodeGraphicsNode
from node_socket import *


class Node:
    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[]):
        self.socket_spacing = 22
        self.scene = scene

        self.title = title
        self.content = NodeContentWidget()
        self.grNode = NodeGraphicsNode(self)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_BOTTOM, socket_type=item)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=RIGHT_TOP, socket_type=item)
            counter += 1
            self.outputs.append(socket)

    def __str__(self):
        return "<Node {}..{}>".format(
            hex(id(self))[2:5],
            hex(id(self))[-3:]
        )

    @property
    def pos(self):
        return self.grNode.pos()

    def setPosition(self, x, y):
        self.grNode.setPos(x, y)

    def getSocketPosition(self, index, position):
        if position in (LEFT_TOP, LEFT_BOTTOM):
            x = 0
        else:
            x = self.grNode.width
        if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
            # start from bottom
            y = self.grNode.height - self.grNode.edge_size - self.grNode._padding - index * self.socket_spacing
        else:
            # start from top
            y = self.grNode.title_height + self.grNode._padding + self.grNode.edge_size + index * self.socket_spacing
        return [x, y]

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                socket.edge.updatePositions()
