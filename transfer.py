from PySide6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QAbstractItemView
from PySide6.QtCore import Qt
from ui.frmTransfer import Ui_Dialog
import openpyxl
import os

from user_select import UserSelectForm

class TransferForm(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lblManageNo.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.ui.btnSearch.setAutoDefault(False)
        self.ui.btnSearch.setDefault(False)

        self.ui.btnUpdate.setAutoDefault(False)
        self.ui.btnUpdate.setDefault(False)

        self.ui.btnClose.setAutoDefault(False)
        self.ui.btnClose.setDefault(False) 

        # コンボボックスの手入力可否
        self.ui.cmbLocation.setEditable(False)

        # 検索ボタン
        self.ui.btnSearch.clicked.connect(self.searchTransfer)
        self.ui.btnSearchTransferUser.clicked.connect(self.openUserSelect)

        # 更新ボタン
        self.ui.btnUpdate.clicked.connect(self.updateTransfer)

        # 閉じるボタン
        self.ui.btnClose.clicked.connect(self.closeWindow)

        # コンボボックス初期化
        self.initComboBox()

        # テーブル初期化
        self.initTable()

    def initComboBox(self):
        locations = [
            "",
            "東京本社",
            "大阪支社",
            "名古屋支社"
        ]

        process_types = [
            "移動",
            "譲渡",
            "予備機"
        ]

        # 拠点
        self.ui.cmbLocation.clear()
        self.ui.cmbLocation.addItems(locations)

        # 処理種別
        self.ui.cmbProcessType.clear()
        self.ui.cmbProcessType.addItems(process_types)

        self.ui.cmbProcessType.currentTextChanged.connect(self.changeProcessType)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            event.ignore()
            return
        super().keyPressEvent(event)

    def changeProcessType(self):
        process_type = self.ui.cmbProcessType.currentText()

        if process_type in ["移動","譲渡"]:
            self.ui.stkTransfer.setCurrentWidget(self.ui.pageTransfer)

        elif process_type == "予備機":
            self.ui.stkTransfer.setCurrentWidget(self.ui.pageReserve)

    def searchTransfer(self):
        location = self.ui.cmbLocation.currentText()
        userName =self.ui.txtUserName.text().strip()

        try:
            wb = openpyxl.load_workbook("Excel/pc_list.xlsx")
            ws = wb["パソコン発番表"]
            print("Excel読込成功")
            print("シート取得成功")

        except Exception as e:
            QMessageBox.critical(self,"エラー",f"Excel読込エラー\n{e}")

        print("拠点：", location)
        print("氏名：", userName)

        searchCount = 0

        # 検索結果クリア
        self.ui.tblTransferPc.setRowCount(0)

        for row in ws.iter_rows(min_row=2, values_only=True):
            # 拠点チェック
            if location != "" and row[6] != location:
                continue

            # 氏名チェック
            if userName != "" and userName not in str(row[4]):
                continue

            searchCount += 1

            print(row)

            rowPosition = self.ui.tblTransferPc.rowCount()
            self.ui.tblTransferPc.insertRow(rowPosition)

            manage_no = QTableWidgetItem(str(row[0]))
            manage_no.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.tblTransferPc.setItem(rowPosition, 0,manage_no)

            self.ui.tblTransferPc.setItem(rowPosition, 1, QTableWidgetItem(str(row[1])))
            # self.ui.tblTransferPc.setItem(rowPosition, 2, QTableWidgetItem(str(row[4])))

            if row[4] is None:
                user_name_text = ""
            else:
                user_name_text = str(row[4])

            user_name = QTableWidgetItem(user_name_text)
            self.ui.tblTransferPc.setItem(rowPosition, 2, user_name)

            self.ui.tblTransferPc.setItem(rowPosition, 3, QTableWidgetItem(str(row[6])))

        totalCount =ws.max_row -1

        if searchCount == 0:
            self.ui.tblTransferPc.setRowCount(1)
            self.ui.tblTransferPc.setSpan(0, 0, 1, 4)
            item = QTableWidgetItem("該当するデータはありません")
            self.ui.tblTransferPc.setItem(0, 0, item)

        print("検索件数：", searchCount)
        print("総件数：", totalCount)

        self.ui.lblResultCount.setText(f"{searchCount}件／全{totalCount}件")

        wb.close()
        
    def initTable(self):
        headers = [
            "管理番号",
            "端末名",
            "氏名",
            "拠点"
        ]

        self.ui.tblTransferPc.setHorizontalHeaderLabels(headers)
        self.ui.tblTransferPc.setRowCount(0)
        self.ui.tblTransferPc.setColumnWidth(0, 60) #  管理番号
        self.ui.tblTransferPc.setColumnWidth(1, 110) # 端末名
        self.ui.tblTransferPc.setColumnWidth(2, 100) # 氏名
        self.ui.tblTransferPc.setColumnWidth(3, 90) # 拠点

        self.ui.tblTransferPc.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tblTransferPc.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 行選択時イベント
        self.ui.tblTransferPc.itemSelectionChanged.connect(self.onTransferSelected)

    def onTransferSelected(self):
        row = self.ui.tblTransferPc.currentRow()

        if row < 0:
            return

        manage_no = self.ui.tblTransferPc.item(row,0).text()
        self.selected_manage_no = manage_no

        print("管理番号：", manage_no)

        wb = openpyxl.load_workbook("Excel/pc_list.xlsx")
        ws = wb["パソコン発番表"]

        for row in range(2, ws.max_row + 1):
            if str(ws.cell(row=row, column=1).value) == manage_no:
                self.ui.lblManageNo.setText(manage_no)
                self.ui.lblTerminalName.setText(str(ws.cell(row=row, column=2).value))
                # self.ui.lblUserName.setText(str(ws.cell(row=row, column=5).value))

                if ws.cell(row=row, column=5).value is None:
                    user_name_text = ""
                else:
                    user_name_text = str(ws.cell(row=row, column=5).value)

                self.ui.lblUserName.setText(user_name_text)

                self.ui.lblLocation.setText(str(ws.cell(row=row, column=7).value))

    def openUserSelect(self):
        user_name = self.ui.txtTransferUserName.text().strip()
        process_type = self.ui.cmbProcessType.currentText()
        current_location = self.ui.lblLocation.text()

        if self.ui.lblManageNo.text() == "○○":
            QMessageBox.warning(self, "警告", "パソコン情報を選択してください。")
            return
        
        self.userSelectForm = UserSelectForm(user_name, process_type, current_location, self)
        self.userSelectForm.show()

    def updateTransfer(self):
        process_type = self.ui.cmbProcessType.currentText()
        manage_no = self.ui.lblManageNo.text()
        terminal_name = self.ui.lblTerminalName.text()
        befor_location = self.ui.lblLocation.text()
        befor_user_name = self.ui.lblUserName.text()
        after_location = self.ui.lblAfterLocation.text()
        after_user_name = self.ui.lblAfterUserName.text()
        remarks = self.ui.txtRemarks.toPlainText()

        excel_path = os.path.join("Excel", "pc_list.xlsx")
        wb = openpyxl.load_workbook(excel_path)
        history_ws = wb["移動・譲渡等履歴"]

        history_no = history_ws.max_row
        write_row = history_ws.max_row + 1

        from datetime import datetime
        process_date = datetime.today().date()

        if process_type in ["移動","譲渡"]:
            print("履歴番号", history_no)
            print("書込み行", write_row)
            print("処理日", process_date)

            print("処理種別：", process_type)
            print("管理番号：", manage_no)
            print("端末名：", terminal_name)

            print("変更前拠点", befor_location)
            print("変更前氏名", befor_user_name)
        
            print("変更後拠点", after_location)
            print("変更後氏名", after_user_name)

            history_ws.cell(row=write_row, column=1, value=history_no)
            history_ws.cell(row=write_row, column=2, value=process_date).number_format = "yyyy/m/d"
            history_ws.cell(row=write_row, column=3, value=process_type)
            history_ws.cell(row=write_row, column=4, value=int(manage_no))
            history_ws.cell(row=write_row, column=5, value=terminal_name)
            history_ws.cell(row=write_row, column=6, value=befor_location)
            history_ws.cell(row=write_row, column=7, value=befor_user_name)
            history_ws.cell(row=write_row, column=8, value=after_location)
            history_ws.cell(row=write_row, column=9, value=after_user_name)
            history_ws.cell(row=write_row, column=10, value=remarks)

        elif process_type == "予備機":
            history_ws.cell(row=write_row, column=1, value=history_no)
            history_ws.cell(row=write_row, column=2, value=process_date).number_format = "yyyy/m/d"
            history_ws.cell(row=write_row, column=3, value=process_type)
            history_ws.cell(row=write_row, column=4, value=int(manage_no))
            history_ws.cell(row=write_row, column=5, value=terminal_name)
            history_ws.cell(row=write_row, column=6, value=befor_location)
            history_ws.cell(row=write_row, column=7, value=befor_user_name)
            history_ws.cell(row=write_row, column=8, value=befor_location)
            history_ws.cell(row=write_row, column=9, value="")
            history_ws.cell(row=write_row, column=10, value=remarks)

        #wb.save(excel_path)
        print("履歴登録完了")

        pc_ws = wb["パソコン発番表"]
        target_row = None

        for row in range(2, pc_ws.max_row + 1):
            kanri_no = pc_ws.cell(row=row, column=1).value

            if str(kanri_no) == manage_no:
                target_row = row
                break

        if process_type in ["移動","譲渡"]:        
            print("対象行：", target_row)
            print("更新前")
            print("ユーザーコード", pc_ws.cell(row=target_row, column=3).value)
            print("氏名", pc_ws.cell(row=target_row, column=5).value)
            print("所属", pc_ws.cell(row=target_row, column=6).value)
            print("拠点", pc_ws.cell(row=target_row, column=7).value)

            pc_ws.cell(row=target_row, column=3).value = self.selected_user_code
            pc_ws.cell(row=target_row, column=5).value = after_user_name
            pc_ws.cell(row=target_row, column=6).value = self.selected_department
            pc_ws.cell(row=target_row, column=7).value = after_location

            print("更新後")
            print(self.selected_user_code)
            print(after_user_name)
            print(self.selected_department)
            print(after_location)

            pc_ws.cell(row=target_row,column=3, value=self.selected_user_code)
            pc_ws.cell(row=target_row, column=4, value=self.selected_email)
            pc_ws.cell(row=target_row, column=5, value=after_user_name)
            pc_ws.cell(row=target_row, column=6, value=self.selected_department)
            pc_ws.cell(row=target_row, column=7, value=after_location)

        elif process_type == "予備機":
            pc_ws.cell(row=target_row, column=3).value = ""
            pc_ws.cell(row=target_row, column=4).value = ""
            pc_ws.cell(row=target_row, column=5).value = ""
            pc_ws.cell(row=target_row, column=6).value = ""

        QMessageBox.information(self,"成功","更新できました。")

        wb.save(excel_path)

        self.clearTransferArea()
        self.searchTransfer()

    def clearTransferArea(self):

        self.ui.lblManageNo.setText("○○")
        self.ui.lblTerminalName.setText("○○○○○○○")
        self.ui.lblUserName.setText("○○○○○○")
        self.ui.lblLocation.setText("○○○○○")

        self.ui.txtRemarks.clear()

        self.ui.txtTransferUserName.clear()

        self.ui.lblAfterUserName.setText("未選択")
        self.ui.lblAfterLocation.setText("未選択")

        self.selected_manage_no = None

    def closeWindow(self):
        self.close()

        if self.parent():
            self.parent().show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = TransferForm()
    window.show()

    sys.exit(app.exec())