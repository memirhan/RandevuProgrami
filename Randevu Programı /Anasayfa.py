from PyQt5 import QtCore, QtGui, QtWidgets

class Anasayfa(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hosgeldinLabel = QtWidgets.QLabel(self.centralwidget)
        self.hosgeldinLabel.setGeometry(QtCore.QRect(20, 30, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(32)
        self.hosgeldinLabel.setFont(font)
        self.hosgeldinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hosgeldinLabel.setObjectName("hosgeldinLabel")

        self.randevuEkle = QtWidgets.QPushButton(self.centralwidget)
        self.randevuEkle.setGeometry(QtCore.QRect(400, 250, 350, 70)) 
        font = QtGui.QFont()
        font.setPointSize(24)
        self.randevuEkle.setFont(font)
        self.randevuEkle.setObjectName("randevuEkle")

        self.randevuListele = QtWidgets.QPushButton(self.centralwidget)
        self.randevuListele.setGeometry(QtCore.QRect(400, 350, 350, 70))  
        font = QtGui.QFont()
        font.setPointSize(24)
        self.randevuListele.setFont(font)
        self.randevuListele.setObjectName("randevuListele")

        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(1027, 590, 50, 30))  
        font = QtGui.QFont()
        font.setPointSize(24)
        self.about.setFont(font)
        self.about.setObjectName("about")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anasayfa"))
        self.hosgeldinLabel.setText(_translate("MainWindow", "HOŞGELDİNİZ"))
        self.randevuEkle.setText(_translate("MainWindow", "RANDEVU EKLE"))
        self.randevuListele.setText(_translate("MainWindow", "RANDEVU LİSTELE"))
        self.about.setText(_translate("MainWindow", "..."))
