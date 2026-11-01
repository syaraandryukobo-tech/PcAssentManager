# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmPcMasterEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 590)
        Dialog.setMinimumSize(QSize(700, 590))
        Dialog.setMaximumSize(QSize(700, 590))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #F0FAF2 ;      /* \u6de1\u3044\u7dd1 */\n"
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
        self.btnClose.setGeometry(QRect(520, 520, 140, 40))
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
        self.btnUpdate.setGeometry(QRect(350, 520, 140, 40))
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
        self.label_4 = QLabel(self.gbxSearchCondition)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 31, 24))
        self.label_4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_4.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtYear = QLineEdit(self.gbxSearchCondition)
        self.txtYear.setObjectName(u"txtYear")
        self.txtYear.setGeometry(QRect(70, 30, 60, 26))
        self.txtYear.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.btnSearch = QPushButton(self.gbxSearchCondition)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setGeometry(QRect(170, 24, 100, 36))
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
        self.gbxSearchResult = QGroupBox(Dialog)
        self.gbxSearchResult.setObjectName(u"gbxSearchResult")
        self.gbxSearchResult.setGeometry(QRect(40, 190, 631, 181))
        self.gbxSearchResult.setFont(font2)
        self.gbxSearchResult.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.tblPcMaster = QTableWidget(self.gbxSearchResult)
        if (self.tblPcMaster.columnCount() < 5):
            self.tblPcMaster.setColumnCount(5)
        self.tblPcMaster.setObjectName(u"tblPcMaster")
        self.tblPcMaster.setGeometry(QRect(30, 30, 570, 150))
        self.tblPcMaster.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #D0D0D0;\n"
"    background-color: white;\n"
"    gridline-color: #E5E5E5;\n"
"}")
        self.tblPcMaster.setColumnCount(5)
        self.gbxEditPcMaster = QGroupBox(Dialog)
        self.gbxEditPcMaster.setObjectName(u"gbxEditPcMaster")
        self.gbxEditPcMaster.setGeometry(QRect(40, 380, 631, 121))
        self.gbxEditPcMaster.setFont(font2)
        self.gbxEditPcMaster.setStyleSheet(u"QGroupBox {\n"
"    border: none;\n"
"}")
        self.cmbEditMaker = QComboBox(self.gbxEditPcMaster)
        self.cmbEditMaker.setObjectName(u"cmbEditMaker")
        self.cmbEditMaker.setGeometry(QRect(80, 34, 140, 26))
        self.cmbEditMaker.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_9 = QLabel(self.gbxEditPcMaster)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 34, 41, 24))
        self.label_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_9.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbEditPcType = QComboBox(self.gbxEditPcMaster)
        self.cmbEditPcType.setObjectName(u"cmbEditPcType")
        self.cmbEditPcType.setGeometry(QRect(310, 80, 120, 26))
        self.cmbEditPcType.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_5 = QLabel(self.gbxEditPcMaster)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 80, 31, 26))
        self.label_5.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtEditModelNo = QLineEdit(self.gbxEditPcMaster)
        self.txtEditModelNo.setObjectName(u"txtEditModelNo")
        self.txtEditModelNo.setGeometry(QRect(70, 80, 180, 26))
        self.txtEditModelNo.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_10 = QLabel(self.gbxEditPcMaster)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 80, 31, 26))
        self.label_10.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.label_7 = QLabel(self.gbxEditPcMaster)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 34, 31, 26))
        self.label_7.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtEditModel = QLineEdit(self.gbxEditPcMaster)
        self.txtEditModel.setObjectName(u"txtEditModel")
        self.txtEditModel.setGeometry(QRect(310, 34, 140, 26))
        self.txtEditModel.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        QWidget.setTabOrder(self.txtYear, self.btnUpdate)
        QWidget.setTabOrder(self.btnUpdate, self.btnClose)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u30d1\u30bd\u30b3\u30f3\u30de\u30b9\u30bf\u5909\u66f4\u30fb\u4fee\u6b63", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
        self.btnUpdate.setText(QCoreApplication.translate("Dialog", u"\u66f4\u65b0", None))
        self.gbxSearchCondition.setTitle(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u3059\u308b\u6761\u4ef6\u3092\u5165\u529b", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5e74\u5ea6", None))
        self.txtYear.setText("")
        self.btnSearch.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u7d50\u679c\uff1a", None))
        self.lblResultCount.setText(QCoreApplication.translate("Dialog", u"\u25cb\u4ef6\uff0f\u5168\u25cb\u4ef6", None))
        self.gbxSearchResult.setTitle(QCoreApplication.translate("Dialog", u"\u8a72\u5f53\u3059\u308b\u30d1\u30bd\u30b3\u30f3\u3092\u9078\u629e", None))
        self.gbxEditPcMaster.setTitle(QCoreApplication.translate("Dialog", u"\u9078\u629e\u3057\u305f\u30e6\u30fc\u30b6\u30fc\u306e\u5909\u66f4\u30fb\u4fee\u6b63", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u30e1\u30fc\u30ab\u30fc", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u5f62\u614b", None))
        self.txtEditModelNo.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u578b\u756a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u6a5f\u7a2e", None))
    # retranslateUi

