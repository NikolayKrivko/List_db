from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from ui.base_qt_ui.ui_mainwindow import Ui_MainWindow
from ui.coordwidget import CoordWidget
from ui.flowlayout import FlowLayout

from db import Database

db = Database('ww.db')


class MainWindow(QMainWindow):
    # def list():
    #     for row in db.fetch():
    #         flowlayout = FlowLayout()
    #         CoordWidget.addLayout(flowlayout)
    #         coord_widget = CoordWidget(row[0])
    #         flowlayout.addWidget(coord_widget)
    #         CoordWidget.label.setText(row[1])
    #         CoordWidget.label_2.setText(row[2])

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0

        self.flowlayout = FlowLayout()
        self.ui.coordwidget_layout.addLayout(self.flowlayout)
        self.ui.add_pushbutton.clicked.connect(self.add_coordwidget)

        # self.list()

    @Slot()
    def add_coordwidget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id)
        self.flowlayout.addWidget(coord_widget)
        coord_widget.delete.connect(self.delete_coordwidget)
