from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import SaatEkle
import SınıfEkle

class RandevuEkle(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.randevuEkleSayfaLabel = QtWidgets.QLabel(self.centralwidget)
        self.randevuEkleSayfaLabel.setGeometry(QtCore.QRect(30, 70, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.randevuEkleSayfaLabel.setFont(font)
        self.randevuEkleSayfaLabel.setObjectName("randevuEkleSayfaLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 180, 321, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.isimLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.isimLineEdit.setObjectName("isimLineEdit")
        self.gridLayout.addWidget(self.isimLineEdit, 1, 1, 1, 1)
        self.isimLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.isimLabel.setFont(font)
        self.isimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.isimLabel.setObjectName("isimLabel")
        self.gridLayout.addWidget(self.isimLabel, 1, 0, 1, 1)
        self.soyisimLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.soyisimLineEdit.setObjectName("soyisimLineEdit")
        self.gridLayout.addWidget(self.soyisimLineEdit, 2, 1, 1, 1)
        self.soyisimLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.soyisimLabel.setFont(font)
        self.soyisimLabel.setObjectName("soyisimLabel")
        self.gridLayout.addWidget(self.soyisimLabel, 2, 0, 1, 1)

        self.kaydetButon = QtWidgets.QPushButton(self.centralwidget)
        self.kaydetButon.setGeometry(QtCore.QRect(450, 400, 201, 51))
        self.kaydetButon.setObjectName("kaydetButon")

        self.yenileButon = QtWidgets.QPushButton(self.centralwidget)
        self.yenileButon.setGeometry(QtCore.QRect(950, 80, 100, 40))
        self.yenileButon.setObjectName("yenileButon")

        self.saatDüzenleButon = QtWidgets.QPushButton(self.centralwidget)
        self.saatDüzenleButon.setGeometry(QtCore.QRect(970, 570, 120, 40))
        self.saatDüzenleButon.setObjectName("saatDüzenleButon")

        self.sınıfDüzenleButon = QtWidgets.QPushButton(self.centralwidget)
        self.sınıfDüzenleButon.setGeometry(QtCore.QRect(845, 570, 120, 40))
        self.sınıfDüzenleButon.setObjectName("sınıfDüzenleButon")

        self.saatEkleWindow = None
        self.sinifEkleWindows = None

        self.saatDüzenleButon.setText("Saat Düzenle")
        self.saatDüzenleButon.clicked.connect(self.runSaatDuzenle)

        self.sınıfDüzenleButon.setText("Sınıf Düzenle")
        self.sınıfDüzenleButon.clicked.connect(self.runSinifEkle)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(590, 350, 250, 250))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.hide()

        turkish_locale = QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey)
        self.calendarWidget.setLocale(turkish_locale)
        
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(590, 295, 260, 30))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("dd.MM.yyyy")  # Saat eklendi
        self.dateTimeEdit.mousePressEvent = self.showCalendar
        self.calendarWidget.clicked.connect(self.updateDateTimeEdit)
        
        self.sinifSecComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sinifSecComboBox.setGeometry(QtCore.QRect(590, 230, 121, 22))
        self.sinifSecComboBox.setObjectName("sinifSecComboBox")
        self.sinifSecComboBox.addItem("")
        
        self.saatSecComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.saatSecComboBox.setGeometry(QtCore.QRect(720, 230, 121, 22))
        self.saatSecComboBox.setObjectName("saatSecComboBox")
        self.saatSecComboBox.addItem("")
        

        self.geriButton = QtWidgets.QPushButton(self.centralwidget)
        self.geriButton.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.geriButton.setObjectName("geriButton")
        self.geriButton.setText("Geri")

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

        self.connection = sqlite3.connect("saatler.db")
        self.cursor = self.connection.cursor()
        self.loadHours()

        self.connection = sqlite3.connect("siniflar.db")
        self.cursor = self.connection.cursor()
        self.loadSinif()

        self.kaydetButon.clicked.connect(self.kaydet)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Randevu Ekle"))
        self.randevuEkleSayfaLabel.setText(_translate("MainWindow", "RANDEVU EKLE"))
        self.isimLabel.setText(_translate("MainWindow", "İSİM"))
        self.soyisimLabel.setText(_translate("MainWindow", "SOYİSİM"))
        self.kaydetButon.setText(_translate("MainWindow", "KAYDET"))
        self.yenileButon.setText(_translate("MainWindow", "Yenile"))

        self.sinifSecComboBox.setItemText(0, _translate("MainWindow", "Sınıf Seçiniz"))
    
        self.saatSecComboBox.setItemText(0, _translate("MainWindow", "Saat Seçiniz"))
       
        self.geriButton.clicked.connect(self.close_saatEkleWindow)
        self.geriButton.clicked.connect(self.close_sinifEkleWindows)

    def showCalendar(self, event):
        self.calendarWidget.show()

    def updateDateTimeEdit(self, date):
        selected_date = self.calendarWidget.selectedDate()
        selected_datetime = QtCore.QDateTime(selected_date)
        now = QtCore.QDateTime.currentDateTime().date()

        if selected_date < now:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Geçersiz Tarih", "Geçmiş bir tarih seçemezsiniz. Lütfen geçerli bir tarih seçin.")
            return
        
        self.dateTimeEdit.setDateTime(selected_datetime)
        self.calendarWidget.hide()

    def runSaatDuzenle(self):
        self.saat_ekle = SaatEkle.SaatEkle()
        self.saat_ekle.send_hour_to_parent = self.add_hour_to_combobox
        self.saat_ekle.send_hour_to_parent2 = self.remove_hour_from_combobox
        self.saat_ekle.show()
        self.saatEkleWindow = self.saat_ekle
    
    def close_saatEkleWindow(self):
        if self.saatEkleWindow:  # Eğer a.py penceresi açıksa
            self.saatEkleWindow.close()

    def close_sinifEkleWindows(self):
        if self.sinifEkleWindows: 
            self.sinifEkleWindows.close()
    
    def loadHours(self):
        self.cursor.execute("SELECT * FROM saatler")
        rows = self.cursor.fetchall()
        self.hour = [row[0] for row in rows]
        self.saatSecComboBox.addItems(self.hour)
        
    def add_hour_to_combobox(self, hour):
        self.saatSecComboBox.addItem(hour)

    def remove_hour_from_combobox(self, hour):
        index = self.saatSecComboBox.findText(hour)
        if index >= 0:
            self.saatSecComboBox.removeItem(index)

    def runSinifEkle(self):
        self.sinifEkle = SınıfEkle.SinifEkle()
        self.sinifEkle.send_sinif_to_parent = self.add_sinif_to_combobox
        self.sinifEkle.send_sinif_to_parent2 = self.remove_sinif_from_combobox
        self.sinifEkle.show()
        self.sinifEkleWindows = self.sinifEkle

    def loadSinif(self):
        self.cursor.execute("SELECT * FROM siniflar")
        rows = self.cursor.fetchall()
        self.sinifs = [row[0] for row in rows]
        self.sinifSecComboBox.addItems(self.sinifs)

    def add_sinif_to_combobox(self, sinifs):
        self.sinifSecComboBox.addItem(sinifs)

    def remove_sinif_from_combobox(self, sinifs):
        index = self.sinifSecComboBox.findText(sinifs)
        if index >= 0:
            self.sinifSecComboBox.removeItem(index)

    def reloadUi(self):
        MainWindow.close()
        self.setupUi(MainWindow)
        MainWindow.show()

    def kaydet(self):
        selected_date = self.dateTimeEdit.date().toString("dd.MM.yyyy")
        if selected_date == "01.01.2000" or not selected_date:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Geçersiz Tarih", "Lütfen geçerli bir tarih seçin.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RandevuEkle()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())