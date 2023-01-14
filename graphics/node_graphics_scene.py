import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class NodeGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene

        # Settings
        self.gridSize = 20
        self.gridSquares = 5

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        self._color_dark = QColor("#292929")

        self._pen_Light = QPen(self._color_light)
        self._pen_Light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.setBackgroundBrush(self._color_background)

    def setGraphicsScene(self, width, height):
        self.setSceneRect(
            -width // 2, -height // 2,
            width, height
        )

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # Grid creation
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        # Compute lines to be draw
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.gridSize):
            if x % (self.gridSize * self.gridSquares) != 0:
                lines_light.append(
                    QLine(x, top, x, bottom)
                )
            else:
                lines_dark.append(
                    QLine(x, top, x, bottom)
                )
        for y in range(first_top, bottom, self.gridSize):
            if y % (self.gridSize * self.gridSquares) != 0:
                lines_light.append(
                    QLine(left, y, right, y)
                )
            else:
                lines_dark.append(
                    QLine(left, y, right, y)
                )

        # Draw lines
        painter.setPen(self._pen_Light)
        painter.drawLines(lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(lines_dark)
