# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmMain.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setMaximumSize(QSize(1200, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(420, 20, 321, 41))
        font = QFont()
        font.setFamilies([u"Meiryo"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #003366;\n"
"font-size: 24pt;\n"
"font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grpPcInfo = QGroupBox(self.centralwidget)
        self.grpPcInfo.setObjectName(u"grpPcInfo")
        self.grpPcInfo.setGeometry(QRect(60, 80, 511, 361))
        font1 = QFont()
        font1.setFamilies([u"Meiryo"])
        font1.setPointSize(20)
        self.grpPcInfo.setFont(font1)
        self.btnNewPcRegister = QPushButton(self.grpPcInfo)
        self.btnNewPcRegister.setObjectName(u"btnNewPcRegister")
        self.btnNewPcRegister.setGeometry(QRect(90, 50, 331, 51))
        font2 = QFont()
        font2.setFamilies([u"Meiryo"])
        font2.setPointSize(18)
        self.btnNewPcRegister.setFont(font2)
        self.btnNewPcRegister.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6F0FA;      /* \u901a\u5e38\uff1a\u6de1\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57 */\n"
"    border: 1px solid #AFC7E3;      /* \u8584\u3044\u9752\u306e\u67a0\u7dda */\n"
"    border-radius: 0px;             /* \u89d2\u4e38\u306a\u3057 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6E6F5;      /* \u30db\u30d0\u30fc\uff1a\u5c11\u3057\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C5D9EE;      /* \u62bc\u4e0b\uff1a\u3055\u3089\u306b\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"")
        self.btnTransfer = QPushButton(self.grpPcInfo)
        self.btnTransfer.setObjectName(u"btnTransfer")
        self.btnTransfer.setEnabled(False)
        self.btnTransfer.setGeometry(QRect(90, 120, 331, 51))
        self.btnDispose = QPushButton(self.grpPcInfo)
        self.btnDispose.setObjectName(u"btnDispose")
        self.btnDispose.setEnabled(False)
        self.btnDispose.setGeometry(QRect(90, 190, 331, 51))
        self.btnSearchEdit = QPushButton(self.grpPcInfo)
        self.btnSearchEdit.setObjectName(u"btnSearchEdit")
        self.btnSearchEdit.setEnabled(False)
        self.btnSearchEdit.setGeometry(QRect(90, 270, 331, 51))
        self.grpUserMaster = QGroupBox(self.centralwidget)
        self.grpUserMaster.setObjectName(u"grpUserMaster")
        self.grpUserMaster.setGeometry(QRect(630, 80, 511, 111))
        self.grpUserMaster.setFont(font1)
        self.btnUserMasterRegister = QPushButton(self.grpUserMaster)
        self.btnUserMasterRegister.setObjectName(u"btnUserMasterRegister")
        self.btnUserMasterRegister.setGeometry(QRect(40, 40, 201, 51))
        self.btnUserMasterRegister.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6F0FA;      /* \u901a\u5e38\uff1a\u6de1\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57 */\n"
"    border: 1px solid #AFC7E3;      /* \u8584\u3044\u9752\u306e\u67a0\u7dda */\n"
"    border-radius: 0px;             /* \u89d2\u4e38\u306a\u3057 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6E6F5;      /* \u30db\u30d0\u30fc\uff1a\u5c11\u3057\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C5D9EE;      /* \u62bc\u4e0b\uff1a\u3055\u3089\u306b\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"")
        self.btnUserMasterEdit = QPushButton(self.grpUserMaster)
        self.btnUserMasterEdit.setObjectName(u"btnUserMasterEdit")
        self.btnUserMasterEdit.setEnabled(False)
        self.btnUserMasterEdit.setGeometry(QRect(270, 40, 201, 51))
        self.grpPCMaster = QGroupBox(self.centralwidget)
        self.grpPCMaster.setObjectName(u"grpPCMaster")
        self.grpPCMaster.setGeometry(QRect(630, 210, 511, 111))
        self.grpPCMaster.setFont(font1)
        self.btnPcMasterRegister = QPushButton(self.grpPCMaster)
        self.btnPcMasterRegister.setObjectName(u"btnPcMasterRegister")
        self.btnPcMasterRegister.setGeometry(QRect(40, 40, 201, 51))
        self.btnPcMasterRegister.setStyleSheet(u"QPushButton {\n"
"    background-color: #E6F0FA;      /* \u901a\u5e38\uff1a\u6de1\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57 */\n"
"    border: 1px solid #AFC7E3;      /* \u8584\u3044\u9752\u306e\u67a0\u7dda */\n"
"    border-radius: 0px;             /* \u89d2\u4e38\u306a\u3057 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D6E6F5;      /* \u30db\u30d0\u30fc\uff1a\u5c11\u3057\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #C5D9EE;      /* \u62bc\u4e0b\uff1a\u3055\u3089\u306b\u6fc3\u3044\u9752 */\n"
"    color: #000000;                 /* \u9ed2\u5b57\u306e\u307e\u307e */\n"
"}\n"
"")
        self.btnPcMasterEdit = QPushButton(self.grpPCMaster)
        self.btnPcMasterEdit.setObjectName(u"btnPcMasterEdit")
        self.btnPcMasterEdit.setEnabled(False)
        self.btnPcMasterEdit.setGeometry(QRect(270, 40, 201, 51))
        self.grpOutput = QGroupBox(self.centralwidget)
        self.grpOutput.setObjectName(u"grpOutput")
        self.grpOutput.setGeometry(QRect(630, 340, 511, 271))
        self.grpOutput.setFont(font1)
        self.btnLocationReport = QPushButton(self.grpOutput)
        self.btnLocationReport.setObjectName(u"btnLocationReport")
        self.btnLocationReport.setEnabled(False)
        self.btnLocationReport.setGeometry(QRect(90, 50, 331, 51))
        self.btnLocationReport.setFont(font2)
        self.btnPcEtcDisposeReport = QPushButton(self.grpOutput)
        self.btnPcEtcDisposeReport.setObjectName(u"btnPcEtcDisposeReport")
        self.btnPcEtcDisposeReport.setEnabled(False)
        self.btnPcEtcDisposeReport.setGeometry(QRect(90, 120, 331, 51))
        self.btnPcEtcDisposeReport.setFont(font2)
        self.btnDisposeLabel = QPushButton(self.grpOutput)
        self.btnDisposeLabel.setObjectName(u"btnDisposeLabel")
        self.btnDisposeLabel.setEnabled(False)
        self.btnDisposeLabel.setGeometry(QRect(90, 190, 331, 51))
        self.btnDisposeLabel.setFont(font2)
        self.btnClose = QPushButton(self.centralwidget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(940, 630, 201, 51))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u30d1\u30bd\u30b3\u30f3\u7ba1\u7406\u53f0\u5e33", None))
        self.grpPcInfo.setTitle(QCoreApplication.translate("MainWindow", u"\u30d1\u30bd\u30b3\u30f3\u60c5\u5831", None))
        self.btnNewPcRegister.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u898f\u767b\u9332", None))
        self.btnTransfer.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\u30fb\u8b72\u6e21\u30fb\u4e88\u5099\u6a5f", None))
        self.btnDispose.setText(QCoreApplication.translate("MainWindow", u"\u5ec3\u68c4", None))
        self.btnSearchEdit.setText(QCoreApplication.translate("MainWindow", u"\u691c\u7d22\u30fb\u7de8\u96c6", None))
        self.grpUserMaster.setTitle(QCoreApplication.translate("MainWindow", u"\u30e6\u30fc\u30b6\u30fc\u30de\u30b9\u30bf", None))
        self.btnUserMasterRegister.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9332", None))
        self.btnUserMasterEdit.setText(QCoreApplication.translate("MainWindow", u"\u5909\u66f4\u30fb\u4fee\u6b63", None))
        self.grpPCMaster.setTitle(QCoreApplication.translate("MainWindow", u"\u30d1\u30bd\u30b3\u30f3\u30de\u30b9\u30bf", None))
        self.btnPcMasterRegister.setText(QCoreApplication.translate("MainWindow", u"\u767b\u9332", None))
        self.btnPcMasterEdit.setText(QCoreApplication.translate("MainWindow", u"\u5909\u66f4\u30fb\u4fee\u6b63", None))
        self.grpOutput.setTitle(QCoreApplication.translate("MainWindow", u"\u51fa\u529b", None))
        self.btnLocationReport.setText(QCoreApplication.translate("MainWindow", u"\u62e0\u70b9\uff65\u90e8\u5225\u30ea\u30b9\u30c8", None))
        self.btnPcEtcDisposeReport.setText(QCoreApplication.translate("MainWindow", u"PC\u7b49\u5ec3\u68c4\u30ea\u30b9\u30c8", None))
        self.btnDisposeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5ec3\u68c4\u30d1\u30bd\u30b3\u30f3\u30e9\u30d9\u30eb", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b", None))
    # retranslateUi

