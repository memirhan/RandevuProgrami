from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class SaatEkle(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Saat Düzenle")
        self.resize(400, 300)
        
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

        self.addButton.clicked.connect(self.addHour)
        self.removeButton.clicked.connect(self.removeHour)

        self.connection = sqlite3.connect("saatler.db")
        self.cursor = self.connection.cursor()

        # Eğer "saatler" adında bir tablo yoksa oluştur
        self.cursor.execute("CREATE TABLE IF NOT EXISTS saatler (saat TEXT)")
        self.connection.commit()

        # Önceden eklenmiş saatleri ComboBox'a ekle
        self.loadHours()

    def loadHours(self):
        # Veritabanından saatleri al ve ComboBox'a ekle
        self.cursor.execute("SELECT * FROM saatler")
        rows = self.cursor.fetchall()
        self.hours = [row[0] for row in rows]
        self.comboBox.addItems(self.hours)

    def addHour(self):
        time, okPressed = QtWidgets.QInputDialog.getText(self, "Saat Ekle", "Saat (HH:MM):", QtWidgets.QLineEdit.Normal, "")
        if okPressed and time.strip():
            self.hours.append(time.strip())
            self.comboBox.addItem(time.strip())
            self.cursor.execute("INSERT INTO saatler (saat) VALUES (?)", (time.strip(),))
            self.connection.commit()

            if hasattr(self, 'send_hour_to_parent') and callable(self.send_hour_to_parent):
                self.send_hour_to_parent(time.strip())

    def removeHour(self):
        index = self.comboBox.currentIndex()
        if index >= 0:
            hour = self.hours[index]
            self.hours.pop(index)
            self.comboBox.removeItem(index)
            self.cursor.execute("DELETE FROM saatler WHERE saat=?", (hour,))
            self.connection.commit()

            if hasattr(self, 'send_hour_to_parent2') and callable(self.send_hour_to_parent2):
                self.send_hour_to_parent2(hour)

    def closeEvent(self, event):
        # Uygulama kapatıldığında SQLite bağlantısını kapat
        self.connection.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SaatEkle()
    MainWindow.show()
    sys.exit(app.exec_())
