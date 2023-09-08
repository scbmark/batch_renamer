# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName("AboutWindow")
        AboutWindow.setWindowModality(Qt.ApplicationModal)
        AboutWindow.resize(400, 600)
        icon = QIcon()
        icon.addFile(":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AboutWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.logo_lb = QLabel(AboutWindow)
        self.logo_lb.setObjectName("logo_lb")
        self.logo_lb.setPixmap(QPixmap(":/statics/icon.ico"))

        self.horizontalLayout.addWidget(self.logo_lb)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.app_name_lb = QLabel(AboutWindow)
        self.app_name_lb.setObjectName("app_name_lb")
        font = QFont()
        font.setPointSize(14)
        self.app_name_lb.setFont(font)
        self.app_name_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.app_name_lb)

        self.version_lb = QLabel(AboutWindow)
        self.version_lb.setObjectName("version_lb")
        self.version_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.version_lb)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(AboutWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.about = QWidget()
        self.about.setObjectName("about")
        self.gridLayout_2 = QGridLayout(self.about)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sofware_info_lb = QLabel(self.about)
        self.sofware_info_lb.setObjectName("sofware_info_lb")
        font1 = QFont()
        font1.setPointSize(12)
        self.sofware_info_lb.setFont(font1)
        self.sofware_info_lb.setTextFormat(Qt.AutoText)
        self.sofware_info_lb.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.sofware_info_lb)

        self.package_lb = QLabel(self.about)
        self.package_lb.setObjectName("package_lb")
        self.package_lb.setFont(font1)
        self.package_lb.setTextFormat(Qt.MarkdownText)
        self.package_lb.setWordWrap(True)
        self.package_lb.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.package_lb)

        self.license_lb = QLabel(self.about)
        self.license_lb.setObjectName("license_lb")
        self.license_lb.setFont(font1)

        self.verticalLayout_3.addWidget(self.license_lb)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.about, "")
        self.author = QWidget()
        self.author.setObjectName("author")
        self.gridLayout_3 = QGridLayout(self.author)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QLabel(self.author)
        self.label.setObjectName("label")
        self.label.setFont(font1)
        self.label.setMouseTracking(True)
        self.label.setTextFormat(Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.author)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 5)

        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.author, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.exit_btn = QPushButton(AboutWindow)
        self.exit_btn.setObjectName("exit_btn")

        self.horizontalLayout_2.addWidget(self.exit_btn)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(AboutWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(AboutWindow)

    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(
            QCoreApplication.translate("AboutWindow", "\u95dc\u65bc Batch Renamer", None)
        )
        self.logo_lb.setText("")
        self.app_name_lb.setText(QCoreApplication.translate("AboutWindow", "Batch Renamer", None))
        self.version_lb.setText(QCoreApplication.translate("AboutWindow", "Version: ", None))
        self.sofware_info_lb.setText(
            QCoreApplication.translate(
                "AboutWindow",
                "\u8edf\u9ad4\u8aaa\u660e\uff1a\u6a94\u6848\u6279\u91cf\u91cd\u65b0\u547d\u540d\u3002",
                None,
            )
        )
        self.package_lb.setText(
            QCoreApplication.translate(
                "AboutWindow",
                '<html><head/><body><p>\u958b\u767c\uff1a\u6b64\u7a0b\u5f0f\u4ee5 <a href="https://www.python.org/"><span style=" text-decoration: underline; color:#1d99f3;">Python 3.11.5</span></a> \u958b\u767c\uff0c\u5716\u5f62\u4ecb\u9762\u57fa\u65bc <a href="https://doc.qt.io/qtforpython-6/index.html"><span style=" text-decoration: underline; color:#1d99f3;">PySide6</span></a>\u3002</p></body></html>',
                None,
            )
        )
        self.license_lb.setText(
            QCoreApplication.translate("AboutWindow", "\u6388\u6b0a\u689d\u6b3e\uff1aGPL v3", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.about),
            QCoreApplication.translate("AboutWindow", "\u95dc\u65bc", None),
        )
        self.label.setText(
            QCoreApplication.translate(
                "AboutWindow",
                "<html><head/><body><p>Bug \u56de\u5831\uff1a\u8acb\u81f3 Github \u5132\u5b58\u5eab\u56de\u5831\u6216\u4ee5 Email \u901a\u77e5\u4f5c\u8005 \u3002</p></body></html>",
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "AboutWindow",
                '<html><head/><body><p>\u4f5c\u8005\uff1aMark Hsiao</p><p>\u96fb\u5b50\u90f5\u4ef6\uff1aTwilight3847@skiff.com</p><p>Github\uff1a<a href="https://github.com/scbmark/batch_renamer"><span style=" text-decoration: underline; color:#1d99f3;">https://github.com/scbmark/batch_renamer</span></a></p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.author),
            QCoreApplication.translate("AboutWindow", "\u4f5c\u8005", None),
        )
        self.exit_btn.setText(QCoreApplication.translate("AboutWindow", "\u95dc\u9589", None))

    # retranslateUi
