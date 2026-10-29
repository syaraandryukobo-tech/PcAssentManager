from PySide6.QtWidgets import QDialog,QMessageBox,QTableWidgetItem,QAbstractItemView
from ui.frmPcMasterEdit import Ui_Dialog
import openpyxl
import os


class PcMasterEditForm(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # コンボボックスの手入力可否
        #self.ui.cmbLocation.setEditable(False)
        
        # 検索ボタン
        self.ui.btnSearch.clicked.connect(self.searchPc)
        
        # 更新ボタン
        self.ui.btnUpdate.clicked.connect(self.updatePc)
        
        # 閉じるボタン
        self.ui.btnClose.clicked.connect(self.closeWindow)
        
        # コンボボックス初期化
        self.initComboBox()
        
        # テーブル初期化
        self.initTable()

    def initComboBox(self):
        maker = [
            "",
            "Lenovo",
            "Dynabook",
            "HP"
        ]

        pctype = [
            "",
            "ノート",
            "デスクトップ"
        ]

        # メーカー
        self.ui.cmbEditMaker.clear()
        self.ui.cmbEditMaker.addItems(maker)

        # 所属
        self.ui.cmbEditPcType.clear()
        self.ui.cmbEditPcType.addItems(pctype)

    def searchPc(self):
        year =self.ui.txtYear.text()

        if year == "":
            QMessageBox.information(self,"警告","検索条件を入力してください。")
            return

        if not year.isdigit() or len(year) !=4:
            QMessageBox.warning(self, "エラー", "年度は4桁の数字で入力してください。")
            return
        
        try:
            wb = openpyxl.load_workbook("Excel/pc_list.xlsx")
            ws = wb["パソコンマスタ"]
            print("Excel読込成功")
            print("シート取得成功")
 
        except Exception as e:
            QMessageBox.critical(self,"エラー",f"Excel読込エラー\n{e}")

        print("年度：", year)

        searchCount = 0

        # 検索結果クリア
        self.ui.tblPcMaster.setRowCount(0)

        for row in ws.iter_rows(min_row=2, values_only=True):
            # 年度チェック
            if year != "" and year not in str(row[1]):
                continue

            searchCount += 1

            print(row)

            rowPosition = self.ui.tblPcMaster.rowCount()
            self.ui.tblPcMaster.insertRow(rowPosition)

            self.ui.tblPcMaster.setItem(rowPosition, 0,QTableWidgetItem(str(row[0])))
            self.ui.tblPcMaster.setItem(rowPosition, 1,QTableWidgetItem(str(row[2])))
            self.ui.tblPcMaster.setItem(rowPosition, 2,QTableWidgetItem(str(row[3])))
            self.ui.tblPcMaster.setItem(rowPosition, 3,QTableWidgetItem(str(row[4])))
            self.ui.tblPcMaster.setItem(rowPosition, 4,QTableWidgetItem(str(row[5])))

        totalCount =ws.max_row -1

        print("検索件数：", searchCount)
        print("総件数：", totalCount)

        self.ui.lblResultCount.setText(f"{searchCount}件／全{totalCount}件")

        wb.close()

    def initTable(self):
        headers = [
            "パソコンコード",
            "メーカー",
            "機種",
            "型番",
            "形態"
            ]

        self.ui.tblPcMaster.setHorizontalHeaderLabels(headers)
        self.ui.tblPcMaster.setRowCount(0)
        self.ui.tblPcMaster.setColumnWidth(0, 80) # パソコンコード
        self.ui.tblPcMaster.setColumnWidth(1, 100) # メーカー
        self.ui.tblPcMaster.setColumnWidth(2, 100) # 機種
        self.ui.tblPcMaster.setColumnWidth(3, 120) # 型番
        self.ui.tblPcMaster.setColumnWidth(4, 90) # 形態

        self.ui.tblPcMaster.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.tblPcMaster.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 行選択時イベント
        self.ui.tblPcMaster.itemSelectionChanged.connect(self.onPcSelected)

    def onPcSelected(self):
            row = self.ui.tblPcMaster.currentRow()
    
            if row < 0:
                return
    
            pc_code = self.ui.tblPcMaster.item(row, 0).text()
            maker = self.ui.tblPcMaster.item(row, 1).text()
            model = self.ui.tblPcMaster.item(row, 2).text()
            model_no = self.ui.tblPcMaster.item(row, 3).text()
            pc_type = self.ui.tblPcMaster.item(row, 4).text()
    
            print("パソコンコード：", pc_code)
            print("メーカー：", maker)
            print("機種：", model)
            print("型番：", model_no)
            print("形態：", pc_type) 
    
            self.selected_pc_code =pc_code
            self.ui.cmbEditMaker.setCurrentText(maker)
            self.ui.txtEditModel.setText(model)
            self.ui.txtEditModelNo.setText(model_no)
            self.ui.cmbEditPcType.setCurrentText(pc_type)

    def updatePc(self):
        print("更新対象")
        print(self.selected_pc_code)

        pc_code = self.selected_pc_code
        maker = self.ui.cmbEditMaker.currentText()
        model = self.ui.txtEditModel.text()
        model_no = self.ui.txtEditModelNo.text()
        pc_type =self.ui.cmbEditPcType.currentText()

        print(maker)
        print(model)
        print(model_no)
        print(pc_type)

        excel_path = os.path.join("Excel","pc_list.xlsx")
        wb = openpyxl.load_workbook(excel_path)
        ws = wb["パソコンマスタ"]

        target_row = None

        for row in range(2, ws.max_row + 1):
            excel_pc_code = ws.cell(row=row,column=1).value

            if excel_pc_code == pc_code:
                target_row = row
                break

        if target_row is not None:
            ws.cell(row=target_row, column=3, value=maker)
            ws.cell(row=target_row, column=4, value=model)
            ws.cell(row=target_row, column=5, value=model_no)
            ws.cell(row=target_row, column=6, value=pc_type)

            QMessageBox.information(self,"成功","更新できました。")

        pc_ws = wb["パソコン発番表"]

        for row in range(2, pc_ws.max_row + 1):
            pc_pc_code = pc_ws.cell(row=row, column=8).value

            if pc_pc_code == pc_code:
                pc_ws.cell(row=row, column=9,value=maker)
                pc_ws.cell(row=row, column=10, value=model)
                pc_ws.cell(row=row, column=11, value=model_no)
                pc_ws.cell(row=row, column=12, value=pc_type)

        wb.save(excel_path)    

        self.clearEditArea()
        self.searchPc()

    def clearEditArea(self):
        self.ui.cmbEditMaker.setCurrentIndex(0)      
        self.ui.txtEditModel.clear()
        self.ui.txtEditModelNo.clear()
        self.ui.cmbEditPcType.setCurrentIndex(0)
        self.selected_pc_code = None

    def closeWindow(self):
        self.close()

        if self.parent():
            self.parent().show()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = PcMasterEditForm()
    window.show()

    sys.exit(app.exec())
