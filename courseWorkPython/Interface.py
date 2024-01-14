from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt

from Generator import generator
from threading import Thread


class Ui_MainWindow(object):
    def __init__(self):
        self.l = 180
        self.h = 23
        self.d = 12
        self.lc = 30
        self.rc = 8

        self.l_check = True
        self.h_check = True
        self.d_check = True
        self.lc_check = True
        self.rc_check = True

    def print(self):
        #print("print")
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        brush = QBrush(Qt.white)
        pen = QPen(Qt.black)
        pen.setWidth(2)

        rect = QtWidgets.QGraphicsRectItem(0, 0, self.l * 3, self.h * 3)
        rect.setBrush(brush)
        rect.setPen(pen)

        ellipse1 = QtWidgets.QGraphicsEllipseItem((self.l - 4 * self.lc) * 3, (self.rc - self.d / 2) * 3, self.d * 3, self.d * 3)
        ellipse1.setBrush(brush)
        ellipse1.setPen(pen)

        ellipse2 = QtWidgets.QGraphicsEllipseItem((self.l - 3 * self.lc) * 3, (self.h - self.d / 2 - self.rc) * 3, self.d * 3, self.d * 3)
        ellipse2.setBrush(brush)
        ellipse2.setPen(pen)

        ellipse3 = QtWidgets.QGraphicsEllipseItem((self.l - 2 * self.lc) * 3, (self.rc - self.d / 2) * 3, self.d * 3, self.d * 3)
        ellipse3.setBrush(brush)
        ellipse3.setPen(pen)

        self.scene.addItem(rect)
        self.scene.addItem(ellipse1)
        self.scene.addItem(ellipse2)
        self.scene.addItem(ellipse3)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Курсовой проект")
        MainWindow.resize(973, 810)
        MainWindow.setMaximumSize(QtCore.QSize(973, 810))
        MainWindow.setMinimumSize(QtCore.QSize(973, 810))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_calc = QtWidgets.QPushButton(self.centralwidget)
        self.but_calc.setGeometry(QtCore.QRect(760, 690, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.but_calc.setFont(font)
        self.but_calc.setObjectName("but_calc")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 721, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("content/schema.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.but_schema = QtWidgets.QPushButton(self.centralwidget)
        self.but_schema.setGeometry(QtCore.QRect(760, 580, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.but_schema.setFont(font)
        self.but_schema.setObjectName("but_schema")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 410, 721, 371))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(760, 10, 201, 551))
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(26, 95, 180)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_l = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_l.setFont(font)
        self.l_l.setAlignment(QtCore.Qt.AlignCenter)
        self.l_l.setObjectName("l_l")
        self.verticalLayout.addWidget(self.l_l)
        self.te_l = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.te_l.setFont(font)
        self.te_l.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_l.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.te_l.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_l.setObjectName("te_l")
        self.verticalLayout.addWidget(self.te_l)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.l_d = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_d.setFont(font)
        self.l_d.setAlignment(QtCore.Qt.AlignCenter)
        self.l_d.setObjectName("l_d")
        self.verticalLayout_3.addWidget(self.l_d)
        self.te_d = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.te_d.setFont(font)
        self.te_d.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_d.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_d.setObjectName("te_d")
        self.verticalLayout_3.addWidget(self.te_d)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.l_h = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_h.setFont(font)
        self.l_h.setAlignment(QtCore.Qt.AlignCenter)
        self.l_h.setObjectName("l_h")
        self.verticalLayout_2.addWidget(self.l_h)
        self.te_h = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.te_h.setFont(font)
        self.te_h.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_h.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_h.setObjectName("te_h")
        self.verticalLayout_2.addWidget(self.te_h)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_lc = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_lc.setFont(font)
        self.l_lc.setAlignment(QtCore.Qt.AlignCenter)
        self.l_lc.setObjectName("l_lc")
        self.verticalLayout_5.addWidget(self.l_lc)
        self.te_lc = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.te_lc.setFont(font)
        self.te_lc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_lc.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_lc.setObjectName("te_lc")
        self.verticalLayout_5.addWidget(self.te_lc)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_rc = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_rc.setFont(font)
        self.l_rc.setAlignment(QtCore.Qt.AlignCenter)
        self.l_rc.setObjectName("l_rc")
        self.verticalLayout_4.addWidget(self.l_rc)
        self.te_rc = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.te_rc.setFont(font)
        self.te_rc.setToolTipDuration(-1)
        self.te_rc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.te_rc.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_rc.setObjectName("te_rc")
        self.verticalLayout_4.addWidget(self.te_rc)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.te_l.setText("180")
        self.te_h.setText("23")
        self.te_d.setText("12")
        self.te_lc.setText("30")
        self.te_rc.setText("8")

        self.te_l.setStyleSheet("border: 2px solid green;")
        self.te_h.setStyleSheet("border: 2px solid green;")
        self.te_d.setStyleSheet("border: 2px solid green;")
        self.te_lc.setStyleSheet("border: 2px solid green;")
        self.te_rc.setStyleSheet("border: 2px solid green;")

        self.te_l.textChanged.connect(self.l_changed)
        self.te_h.textChanged.connect(self.h_changed)
        self.te_d.textChanged.connect(self.d_changed)
        self.te_lc.textChanged.connect(self.lc_changed)
        self.te_rc.textChanged.connect(self.rc_changed)

        self.but_schema.clicked.connect(self.print)
        self.but_calc.clicked.connect(self.generate)

    def all_correct(self):
        self.l_check = self.l > self.lc * 2 * 2
        self.d_check = self.d > 0 and self.d < self.lc and self.d / 2 < self.rc
        self.h_check = self.h > 0 and self.h > self.rc + self.d / 2
        self.lc_check = self.lc > 0 and self.lc > self.d
        self.rc_check = self.rc > 0 and self.rc < self.h - self.d / 2

        self.but_calc.setEnabled(self.isCorrect())

        if (self.l_check):
            self.te_l.setStyleSheet("border: 2px solid green;")
        else:
            self.te_l.setStyleSheet("border: 2px solid red;")        
        
        if (self.h_check):
            self.te_h.setStyleSheet("border: 2px solid green;")
        else:
            self.te_h.setStyleSheet("border: 2px solid red;")

        if (self.d_check):
            self.te_d.setStyleSheet("border: 2px solid green;")
        else:
            self.te_d.setStyleSheet("border: 2px solid red;")

        if (self.lc_check):
            self.te_lc.setStyleSheet("border: 2px solid green;")
        else:
            self.te_lc.setStyleSheet("border: 2px solid red;")

        if (self.rc_check):
            self.te_rc.setStyleSheet("border: 2px solid green;")
        else:
            self.te_rc.setStyleSheet("border: 2px solid red;")

        #self.print()


    def l_changed(self):
            self.l_check = self.te_l.toPlainText().isdigit()
            if (self.l_check):
                self.l = int(self.te_l.toPlainText()) if int(self.te_l.toPlainText()) > 0 else 0
                self.all_correct()

    def h_changed(self):
            self.h_check = self.te_h.toPlainText().isdigit()
            if (self.h_check):
                self.h = int(self.te_h.toPlainText()) if int(self.te_h.toPlainText()) > 0 else 0
                self.all_correct()

    def d_changed(self):
            self.d_check = self.te_d.toPlainText().isdigit()
            if (self.d_check):
                self.d = int(self.te_d.toPlainText()) if int(self.te_d.toPlainText()) > 0 else 0
                self.all_correct()

    def lc_changed(self):
            self.lc_check = self.te_lc.toPlainText().isdigit()
            if (self.lc_check):
                self.lc = int(self.te_lc.toPlainText()) if int(self.te_lc.toPlainText()) > 0 else 0
                self.all_correct()

    def rc_changed(self):
            self.rc_check = self.te_rc.toPlainText().isdigit()
            if (self.rc_check):
                self.rc = int(self.te_rc.toPlainText()) if int(self.te_rc.toPlainText()) > 0 else 0
                self.all_correct()


    def generate(self):
        t1 = Thread(target=generator, args=(self.l, self.h, self.d, self.lc, self.rc), daemon=True)
        t1.start()
        #generator(self.l, self.h, self.d, self.lc, self.rc)

    def isCorrect(self):
        return self.l_check and self.h_check and self.d_check and self.lc_check and self.rc_check


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовой проект"))
        self.but_calc.setText(_translate("MainWindow", "РАССЧИТАТЬ"))
        self.but_schema.setText(_translate("MainWindow", "ОТОБРАЗИТЬ"))
        self.label_2.setText(_translate("MainWindow", "ПАРАМЕТРЫ"))
        self.l_l.setText(_translate("MainWindow", "l"))
        self.l_d.setText(_translate("MainWindow", "d"))
        self.l_h.setText(_translate("MainWindow", "h"))
        self.l_lc.setText(_translate("MainWindow", "lc"))
        self.l_rc.setText(_translate("MainWindow", "rc"))
