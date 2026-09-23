from PySide6.QtWidgets import QMainWindow
from ui.frmMain import Ui_MainWindow

# 各フォームのインポート
from pc_new_reg import PcNewRegForm
from pc_master import PcMasterForm
from user_master import UserMasterForm


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ボタンイベントの接続
        self.ui.btnNewPcRegister.clicked.connect(self.openPcRegister)
        self.ui.btnPcMasterRegister.clicked.connect(self.openPcMaster)
        self.ui.btnUserMasterRegister.clicked.connect(self.openUserMaster)

        self.ui.btnClose.clicked.connect(self.close)

    def openPcRegister(self):
        self.pcRegForm = PcNewRegForm(parent=self)
        self.pcRegForm.show()
        self.hide()

    def openPcMaster(self):
        self.pcMasterForm = PcMasterForm(parent=self)
        self.pcMasterForm.show()
        self.hide()


    def openUserMaster(self):
        self.userMasterForm = UserMasterForm(parent=self)
        self.userMasterForm.show()
        self.hide()



if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
