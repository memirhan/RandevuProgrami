from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class SinifEkle(QtWidgets.QMainWindow):
    sinif_ekle = QtCore.pyqtSignal(str)  # Sinyal tanımlandı

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Sınıf Düzenle")
        self.setFixedSize(400, 300)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setText("+")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setText("-")
        self.gridLayout.addWidget(self.removeButton, 0, 2, 1, 1)

        self.addButton.clicked.connect(self.addSinif)
        self.removeButton.clicked.connect(self.removeSinif)

        # SQLite veritabanı bağlantısı
        self.connection = sqlite3.connect("siniflar.db")
        self.cursor = self.connection.cursor()

        # Eğer "siniflar" adında bir tablo yoksa oluştur
        self.cursor.execute("CREATE TABLE IF NOT EXISTS siniflar (sinif TEXT)")
        self.connection.commit()

        # Önceden eklenmiş sınıfları ComboBox'a ekle
        self.loadSiniflar()

    def loadSiniflar(self):
        # Veritabanından sınıfları al ve ComboBox'a ekle
        self.cursor.execute("SELECT * FROM siniflar")
        rows = self.cursor.fetchall()
        self.siniflar = [row[0] for row in rows]
        self.comboBox.addItems(self.siniflar)

    def addSinif(self):
        # Kullanıcıdan sınıfı girmesini iste
        sinif, okPressed = QtWidgets.QInputDialog.getText(self, "Sınıf Ekle", "Sınıf Adı:", QtWidgets.QLineEdit.Normal, "")
        # Kullanıcı tamam tuşuna bastıysa ve sınıf girişi yapıldıysa
        if okPressed and sinif.strip():
            # Giriş kutusundan alınan sınıfı siniflar listesine ekle
            self.siniflar.append(sinif.strip())
            # ComboBox'a yeni sınıfı ekle
            self.comboBox.addItem(sinif.strip())
            # Veritabanına yeni sınıfı ekle
            self.cursor.execute("INSERT INTO siniflar (sinif) VALUES (?)", (sinif.strip(),))
            self.connection.commit()
    

    def removeSinif(self):
        # Seçili sınıfı kaldır ve veritabanından sil
        index = self.comboBox.currentIndex()
        if index >= 0:
            sinif = self.siniflar[index]
            self.siniflar.pop(index)
            self.comboBox.removeItem(index)
            self.cursor.execute("DELETE FROM siniflar WHERE sinif=?", (sinif,))
            self.connection.commit()

            if hasattr(self, 'send_sinif_to_parent2') and callable(self.send_sinif_to_parent2):
                self.send_sinif_to_parent2(sinif)

    def closeEvent(self, event):
        # Uygulama kapatıldığında SQLite bağlantısını kapat
        self.connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SinifEkle()
    MainWindow.show()
    sys.exit(app.exec_())
