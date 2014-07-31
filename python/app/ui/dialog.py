# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 326)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        Dialog.setFont(font)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.engine = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engine.sizePolicy().hasHeightForWidth())
        self.engine.setSizePolicy(sizePolicy)
        self.engine.setObjectName("engine")
        self.verticalLayout.addWidget(self.engine)
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.verticalLayout.addWidget(self.context)
        self.apps = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apps.sizePolicy().hasHeightForWidth())
        self.apps.setSizePolicy(sizePolicy)
        self.apps.setObjectName("apps")
        self.verticalLayout.addWidget(self.apps)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushBut = QtGui.QPushButton(Dialog)
        self.pushBut.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBut.sizePolicy().hasHeightForWidth())
        self.pushBut.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(False)
        self.pushBut.setFont(font)
        self.pushBut.setMouseTracking(True)
        self.pushBut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushBut.setCheckable(False)
        self.pushBut.setObjectName("pushBut")
        self.verticalLayout.addWidget(self.pushBut)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.engine.setText(QtGui.QApplication.translate("Dialog", "Current engine :", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "The Current Context is : ", None, QtGui.QApplication.UnicodeUTF8))
        self.apps.setText(QtGui.QApplication.translate("Dialog", "Current Apps loaded : ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushBut.setToolTip(QtGui.QApplication.translate("Dialog", "Press this button ... and see what happens :)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushBut.setText(QtGui.QApplication.translate("Dialog", "Push this Button", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
