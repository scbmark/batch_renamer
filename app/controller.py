import json
import re
import ssl
import string
from pathlib import Path
from urllib import request

import certifi
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox

import resources
from app.AboutUI import Ui_AboutWindow
from app.CustomWidgets import QListWidgetItemPlus, QListWidgetItemRule
from app.MainUI import Ui_MainWindow
from app.ManualUI import Ui_ManualWindow


class MainWindow_controller(QtWidgets.QMainWindow):
    send_update_image_count = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.version = "1.0"

        self.show_usage_warrning_window()

        self.setup_control()
        self.set_statusbar()

    def setup_control(self):
        """
        initialize global variable and connect slot functions
        """
        self.ui.menu_info_manual.triggered.connect(self.show_manual_window)
        self.ui.menu_info_about.triggered.connect(self.show_about_window)
        self.ui.menu_info_update.triggered.connect(self.check_update)

        self.ui.added_rule_list.update_after_list.connect(self.update_after_list)
        self.ui.start_rename_btn.clicked.connect(self.start_rename)
        self.ui.add_new_files_btn.clicked.connect(self.add_files)
        self.ui.before_list.send_new_item.connect(self.add_drop_files)
        self.ui.replace_add_btn.clicked.connect(self.add_replace_rule)
        self.ui.remove_add_btn.clicked.connect(self.add_remove_rule)
        self.ui.strip_add_btn.clicked.connect(self.add_strip_rule)
        self.ui.delete_add_btn.clicked.connect(self.add_delete_rule)
        self.ui.insert_add_btn.clicked.connect(self.add_insert_rule)
        self.ui.serialize_add_btn.clicked.connect(self.add_serialize_rule)
        self.ui.case_add_btn.clicked.connect(self.add_case_rule)
        self.ui.serialize_mode_group.buttonClicked.connect(self.change_serialize_mode)
        self.ui.delete_start_mode_group.buttonClicked.connect(self.change_delete_start_mode)
        self.ui.delete_end_mode_group.buttonClicked.connect(self.change_delete_end_mode)

    def set_statusbar(self):
        """
        configurate the statusbar
        """
        self.file_count = QtWidgets.QLabel()
        self.file_count.setText(f"將命名 0/0 個檔案")
        self.status = QtWidgets.QLabel()
        self.status.setText("狀態： 正常")
        self.ui.statusbar.addPermanentWidget(self.file_count)
        self.ui.statusbar.addPermanentWidget(self.status)

    def show_usage_warrning_window(self):
        """
        show the usage_warrning message
        """
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle("警告")
        messagebox.setText("任何檔案在進入此程式使用前，請務必做好備份，並且使用副本來操作。本程式會對匯入的檔案進行讀寫的操作，請在確認新命名的預覽之後再重新命名。")
        messagebox.setIcon(QMessageBox.Icon.Critical)
        messagebox.addButton("我了解了", QMessageBox.ButtonRole.AcceptRole)
        messagebox.addButton("我不同意", QMessageBox.ButtonRole.RejectRole)

        result = messagebox.exec()
        if result == 1:
            import sys

            sys.exit()

    def show_manual_window(self):
        """
        open manual window
        """
        self.ManualWindows = QtWidgets.QWidget()
        self.manual_ui = Ui_ManualWindow()
        self.manual_ui.setupUi(self.ManualWindows)
        self.ManualWindows.setFixedSize(800, 600)
        self.manual_ui.exit_btn.clicked.connect(lambda: self.ManualWindows.close())
        self.ManualWindows.show()

    def check_update(self):
        github_release_url: str = "https://github.com/scbmark/batch_renamer/releases/latest"
        github_release_url_api: str = (
            "https://api.github.com/repos/scbmark/batch_renamer/releases/latest"
        )

        req = request.Request(github_release_url_api)

        try:
            context = ssl.create_default_context(cafile=certifi.where())
            with request.urlopen(req, context=context) as response:
                res = json.load(response)
                latest_version = res["tag_name"]
        except:
            messagebox = QMessageBox(self)
            messagebox.warning(self, "更新", "網路連線失敗")
            return

        if latest_version != self.version:
            messagebox = QMessageBox(self)
            messagebox.setWindowTitle("更新")
            messagebox.setText(f"發現更新\n目前版本： {self.version}\n最新版本： {res['tag_name']}")
            messagebox.setIcon(QMessageBox.Icon.Information)
            messagebox.addButton("現在更新", QMessageBox.ButtonRole.AcceptRole)
            messagebox.addButton("不要更新", QMessageBox.ButtonRole.RejectRole)

            result = messagebox.exec()
            if result == 0:
                import webbrowser

                webbrowser.open(github_release_url)
            else:
                pass
        else:
            messagebox = QMessageBox(self)
            messagebox.information(self, "檢查更新", f"目前為最新版本\n目前版本： {self.version}")

    def show_about_window(self):
        """
        open about window
        """
        self.AboutWindows = QtWidgets.QWidget()
        self.about_ui = Ui_AboutWindow()
        self.about_ui.setupUi(self.AboutWindows)
        self.about_ui.version_lb.setText(f"Version: {self.version}")
        self.AboutWindows.setFixedSize(400, 600)
        self.about_ui.exit_btn.clicked.connect(lambda: self.AboutWindows.close())
        self.AboutWindows.show()

    def add_drop_files(self, files: list):
        for file in files:
            self.add_file_to_list(file)

        self.update_after_list()

    def add_files(self):
        files = self.open_files_dialog()
        for file in files:
            self.add_file_to_list(file)

        self.update_after_list()

    def open_files_dialog(self) -> list[str]:
        """
        show the file dialog and get the folder's path
        """
        dir_path = QtWidgets.QFileDialog.getOpenFileNames(caption="選取檔案")

        return dir_path[0]

    def add_file_to_list(self, file: str):
        item = QListWidgetItemPlus(file)
        item_widget = QtWidgets.QWidget()

        name_lb = QtWidgets.QLabel()
        name_lb.setText(Path(file).name)
        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_item(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(name_lb)
        item_layout.addStretch()
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.before_list.addItem(item)
        self.ui.before_list.setItemWidget(item, item_widget)
        self.ui.before_list.repaint()

    def delete_item(self, item: QListWidgetItemPlus):
        """
        get the QListWidgetItem and remove it from QListWidget
        """
        index = self.ui.before_list.row(item)
        self.ui.before_list.takeItem(index)
        self.update_after_list()

    def delete_rule(self, item):
        """
        get the QListWidgetItem and remove it from QListWidget
        """
        index = self.ui.added_rule_list.row(item)
        self.ui.added_rule_list.takeItem(index)
        self.update_after_list()

    def change_delete_start_mode(self):
        if (
            self.ui.delete_start_mode_group.checkedButton().objectName()
            == "delete_start_position_rtn"
        ):
            self.ui.delete_start_position_box.setEnabled(True)
            self.ui.delete_start_str_box.setEnabled(False)
        elif self.ui.delete_start_mode_group.checkedButton().objectName() == "delete_start_str_rtn":
            self.ui.delete_start_position_box.setEnabled(False)
            self.ui.delete_start_str_box.setEnabled(True)
        else:
            self.ui.delete_start_position_box.setEnabled(True)
            self.ui.delete_start_str_box.setEnabled(False)

    def change_delete_end_mode(self):
        if self.ui.delete_end_mode_group.checkedButton().objectName() == "delete_end_position_rtn":
            self.ui.delete_end_position_box.setEnabled(True)
            self.ui.delete_end_str_box.setEnabled(False)
        elif self.ui.delete_end_mode_group.checkedButton().objectName() == "delete_end_str_rtn":
            self.ui.delete_end_position_box.setEnabled(False)
            self.ui.delete_end_str_box.setEnabled(True)
        else:
            self.ui.delete_end_position_box.setEnabled(True)
            self.ui.delete_end_str_box.setEnabled(False)

    def change_serialize_mode(self):
        if self.ui.serialize_mode_group.checkedButton().objectName() == "serialize_replace_rtn":
            self.ui.serialize_insert_before_str_box.setEnabled(False)
            self.ui.serialize_insert_before_position_box.setEnabled(False)
        elif (
            self.ui.serialize_mode_group.checkedButton().objectName()
            == "serialize_insert_before_str_rtn"
        ):
            self.ui.serialize_insert_before_str_box.setEnabled(True)
            self.ui.serialize_insert_before_position_box.setEnabled(False)
        elif (
            self.ui.serialize_mode_group.checkedButton().objectName()
            == "serialize_insert_before_position_rtn"
        ):
            self.ui.serialize_insert_before_str_box.setEnabled(False)
            self.ui.serialize_insert_before_position_box.setEnabled(True)
        else:
            self.ui.serialize_insert_before_str_box.setEnabled(False)
            self.ui.serialize_insert_before_position_box.setEnabled(False)

    def add_replace_rule(self):
        rule = {
            "type": "replace",
            "old_str": self.ui.replace_old_str_box.text(),
            "new_str": self.ui.replace_new_str_box.text(),
        }

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Replace: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(
            f"{self.ui.replace_old_str_box.text()} → {self.ui.replace_new_str_box.text()}"
        )

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.replace_old_str_box.setText("")
        self.ui.replace_new_str_box.setText("")

    def add_remove_rule(self):
        rule = {
            "type": "remove",
            "remove_str": self.ui.remove_str_box.text(),
        }

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Remove: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(f"{self.ui.remove_str_box.text()}")

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.remove_str_box.setText("")

    def add_strip_rule(self):
        rule = {
            "type": "strip",
            "strip_str": self.ui.strip_str_box.text(),
        }

        display_str = self.ui.strip_str_box.text()
        if self.ui.strip_eng_box.isChecked():
            rule["strip_str"] = rule["strip_str"] + string.ascii_letters
            display_str += f" ascii_letters"
        if self.ui.strip_num_box.isChecked():
            rule["strip_str"] = rule["strip_str"] + string.digits
            display_str += f" digits"
        if self.ui.strip_space_box.isChecked():
            rule["strip_str"] = rule["strip_str"] + string.whitespace
            display_str += f" whitespace"

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Strip: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(display_str)

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.strip_str_box.setText("")
        self.ui.strip_space_box.setChecked(False)
        self.ui.strip_eng_box.setChecked(False)
        self.ui.strip_num_box.setChecked(False)

    def add_delete_rule(self):
        rule = {
            "type": "delete",
        }

        if self.ui.delete_start_position_rtn.isChecked():
            rule["delete_start_mode"] = "position"
            rule["delete_start_position"] = self.ui.delete_start_position_box.value()
            display_start_text = f"start at position {self.ui.delete_start_position_box.value()}"
        else:
            rule["delete_start_mode"] = "str"
            rule["delete_start_str"] = self.ui.delete_start_str_box.text()
            display_start_text = f"start at str {self.ui.delete_start_str_box.text()}"

        if self.ui.delete_end_position_rtn.isChecked():
            rule["delete_end_mode"] = "position"
            rule["delete_end_position"] = self.ui.delete_end_position_box.value()
            display_end_text = f"end at position {self.ui.delete_end_position_box.value()}"
        else:
            rule["delete_end_mode"] = "str"
            rule["delete_end_str"] = self.ui.delete_end_str_box.text()
            display_end_text = f"end at str {self.ui.delete_end_str_box.text()}"

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Delete: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(f"{display_start_text}, {display_end_text}")

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.delete_start_position_rtn.setChecked(True)
        self.ui.delete_start_position_box.setValue(0)
        self.ui.delete_start_str_box.setText("")
        self.ui.delete_start_position_box.setDisabled(False)
        self.ui.delete_start_str_box.setDisabled(True)
        self.ui.delete_end_position_rtn.setChecked(True)
        self.ui.delete_end_position_box.setValue(-1)
        self.ui.delete_end_str_box.setText("")
        self.ui.delete_end_position_box.setDisabled(False)
        self.ui.delete_end_str_box.setDisabled(True)

    def add_insert_rule(self):
        rule = {
            "type": "insert",
            "insert_str": self.ui.insert_str_box.text(),
            "insert_position": self.ui.insert_position_box.value(),
        }

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Insert: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(
            f"{self.ui.insert_str_box.text()} at {self.ui.insert_position_box.text()}"
        )

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.insert_str_box.setText("")
        self.ui.insert_position_box.setValue(0)

    def add_serialize_rule(self):
        rule = {
            "type": "serialize",
            "start_num": int(self.ui.start_num_box.text()),
            "gap_num": int(self.ui.gap_num_box.text()),
            "padding_num": self.ui.padding_num_box.value(),
        }
        if self.ui.serialize_replace_rtn.isChecked():
            rule["serialize_mode"] = "replace"
        elif self.ui.serialize_insert_before_str_rtn.isChecked():
            rule["serialize_mode"] = "insert_before_str"
            rule["insert_before_str"] = self.ui.serialize_insert_before_str_box.text()
        elif self.ui.serialize_insert_before_position_rtn.isChecked():
            rule["serialize_mode"] = "insert_before_position"
            rule["insert_before_position"] = self.ui.serialize_insert_before_position_box.value()
        else:
            rule["serialize_mode"] = "replace"

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Serialize: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(
            f"from {self.ui.start_num_box.text()} every {self.ui.gap_num_box.text()} padding {self.ui.padding_num_box.value()} digits by {rule['serialize_mode']}"
        )

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.start_num_box.setText("")
        self.ui.gap_num_box.setText("")
        self.ui.padding_num_box.setValue(0)
        self.ui.serialize_replace_rtn.setChecked(True)

    def add_case_rule(self):
        rule = {
            "type": "case",
            "case_mode": self.ui.case_mode_box.currentIndex(),
            "is_suffix": self.ui.is_suffix_box.isChecked(),
        }

        item = QListWidgetItemRule(rule)
        item_widget = QtWidgets.QWidget()

        rule_lb = QtWidgets.QLabel()
        rule_lb.setText("Case: ")

        rule_content_lb = QtWidgets.QLabel()
        rule_content_lb.setText(
            f"{self.ui.case_mode_box.currentText()} suffix {self.ui.is_suffix_box.isChecked()}"
        )

        item_layout = QtWidgets.QHBoxLayout()

        delete_button = QtWidgets.QPushButton("")
        delete_button.setIcon(QtGui.QIcon(QtGui.QPixmap(":/statics/close.svg")))
        delete_button.clicked.connect(lambda: self.delete_rule(item))

        enable_box = QtWidgets.QCheckBox()
        enable_box.setChecked(True)
        enable_box.toggled.connect(self.update_after_list)

        item_layout.addWidget(enable_box)
        item_layout.addWidget(rule_lb)
        item_layout.addStretch()
        item_layout.addWidget(rule_content_lb)
        item_layout.addWidget(delete_button)

        item_widget.setLayout(item_layout)
        item.setSizeHint(item_widget.sizeHint())

        self.ui.added_rule_list.addItem(item)
        self.ui.added_rule_list.setItemWidget(item, item_widget)
        self.ui.added_rule_list.repaint()

        self.update_after_list()
        self.ui.case_mode_box.setCurrentIndex(0)
        self.ui.is_suffix_box.setChecked(False)

    def update_after_list(self):
        self.ui.after_list.clear()
        self.ui.start_rename_btn.setEnabled(True)
        status = "狀態： 正常"
        serialize_index = 0
        full_name_list = list()

        for index_name in range(self.ui.before_list.count()):
            name_item: QListWidgetItemPlus = self.ui.before_list.item(index_name)
            name_widget = self.ui.before_list.itemWidget(name_item)

            full_name: str = name_item.text
            base_name = Path(full_name).name

            checked = name_widget.layout().itemAt(0).widget().isChecked()

            if checked:
                for index_rule in range(self.ui.added_rule_list.count()):
                    rule_item: QListWidgetItemRule = self.ui.added_rule_list.item(index_rule)
                    rule_widget = self.ui.added_rule_list.itemWidget(rule_item)
                    if rule_widget.layout().itemAt(0).widget().isChecked():
                        base_name, full_name, serialize_index = self.rename_logic(
                            base_name, full_name, rule_item, serialize_index
                        )

            item = QListWidgetItemPlus(full_name)
            item_widget = QtWidgets.QWidget()

            name_lb = QtWidgets.QLabel()
            name_lb.setText(base_name)

            if checked:
                if full_name in full_name_list:
                    name_lb.setStyleSheet("color: red")
                    self.ui.start_rename_btn.setEnabled(False)
                    status = "狀態： 異常"
                else:
                    full_name_list.append(full_name)
                    name_lb.setStyleSheet("color: green")
            else:
                name_lb.setStyleSheet("color: gray")

            item_layout = QtWidgets.QHBoxLayout()

            item_layout.addWidget(name_lb)

            item_widget.setLayout(item_layout)
            item.setSizeHint(item_widget.sizeHint())

            self.ui.after_list.addItem(item)
            self.ui.after_list.setItemWidget(item, item_widget)
            self.ui.after_list.repaint()

        self.file_count.setText(f"將命名 {len(full_name_list)}/{self.ui.before_list.count()} 個檔案")
        self.status.setText(status)

    def rename_logic(
        self, base_name: str, full_name: str, rule_item: QListWidgetItemRule, serialize_index: int
    ) -> tuple[str, str, int]:
        if rule_item.type == "replace":
            base_name = (
                f"{base_name.replace(rule_item.content['old_str'], rule_item.content['new_str'])}"
            )
            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

        elif rule_item.type == "remove":
            base_name = f"{base_name.replace(rule_item.content['remove_str'], '')}"
            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

        elif rule_item.type == "strip":
            reg = re.sub(
                f"[{rule_item.content['strip_str']}]",
                "",
                Path(base_name).name.replace(Path(base_name).suffix, ""),
            )
            base_name = f"{reg+Path(base_name).suffix}"
            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

        elif rule_item.type == "delete":
            if (rule_item.content["delete_start_mode"] == "position") and (
                rule_item.content["delete_end_mode"] == "position"
            ):
                base_name = f"{base_name.replace(base_name[rule_item.content['delete_start_position']:rule_item.content['delete_end_position']+1], '')}"
            elif (rule_item.content["delete_start_mode"] == "position") and (
                rule_item.content["delete_end_mode"] == "str"
            ):
                try:
                    end_index: int = base_name.index(rule_item.content["delete_end_str"])
                    base_name = f"{base_name.replace(base_name[rule_item.content['delete_start_position']:end_index+1], '')}"
                except:
                    pass
            elif (rule_item.content["delete_start_mode"] == "str") and (
                rule_item.content["delete_end_mode"] == "position"
            ):
                try:
                    start_index: int = base_name.index(rule_item.content["delete_start_str"])
                    base_name = f"{base_name.replace(base_name[start_index:rule_item.content['delete_end_position']+1], '')}"
                except:
                    pass
            elif (rule_item.content["delete_start_mode"] == "str") and (
                rule_item.content["delete_end_mode"] == "str"
            ):
                try:
                    start_index: int = base_name.index(rule_item.content["delete_start_str"])
                    end_index: int = base_name.index(rule_item.content["delete_end_str"])
                    base_name = f"{base_name.replace(base_name[start_index:end_index+1], '')}"
                except:
                    pass
            else:
                base_name = f"{base_name.replace(base_name[rule_item.content['delete_start_position']:rule_item.content['delete_end_position']+1], '')}"

            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

        elif rule_item.type == "insert":
            if rule_item.content["insert_position"] == 0:
                base_name = rule_item.content["insert_str"] + base_name
            elif rule_item.content["insert_position"] == -1:
                base_name = base_name + rule_item.content["insert_str"]
            else:
                base_name_head = base_name[0 : rule_item.content["insert_position"]]
                base_name_tail = base_name[rule_item.content["insert_position"] :]

                base_name = base_name_head + rule_item.content["insert_str"] + base_name_tail
            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

        elif rule_item.type == "serialize":
            index = str(
                rule_item.content["start_num"] + serialize_index * rule_item.content["gap_num"]
            )

            index = index.zfill(rule_item.content["padding_num"])

            if rule_item.content["serialize_mode"] == "replace":
                base_name = str(index + Path(base_name).suffix)
            elif rule_item.content["serialize_mode"] == "insert_before_str":
                base_name = f"{base_name.replace(rule_item.content['insert_before_str'], index + rule_item.content['insert_before_str'])}"
            elif rule_item.content["serialize_mode"] == "insert_before_position":
                if rule_item.content["insert_before_position"] == 0:
                    base_name = index + base_name
                elif rule_item.content["insert_before_position"] == -1:
                    base_name = base_name + index
                else:
                    base_name_head = base_name[0 : rule_item.content["insert_before_position"]]
                    base_name_tail = base_name[rule_item.content["insert_before_position"] :]

                    base_name = base_name_head + index + base_name_tail

            full_name = str(Path(full_name).parent.joinpath(base_name))

            serialize_index += 1
            return base_name, full_name, serialize_index

        elif rule_item.type == "case":
            if rule_item.content["case_mode"] == 0:
                base_name = base_name.capitalize()
            elif rule_item.content["case_mode"] == 1:
                base_name = base_name[0].lower() + base_name[1:]
            elif rule_item.content["case_mode"] == 2:
                if rule_item.content["is_suffix"]:
                    base_name = base_name.upper()
                else:
                    base_name = Path(base_name)
                    base_name = (
                        base_name.name.replace(base_name.suffix, "").upper() + base_name.suffix
                    )
            elif rule_item.content["case_mode"] == 3:
                if rule_item.content["is_suffix"]:
                    base_name = base_name.lower()
                else:
                    base_name = Path(base_name)
                    base_name = (
                        base_name.name.replace(base_name.suffix, "").lower() + base_name.suffix
                    )
            elif rule_item.content["case_mode"] == 4:
                if rule_item.content["is_suffix"]:
                    base_name = base_name.swapcase()
                else:
                    base_name = Path(base_name)
                    base_name = (
                        base_name.name.replace(base_name.suffix, "").swapcase() + base_name.suffix
                    )

            full_name = str(Path(full_name).parent.joinpath(base_name))

            return base_name, full_name, serialize_index

    def start_rename(self):
        failed = False
        failed_list = list()

        for index_name in range(self.ui.before_list.count()):
            old_name_item: QListWidgetItemPlus = self.ui.before_list.item(index_name)
            old_name_widget = self.ui.before_list.itemWidget(old_name_item)

            if old_name_widget.layout().itemAt(0).widget().isChecked():
                new_name_item: QListWidgetItemPlus = self.ui.after_list.item(index_name)

                old_name = Path(old_name_item.text)
                new_name = new_name_item.text
                try:
                    old_name.rename(new_name)
                except:
                    failed = True
                    failed_list.append(old_name.name)
                    continue

        if failed:
            messabebox = QtWidgets.QMessageBox(self)
            messabebox.warning(self, "Error", "重新命名失敗")
        else:
            messabebox = QtWidgets.QMessageBox(self)
            messabebox.warning(self, "Success", "重新命名完成")

            messagebox = QMessageBox(self)
            messagebox.setWindowTitle("繼續")
            messagebox.setText("是否繼續命名這些檔案")
            messagebox.setIcon(QMessageBox.Icon.Information)
            messagebox.addButton("是", QMessageBox.ButtonRole.AcceptRole)
            messagebox.addButton("否", QMessageBox.ButtonRole.RejectRole)

            result = messagebox.exec()
            if result == 0:
                self.ui.before_list.clear()
                for index_name in range(self.ui.after_list.count()):
                    item_name = self.ui.after_list.item(index_name).text
                    self.add_file_to_list(item_name)

                self.update_after_list()
            else:
                self.ui.before_list.clear()
                self.update_after_list()
