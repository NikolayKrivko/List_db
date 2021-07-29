from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import res_rc


class Ui_CoordWidget(object):
    def setupUi(self, CoordWidget):
        if not CoordWidget.objectName():
            CoordWidget.setObjectName(u"CoordWidget")
        CoordWidget.resize(302, 61)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            CoordWidget.sizePolicy().hasHeightForWidth())
        CoordWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        CoordWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(CoordWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CoordWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(CoordWidget)

        QMetaObject.connectSlotsByName(CoordWidget)
    # setupUi

    def retranslateUi(self, CoordWidget):
        CoordWidget.setWindowTitle(
            QCoreApplication.translate("CoordWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate(
            "CoordWidget", u"Name", None))
        self.label_2.setText(QCoreApplication.translate(
            "CoordWidget", u"Surname", None))
    # retranslateUi
