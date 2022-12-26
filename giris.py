import sys
import sqlite3
from Ana_sayfa import App
from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore
import time
import hashlib



class Kullanici_girisi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists KullaniciBilgileri(Ad TEXT, Soyad TEXT, Mail TEXT, Kullanıcı_adı TEXT, Şifre TEXT, SHA256 TEXT, Carbon INTEGER, Coin INTEGER)")
        self.cursor.execute("Create Table If not exists GeriDonusumSozleri(id INTEGER, Sözler TEXT)")
        self.cursor.execute("Create Table If not exists DonusumMaddeleri(Plastik TEXT, Plastik_carbon_degeri INTEGER, Cam TEXT, Cam_carbon_degeri INTEGER, Kagıt TEXT, Kagıt_carbon_degeri INTEGER)")

        self.baglanti.commit()

    def init_ui(self):
        self.kullanıcıAdıLabel = QtWidgets.QLabel("Kullanıcı Adı")
        self.kullanıcıAdı = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.kayit = QtWidgets.QPushButton("Kayıt Ol")
        self.yaziAlanı = QtWidgets.QLabel()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcıAdıLabel)
        v_box.addWidget(self.kullanıcıAdı)
        v_box.addWidget(self.passwordLabel)
        v_box.addWidget(self.password)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)
        v_box.addStretch()
        v_box.addWidget(self.yaziAlanı)
        v_box.addStretch()

        self.setLayout(v_box)

        self.giris.clicked.connect(self.Giris)
        self.password.returnPressed.connect(self.gir)
        self.kayit.clicked.connect(self.Kayit_olma)

        width = 960
        height = 540
        uygulamaWidth = 160
        uygulamaHeight = 125
        self.setGeometry(width - uygulamaWidth, height - uygulamaHeight, uygulamaWidth * 2, uygulamaHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

    def Giris(self):
        if self.kullanıcıAdı.text() != "" and self.password.text() != "":
            self.cursor.execute("Select * From KullaniciBilgileri Where Kullanıcı_adı = ? and Şifre = ?",
                                (self.kullanıcıAdı.text(), self.password.text()))
            kullanici = self.cursor.fetchall()

            if len(kullanici) != 0:
                self.close()
                time.sleep(1)
                self.kullanici_bilgilendirme = App(kullanici[0][0])


            else:
                self.yaziAlanı.setText("Girdiğiniz kullanıcı adı veya şifre hatalı.")

        else:
            self.yaziAlanı.setText("Lütfen kullanıcı adı ve parola bölümünü doldurunuz")

    def gir(self):
        if self.kullanıcıAdı.text() != "" and self.password.text() != "":
            self.cursor.execute("Select * From KullaniciBilgileri Where Kullanıcı_adı = ? and Şifre = ?",
                                (self.kullanıcıAdı.text(), self.password.text()))
            kullanici = self.cursor.fetchall()
            if len(kullanici) != 0:
                self.close()
                time.sleep(1)
                self.kullanici_bilgilendirme = App(kullanici[0][0])

            else:
                self.yaziAlanı.setText("Girdiğiniz kullanıcı adı veya şifre hatalı.")

        else:
            self.yaziAlanı.setText("Lütfen kullanıcı adı ve parola bölümünü doldurunuz")


    def Kayit_olma(self):
        self.close()
        time.sleep(1)
        self.kullanici_kayiti = Kullanici_kayiti()

# class Kullanici_bilgilendirme(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#         self.baglanti_olustur()
#
#     def baglanti_olustur(self):
#         self.baglanti = sqlite3.connect("recycle.db")
#
#         self.imlec = self.baglanti.cursor()
#
#         self.baglanti.commit()
#
#     def init_ui(self):
#
#         self.setGeometry(50, 50, 1800, 950)
#
#         self.setWindowTitle("Okul Kayıt Sistemi")
#
#         self.show()

class Kullanici_kayiti(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")

        self.imlec = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.adLabel = QtWidgets.QLabel("Ad")
        self.ad = QtWidgets.QLineEdit()
        self.soyadLabel = QtWidgets.QLabel("Soyad")
        self.soyad = QtWidgets.QLineEdit()
        self.mailLabel = QtWidgets.QLabel("Mail")
        self.mail = QtWidgets.QLineEdit()
        self.kullanıcıAdıLabel = QtWidgets.QLabel("Kullanıcı Adı")
        self.kullanıcıAdı = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordDoğrulamaLabel = QtWidgets.QLabel("Password Doğrulama")
        self.passwordDoğrulama = QtWidgets.QLineEdit()
        self.passwordDoğrulama.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kayitOl = QtWidgets.QPushButton("Kayıt Ol")
        self.giris = QtWidgets.QPushButton("Giriş")
        self.geri = QtWidgets.QPushButton("Geri")
        self.yaziAlanı = QtWidgets.QLabel()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.geri)
        h_box.addStretch()


        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.adLabel)
        v_box.addWidget(self.ad)
        v_box.addWidget(self.soyadLabel)
        v_box.addWidget(self.soyad)
        v_box.addWidget(self.mailLabel)
        v_box.addWidget(self.mail)
        v_box.addWidget(self.kullanıcıAdıLabel)
        v_box.addWidget(self.kullanıcıAdı)
        v_box.addWidget(self.passwordLabel)
        v_box.addWidget(self.password)
        v_box.addWidget(self.passwordDoğrulamaLabel)
        v_box.addWidget(self.passwordDoğrulama)
        v_box.addStretch()
        v_box.addWidget(self.kayitOl)
        v_box.addStretch()
        v_box.addWidget(self.yaziAlanı)
        v_box.addStretch()

        self.setLayout(v_box)

        self.kayitOl.clicked.connect(self.Kayit_olma)
        self.geri.clicked.connect(self.Geri)

        width = 960
        height = 540
        uygulamaWidth = 160
        uygulamaHeight = 250
        self.setGeometry(width - uygulamaWidth, height - uygulamaHeight, uygulamaWidth * 2, uygulamaHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

    def Kayit_olma(self):
        ad= self.ad.text()
        soyad= self.soyad.text()
        mail= self.mail.text()
        kullanıcıAdı= self.kullanıcıAdı.text()
        password= self.password.text()
        hashedSifre = hashlib.sha256(self.password.text().encode("UTF-8")).hexdigest()

        if ad != "" and soyad != "" and mail != "" and kullanıcıAdı != "" and password != "" and self.passwordDoğrulama.text() != "":
            if self.password.text() != self.passwordDoğrulama.text():
                self.yaziAlanı.setText("Girdiğiniz şifreler uyuşmuyor.")
            else:
                self.imlec.execute("Insert into KullaniciBilgileri Values(?, ?, ?, ?, ?, ?, 0, 0)", (ad, soyad, mail, kullanıcıAdı, password, hashedSifre))
                self.baglanti.commit()
                self.close()
                time.sleep(1)
                self.Kullanici_girisi = Kullanici_girisi()

        else:
            self.yaziAlanı.setText("Lütfen tüm alanları doldurunuz.")

    def Geri(self):
        self.close()
        time.sleep(1)
        self.Kullanici_girisi = Kullanici_girisi()

app = QtWidgets.QApplication(sys.argv)
kullanici_girisi = Kullanici_girisi()
sys.exit(app.exec_())


