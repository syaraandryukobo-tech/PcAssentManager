from PySide6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QAbstractItemView
from PySide6.QtCore import Qt
from ui.frmUserSelect import Ui_Dialog
import openpyxl

class UserSelectForm(QDialog):

    def __init__(self, search_user_name, process_type, current_location, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.search_user_name = search_user_name
        print(search_user_name)
        self.ui.lblSearchCondition.setText(search_user_name)
        self.process_type = process_type
        self.current_location = current_location

        self.ui.btnDecision.setAutoDefault(False)
        self.ui.btnDecision.setDefault(False) 

        # 選択されたユーザー情報
        self.selected_user_code = None
        self.selected_user_name = None
        self.selected_department = None
        self.selected_location = None
        self.selected_email = None # メールアドレス(非表示)

        # 決定ボタン
        self.ui.btnDecision.clicked.connect(self.decisionUser)

        # テーブル初期化
        self.initTable()

        self.serachUser()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()
            return
        super().keyPressEvent(event)

    def serachUser(self):
        user_name = self.search_user_name
        print(user_name)

        wb = openpyxl.load_workbook("Excel/pc_list.xlsx")
        ws = wb["ユーザーマスタ"]
        print("Excel読込成功")
        print("シート取得成功")

        searchCount = 0

        # 検索結果クリア
        self.ui.tblUserSelect.setRowCount(0)

        for row in ws.iter_rows(min_row=2, values_only=True):
            # 氏名チェック
            if user_name != "" and user_name not in str(row[1]):
                continue

            if self.process_type == "移動":
                if row[3] != self.current_location:
                    continue
            elif self.process_type == "譲渡":
                if row[3] == self.current_location:
                    continue

            searchCount += 1
            print(row)

            # addUserRowを使ってメールアドレスを非表示で保持
            self.addUserRow(
                str(row[0]), # ユーザーコード
                str(row[1]), # 氏名
                str(row[2]), # 所属
                str(row[3]), # 拠点
                str(row[5])  # メールアドレス(非表示保持)
            )

            # rowPosition = self.ui.tblUserSelect.rowCount()
            # self.ui.tblUserSelect.insertRow(rowPosition)

            # self.ui.tblUserSelect.setItem(rowPosition, 0,QTableWidgetItem(str(row[0])))
            # self.ui.tblUserSelect.setItem(rowPosition, 1,QTableWidgetItem(str(row[1])))
            # self.ui.tblUserSelect.setItem(rowPosition, 2,QTableWidgetItem(str(row[2])))
            # self.ui.tblUserSelect.setItem(rowPosition, 3,QTableWidgetItem(str(row[3])))

        totalCount =ws.max_row -1

        if searchCount == 0:
            self.ui.tblUserSelect.setRowCount(1)
            self.ui.tblUserSelect.setSpan(0, 0, 1, 4)
            item = QTableWidgetItem("該当するデータはありません")
            self.ui.tblUserSelect.setItem(0, 0, item)

        print("検索件数：", searchCount)
        print("総件数：", totalCount)

        self.ui.lblResultCount.setText(f"{searchCount}件／全{totalCount}件")

        wb.close()

    def initTable(self):
        headers = [
            "ユーザーコード",
            "氏名",
            "所属",
            "拠点",
            "メールアドレス" # 隠し列
        ]

        self.ui.tblUserSelect.setColumnCount(len(headers))
        self.ui.tblUserSelect.setHorizontalHeaderLabels(headers)
        self.ui.tblUserSelect.setRowCount(0)
        self.ui.tblUserSelect.setColumnWidth(0, 80) # ユーザーコード
        self.ui.tblUserSelect.setColumnWidth(1, 100) # 氏名
        self.ui.tblUserSelect.setColumnWidth(2, 80) # 所属
        self.ui.tblUserSelect.setColumnWidth(3, 90) # 拠点

        # メールアドレス列を非表示
        self.ui.tblUserSelect.setColumnHidden(4, True)

        self.ui.tblUserSelect.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tblUserSelect.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 行選択時イベント
        self.ui.tblUserSelect.itemSelectionChanged.connect(self.onUserSelected)

    def addUserRow(self, user_code, name, dept, base, email):
        row_position = self.ui.tblUserSelect.rowCount()
        self.ui.tblUserSelect.insertRow(row_position)

        self.ui.tblUserSelect.setItem(row_position, 0, QTableWidgetItem(user_code))
        self.ui.tblUserSelect.setItem(row_position, 1, QTableWidgetItem(name))
        self.ui.tblUserSelect.setItem(row_position, 2, QTableWidgetItem(dept))
        self.ui.tblUserSelect.setItem(row_position, 3, QTableWidgetItem(base))
        self.ui.tblUserSelect.setItem(row_position, 4, QTableWidgetItem(email)) # 隠し列にメールアドレス

    def onUserSelected(self):
        row = self.ui.tblUserSelect.currentRow()

        if row < 0:
            return

        self.selected_user_code = (self.ui.tblUserSelect.item(row, 0).text())
        self.selected_user_name = (self.ui.tblUserSelect.item(row, 1).text())
        self.selected_department = (self.ui.tblUserSelect.item(row, 2).text())
        self.selected_location = (self.ui.tblUserSelect.item(row, 3).text())
        self.selected_email = (self.ui.tblUserSelect.item(row, 4).text()) # 隠し列から取得

        print("選択ユーザー：", self.selected_user_name)
        print("選択拠点：,", self.selected_location)
        print("メールアドレス：", self.selected_email)

    def decisionUser(self):
        print("decisionUser開始")
        print(hasattr(self, "selected_user_name"))

        if self.selected_user_name is None:
            QMessageBox.warning(self, "警告", "利用者を選択してください")
            return

        parent = self.parent()
        parent.ui.lblAfterUserName.setText(self.selected_user_name)
        parent.ui.lblAfterLocation.setText(self.selected_location)
        parent.selected_user_code = self.selected_user_code
        parent.selected_department = self.selected_department
        parent.selected_email = self.selected_email

        self.close()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = UserSelectForm()
    window.show()

    sys.exit(app.exec())