from PySide6.QtWidgets import QMainWindow
from ui.frmMain import Ui_MainWindow

# 各フォームのインポート
from pc_new_reg import PcNewRegForm
from pc_master import PcMasterForm
from user_master import UserMasterForm
from user_master_edit import UserMasterEditForm
from pc_master_edit import PcMasterEditForm
from pc_info import PcInfoForm

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ボタンイベントの接続
        self.ui.btnNewPcRegister.clicked.connect(self.openPcRegister)
        self.ui.btnPcMasterRegister.clicked.connect(self.openPcMaster)
        self.ui.btnUserMasterRegister.clicked.connect(self.openUserMaster)
        self.ui.btnUserMasterEdit.clicked.connect(self.openUserMasterEdit)
        self.ui.btnPcMasterEdit.clicked.connect(self.openPcMasterEdit)
        self.ui.btnSearchEdit.clicked.connect(self.openPcInfo)
    

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

    def openUserMasterEdit(self):
        self.userMasterEditForm = UserMasterEditForm(parent=self)
        self.userMasterEditForm.show()
        self.hide()

    def openPcMasterEdit(self):
        self.pcMasterEditForm = PcMasterEditForm(parent=self)
        self.pcMasterEditForm.show()
        self.hide()

    def openPcInfo(self):
        self.pcInfoForm = PcInfoForm(parent=self)
        self.pcInfoForm.show()
        self.hide()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
