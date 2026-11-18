# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmTransfer.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 660)
        Dialog.setMinimumSize(QSize(700, 660))
        Dialog.setMaximumSize(QSize(700, 660))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #FFFDF2 ;      /* \u6de1\u3044\u9ec4\u8272 */\n"
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
"    background-color: #C6A700;\n"
"    color: white;\n"
"    border: 1px solid #C6A700;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnUpdate:hover {\n"
"    background-color: #D9B800;\n"
"    border: 1px solid #D9B800;\n"
"}\n"
"\n"
"QPushButton#btnUpdate:pressed {\n"
"    background-color: #A88D00;\n"
"    border: 1px solid #A88D00;\n"
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
        self.tblTransferPc = QTableWidget(self.gbxSearchResult)
        if (self.tblTransferPc.columnCount() < 4):
            self.tblTransferPc.setColumnCount(4)
        self.tblTransferPc.setObjectName(u"tblTransferPc")
        self.tblTransferPc.setGeometry(QRect(30, 30, 570, 150))
        self.tblTransferPc.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #D0D0D0;\n"
"    background-color: white;\n"
"    gridline-color: #E5E5E5;\n"
"}")
        self.tblTransferPc.setColumnCount(4)
        self.gbxPcInfo = QGroupBox(Dialog)
        self.gbxPcInfo.setObjectName(u"gbxPcInfo")
        self.gbxPcInfo.setGeometry(QRect(40, 380, 631, 191))
        self.gbxPcInfo.setFont(font2)
        self.gbxPcInfo.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.label_9 = QLabel(self.gbxPcInfo)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 30, 71, 24))
        self.label_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_9.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_5 = QLabel(self.gbxPcInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(145, 30, 61, 26))
        self.label_5.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_10 = QLabel(self.gbxPcInfo)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(320, 30, 41, 26))
        self.label_10.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_7 = QLabel(self.gbxPcInfo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 65, 61, 26))
        self.label_7.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblTerminalName = QLabel(self.gbxPcInfo)
        self.lblTerminalName.setObjectName(u"lblTerminalName")
        self.lblTerminalName.setGeometry(QRect(205, 30, 111, 24))
        self.lblTerminalName.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblTerminalName.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblManageNo = QLabel(self.gbxPcInfo)
        self.lblManageNo.setObjectName(u"lblManageNo")
        self.lblManageNo.setGeometry(QRect(105, 30, 31, 24))
        self.lblManageNo.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblManageNo.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblManageNo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblUserName = QLabel(self.gbxPcInfo)
        self.lblUserName.setObjectName(u"lblUserName")
        self.lblUserName.setGeometry(QRect(365, 30, 101, 24))
        self.lblUserName.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblUserName.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblUserName.setFrameShape(QFrame.Shape.NoFrame)
        self.label_11 = QLabel(self.gbxPcInfo)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(465, 30, 41, 26))
        self.label_11.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblLocation = QLabel(self.gbxPcInfo)
        self.lblLocation.setObjectName(u"lblLocation")
        self.lblLocation.setGeometry(QRect(510, 30, 91, 24))
        self.lblLocation.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblLocation.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblLocation.setFrameShape(QFrame.Shape.NoFrame)
        self.cmbProcessType = QComboBox(self.gbxPcInfo)
        self.cmbProcessType.setObjectName(u"cmbProcessType")
        self.cmbProcessType.setGeometry(QRect(100, 65, 85, 26))
        self.cmbProcessType.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.stkTransfer = QStackedWidget(self.gbxPcInfo)
        self.stkTransfer.setObjectName(u"stkTransfer")
        self.stkTransfer.setGeometry(QRect(200, 60, 421, 131))
        self.pageTransfer = QWidget()
        self.pageTransfer.setObjectName(u"pageTransfer")
        self.label_12 = QLabel(self.pageTransfer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 5, 91, 26))
        self.label_12.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_13 = QLabel(self.pageTransfer)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 30, 131, 26))
        self.label_13.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_14 = QLabel(self.pageTransfer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 60, 31, 26))
        self.label_14.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtTransferUserName = QLineEdit(self.pageTransfer)
        self.txtTransferUserName.setObjectName(u"txtTransferUserName")
        self.txtTransferUserName.setGeometry(QRect(60, 60, 140, 26))
        self.txtTransferUserName.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.btnSearchTransferUser = QPushButton(self.pageTransfer)
        self.btnSearchTransferUser.setObjectName(u"btnSearchTransferUser")
        self.btnSearchTransferUser.setGeometry(QRect(100, 95, 100, 36))
        self.btnSearchTransferUser.setFont(font3)
        self.btnSearchTransferUser.setStyleSheet(u"QPushButton#btnSearchTransferUser {\n"
"    background-color: #F2F2F2;\n"
"    color: #000000;\n"
"    border: 1px solid #C8C8C8;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnSearchTransferUser:hover {\n"
"    background-color: #E6E6E6;\n"
"    border: 1px solid #BFBFBF;\n"
"}\n"
"\n"
"QPushButton#btnSearchTransferUser:pressed {\n"
"    background-color: #D9D9D9;\n"
"    border: 1px solid #B3B3B3;\n"
"}")
        self.label_15 = QLabel(self.pageTransfer)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(220, 30, 91, 26))
        self.label_15.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblAfterUserName = QLabel(self.pageTransfer)
        self.lblAfterUserName.setObjectName(u"lblAfterUserName")
        self.lblAfterUserName.setGeometry(QRect(310, 30, 101, 24))
        self.lblAfterUserName.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblAfterUserName.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblAfterUserName.setFrameShape(QFrame.Shape.NoFrame)
        self.label_16 = QLabel(self.pageTransfer)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(220, 60, 91, 26))
        self.label_16.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblAfterLocation = QLabel(self.pageTransfer)
        self.lblAfterLocation.setObjectName(u"lblAfterLocation")
        self.lblAfterLocation.setGeometry(QRect(310, 60, 91, 24))
        self.lblAfterLocation.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblAfterLocation.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblAfterLocation.setFrameShape(QFrame.Shape.NoFrame)
        self.stkTransfer.addWidget(self.pageTransfer)
        self.pageReserve = QWidget()
        self.pageReserve.setObjectName(u"pageReserve")
        self.label_17 = QLabel(self.pageReserve)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 5, 91, 26))
        self.label_17.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblReserveMessage = QLabel(self.pageReserve)
        self.lblReserveMessage.setObjectName(u"lblReserveMessage")
        self.lblReserveMessage.setGeometry(QRect(120, 60, 191, 26))
        self.lblReserveMessage.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.stkTransfer.addWidget(self.pageReserve)
        self.label_18 = QLabel(self.gbxPcInfo)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 92, 31, 26))
        self.label_18.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtRemarks = QPlainTextEdit(self.gbxPcInfo)
        self.txtRemarks.setObjectName(u"txtRemarks")
        self.txtRemarks.setGeometry(QRect(30, 120, 160, 70))
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
        QWidget.setTabOrder(self.txtUserName, self.btnSearch)
        QWidget.setTabOrder(self.btnSearch, self.tblTransferPc)
        QWidget.setTabOrder(self.tblTransferPc, self.cmbProcessType)
        QWidget.setTabOrder(self.cmbProcessType, self.txtRemarks)
        QWidget.setTabOrder(self.txtRemarks, self.txtTransferUserName)
        QWidget.setTabOrder(self.txtTransferUserName, self.btnSearchTransferUser)
        QWidget.setTabOrder(self.btnSearchTransferUser, self.btnUpdate)
        QWidget.setTabOrder(self.btnUpdate, self.btnClose)

        self.retranslateUi(Dialog)

        self.stkTransfer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u79fb\u52d5\u30fb\u8b72\u6e21\u30fb\u4e88\u5099\u6a5f", None))
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
        self.gbxSearchResult.setTitle(QCoreApplication.translate("Dialog", u"\u79fb\u52d5\u30fb\u8b72\u6e21\u30fb\u4e88\u5099\u6a5f\u306e\u5909\u66f4\u3092\u884c\u3044\u305f\u3044\u30d1\u30bd\u30b3\u30f3\u60c5\u5831\u3092\u9078\u629e", None))
        self.gbxPcInfo.setTitle(QCoreApplication.translate("Dialog", u"\u9078\u629e\u3057\u305f\u30d1\u30bd\u30b3\u30f3\u60c5\u5831\u306e\u5909\u66f4", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u7ba1\u7406\u756a\u53f7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7aef\u672b\u540d\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u6c0f\u540d\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u51e6\u7406\u7a2e\u5225", None))
        self.lblTerminalName.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.lblManageNo.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb", None))
        self.lblUserName.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u62e0\u70b9\uff1a", None))
        self.lblLocation.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5909\u66f4\u5f8c\u5229\u7528\u8005", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u3059\u308b\u6761\u4ef6\u3092\u5165\u529b", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u6c0f\u540d", None))
        self.txtTransferUserName.setText("")
        self.btnSearchTransferUser.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u5909\u66f4\u5f8c\u6c0f\u540d\uff1a", None))
        self.lblAfterUserName.setText(QCoreApplication.translate("Dialog", u"\u672a\u9078\u629e", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u5909\u66f4\u5f8c\u62e0\u70b9\uff1a", None))
        self.lblAfterLocation.setText(QCoreApplication.translate("Dialog", u"\u672a\u9078\u629e", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u4e88\u5099\u6a5f\u306b\u8a2d\u5b9a", None))
        self.lblReserveMessage.setText(QCoreApplication.translate("Dialog", u"\u305d\u306e\u307e\u307e\u300c\u66f4\u65b0\u300d\u30dc\u30bf\u30f3\u3092\u30af\u30ea\u30c3\u30af", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u5099\u8003", None))
    # retranslateUi

