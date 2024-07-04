from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Listele(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.randevuListeleLabel = QtWidgets.QLabel(self.centralwidget)
        self.randevuListeleLabel.setGeometry(QtCore.QRect(-95, 70, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(28)
        self.randevuListeleLabel.setFont(font)
        self.randevuListeleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.randevuListeleLabel.setObjectName("randevuListeleLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(260, 170, 600, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["İsim", "Soyisim", "Sınıf", "Saat", "Tarih"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Satır seçimini etkinleştir

        self.silButon = QtWidgets.QPushButton(self.centralwidget)
        self.silButon.setGeometry(QtCore.QRect(255, 520, 615, 40))
        font = QtGui.QFont()
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(14)
        self.silButon.setFont(font)
        self.silButon.setObjectName("silButon")
        self.silButon.setText("Seçili Kullanıcıyı Sil")
        self.silButon.clicked.connect(self.silKullanici)

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

        self.listele()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Randevu Listele"))
        self.randevuListeleLabel.setText(_translate("MainWindow", "RANDEVU LİSTELE"))

    def listele(self):
        # SQLite veritabanına bağlan
        con = sqlite3.connect("veritabani.db")
        cursor = con.cursor()

        # Veritabanından verileri al
        cursor.execute("SELECT * FROM randevular")
        rows = cursor.fetchall()

        # Satır sayısını ayarla
        self.tableWidget.setRowCount(len(rows))

        # Alınan verileri tabloya ekle
        for i, row in enumerate(rows):
            isim = row[1]
            soyisim = row[2]
            tarih = row[3]
            saat = row[4]
            sinif = row[5]
        
            item_isim = QtWidgets.QTableWidgetItem(isim)
            item_isim.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item_isim)

            item_soyisim = QtWidgets.QTableWidgetItem(soyisim)
            item_soyisim.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 1, item_soyisim)

            item_sinif = QtWidgets.QTableWidgetItem(sinif)
            item_sinif.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 2, item_sinif)

            item_saat = QtWidgets.QTableWidgetItem(saat)
            item_saat.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 3, item_saat)

            item_tarih = QtWidgets.QTableWidgetItem(tarih)
            item_tarih.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 4, item_tarih)

        # Bağlantıyı kapat
        con.close()

    def silKullanici(self):
        # Seçili satırları bul
        selected_rows = self.tableWidget.selectionModel().selectedRows()
        if not selected_rows:
            return

        # SQLite veritabanına bağlan
        con = sqlite3.connect("veritabani.db")
        cursor = con.cursor()

        # Seçili satırları sil
        for index in selected_rows:
            row = index.row()
            isim = self.tableWidget.item(row, 0).text()
            soyisim = self.tableWidget.item(row, 1).text()
            sinif = self.tableWidget.item(row, 2).text()
            saat = self.tableWidget.item(row, 3).text()
            tarih = self.tableWidget.item(row, 4).text()
            cursor.execute("DELETE FROM randevular WHERE isim = ? AND soyisim = ? AND sinif = ? AND saat = ? AND tarih = ?", (isim, soyisim, sinif, saat, tarih))
        
        # Veritabanındaki değişiklikleri kaydet
        con.commit()

        con.close()

        # Seçili satırları ters sırayla kaldır (indeks kaymalarını önlemek için)
        for index in sorted(selected_rows, reverse=True):
            self.tableWidget.removeRow(index.row())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Listele()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
