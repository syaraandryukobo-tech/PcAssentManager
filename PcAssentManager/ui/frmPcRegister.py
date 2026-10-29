# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmPcRegister.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 520)
        Dialog.setMinimumSize(QSize(750, 520))
        Dialog.setMaximumSize(QSize(750, 520))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #EAF4FF ;      /* \u767b\u9332\u30d5\u30a9\u30fc\u30e0\u306e\u6de1\u3044\u9752 */\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(210, 30, 321, 41))
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
        self.btnClose.setGeometry(QRect(570, 440, 140, 40))
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
        self.btnDecision = QPushButton(Dialog)
        self.btnDecision.setObjectName(u"btnDecision")
        self.btnDecision.setGeometry(QRect(400, 440, 140, 40))
        self.btnDecision.setFont(font1)
        self.btnDecision.setStyleSheet(u"QPushButton#btnDecision {\n"
"    background-color: #1A3D6E;\n"
"    color: white;\n"
"    border: 1px solid #1A3D6E;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnDecision:hover {\n"
"    background-color: #2C5AA0;\n"
"    border: 1px solid #2C5AA0;\n"
"}\n"
"\n"
"QPushButton#btnDecision:pressed {\n"
"    background-color: #102A4C;\n"
"    border: 1px solid #102A4C;\n"
"}\n"
"")
        self.grpPcSelect = QGroupBox(Dialog)
        self.grpPcSelect.setObjectName(u"grpPcSelect")
        self.grpPcSelect.setGeometry(QRect(380, 90, 340, 250))
        font2 = QFont()
        font2.setPointSize(11)
        self.grpPcSelect.setFont(font2)
        self.cmbPcYear = QComboBox(self.grpPcSelect)
        self.cmbPcYear.setObjectName(u"cmbPcYear")
        self.cmbPcYear.setGeometry(QRect(20, 30, 80, 26))
        self.cmbPcYear.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.lstPc = QListWidget(self.grpPcSelect)
        self.lstPc.setObjectName(u"lstPc")
        self.lstPc.setGeometry(QRect(110, 30, 210, 200))
        self.lstPc.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #8f8f8f;\n"
"    font-size: 10pt;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #d0e7ff;   /* \u3042\u306a\u305f\u306e\u30d5\u30a9\u30fc\u30e0\u306b\u5408\u3046\u6de1\u3044\u9752 */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e8f3ff;   /* \u30db\u30d0\u30fc\u6642\u306e\u5c11\u3057\u660e\u308b\u3044\u9752 */\n"
"}\n"
"")
        self.grpUserSelect = QGroupBox(Dialog)
        self.grpUserSelect.setObjectName(u"grpUserSelect")
        self.grpUserSelect.setGeometry(QRect(30, 90, 320, 360))
        self.grpUserSelect.setFont(font2)
        self.lstUser = QListWidget(self.grpUserSelect)
        self.lstUser.setObjectName(u"lstUser")
        self.lstUser.setGeometry(QRect(150, 30, 150, 310))
        self.lstUser.setStyleSheet(u"QListWidget {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #8f8f8f;\n"
"    font-size: 10pt;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #d0e7ff;   /* \u3042\u306a\u305f\u306e\u30d5\u30a9\u30fc\u30e0\u306b\u5408\u3046\u6de1\u3044\u9752 */\n"
"    color: #000000;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #e8f3ff;   /* \u30db\u30d0\u30fc\u6642\u306e\u5c11\u3057\u660e\u308b\u3044\u9752 */\n"
"}\n"
"")
        self.cmbUserLocation = QComboBox(self.grpUserSelect)
        self.cmbUserLocation.setObjectName(u"cmbUserLocation")
        self.cmbUserLocation.setGeometry(QRect(20, 30, 120, 26))
        self.cmbUserLocation.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        QWidget.setTabOrder(self.cmbUserLocation, self.lstUser)
        QWidget.setTabOrder(self.lstUser, self.cmbPcYear)
        QWidget.setTabOrder(self.cmbPcYear, self.lstPc)
        QWidget.setTabOrder(self.lstPc, self.btnDecision)
        QWidget.setTabOrder(self.btnDecision, self.btnClose)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u30d1\u30bd\u30b3\u30f3\u65b0\u898f\u767b\u9332", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
        self.btnDecision.setText(QCoreApplication.translate("Dialog", u"\u6c7a\u5b9a", None))
        self.grpPcSelect.setTitle(QCoreApplication.translate("Dialog", u"\u30d1\u30bd\u30b3\u30f3\u9078\u629e", None))
        self.grpUserSelect.setTitle(QCoreApplication.translate("Dialog", u"\u30e6\u30fc\u30b6\u30fc\u9078\u629e", None))
    # retranslateUi

