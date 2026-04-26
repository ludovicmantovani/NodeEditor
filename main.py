import sys

from PyQt5.QtWidgets import *
from node_editor_widget import NodeEditorWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ne_widget = NodeEditorWidget()

    sys.exit(app.exec_())
