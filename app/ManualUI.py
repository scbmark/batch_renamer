# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
    QUrl,
)
from PySide6.QtGui import (
    QFont,
    QIcon,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTextBrowser,
)


class Ui_ManualWindow(object):
    def setupUi(self, ManualWindow):
        if not ManualWindow.objectName():
            ManualWindow.setObjectName("ManualWindow")
        ManualWindow.setWindowModality(Qt.ApplicationModal)
        ManualWindow.resize(502, 505)
        icon = QIcon()
        icon.addFile(":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        ManualWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ManualWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exit_btn = QPushButton(ManualWindow)
        self.exit_btn.setObjectName("exit_btn")

        self.horizontalLayout.addWidget(self.exit_btn)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.textBrowser = QTextBrowser(ManualWindow)
        self.textBrowser.setObjectName("textBrowser")
        font = QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setSource(QUrl("qrc:/manual.md"))

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(ManualWindow)

        QMetaObject.connectSlotsByName(ManualWindow)

    # setupUi

    def retranslateUi(self, ManualWindow):
        ManualWindow.setWindowTitle(
            QCoreApplication.translate("ManualWindow", "\u4f7f\u7528\u8aaa\u660e", None)
        )
        self.exit_btn.setText(QCoreApplication.translate("ManualWindow", "\u96e2\u958b", None))

    # retranslateUi
