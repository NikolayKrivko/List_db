from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.base_qt_ui.ui_coordwidget import Ui_CoordWidget


class CoordWidget(QWidget):
    def __init__(self, id_widget: int, parent=None):
        super(CoordWidget, self).__init__(parent)
        self.ui = Ui_CoordWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.groupBox.setTitle(str(id_widget))
