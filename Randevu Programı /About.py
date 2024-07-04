from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.aboutSayfaLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutSayfaLabel.setGeometry(QtCore.QRect(28, 55, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.aboutSayfaLabel.setFont(font)
        self.aboutSayfaLabel.setObjectName("aboutSayfaLabel")
        
        self.geriButton = QtWidgets.QPushButton(self.centralwidget)
        self.geriButton.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.geriButton.setObjectName("geriButton")
        self.geriButton.setText("Geri")

        self.centralLabel = QtWidgets.QLabel(self.centralwidget)
        self.centralLabel.setGeometry(QtCore.QRect(50, 150, 1000, 450))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.centralLabel.setFont(font)
        self.centralLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.centralLabel.setWordWrap(True)
        self.centralLabel.setObjectName("centralLabel")
        self.centralLabel.setText("""Rehberlik öğretmenim olarak bana kattığınız değerler ve rehberliğiniz için minnettarım. Sizin yönlendirmeleriniz ve desteğiniz sayesinde, kişisel ve akademik gelişimimde önemli adımlar attım. Bu uygulama, size olan minnettarlığımın ve takdirimin bir ifadesidir.

Rehberlikteki bilgi ve tecrübelerinizin ışığında, birçok öğrenciye yol gösterdiniz ve onlara doğru adımlar atmalarında yardımcı oldunuz. Ben de bu uygulama ile sizin bu değerli çalışmalarınızı daha da kolaylaştırmak ve daha geniş bir kitleye ulaşmanıza katkıda bulunmak istedim.

Her zaman yanımda olduğunuz ve bana inandığınız için teşekkür ederim. Bu uygulama, size ve sizin gibi değerli öğretmenlerimize olan şükran borcumun küçük bir sembolüdür. Umarım size ve öğrencilerinize faydalı olur.

Sevgi ve saygılarımla,
                                  
Muhammet Emirhan Sümer""")

        self.tarihLabel = QtWidgets.QLabel(self.centralwidget)
        self.tarihLabel.setGeometry(QtCore.QRect(20, 600, 1061, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tarihLabel.setFont(font)
        self.tarihLabel.setObjectName("tarihLabel")
        self.tarihLabel.setAlignment(QtCore.Qt.AlignRight)
        self.tarihLabel.setText("07.06.2024")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sizin İçin"))
        self.aboutSayfaLabel.setText(_translate("MainWindow", "Sizin İçin"))

