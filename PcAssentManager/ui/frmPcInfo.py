# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmPcInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 660)
        Dialog.setMinimumSize(QSize(700, 660))
        Dialog.setMaximumSize(QSize(700, 660))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #F0FAF2 ;      /* \u767b\u9332\u30d5\u30a9\u30fc\u30e0\u306e\u6de1\u3044\u7dd1 */\n"
"}")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QRect(150, 30, 381, 41))
        font = QFont()
        font.setFamilies([u"Meiryo"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #003366;\n"
"font-size: 24pt;\n"
"font-weight: bold;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnClose = QPushButton(Dialog)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(520, 590, 140, 40))
        font1 = QFont()
        font1.setFamilies([u"Meiryo"])
        font1.setPointSize(16)
        self.btnClose.setFont(font1)
        self.btnClose.setStyleSheet(u"QPushButton {\n"
"    background-color: #E0E0E0;      /* \u80cc\u666f\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    color: #000000;                 /* \u9ed2\u5b57 */\n"
"    border: 1px solid #B8B8B8;      /* \u8584\u3044\u30b0\u30ec\u30fc\u306e\u67a0\u7dda */\n"
"    border-radius: 0px;             /* \u89d2\u4e38\u306a\u3057 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D0D0D0;      /* \u30db\u30d0\u30fc\uff1a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C0C0C0;      /* \u62bc\u4e0b\uff1a\u3055\u3089\u306b\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"")
        self.btnUpdate = QPushButton(Dialog)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(350, 590, 140, 40))
        self.btnUpdate.setFont(font1)
        self.btnUpdate.setStyleSheet(u"QPushButton#btnUpdate {\n"
"    background-color: #3F7D52;\n"
"    color: white;\n"
"    border: 1px solid #3F7D52;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnUpdate:hover {\n"
"    background-color: #4E9964;\n"
"    border: 1px solid #4E9964;\n"
"}\n"
"\n"
"QPushButton#btnUpdate:pressed {\n"
"    background-color: #2F6040;\n"
"    border: 1px solid #2F6040;\n"
"}\n"
"")
        self.gbxSearchCondition = QGroupBox(Dialog)
        self.gbxSearchCondition.setObjectName(u"gbxSearchCondition")
        self.gbxSearchCondition.setGeometry(QRect(40, 80, 621, 101))
        font2 = QFont()
        font2.setPointSize(12)
        self.gbxSearchCondition.setFont(font2)
        self.gbxSearchCondition.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.cmbLocation = QComboBox(self.gbxSearchCondition)
        self.cmbLocation.setObjectName(u"cmbLocation")
        self.cmbLocation.setGeometry(QRect(70, 30, 120, 26))
        self.cmbLocation.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_4 = QLabel(self.gbxSearchCondition)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 31, 24))
        self.label_4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_4.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtUserName = QLineEdit(self.gbxSearchCondition)
        self.txtUserName.setObjectName(u"txtUserName")
        self.txtUserName.setGeometry(QRect(260, 30, 140, 26))
        self.txtUserName.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_6 = QLabel(self.gbxSearchCondition)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 30, 31, 26))
        self.label_6.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.btnSearch = QPushButton(self.gbxSearchCondition)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(450, 24, 100, 36))
        font3 = QFont()
        font3.setFamilies([u"Meiryo"])
        font3.setPointSize(14)
        self.btnSearch.setFont(font3)
        self.btnSearch.setStyleSheet(u"QPushButton#btnSearch {\n"
"    background-color: #F2F2F2;\n"
"    color: #000000;\n"
"    border: 1px solid #C8C8C8;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnSearch:hover {\n"
"    background-color: #E6E6E6;\n"
"    border: 1px solid #BFBFBF;\n"
"}\n"
"\n"
"QPushButton#btnSearch:pressed {\n"
"    background-color: #D9D9D9;\n"
"    border: 1px solid #B3B3B3;\n"
"}")
        self.label = QLabel(self.gbxSearchCondition)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 76, 21))
        font4 = QFont()
        font4.setPointSize(11)
        self.label.setFont(font4)
        self.lblResultCount = QLabel(self.gbxSearchCondition)
        self.lblResultCount.setObjectName(u"lblResultCount")
        self.lblResultCount.setGeometry(QRect(110, 70, 101, 21))
        self.lblResultCount.setFont(font4)
        self.label_2 = QLabel(self.gbxSearchCondition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(145, 3, 161, 16))
        self.gbxSearchResult = QGroupBox(Dialog)
        self.gbxSearchResult.setObjectName(u"gbxSearchResult")
        self.gbxSearchResult.setGeometry(QRect(40, 190, 631, 181))
        self.gbxSearchResult.setFont(font2)
        self.gbxSearchResult.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.tblPcInfo = QTableWidget(self.gbxSearchResult)
        if (self.tblPcInfo.columnCount() < 5):
            self.tblPcInfo.setColumnCount(5)
        self.tblPcInfo.setObjectName(u"tblPcInfo")
        self.tblPcInfo.setGeometry(QRect(30, 30, 570, 150))
        self.tblPcInfo.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #D0D0D0;\n"
"    background-color: white;\n"
"    gridline-color: #E5E5E5;\n"
"}")
        self.tblPcInfo.setColumnCount(5)
        self.gbxEditPcInfo = QGroupBox(Dialog)
        self.gbxEditPcInfo.setObjectName(u"gbxEditPcInfo")
        self.gbxEditPcInfo.setGeometry(QRect(40, 380, 631, 191))
        self.gbxEditPcInfo.setFont(font2)
        self.gbxEditPcInfo.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.label_9 = QLabel(self.gbxEditPcInfo)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 30, 71, 24))
        self.label_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_9.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_5 = QLabel(self.gbxEditPcInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 30, 61, 26))
        self.label_5.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_10 = QLabel(self.gbxEditPcInfo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(330, 30, 41, 26))
        self.label_10.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_7 = QLabel(self.gbxEditPcInfo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 70, 81, 26))
        self.label_7.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtSerialNo = QLineEdit(self.gbxEditPcInfo)
        self.txtSerialNo.setObjectName(u"txtSerialNo")
        self.txtSerialNo.setGeometry(QRect(115, 70, 180, 26))
        self.txtSerialNo.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lblTerminalName = QLabel(self.gbxEditPcInfo)
        self.lblTerminalName.setObjectName(u"lblTerminalName")
        self.lblTerminalName.setGeometry(QRect(210, 30, 111, 24))
        self.lblTerminalName.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblTerminalName.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblManageNo = QLabel(self.gbxEditPcInfo)
        self.lblManageNo.setObjectName(u"lblManageNo")
        self.lblManageNo.setGeometry(QRect(105, 30, 31, 24))
        self.lblManageNo.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblManageNo.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblManageNo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblUserName = QLabel(self.gbxEditPcInfo)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setGeometry(QRect(375, 30, 101, 24))
        self.lblUserName.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblUserName.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblUserName.setFrameShape(QFrame.Shape.NoFrame)
        self.label_11 = QLabel(self.gbxEditPcInfo)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 70, 81, 26))
        self.label_11.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtStartDate = QLineEdit(self.gbxEditPcInfo)
        self.txtStartDate.setObjectName(u"txtStartDate")
        self.txtStartDate.setGeometry(QRect(415, 70, 100, 26))
        self.txtStartDate.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_12 = QLabel(self.gbxEditPcInfo)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 115, 31, 26))
        self.label_12.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtRemarks = QPlainTextEdit(self.gbxEditPcInfo)
        self.txtRemarks.setObjectName(u"txtRemarks")
        self.txtRemarks.setGeometry(QRect(70, 120, 525, 71))
        self.txtRemarks.setStyleSheet(u"QPlainTextEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        QWidget.setTabOrder(self.cmbLocation, self.txtUserName)
        QWidget.setTabOrder(self.txtUserName, self.btnUpdate)
        QWidget.setTabOrder(self.btnUpdate, self.btnClose)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u30fb\u7de8\u96c6", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
        self.btnUpdate.setText(QCoreApplication.translate("Dialog", u"\u66f4\u65b0", None))
        self.gbxSearchCondition.setTitle(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u3059\u308b\u6761\u4ef6\u3092\u5165\u529b", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u62e0\u70b9", None))
        self.txtUserName.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6c0f\u540d", None))
        self.btnSearch.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u7d50\u679c\uff1a", None))
        self.lblResultCount.setText(QCoreApplication.translate("Dialog", u"\u25cb\u4ef6\uff0f\u5168\u25cb\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\uff08\u5165\u529b\u3057\u306a\u3044\u5834\u5408\u306f\u5168\u4ef6\u8868\u793a\uff09", None))
        self.gbxSearchResult.setTitle(QCoreApplication.translate("Dialog", u"\u8ffd\u52a0\u307e\u305f\u306f\u5909\u66f4\u30fb\u4fee\u6b63\u3092\u884c\u3044\u305f\u3044\u30d1\u30bd\u30b3\u30f3\u60c5\u5831\u304c\u3042\u308b\u5834\u5408\u306f\u9078\u629e", None))
        self.gbxEditPcInfo.setTitle(QCoreApplication.translate("Dialog", u"\u9078\u629e\u3057\u305f\u30d1\u30bd\u30b3\u30f3\u60c5\u5831\u306e\u8ffd\u52a0\u307e\u305f\u306f\u5909\u66f4\u30fb\u4fee\u6b63", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u7ba1\u7406\u756a\u53f7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7aef\u672b\u540d\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u6c0f\u540d\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u30b7\u30ea\u30a2\u30eb\u756a\u53f7", None))
        self.lblTerminalName.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.lblManageNo.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb", None))
        self.lblUserName.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\u958b\u59cb\u65e5", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5099\u8003", None))
    # retranslateUi

