# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designnJUvXW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MemoryFinder(object):
    def setupUi(self, MemoryFinder):
        if MemoryFinder.objectName():
            MemoryFinder.setObjectName(u"MemoryFinder")
        MemoryFinder.resize(800, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MemoryFinder.sizePolicy().hasHeightForWidth())
        MemoryFinder.setSizePolicy(sizePolicy)
        MemoryFinder.setMinimumSize(QSize(800, 450))
        MemoryFinder.setMaximumSize(QSize(800, 450))
        MemoryFinder.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: #121212;\n"
"\n"
"}")
        MemoryFinder.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MemoryFinder.setAnimated(False)
        self.centralwidget = QWidget(MemoryFinder)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 410, 801, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(705, 16777215))
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color: #2b2b2b;\n"
"border: none;\n"
"}")
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setText(u"")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setFrame(False)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(60, 16))
        self.pushButton.setMaximumSize(QSize(60, 16))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2b2b2b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #454545;\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 781, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"	background-color: #2b2b2b;\n"
"	borde: none;\n"
"}")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.textBrowser)

        MemoryFinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(MemoryFinder)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MemoryFinder)
    # setupUi

    def retranslateUi(self, MemoryFinder):
        MemoryFinder.setWindowTitle(QCoreApplication.translate("MemoryFinder", u"MemoryFinder", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MemoryFinder", u">>", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MemoryFinder", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

