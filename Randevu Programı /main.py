from PyQt5 import QtWidgets, QtCore
from Anasayfa import Anasayfa
import RandevuEkle
from About import Ui_About
from RandevuListele import Ui_Listele
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import datetime

class VeritabaniKontrolThread(QtCore.QThread):
    verilerSilindiSinyal = QtCore.pyqtSignal(bool)
    def run(self):
        while True:
            con = sqlite3.connect("veritabani.db")
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS randevular (id INTEGER PRIMARY KEY, isim TEXT, soyisim TEXT, tarih TEXT, saat TEXT, sinif TEXT)")
            cursor.execute("SELECT id, tarih, saat FROM randevular")
            su_an = datetime.datetime.now()
            veriler_silindi = False
            row = cursor.fetchone()
            while row is not None:
                kayit_id, kayit_tarih, kayit_saat = row
                
                if kayit_saat == 'Saat Seçiniz':
                    row = cursor.fetchone()
                    continue
                
                kayit_tam_tarih = datetime.datetime.strptime(kayit_tarih + " " + kayit_saat, "%d-%m-%Y %H:%M")

                if kayit_tam_tarih < su_an:
                    print(f"{kayit_id} ID'li veri silindi.")
                    cursor.execute("DELETE FROM randevular WHERE id=?", (kayit_id,))
                    veriler_silindi = True
                    
                row = cursor.fetchone()

            if veriler_silindi:
                self.verilerSilindiSinyal.emit(True)

            con.commit()
            con.close()
            self.msleep(10000)

class AnaSayfa(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_anasayfa = Anasayfa()
        self.ui_anasayfa.setupUi(self)
        self.ui_anasayfa.randevuEkle.clicked.connect(self.openRandevuEkle)
        self.ui_anasayfa.randevuListele.clicked.connect(self.openRandevuListele)
        self.ui_anasayfa.about.clicked.connect(self.openAbout)

    def saatEkle(self):
        self.ui_saat_ekle = QtWidgets.QMainWindow()
        self.ui_saat_ekle.show()

    def sinifEkle(self):
        self.uiSinifEkle = QtWidgets.QMainWindow()
        self.uiSinifEkle.show()

    def openRandevuEkle(self):
        self.randevuEkleSayfasi = RandevuEkle.RandevuEkle()
        self.randevuEkleSayfasi.setupUi(self)
        self.randevuEkleSayfasi.kaydetButon.clicked.connect(self.kaydet)
        self.randevuEkleSayfasi.geriButton.clicked.connect(self.anaSayfayaGit)
        self.randevuEkleSayfasi.yenileButon.clicked.connect(self.openRandevuEkle)

    def openRandevuListele(self):
        self.ui_randevu_listele = Ui_Listele()
        self.ui_randevu_listele.setupUi(self)
        self.ui_randevu_listele.geriButton.clicked.connect(self.anaSayfayaGit)

    def openAbout(self):
        self.ui_about = Ui_About()
        self.ui_about.setupUi(self)
        self.ui_about.geriButton.clicked.connect(self.anaSayfayaGit)

    def anaSayfayaGit(self):
        self.ui_anasayfa.setupUi(self)
        self.ui_anasayfa.randevuEkle.clicked.connect(self.openRandevuEkle)
        self.ui_anasayfa.randevuListele.clicked.connect(self.openRandevuListele)
        self.ui_anasayfa.about.clicked.connect(self.openAbout)

    def kaydet(self):
        if not self.sender() == self.randevuEkleSayfasi.kaydetButon:
            return
        
        isim = self.randevuEkleSayfasi.isimLineEdit.text()
        soyisim = self.randevuEkleSayfasi.soyisimLineEdit.text()
        tarih = self.randevuEkleSayfasi.dateTimeEdit.dateTime().toString("dd-MM-yyyy")


        saat = self.randevuEkleSayfasi.saatSecComboBox.currentText()
        secilen_sinif = self.randevuEkleSayfasi.sinifSecComboBox.currentText()
        self.randevuEkleSayfasi.saatSecComboBox.activated.connect(self.kaydet)

        secilenTarih = self.randevuEkleSayfasi.dateTimeEdit.date().toPyDate()
        secilenSaat = self.randevuEkleSayfasi.saatSecComboBox.currentText()

        suankiTarih = datetime.date.today()
        suankiSaat = QtCore.QTime.currentTime()

        secilenSaat_str = QtCore.QTime.fromString(secilenSaat, "hh:mm")


        if saat == "Saat Seçiniz":
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Geçersiz Saat", "Lütfen saat seçiniz.")

        elif secilenTarih == "01.01.2000":
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Geçersiz wergetryt", "Lütfen saat seçiniz.")
        

        elif secilen_sinif == "Sınıf Seçiniz":
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Geçersiz Sınıf", "Lütfen sınıf seçiniz.")
        
        elif secilenTarih == suankiTarih and secilenSaat_str < suankiSaat:
            QtWidgets.QMessageBox.warning(self.centralWidget(), "Geçmiş Tarih", "Geçmiş bir zamana randevu ekleyemessiniz.")
            return

        else:
            QtWidgets.QMessageBox.information(self.centralWidget(),"Randevu Eklendi", "Randevunuz başarıyla eklendi.")
            con = sqlite3.connect("veritabani.db")
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS randevular (id INTEGER PRIMARY KEY, isim TEXT, soyisim TEXT, tarih TEXT, sinif TEXT, saat TEXT)")
            cursor.execute("INSERT INTO randevular (isim, soyisim, tarih, saat, sinif) VALUES (?, ?, ?, ?, ?)", (isim, soyisim, tarih, saat, secilen_sinif))
            con.commit()
            con.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = AnaSayfa()
    MainWindow.show()

    kontrol_thread = VeritabaniKontrolThread()
    kontrol_thread.verilerSilindiSinyal.connect(lambda silindi: print("Eski veriler silindi.") if silindi else None)
    kontrol_thread.start()
    sys.exit(app.exec_())