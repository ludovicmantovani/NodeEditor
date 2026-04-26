import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar
from PyQt5.QtCore import Qt
from node_editor_widget import NodeEditorWidget

class TempMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.showMaximized()


    def initUI(self):
        self.setWindowTitle("Node Editor")

        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.addAction("Open")
        self.toolbar.addAction("Save")
        self.toolbar.addAction("Save As")
        self.toolbar.addSeparator()
        self.toolbar.addAction("Undo")
        self.toolbar.addAction("Redo")
        self.toolbar.addSeparator()
        self.toolbar.addAction("Cut")
        self.toolbar.addAction("Copy")
        self.toolbar.addAction("Paste")

        self.setStatusBar(QStatusBar())

        self.ne = NodeEditorWidget()
        self.setCentralWidget(self.ne)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # ne_widget = NodeEditorWidget()
    main_window = TempMainWindow()

    sys.exit(app.exec_())
