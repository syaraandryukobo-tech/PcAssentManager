# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmPcMasterRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 450)
        Dialog.setMinimumSize(QSize(700, 450))
        Dialog.setMaximumSize(QSize(700, 450))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #EAF4FF ;      /* \u767b\u9332\u30d5\u30a9\u30fc\u30e0\u306e\u6de1\u3044\u9752 */\n"
"}")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(60, 190, 571, 48))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 41, 26))
        self.label_4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_4.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbMaker = QComboBox(self.widget_2)
        self.cmbMaker.setObjectName(u"cmbMaker")
        self.cmbMaker.setGeometry(QRect(60, 10, 140, 26))
        self.cmbMaker.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 10, 31, 26))
        self.label_5.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtModel = QLineEdit(self.widget_2)
        self.txtModel.setObjectName(u"txtModel")
        self.txtModel.setGeometry(QRect(280, 10, 140, 26))
        self.txtModel.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.txtModel.setReadOnly(False)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 100, 571, 48))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 31, 26))
        self.label_2.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;\n"
"")
        self.txtYear = QLineEdit(self.widget)
        self.txtYear.setObjectName(u"txtYear")
        self.txtYear.setGeometry(QRect(50, 10, 60, 26))
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
        self.txtYear.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 10, 70, 26))
        self.label_3.setStyleSheet(u"font-size: 10pt;\n"
"color: #000000;")
        self.txtPcCode = QLineEdit(self.widget)
        self.txtPcCode.setObjectName(u"txtPcCode")
        self.txtPcCode.setGeometry(QRect(230, 10, 100, 26))
        self.txtPcCode.setStyleSheet(u"QLineEdit#txtPcCode {\n"
"    background-color: #F0F0F0;\n"
"    border: 1px solid #C0C0C0;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"")
        self.txtPcCode.setReadOnly(True)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(180, 30, 321, 41))
        font = QFont()
        font.setFamilies([u"Meiryo"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #003366;\n"
"font-size: 24pt;\n"
"font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnClose = QPushButton(Dialog)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(520, 370, 140, 40))
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
        self.btnRegister = QPushButton(Dialog)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(350, 370, 140, 40))
        self.btnRegister.setFont(font1)
        self.btnRegister.setStyleSheet(u"QPushButton#btnRegister {\n"
"    background-color: #1A3D6E;\n"
"    color: white;\n"
"    border: 1px solid #1A3D6E;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnRegister:hover {\n"
"    background-color: #2C5AA0;\n"
"    border: 1px solid #2C5AA0;\n"
"}\n"
"\n"
"QPushButton#btnRegister:pressed {\n"
"    background-color: #102A4C;\n"
"    border: 1px solid #102A4C;\n"
"}\n"
"")
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(60, 280, 571, 48))
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 31, 26))
        self.label_6.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtModelNo = QLineEdit(self.widget_3)
        self.txtModelNo.setObjectName(u"txtModelNo")
        self.txtModelNo.setGeometry(QRect(50, 10, 180, 26))
        self.txtModelNo.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 10, 31, 26))
        self.label_7.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbPcType = QComboBox(self.widget_3)
        self.cmbPcType.setObjectName(u"cmbPcType")
        self.cmbPcType.setGeometry(QRect(300, 10, 120, 26))
        self.cmbPcType.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        QWidget.setTabOrder(self.txtYear, self.txtPcCode)
        QWidget.setTabOrder(self.txtPcCode, self.cmbMaker)
        QWidget.setTabOrder(self.cmbMaker, self.txtModel)
        QWidget.setTabOrder(self.txtModel, self.txtModelNo)
        QWidget.setTabOrder(self.txtModelNo, self.cmbPcType)
        QWidget.setTabOrder(self.cmbPcType, self.btnRegister)
        QWidget.setTabOrder(self.btnRegister, self.btnClose)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u30e1\u30fc\u30ab\u30fc", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6a5f\u7a2e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5e74\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u30d1\u30bd\u30b3\u30f3\u30b3\u30fc\u30c9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u30d1\u30bd\u30b3\u30f3\u30de\u30b9\u30bf\u767b\u9332", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
        self.btnRegister.setText(QCoreApplication.translate("Dialog", u"\u767b\u9332", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u578b\u756a", None))
        self.txtModelNo.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5f62\u614b", None))
    # retranslateUi

