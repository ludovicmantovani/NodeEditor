from node_content_widget import NodeContentWidget
from node_graphics_node import NodeGraphicsNode


class Node():
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene

        self.title = title
        self.content = NodeContentWidget()
        self.grNode = NodeGraphicsNode(self)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.inputs = []
        self.outputs = []