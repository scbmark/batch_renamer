from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QAbstractItemView


class DropListWidget(QtWidgets.QListWidget):
    """This custom widget based on  QListWidget.

    Added features:

        1.Drag and drop features

        2.Placeholder

    Emit:
        send_new_item -> list[str]: Sending the files's path
    """

    send_new_item = Signal(list)

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setDefaultDropAction(Qt.MoveAction)
        self._placeholder_text: str = "拖曳至此新增檔案"

    @property
    def placeholder_text(self):
        return self._placeholder_text

    @placeholder_text.setter
    def placeholder_text(self, text):
        self._placeholder_text = text
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.count() == 0:
            painter = QtGui.QPainter(self.viewport())
            painter.save()
            col = self.palette().placeholderText().color()
            painter.setPen(col)
            fm = self.fontMetrics()
            elided_text = fm.elidedText(
                self.placeholder_text,
                QtCore.Qt.TextElideMode.ElideRight,
                self.viewport().width(),
            )
            painter.drawText(
                self.viewport().rect(), QtCore.Qt.AlignmentFlag.AlignCenter, elided_text
            )
            painter.restore()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(DropListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
        else:
            super(DropListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()

            valid_links: list[str] = list()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    path = Path(url.toLocalFile())
                    if path.is_dir():
                        valid_links.extend(path.glob("*"))
                    else:
                        valid_links.append(path)
                else:
                    messabebox = QtWidgets.QMessageBox(self)
                    messabebox.warning(self, "Error", "不支援的檔案")

            self.send_new_item.emit(valid_links)
        else:
            super(DropListWidget, self).dropEvent(event)
            self.send_new_item.emit([])


class RuleListWidget(QtWidgets.QListWidget):
    """This custom widget based on  QListWidget.

    Added features:

        1.Drag and drop features

    Emit:
        update_after_list -> bool: Call update_after_list function in main
    """

    update_after_list = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setDefaultDropAction(Qt.MoveAction)

    def dragEnterEvent(self, event):
        super(RuleListWidget, self).dragEnterEvent(event)
        event.accept()

    def dragMoveEvent(self, event):
        super(RuleListWidget, self).dragMoveEvent(event)
        event.accept()

    def dropEvent(self, event):
        super(RuleListWidget, self).dropEvent(event)
        event.accept()
        self.update_after_list.emit()


class QListWidgetItemPlus(QtWidgets.QListWidgetItem):
    """This custom widget based on QListWidgetItem.

    Added features:

        1.add the variable 'text' on QListWidgetItem that store the file's absolute path

    Args:

        test(str): The absolute path of the image
    """

    def __init__(self, text: str):
        super().__init__()
        self.text: str = text


class QListWidgetItemRule(QtWidgets.QListWidgetItem):
    """This custom widget based on QListWidgetItem.

    Added features:

        1.add the variable 'type' that store the rename type

        2.add the variable 'content' that store the rename detail

    Args:

        test(str): The absolute path of the image
    """

    def __init__(self, rule: dict):
        super().__init__()
        self.type: str = rule["type"]
        self.content: dict = rule
