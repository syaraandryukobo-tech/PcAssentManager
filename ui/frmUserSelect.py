# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmUserSelect.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 420)
        Dialog.setMinimumSize(QSize(580, 420))
        Dialog.setMaximumSize(QSize(580, 420))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #FFFDF2 ;      /* \u6de1\u3044\u9ec4\u8272 */\n"
"}")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QRect(100, 30, 381, 41))
        font = QFont()
        font.setFamilies([u"Meiryo"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: #003366;\n"
"font-size: 24pt;\n"
"font-weight: bold;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblResultCount = QLabel(Dialog)
        self.lblResultCount.setObjectName(u"lblResultCount")
        self.lblResultCount.setGeometry(QRect(120, 110, 101, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.lblResultCount.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 110, 76, 21))
        self.label.setFont(font1)
        self.tblUserSelect = QTableWidget(Dialog)
        if (self.tblUserSelect.columnCount() < 4):
            self.tblUserSelect.setColumnCount(4)
        self.tblUserSelect.setObjectName(u"tblUserSelect")
        self.tblUserSelect.setGeometry(QRect(45, 180, 491, 150))
        self.tblUserSelect.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #D0D0D0;\n"
"    background-color: white;\n"
"    gridline-color: #E5E5E5;\n"
"}")
        self.tblUserSelect.setColumnCount(4)
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 80, 81, 26))
        self.label_13.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.btnDecision = QPushButton(Dialog)
        self.btnDecision.setObjectName(u"btnDecision")
        self.btnDecision.setGeometry(QRect(435, 350, 100, 36))
        font2 = QFont()
        font2.setFamilies([u"Meiryo"])
        font2.setPointSize(14)
        self.btnDecision.setFont(font2)
        self.btnDecision.setStyleSheet(u"QPushButton#btnDecision {\n"
"    background-color: #F2F2F2;\n"
"    color: #000000;\n"
"    border: 1px solid #C8C8C8;\n"
"    border-radius: 0px;\n"
"    padding: 4px 12px;\n"
"}\n"
"\n"
"QPushButton#btnDecision:hover {\n"
"    background-color: #E6E6E6;\n"
"    border: 1px solid #BFBFBF;\n"
"}\n"
"\n"
"QPushButton#btnDecision:pressed {\n"
"    background-color: #D9D9D9;\n"
"    border: 1px solid #B3B3B3;\n"
"}")
        self.lblSearchCondition = QLabel(Dialog)
        self.lblSearchCondition.setObjectName(u"lblSearchCondition")
        self.lblSearchCondition.setGeometry(QRect(120, 80, 91, 24))
        self.lblSearchCondition.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lblSearchCondition.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.lblSearchCondition.setFrameShape(QFrame.Shape.NoFrame)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 150, 181, 24))
        self.label_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_9.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u5229\u7528\u8005\u9078\u629e", None))
        self.lblResultCount.setText(QCoreApplication.translate("Dialog", u"\u25cb\u4ef6\uff0f\u5168\u25cb\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u7d50\u679c\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u691c\u7d22\u6761\u4ef6\uff1a", None))
        self.btnDecision.setText(QCoreApplication.translate("Dialog", u"\u6c7a\u5b9a", None))
        self.lblSearchCondition.setText(QCoreApplication.translate("Dialog", u"\u25cb\u25cb\u25cb\u25cb\u25cb", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u8a72\u5f53\u3059\u308b\u30e6\u30fc\u30b6\u30fc\u3092\u9078\u629e", None))
    # retranslateUi

