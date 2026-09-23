# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmUserMasterRegister.ui'
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
"}\n"
"")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 100, 571, 48))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 62, 26))
        self.label.setMaximumSize(QSize(16777215, 16777203))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbEmploymentType = QComboBox(self.widget)
        self.cmbEmploymentType.setObjectName(u"cmbEmploymentType")
        self.cmbEmploymentType.setGeometry(QRect(80, 10, 120, 26))
        self.cmbEmploymentType.setMinimumSize(QSize(0, 26))
        self.cmbEmploymentType.setMaximumSize(QSize(16777215, 16777213))
        font1 = QFont()
        font1.setPointSize(10)
        self.cmbEmploymentType.setFont(font1)
        self.cmbEmploymentType.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 10, 61, 26))
        self.label_2.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;\n"
"")
        self.txtJoinYear = QLineEdit(self.widget)
        self.txtJoinYear.setObjectName(u"txtJoinYear")
        self.txtJoinYear.setGeometry(QRect(300, 10, 60, 26))
        self.txtJoinYear.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.txtJoinYear.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 10, 70, 26))
        self.label_3.setStyleSheet(u"font-size: 10pt;\n"
"color: #000000;")
        self.txtUserCode = QLineEdit(self.widget)
        self.txtUserCode.setObjectName(u"txtUserCode")
        self.txtUserCode.setGeometry(QRect(460, 10, 100, 26))
        self.txtUserCode.setStyleSheet(u"QLineEdit#txtUserCode {\n"
"    background-color: #F0F0F0;\n"
"    border: 1px solid #C0C0C0;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"")
        self.txtUserCode.setReadOnly(True)
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(60, 280, 571, 48))
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 31, 26))
        self.label_6.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtUserName = QLineEdit(self.widget_3)
        self.txtUserName.setObjectName(u"txtUserName")
        self.txtUserName.setGeometry(QRect(50, 10, 140, 26))
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
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 10, 81, 26))
        self.label_7.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.txtMailAddress = QLineEdit(self.widget_3)
        self.txtMailAddress.setObjectName(u"txtMailAddress")
        self.txtMailAddress.setGeometry(QRect(310, 10, 220, 26))
        self.txtMailAddress.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(60, 190, 571, 48))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 31, 26))
        self.label_4.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_4.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbLocation = QComboBox(self.widget_2)
        self.cmbLocation.setObjectName(u"cmbLocation")
        self.cmbLocation.setGeometry(QRect(50, 10, 120, 26))
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
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 10, 31, 26))
        self.label_5.setStyleSheet(u"font-size: 11pt;\n"
"color: #000000;")
        self.cmbDepartment = QComboBox(self.widget_2)
        self.cmbDepartment.setObjectName(u"cmbDepartment")
        self.cmbDepartment.setGeometry(QRect(240, 10, 140, 26))
        self.cmbDepartment.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #A0A0A0;   /* \u6a19\u6e96\u3088\u308a\u5c11\u3057\u6fc3\u3044\u30b0\u30ec\u30fc */\n"
"    padding: 2px;\n"
"\u3000font-size: 10pt;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #4A90E2;   /* \u6de1\u3044\u9752 */\n"
"    background-color: #FFFFFF;\n"
"}")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QRect(180, 30, 321, 41))
        font2 = QFont()
        font2.setFamilies([u"Meiryo"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: #003366;\n"
"font-size: 24pt;\n"
"font-weight: bold;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnClose = QPushButton(Dialog)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(520, 370, 140, 40))
        font3 = QFont()
        font3.setFamilies([u"Meiryo"])
        font3.setPointSize(16)
        self.btnClose.setFont(font3)
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
        self.btnRegister.setFont(font3)
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
        QWidget.setTabOrder(self.cmbEmploymentType, self.txtJoinYear)
        QWidget.setTabOrder(self.txtJoinYear, self.txtUserCode)
        QWidget.setTabOrder(self.txtUserCode, self.cmbLocation)
        QWidget.setTabOrder(self.cmbLocation, self.cmbDepartment)
        QWidget.setTabOrder(self.cmbDepartment, self.txtUserName)
        QWidget.setTabOrder(self.txtUserName, self.txtMailAddress)
        QWidget.setTabOrder(self.txtMailAddress, self.btnRegister)
        QWidget.setTabOrder(self.btnRegister, self.btnClose)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u96c7\u7528\u533a\u5206", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5165\u793e\u5e74\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u30e6\u30fc\u30b6\u30fc\u30b3\u30fc\u30c9", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6c0f\u540d", None))
        self.txtUserName.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u62e0\u70b9", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u6240\u5c5e", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u30e6\u30fc\u30b6\u30fc\u30de\u30b9\u30bf\u767b\u9332", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
        self.btnRegister.setText(QCoreApplication.translate("Dialog", u"\u767b\u9332", None))
    # retranslateUi

