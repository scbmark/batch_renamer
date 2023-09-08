# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from .CustomWidgets import DropListWidget, RuleListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        icon = QIcon()
        icon.addFile(":/statics/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_info_about = QAction(MainWindow)
        self.menu_info_about.setObjectName("menu_info_about")
        self.menu_info_update = QAction(MainWindow)
        self.menu_info_update.setObjectName("menu_info_update")
        self.menu_info_manual = QAction(MainWindow)
        self.menu_info_manual.setObjectName("menu_info_manual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_new_files_btn = QPushButton(self.centralwidget)
        self.add_new_files_btn.setObjectName("add_new_files_btn")

        self.horizontalLayout_3.addWidget(self.add_new_files_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.start_rename_btn = QPushButton(self.centralwidget)
        self.start_rename_btn.setObjectName("start_rename_btn")

        self.horizontalLayout_3.addWidget(self.start_rename_btn)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_rule_lb = QLabel(self.centralwidget)
        self.add_rule_lb.setObjectName("add_rule_lb")
        self.add_rule_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.add_rule_lb)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.replace = QWidget()
        self.replace.setObjectName("replace")
        self.gridLayout_3 = QGridLayout(self.replace)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.replace_old_str_lb = QLabel(self.replace)
        self.replace_old_str_lb.setObjectName("replace_old_str_lb")

        self.horizontalLayout_5.addWidget(self.replace_old_str_lb)

        self.replace_old_str_box = QLineEdit(self.replace)
        self.replace_old_str_box.setObjectName("replace_old_str_box")

        self.horizontalLayout_5.addWidget(self.replace_old_str_box)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.replace_new_str_lb = QLabel(self.replace)
        self.replace_new_str_lb.setObjectName("replace_new_str_lb")

        self.horizontalLayout_6.addWidget(self.replace_new_str_lb)

        self.replace_new_str_box = QLineEdit(self.replace)
        self.replace_new_str_box.setObjectName("replace_new_str_box")

        self.horizontalLayout_6.addWidget(self.replace_new_str_box)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.replace_add_btn = QPushButton(self.replace)
        self.replace_add_btn.setObjectName("replace_add_btn")
        icon1 = QIcon()
        icon1.addFile(":/statics/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.replace_add_btn.setIcon(icon1)
        self.replace_add_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_8.addWidget(self.replace_add_btn)

        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.replace, "")
        self.remove = QWidget()
        self.remove.setObjectName("remove")
        self.gridLayout_2 = QGridLayout(self.remove)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.remove_str_lb = QLabel(self.remove)
        self.remove_str_lb.setObjectName("remove_str_lb")

        self.horizontalLayout_4.addWidget(self.remove_str_lb)

        self.remove_str_box = QLineEdit(self.remove)
        self.remove_str_box.setObjectName("remove_str_box")

        self.horizontalLayout_4.addWidget(self.remove_str_box)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.remove_add_btn = QPushButton(self.remove)
        self.remove_add_btn.setObjectName("remove_add_btn")

        self.verticalLayout_7.addWidget(self.remove_add_btn)

        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.remove, "")
        self.strip = QWidget()
        self.strip.setObjectName("strip")
        self.gridLayout_7 = QGridLayout(self.strip)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.strip_str_lb = QLabel(self.strip)
        self.strip_str_lb.setObjectName("strip_str_lb")

        self.horizontalLayout_12.addWidget(self.strip_str_lb)

        self.strip_str_box = QLineEdit(self.strip)
        self.strip_str_box.setObjectName("strip_str_box")

        self.horizontalLayout_12.addWidget(self.strip_str_box)

        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.strip_space_box = QCheckBox(self.strip)
        self.strip_space_box.setObjectName("strip_space_box")

        self.horizontalLayout_13.addWidget(self.strip_space_box)

        self.strip_eng_box = QCheckBox(self.strip)
        self.strip_eng_box.setObjectName("strip_eng_box")

        self.horizontalLayout_13.addWidget(self.strip_eng_box)

        self.strip_num_box = QCheckBox(self.strip)
        self.strip_num_box.setObjectName("strip_num_box")

        self.horizontalLayout_13.addWidget(self.strip_num_box)

        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.strip_add_btn = QPushButton(self.strip)
        self.strip_add_btn.setObjectName("strip_add_btn")

        self.verticalLayout_12.addWidget(self.strip_add_btn)

        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.strip, "")
        self.delete = QWidget()
        self.delete.setObjectName("delete")
        self.gridLayout_8 = QGridLayout(self.delete)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.delete_start_lb = QLabel(self.delete)
        self.delete_start_lb.setObjectName("delete_start_lb")

        self.horizontalLayout_14.addWidget(self.delete_start_lb)

        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.delete_start_position_rtn = QRadioButton(self.delete)
        self.delete_start_mode_group = QButtonGroup(MainWindow)
        self.delete_start_mode_group.setObjectName("delete_start_mode_group")
        self.delete_start_mode_group.addButton(self.delete_start_position_rtn)
        self.delete_start_position_rtn.setObjectName("delete_start_position_rtn")
        self.delete_start_position_rtn.setChecked(True)

        self.horizontalLayout_19.addWidget(self.delete_start_position_rtn)

        self.delete_start_position_box = QSpinBox(self.delete)
        self.delete_start_position_box.setObjectName("delete_start_position_box")
        self.delete_start_position_box.setMinimum(-99)

        self.horizontalLayout_19.addWidget(self.delete_start_position_box)

        self.delete_start_str_rtn = QRadioButton(self.delete)
        self.delete_start_mode_group.addButton(self.delete_start_str_rtn)
        self.delete_start_str_rtn.setObjectName("delete_start_str_rtn")

        self.horizontalLayout_19.addWidget(self.delete_start_str_rtn)

        self.delete_start_str_box = QLineEdit(self.delete)
        self.delete_start_str_box.setObjectName("delete_start_str_box")
        self.delete_start_str_box.setEnabled(False)

        self.horizontalLayout_19.addWidget(self.delete_start_str_box)

        self.verticalLayout_13.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.delete_end_lb = QLabel(self.delete)
        self.delete_end_lb.setObjectName("delete_end_lb")

        self.horizontalLayout_15.addWidget(self.delete_end_lb)

        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 0, 0)
        self.delete_end_position_rtn = QRadioButton(self.delete)
        self.delete_end_mode_group = QButtonGroup(MainWindow)
        self.delete_end_mode_group.setObjectName("delete_end_mode_group")
        self.delete_end_mode_group.addButton(self.delete_end_position_rtn)
        self.delete_end_position_rtn.setObjectName("delete_end_position_rtn")
        self.delete_end_position_rtn.setChecked(True)

        self.horizontalLayout_20.addWidget(self.delete_end_position_rtn)

        self.delete_end_position_box = QSpinBox(self.delete)
        self.delete_end_position_box.setObjectName("delete_end_position_box")
        self.delete_end_position_box.setMinimum(-99)
        self.delete_end_position_box.setValue(-1)

        self.horizontalLayout_20.addWidget(self.delete_end_position_box)

        self.delete_end_str_rtn = QRadioButton(self.delete)
        self.delete_end_mode_group.addButton(self.delete_end_str_rtn)
        self.delete_end_str_rtn.setObjectName("delete_end_str_rtn")

        self.horizontalLayout_20.addWidget(self.delete_end_str_rtn)

        self.delete_end_str_box = QLineEdit(self.delete)
        self.delete_end_str_box.setObjectName("delete_end_str_box")
        self.delete_end_str_box.setEnabled(False)

        self.horizontalLayout_20.addWidget(self.delete_end_str_box)

        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_7)

        self.delete_add_btn = QPushButton(self.delete)
        self.delete_add_btn.setObjectName("delete_add_btn")

        self.verticalLayout_13.addWidget(self.delete_add_btn)

        self.gridLayout_8.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.delete, "")
        self.insert = QWidget()
        self.insert.setObjectName("insert")
        self.gridLayout_4 = QGridLayout(self.insert)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.insert_str_lb = QLabel(self.insert)
        self.insert_str_lb.setObjectName("insert_str_lb")

        self.horizontalLayout_7.addWidget(self.insert_str_lb)

        self.insert_str_box = QLineEdit(self.insert)
        self.insert_str_box.setObjectName("insert_str_box")

        self.horizontalLayout_7.addWidget(self.insert_str_box)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.insert_position_lb = QLabel(self.insert)
        self.insert_position_lb.setObjectName("insert_position_lb")

        self.horizontalLayout_8.addWidget(self.insert_position_lb)

        self.insert_position_box = QSpinBox(self.insert)
        self.insert_position_box.setObjectName("insert_position_box")
        self.insert_position_box.setMinimum(-99)

        self.horizontalLayout_8.addWidget(self.insert_position_box)

        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.insert_add_btn = QPushButton(self.insert)
        self.insert_add_btn.setObjectName("insert_add_btn")

        self.verticalLayout_9.addWidget(self.insert_add_btn)

        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.insert, "")
        self.case = QWidget()
        self.case.setObjectName("case")
        self.gridLayout_6 = QGridLayout(self.case)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.case_lb = QLabel(self.case)
        self.case_lb.setObjectName("case_lb")

        self.horizontalLayout_10.addWidget(self.case_lb)

        self.case_mode_box = QComboBox(self.case)
        self.case_mode_box.addItem("")
        self.case_mode_box.addItem("")
        self.case_mode_box.addItem("")
        self.case_mode_box.addItem("")
        self.case_mode_box.addItem("")
        self.case_mode_box.setObjectName("case_mode_box")

        self.horizontalLayout_10.addWidget(self.case_mode_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.is_suffix_box = QCheckBox(self.case)
        self.is_suffix_box.setObjectName("is_suffix_box")

        self.verticalLayout_11.addWidget(self.is_suffix_box)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.case_add_btn = QPushButton(self.case)
        self.case_add_btn.setObjectName("case_add_btn")

        self.verticalLayout_11.addWidget(self.case_add_btn)

        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.tabWidget.addTab(self.case, "")
        self.serialize = QWidget()
        self.serialize.setObjectName("serialize")
        self.gridLayout_5 = QGridLayout(self.serialize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.start_num_lb = QLabel(self.serialize)
        self.start_num_lb.setObjectName("start_num_lb")

        self.horizontalLayout_9.addWidget(self.start_num_lb)

        self.start_num_box = QLineEdit(self.serialize)
        self.start_num_box.setObjectName("start_num_box")

        self.horizontalLayout_9.addWidget(self.start_num_box)

        self.gap_num_lb = QLabel(self.serialize)
        self.gap_num_lb.setObjectName("gap_num_lb")

        self.horizontalLayout_9.addWidget(self.gap_num_lb)

        self.gap_num_box = QLineEdit(self.serialize)
        self.gap_num_box.setObjectName("gap_num_box")

        self.horizontalLayout_9.addWidget(self.gap_num_box)

        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.padding_lb = QLabel(self.serialize)
        self.padding_lb.setObjectName("padding_lb")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.padding_lb.sizePolicy().hasHeightForWidth())
        self.padding_lb.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.padding_lb)

        self.padding_num_box = QSpinBox(self.serialize)
        self.padding_num_box.setObjectName("padding_num_box")

        self.horizontalLayout_11.addWidget(self.padding_num_box)

        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.serialize_mode_lb = QLabel(self.serialize)
        self.serialize_mode_lb.setObjectName("serialize_mode_lb")

        self.horizontalLayout_16.addWidget(self.serialize_mode_lb)

        self.serialize_replace_rtn = QRadioButton(self.serialize)
        self.serialize_mode_group = QButtonGroup(MainWindow)
        self.serialize_mode_group.setObjectName("serialize_mode_group")
        self.serialize_mode_group.addButton(self.serialize_replace_rtn)
        self.serialize_replace_rtn.setObjectName("serialize_replace_rtn")
        self.serialize_replace_rtn.setChecked(True)

        self.horizontalLayout_16.addWidget(self.serialize_replace_rtn)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.serialize_insert_before_str_rtn = QRadioButton(self.serialize)
        self.serialize_mode_group.addButton(self.serialize_insert_before_str_rtn)
        self.serialize_insert_before_str_rtn.setObjectName("serialize_insert_before_str_rtn")

        self.horizontalLayout_17.addWidget(self.serialize_insert_before_str_rtn)

        self.serialize_insert_before_str_box = QLineEdit(self.serialize)
        self.serialize_insert_before_str_box.setObjectName("serialize_insert_before_str_box")
        self.serialize_insert_before_str_box.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.serialize_insert_before_str_box)

        self.label_7 = QLabel(self.serialize)
        self.label_7.setObjectName("label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.serialize_insert_before_position_rtn = QRadioButton(self.serialize)
        self.serialize_mode_group.addButton(self.serialize_insert_before_position_rtn)
        self.serialize_insert_before_position_rtn.setObjectName(
            "serialize_insert_before_position_rtn"
        )

        self.horizontalLayout_18.addWidget(self.serialize_insert_before_position_rtn)

        self.serialize_insert_before_position_box = QSpinBox(self.serialize)
        self.serialize_insert_before_position_box.setObjectName(
            "serialize_insert_before_position_box"
        )
        self.serialize_insert_before_position_box.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.serialize_insert_before_position_box.sizePolicy().hasHeightForWidth()
        )
        self.serialize_insert_before_position_box.setSizePolicy(sizePolicy1)

        self.horizontalLayout_18.addWidget(self.serialize_insert_before_position_box)

        self.label_8 = QLabel(self.serialize)
        self.label_8.setObjectName("label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.label_8)

        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_16.addLayout(self.verticalLayout_14)

        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.serialize_add_btn = QPushButton(self.serialize)
        self.serialize_add_btn.setObjectName("serialize_add_btn")

        self.verticalLayout_10.addWidget(self.serialize_add_btn)

        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.serialize, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.added_rule_lb = QLabel(self.centralwidget)
        self.added_rule_lb.setObjectName("added_rule_lb")
        self.added_rule_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.added_rule_lb)

        self.added_rule_list = RuleListWidget(self.centralwidget)
        self.added_rule_list.setObjectName("added_rule_list")

        self.verticalLayout_4.addWidget(self.added_rule_list)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.before_lb = QLabel(self.centralwidget)
        self.before_lb.setObjectName("before_lb")
        self.before_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.before_lb)

        self.before_list = DropListWidget(self.centralwidget)
        self.before_list.setObjectName("before_list")

        self.verticalLayout.addWidget(self.before_list)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.after_lb = QLabel(self.centralwidget)
        self.after_lb.setObjectName("after_lb")
        self.after_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.after_lb)

        self.after_list = QListWidget(self.centralwidget)
        self.after_list.setObjectName("after_list")

        self.verticalLayout_2.addWidget(self.after_list)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 2)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 32))
        self.menu_info = QMenu(self.menubar)
        self.menu_info.setObjectName("menu_info")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_info.menuAction())
        self.menu_info.addAction(self.menu_info_manual)
        self.menu_info.addAction(self.menu_info_update)
        self.menu_info.addAction(self.menu_info_about)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Batch Renamer", None))
        self.menu_info_about.setText(QCoreApplication.translate("MainWindow", "\u95dc\u65bc", None))
        self.menu_info_update.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5\u66f4\u65b0", None)
        )
        self.menu_info_manual.setText(
            QCoreApplication.translate("MainWindow", "\u4f7f\u7528\u8aaa\u660e", None)
        )
        self.add_new_files_btn.setText(
            QCoreApplication.translate("MainWindow", "\u65b0\u589e\u6a94\u6848", None)
        )
        self.start_rename_btn.setText(
            QCoreApplication.translate("MainWindow", "\u958b\u59cb\u547d\u540d", None)
        )
        self.add_rule_lb.setText(
            QCoreApplication.translate("MainWindow", "\u65b0\u589e\u898f\u5247", None)
        )
        self.replace_old_str_lb.setText(
            QCoreApplication.translate("MainWindow", "\u539f\u5b57\u4e32\uff1a", None)
        )
        self.replace_new_str_lb.setText(
            QCoreApplication.translate("MainWindow", "\u65b0\u5b57\u4e32\uff1a", None)
        )
        self.replace_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.replace),
            QCoreApplication.translate("MainWindow", "\u53d6\u4ee3", None),
        )
        self.remove_str_lb.setText(
            QCoreApplication.translate("MainWindow", "\u79fb\u9664\u5b57\u4e32\uff1a", None)
        )
        self.remove_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.remove),
            QCoreApplication.translate("MainWindow", "\u79fb\u9664", None),
        )
        self.strip_str_lb.setText(
            QCoreApplication.translate("MainWindow", "\u525d\u9664\u5b57\u5143\uff1a", None)
        )
        self.strip_space_box.setText(QCoreApplication.translate("MainWindow", "\u7a7a\u767d", None))
        self.strip_eng_box.setText(
            QCoreApplication.translate("MainWindow", "\u82f1\u6587\u5b57\u6bcd", None)
        )
        self.strip_num_box.setText(QCoreApplication.translate("MainWindow", "\u6578\u5b57", None))
        self.strip_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.strip),
            QCoreApplication.translate("MainWindow", "\u525d\u9664", None),
        )
        self.delete_start_lb.setText(
            QCoreApplication.translate("MainWindow", "\u555f\u59cb\u65bc\uff1a", None)
        )
        self.delete_start_position_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u4f4d\u7f6e\uff1a", None)
        )
        self.delete_start_str_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u5b57\u5143", None)
        )
        self.delete_end_lb.setText(
            QCoreApplication.translate("MainWindow", "\u7d50\u675f\u65bc\uff1a", None)
        )
        self.delete_end_position_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u4f4d\u7f6e\uff1a", None)
        )
        self.delete_end_str_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u5b57\u5143", None)
        )
        self.delete_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.delete),
            QCoreApplication.translate("MainWindow", "\u522a\u9664", None),
        )
        self.insert_str_lb.setText(
            QCoreApplication.translate("MainWindow", "\u63d2\u5165\u5b57\u4e32\uff1a", None)
        )
        self.insert_position_lb.setText(
            QCoreApplication.translate("MainWindow", "\u63d2\u5165\u4f4d\u7f6e\uff1a", None)
        )
        self.insert_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.insert),
            QCoreApplication.translate("MainWindow", "\u63d2\u5165", None),
        )
        self.case_lb.setText(QCoreApplication.translate("MainWindow", "\u6a21\u5f0f\uff1a", None))
        self.case_mode_box.setItemText(
            0, QCoreApplication.translate("MainWindow", "\u9996\u5b57\u5927\u5beb", None)
        )
        self.case_mode_box.setItemText(
            1, QCoreApplication.translate("MainWindow", "\u9996\u5b57\u5c0f\u5beb", None)
        )
        self.case_mode_box.setItemText(
            2, QCoreApplication.translate("MainWindow", "\u5168\u90e8\u5927\u5beb", None)
        )
        self.case_mode_box.setItemText(
            3, QCoreApplication.translate("MainWindow", "\u5168\u90e8\u5c0f\u5beb", None)
        )
        self.case_mode_box.setItemText(
            4, QCoreApplication.translate("MainWindow", "\u5927\u5c0f\u5beb\u4e92\u63db", None)
        )

        self.is_suffix_box.setText(
            QCoreApplication.translate("MainWindow", "\u5305\u542b\u526f\u6a94\u540d", None)
        )
        self.case_add_btn.setText(QCoreApplication.translate("MainWindow", "\u65b0\u589e", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.case),
            QCoreApplication.translate("MainWindow", "\u5927\u5c0f\u5beb", None),
        )
        self.start_num_lb.setText(
            QCoreApplication.translate("MainWindow", "\u555f\u59cb\u6578\u5b57\uff1a", None)
        )
        self.gap_num_lb.setText(
            QCoreApplication.translate("MainWindow", "\u9593\u9694\uff1a", None)
        )
        self.padding_lb.setText(
            QCoreApplication.translate("MainWindow", "\u586b\u5145\u4f4d\u6578\uff1a", None)
        )
        self.serialize_mode_lb.setText(
            QCoreApplication.translate("MainWindow", "\u6a21\u5f0f\uff1a", None)
        )
        self.serialize_replace_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u53d6\u4ee3", None)
        )
        self.serialize_insert_before_str_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u63d2\u5165\u5728", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "\u4e4b\u524d", None))
        self.serialize_insert_before_position_rtn.setText(
            QCoreApplication.translate("MainWindow", "\u63d2\u5165\u5728", None)
        )
        self.label_8.setText(QCoreApplication.translate("MainWindow", "\u4f4d\u7f6e", None))
        self.serialize_add_btn.setText(
            QCoreApplication.translate("MainWindow", "\u65b0\u589e", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.serialize),
            QCoreApplication.translate("MainWindow", "\u5e8f\u5217\u5316", None),
        )
        self.added_rule_lb.setText(
            QCoreApplication.translate("MainWindow", "\u5df2\u65b0\u589e\u898f\u5247", None)
        )
        self.before_lb.setText(QCoreApplication.translate("MainWindow", "\u547d\u540d\u524d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "\u2192", None))
        self.after_lb.setText(QCoreApplication.translate("MainWindow", "\u547d\u540d\u5f8c", None))
        self.menu_info.setTitle(QCoreApplication.translate("MainWindow", "\u8aaa\u660e", None))

    # retranslateUi
