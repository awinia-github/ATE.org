from PyQt5 import QtGui, QtCore, QtWidgets, uic
import os
import shutil
import qtawesome as qta


DELETE_DIALOG = 'Delete.ui'
RENAME_DIALOG = 'Rename.ui'


class MenuDialog(QtWidgets.QDialog):
    def __init__(self, ui_name, action):
        super().__init__()
        self.ui_name = ui_name
        self.action = action
        for _ in self._steps():
            pass

    def _steps(self):
        self._load_ui()
        yield
        self._setup()
        yield
        self._connect_action_handler()

    def show(self):
        return self.exec_()

    def _load_ui(self):
        current_dir = os.path.dirname(__file__)
        uic.loadUi(os.path.join(current_dir, self.ui_name), self)

    def _setup(self):
        self.setWindowTitle(self.action)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, on=False)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, on=False)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, on=False)
        self.setFixedSize(self.size())
        self.ok_button = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.cancel_button = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)

    def _connect_action_handler(self):
        self.ok_button.clicked.connect(self._accept)
        self.cancel_button.clicked.connect(self._cancel)

    def _accept(self):
        self.accept()

    def _cancel(self):
        self.reject()


class DeleteFileDialog(MenuDialog):
    def __init__(self, path, action):
        super().__init__(DELETE_DIALOG, action)
        self.path = path
        self.icon_label.setPixmap(qta.icon('mdi.alert-outline', color='orange').pixmap(50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        self.file_name_label.setFont(font)
        self.file_name_label.setText(os.path.basename(self.path))
        self.label.setText(f"Are you sure you want to delete")

    def _accept(self):
        os.remove(self.path)
        self.accept()


class DeleteDirDialog(DeleteFileDialog):
    def __init__(self, path, action):
        super().__init__(path, action)

    def _accept(self):
        shutil.rmtree(self.path)
        self.accept()


class RenameDialog(MenuDialog):
    def __init__(self, path, action):
        super().__init__(RENAME_DIALOG, action)
        self.path = path
        self.fileName.setText(os.path.basename(self.path))
        self.fileName.textChanged.connect(self.validate)
        self.fileName.setFocus(QtCore.Qt.MouseFocusReason)

    def validate(self, text):
        if not text:
            self.feedback.setText("name field is empty")
            self.feedback.setStyleSheet("color: orange")
            self.ok_button.setDisabled(True)
            return

        self.feedback.setText("")
        self.ok_button.setDisabled(False)

    def _accept(self):
        shutil.move(self.path, os.path.join(os.path.dirname(self.path), self.fileName.text()))
        self.accept()


class AddDirectoryDialog(RenameDialog):
    def __init__(self, path, action):
        super().__init__(RENAME_DIALOG, action)
        self.path = path
        self.fileName.setText('')

    def _accept(self):
        try:
            os.mkdir(os.path.join(self.path, self.fileName.text()))
        except Exception as e:
            print(e)

        self.accept()
