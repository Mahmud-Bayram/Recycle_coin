import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sqlite3
from Kullanici_bakiye import Kullanici_bakiye


id = 0
coin = 0

class App(QtWidgets.QMainWindow):
    def __init__(self, ad):
        super().__init__()
        width = 960
        height = 540
        uygulamaWidth = 450
        uygulamaHeight = 300
        self.setGeometry(width-uygulamaWidth, height-uygulamaHeight, uygulamaWidth*2, uygulamaHeight*2)
        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.tab_app = Tablar(self, ad)

        self.setCentralWidget(self.tab_app)
        self.show()


class Tablar(QtWidgets.QWidget):
    def __init__(self, temel, ad):
        self.baglanti_olustur()

        self.ad = ad

        super(QtWidgets.QWidget, self).__init__(temel)
        self.arayuz = QtWidgets.QVBoxLayout(self)
        self.arayuz2 = QtWidgets.QHBoxLayout(self)

        self.tablar = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tablar.resize(300, 200)

        self.tablar.addTab(self.tab1, "Ana Sayfa")
        self.tablar.addTab(self.tab2, "Dönüştür")
        self.tablar.addTab(self.tab3, "Bilgiler")

        # TAB - 1
        self.image_tab1_1 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_1.setPixmap(QtGui.QPixmap("geri_1.jpg"))
        self.image_tab1_2 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_2.setPixmap(QtGui.QPixmap("geri_2.png"))
        self.image_tab1_3 = QtWidgets.QLabel(self.tab1)
        self.image_tab1_3.setPixmap(QtGui.QPixmap("geri_3.jpg"))
        self.yaziAlani_tab1 = QtWidgets.QLabel(self.tab1)
        self.yaziAlani_tab1.move(100, 100)
        self.yaziAlani_tab1.setWindowIcon(QIcon("img.png"))
        self.degistirButon = QtWidgets.QPushButton("Değiştir")

        self.tab1.arayuz = QtWidgets.QVBoxLayout(self)
        self.tab1.arayuz2 = QtWidgets.QHBoxLayout(self)

        self.tab1.arayuz2.addWidget(self.image_tab1_1)
        self.tab1.arayuz2.addStretch()
        self.tab1.arayuz2.addWidget(self.image_tab1_2)
        self.tab1.arayuz2.addStretch()
        self.tab1.arayuz2.addWidget(self.image_tab1_3)

        self.tab1.arayuz.addLayout(self.tab1.arayuz2)
        self.tab1.arayuz.addSpacing(100)
        self.tab1.arayuz.addWidget(self.yaziAlani_tab1)
        self.tab1.arayuz.addSpacing(50)
        self.tab1.arayuz.addWidget(self.degistirButon)
        self.tab1.arayuz.addStretch()
        self.cursor.execute("Select Sözler From GeriDonusumSozleri where id = ?", (id,))
        soz = self.cursor.fetchall()
        self.yaziAlani_tab1.setText(soz[0][0])

        self.degistirButon.clicked.connect(self.Degistir)


        self.tab1.setLayout(self.tab1.arayuz)


        # TAB - 2
        self.image_tab2_1 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_1.setPixmap(QtGui.QPixmap("plastik_kucuk.jpg"))
        self.yaziAlani_tab2_1 = QtWidgets.QLabel()
        self.yaziAlani_tab2_1.setText("""Plastik olarak:
                      0,5L Şişe
                      0,33L Şişe
                      1,5L Şişe
                      2,5L Şişe
dönüştürebilirsin.""")
        self.yaziAlani_tab2_2 = QtWidgets.QLabel()
        self.yaziAlani_tab2_2.setText("""Cam olarak:
                      200ml Cam Şişe
                      500ml Cam Şişe
                      1L Cam Şişe
dönüştürebilirsin.""")
        self.yaziAlani_tab2_3 = QtWidgets.QLabel()
        self.yaziAlani_tab2_3.setText("""Kağıt olarak:
                      Gazete
                      Dergi
                      Kitap
dönüştürebilirsin.""")
        self.image_tab2_2 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_2.setPixmap(QtGui.QPixmap("cam_kucuk.jpg"))
        self.image_tab2_3 = QtWidgets.QLabel(self.tab2)
        self.image_tab2_3.setPixmap(QtGui.QPixmap("kagit_kucuk.jpg"))
        self.donusturButon = QtWidgets.QPushButton("Dönüştür")
        self.duzenleme_tab2_1 = QtWidgets.QLineEdit(self.tab2)
        self.duzenleme_tab2_1.setPlaceholderText("Ürün ismi")
        self.miktar_1 = QtWidgets.QLineEdit()
        self.miktar_1.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.miktar_1.setPlaceholderText("Ürün miktarı")
        self.miktar_1.setToolTip("Eğer hiçbir değer girmezseniz, ismini girdiğiniz üründen 1 tane dönüştürülecektir")
        self.duzenleme_tab2_2 = QtWidgets.QLineEdit(self.tab2)
        self.duzenleme_tab2_2.setPlaceholderText("Ürün ismi")
        self.miktar_2 = QtWidgets.QLineEdit()
        self.miktar_2.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.miktar_2.setPlaceholderText("Ürün miktarı")
        self.miktar_2.setToolTip("Eğer hiçbir değer girmezseniz, ismini girdiğiniz üründen 1 tane dönüştürülecektir")
        self.duzenleme_tab2_1.setPlaceholderText("Ürün ismi")
        self.duzenleme_tab2_3 = QtWidgets.QLineEdit(self.tab2)
        self.duzenleme_tab2_3.setPlaceholderText("Ürün ismi")
        self.miktar_3 = QtWidgets.QLineEdit()
        self.miktar_3.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.miktar_3.setPlaceholderText("Ürün miktarı")
        self.miktar_3.setToolTip("Eğer hiçbir değer girmezseniz, ismini girdiğiniz üründen 1 tane dönüştürülecektir")


        self.tab2.arayuzV1 = QtWidgets.QVBoxLayout(self)
        self.tab2.arayuzV2 = QtWidgets.QVBoxLayout(self)
        self.tab2.arayuzV3 = QtWidgets.QVBoxLayout(self)
        self.tab2.arayuzH = QtWidgets.QHBoxLayout(self)

        self.tab2.arayuzV1.addWidget(self.image_tab2_1)
        self.tab2.arayuzV1.addWidget(self.duzenleme_tab2_1)
        self.tab2.arayuzV1.addWidget(self.miktar_1)
        self.tab2.arayuzV1.addWidget(self.yaziAlani_tab2_1)
        self.tab2.arayuzV2.addWidget(self.image_tab2_2)
        self.tab2.arayuzV2.addWidget(self.duzenleme_tab2_2)
        self.tab2.arayuzV2.addWidget(self.miktar_2)
        # self.tab2.arayuzV2.addSpacing(35)
        self.tab2.arayuzV2.addWidget(self.yaziAlani_tab2_2)
        self.tab2.arayuzV2.addWidget(self.donusturButon)
        self.tab2.arayuzV3.addWidget(self.image_tab2_3)
        self.tab2.arayuzV3.addWidget(self.duzenleme_tab2_3)
        self.tab2.arayuzV3.addWidget(self.miktar_3)
        self.tab2.arayuzV3.addWidget(self.yaziAlani_tab2_3)

        self.tab2.arayuzH.addLayout(self.tab2.arayuzV1)
        self.tab2.arayuzH.addStretch()
        self.tab2.arayuzH.addLayout(self.tab2.arayuzV2)
        self.tab2.arayuzH.addStretch()
        self.tab2.arayuzH.addLayout(self.tab2.arayuzV3)

        self.donusturButon.clicked.connect(self.Donustur)

        self.tab2.setLayout(self.tab2.arayuzH)


        # TAB - 3
        self.aranacakSHA256 = QtWidgets.QLineEdit()
        self.aranacakSHA256.setPlaceholderText("SHA256 Adresi")
        self.aranacakSHA256.setToolTip("SHA256 adresini girerek aradığınız kişinin sahip olduğu coin ve carbon miktarını öğrenebilirsiniz.")
        self.araButon = QtWidgets.QPushButton("Kullanıcı Ara")
        self.guncelleButon = QtWidgets.QPushButton(self.tab3)
        self.guncelleButon.setText("Güncelle")
        self.guncelleButon.move(200, 435)
        self.silButon = QtWidgets.QPushButton(self.tab3)
        self.silButon.setText("Sil")
        self.silButon.move(550, 435)
        self.coinAktar = QtWidgets.QPushButton(self.tab3)
        self.coinAktar.setText("Coin Gönder")
        self.coinAktar.move(120, 375)
        self.yaziAlani_tab3 = QtWidgets.QLabel(self.tab3)
        self.yaziAlani_tab3_2 = QtWidgets.QLabel(self.tab3)
        self.adiniz = QtWidgets.QLabel(self.tab3)
        self.adiniz.setText("Ad:")
        self.adinizLine = QtWidgets.QLineEdit(self.tab3)
        self.soyadiniz = QtWidgets.QLabel(self.tab3)
        self.soyadiniz.setText("Soyad:")
        self.soyadinizLine = QtWidgets.QLineEdit(self.tab3)
        self.mailiniz = QtWidgets.QLabel(self.tab3)
        self.mailiniz.setText("Mail:")
        self.mailinizLine = QtWidgets.QLineEdit(self.tab3)
        self.kullaniciAdiniz = QtWidgets.QLabel(self.tab3)
        self.kullaniciAdiniz.setText("Kullanıcı adı:")
        self.kullaniciAdinizLine = QtWidgets.QLineEdit(self.tab3)
        self.SHA256 = QtWidgets.QLabel(self.tab3)
        self.SHA256.setText("SHA256 Adresiniz:")
        self.SHA256Line = QtWidgets.QLabel(self.tab3)
        self.carbonunuz = QtWidgets.QLabel(self.tab3)
        self.carbonunuz.setText("Carbon:")
        self.carbonunuzLine = QtWidgets.QLabel(self.tab3)
        self.coininiz = QtWidgets.QLabel(self.tab3)
        self.coininiz.setText("Recycle Coin:")
        self.coininizLine = QtWidgets.QLabel(self.tab3)

        self.cursor.execute("Select Ad, Soyad, Mail, Kullanıcı_adı, SHA256, Carbon, Coin From KullaniciBilgileri Where Ad = ?",
                            (self.ad,))
        kullanici = self.cursor.fetchall()

        ad = str(kullanici[0][0])
        soyad = str(kullanici[0][1])
        mail = str(kullanici[0][2])
        kullanici_adi = str(kullanici[0][3])
        SHA256 = str(kullanici[0][4])
        carbon = str(kullanici[0][5])
        carbonInt = int(carbon)
        coin = 0
        print(carbonInt)

        if carbonInt > 99999999:
            coin = int(carbonInt / 100000000)

        if coin > 100000000:
            self.yaziAlani_tab3.setText("100000000 üstünde Recycle Coin'e sahip olamazsanız")
            coin = 100000000
        self.cursor.execute("Update KullaniciBilgileri set Coin = ? where Ad = ?",
                            (coin, self.ad))

        self.baglanti.commit()

        self.adinizLine.setText(ad)
        self.soyadinizLine.setText(soyad)
        self.mailinizLine.setText(mail)
        self.kullaniciAdinizLine.setText(kullanici_adi)
        self.SHA256Line.setText(SHA256)
        self.carbonunuzLine.setText(carbon)
        self.coininizLine.setText(str(coin))

        self.tab3.arayuz = QtWidgets.QVBoxLayout(self)
        self.tab3.arayuzH = QtWidgets.QHBoxLayout(self)
        self.tab3.arayuzV2 = QtWidgets.QVBoxLayout(self)

        self.tab3.arayuzH.addWidget(self.aranacakSHA256)
        self.tab3.arayuzH.addWidget(self.araButon)

        self.tab3.arayuzV2.addLayout(self.tab3.arayuzH)
        self.tab3.arayuzV2.addSpacing(10)
        self.tab3.arayuzV2.addWidget(self.yaziAlani_tab3_2)

        self.tab3.arayuz.addLayout(self.tab3.arayuzV2)
        # self.tab3.arayuz.addStretch()
        self.tab3.arayuz.addWidget(self.adiniz)
        self.tab3.arayuz.addWidget(self.adinizLine)
        self.tab3.arayuz.addWidget(self.soyadiniz)
        self.tab3.arayuz.addWidget(self.soyadinizLine)
        self.tab3.arayuz.addWidget(self.mailiniz)
        self.tab3.arayuz.addWidget(self.mailinizLine)
        self.tab3.arayuz.addWidget(self.kullaniciAdiniz)
        self.tab3.arayuz.addWidget(self.kullaniciAdinizLine)
        self.tab3.arayuz.addWidget(self.SHA256)
        self.tab3.arayuz.addWidget(self.SHA256Line)
        self.tab3.arayuz.addWidget(self.carbonunuz)
        self.tab3.arayuz.addWidget(self.carbonunuzLine)
        self.tab3.arayuz.addWidget(self.coininiz)
        self.tab3.arayuz.addWidget(self.coininizLine)

        self.tab3.arayuz.addStretch()
        self.tab3.arayuz.addWidget(self.yaziAlani_tab3)
        # self.tab1.arayuz.addWidget(self.error)

        # self.yaziAlani_tab3.setMaximumHeight()

        self.guncelleButon.clicked.connect(self.guncelle)
        self.silButon.clicked.connect(self.sil)
        self.coinAktar.clicked.connect(self.Coin_aktar)
        self.araButon.clicked.connect(self.Kullanici_ara)

        self.tab3.setLayout(self.tab3.arayuz)


        self.arayuz.addWidget(self.tablar)
        self.setLayout(self.arayuz)

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()




# Tab - 1 Functions

    def Degistir(self):
        global id
        self.cursor.execute("Select Sözler From GeriDonusumSozleri where id = ?", (id,))
        soz = self.cursor.fetchall()
        self.yaziAlani_tab1.setText(soz[0][0])
        if True:
            id += 1
            if id == 20:
                id = 0


# Tab - 2 Functions

    def Donustur(self):
        self.cursor.execute("Select Carbon from KullaniciBilgileri where SHA256 = ?",(self.SHA256Line.text(),))
        carbon = self.cursor.fetchall()
        carbonInt = int(carbon[0][0])


        self.cursor.execute("Select Plastik_carbon_degeri from DonusumMaddeleri where Plastik = ?",(self.duzenleme_tab2_1.text(),))
        plastik = self.cursor.fetchall()
        self.cursor.execute("Select Cam_carbon_degeri from DonusumMaddeleri where Cam = ?",(self.duzenleme_tab2_2.text(),))
        cam = self.cursor.fetchall()
        self.cursor.execute("Select Kagıt_carbon_degeri from DonusumMaddeleri where Kagıt = ?",(self.duzenleme_tab2_3.text(),))
        kagit = self.cursor.fetchall()


        if len(plastik) > 0:
            miktar = 1
            if self.miktar_1.text() != "":
                miktar = int(self.miktar_1.text())
            carbonInt += (miktar * int(plastik[0][0]))
            coin = int(carbonInt / 100000000)

            self.cursor.execute("Update KullaniciBilgileri set Carbon = ?, Coin = ? where Ad = ?", (carbonInt, coin, self.ad))
            self.baglanti.commit()

            self.carbonunuzLine.setText(str(carbonInt))
            self.coininizLine.setText(str(coin))
            self.duzenleme_tab2_1.setText("")
            self.miktar_1.setText("")

        if len(cam) > 0:
            miktar = 1
            if self.miktar_1.text() != "":
                miktar = int(self.miktar_1.text())
            carbonInt += (miktar * int(plastik[0][0]))
            carbonInt += int(cam[0][0])
            self.cursor.execute("Update KullaniciBilgileri set Carbon = ? where Ad = ?", (carbonInt, self.ad))
            self.baglanti.commit()

            coin = int(carbonInt / 100000000)

            self.carbonunuzLine.setText(str(carbonInt))
            self.coininizLine.setText(str(coin))

            self.duzenleme_tab2_2.setText("")
            self.miktar_2.setText("")

        if len(kagit) > 0:
            miktar = 1
            if self.miktar_1.text() != "":
                miktar = int(self.miktar_1.text())
            carbonInt += (miktar * int(plastik[0][0]))
            carbonInt += int(kagit[0][0])
            self.cursor.execute("Update KullaniciBilgileri set Carbon = ? where Ad = ?", (carbonInt, self.ad))
            self.baglanti.commit()

            coin = int(carbonInt / 100000000)

            self.carbonunuzLine.setText(str(carbonInt))
            self.coininizLine.setText(str(coin))

            self.duzenleme_tab2_3.setText("")
            self.miktar_3.setText("")


# Tab - 3 Functions

    def guncelle(self):
        self.cursor.execute("Update KullaniciBilgileri set Ad = ?, Soyad = ?, Mail = ?, Kullanıcı_adı = ? where SHA256 = ?",
                    (self.adinizLine.text(), self.soyadinizLine.text(), self.mailinizLine.text(),
                     self.kullaniciAdinizLine.text(), self.SHA256Line.text()))
        self.baglanti.commit()

        self.yaziAlani_tab3.setText("Başarıyla güncelleme işlemi gerçekleştirilmiştir.")
        # time.sleep(3)
        # self.yaziAlani_tab3.setText("")


    def sil(self):
        self.eminlik = eminmisiniz(self.ad)

        self.cursor.execute("Select * from KullaniciBilgileri where Ad = ?", (self.ad,))
        hesap = self.cursor.fetchall()

    def Coin_aktar(self):
        self.coin_aktar = CoinAktar(self.SHA256Line, self.coininizLine, self.carbonunuzLine)

    def Kullanici_ara(self):
        if self.aranacakSHA256.text() == "":
            self.yaziAlani_tab3_2.setText("Lütfen bir SHA256 adresi giriniz.")
        else:
            self.cursor.execute("Select Carbon, Coin from KullaniciBilgileri where SHA256 = ?", (self.aranacakSHA256.text(),))
            kullanici = self.cursor.fetchall()
            if len(self.aranacakSHA256.text()) == 64:
                if self.SHA256Line.text() != self.aranacakSHA256.text():
                    if len(kullanici) != 0:
                        self.Kullanici_bakiye = Kullanici_bakiye(self.aranacakSHA256.text())
                        self.yaziAlani_tab3_2.setText("")
                    else:
                        self.yaziAlani_tab3_2.setText("Bu SHA256 adresine sahip herhangi biri bulunamadı.")
                else:
                    self.yaziAlani_tab3_2.setText("Bu kendi SHA256 adresiniz.")
            else:
                self.yaziAlani_tab3_2.setText("SHA256 adresi 64 birimden oluşur.")



class eminmisiniz(QtWidgets.QWidget):
    def __init__(self, ad):
        super().__init__()
        self.init_ui()

        self.ad = ad

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.onaylaButon = QtWidgets.QPushButton("Onayla")
        self.yaziAlani = QtWidgets.QLabel()
        self.yaziAlani.setText("Hesabınızı silmek istediğinize emin misiniz?")

        self.onaylaButon.close()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addStretch()
        v_box.addWidget(self.onaylaButon)

        self.setLayout(v_box)

        self.onaylaButon.clicked.connect(self.Onayla)

        width = 960
        height = 540
        uygulamaWidth = 110
        uygulamaHeight = 50
        self.setGeometry(width - uygulamaWidth, height - uygulamaHeight, uygulamaWidth * 2, uygulamaHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

    def Onayla(self):
        self.cursor.execute("Delete From KullaniciBilgileri Where Ad = ?",
                            (self.ad,))
        self.baglanti.commit()
        self.close()

class CoinAktar(QtWidgets.QWidget):
    def __init__(self, SHA256Line, coinLine, carbonLine):
        super().__init__()
        self.init_ui()

        self.SHA256Line = SHA256Line
        self.coinLine = coinLine
        self.carbonLine = carbonLine

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.gonderilecekMiktar = QtWidgets.QLabel("Gönderilecek Miktar:")
        self.gonderilecekMiktarLine = QtWidgets.QLineEdit()
        self.gonderilecekMiktarLine.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.gonderilecekKisi = QtWidgets.QLabel("Gönderilecek Kişi:")
        self.gonderilecekKisiLine = QtWidgets.QLineEdit()
        self.gonderilecekKisiLine.setPlaceholderText("SHA-256 Adresi")
        self.bilgilendirmeAlani = QtWidgets.QLabel()
        self.gonderButon = QtWidgets.QPushButton("Gönder")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.gonderilecekMiktar)
        v_box.addWidget(self.gonderilecekMiktarLine)
        v_box.addWidget(self.gonderilecekKisi)
        v_box.addWidget(self.gonderilecekKisiLine)
        v_box.addStretch()
        v_box.addWidget(self.bilgilendirmeAlani)
        v_box.addStretch()
        v_box.addWidget(self.gonderButon)

        self.setLayout(v_box)

        self.gonderButon.clicked.connect(self.Gonder)

        width = 960
        height = 540
        uygulamaWidth = 250
        uygulamaHeight = 150
        self.setGeometry(width - uygulamaWidth, height - uygulamaHeight, uygulamaWidth * 2, uygulamaHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

    def Gonder(self):
        self.cursor.execute("Select Coin, Carbon from KullaniciBilgileri where SHA256 = ?", (self.SHA256Line.text(),))
        bilgiler = self.cursor.fetchall()

        self.cursor.execute("Select Coin From KullaniciBilgileri Where SHA256 = ?", (self.gonderilecekKisiLine.text(),))
        gonderilenKisi = self.cursor.fetchall()

        print(bilgiler)

        coinInt = int(bilgiler[0][0])
        carbonInt = int(bilgiler[0][1])

        if self.gonderilecekMiktarLine.text() != "" and self.gonderilecekKisiLine.text() != "":
            if len(self.gonderilecekKisiLine.text()) == 64:
                if len(gonderilenKisi)!= 0:
                    if self.SHA256Line.text() != self.gonderilecekKisiLine.text():
                        if int(self.gonderilecekMiktarLine.text()) <= coinInt:
                            coinInt -= int(self.gonderilecekMiktarLine.text())
                            print(coinInt)
                            carbonInt -= (100000000 * int(self.gonderilecekMiktarLine.text()))
                            print(carbonInt)
                            self.cursor.execute("Update KullaniciBilgileri set Coin = ?, Carbon = ? where SHA256 = ?",
                                                (coinInt, carbonInt, self.SHA256Line.text()))

                            self.cursor.execute("Select Coin, Carbon from KullaniciBilgileri where SHA256 = ?", (self.gonderilecekKisiLine.text(),))
                            gonderilenKisiBilgiler = self.cursor.fetchall()

                            gonderilenKisiCoin = int(gonderilenKisiBilgiler[0][0])
                            gonderilenKisiCarbon = int(gonderilenKisiBilgiler[0][1])

                            gonderilenKisiCoin += int(self.gonderilecekMiktarLine.text())
                            gonderilenKisiCarbon += (100000000 * int(self.gonderilecekMiktarLine.text()))

                            self.cursor.execute("Update KullaniciBilgileri set Coin = ?, Carbon = ? where SHA256 = ?",
                                                (gonderilenKisiCoin, gonderilenKisiCarbon, self.gonderilecekKisiLine.text()))

                            self.baglanti.commit()

                            self.gonderilecekMiktarLine.setText("")
                            self.bilgilendirmeAlani.setText("Gönderme işlemi başarılı")

                            self.coinLine.setText(str(coinInt))
                            self.carbonLine.setText(str(carbonInt))

                        else:
                            self.bilgilendirmeAlani.setText("Yeterli Recycle Coin'iniz yok.")
                    else:
                        self.bilgilendirmeAlani.setText("Kendinize Recycle Coin gönderemezsiniz.")
                else:
                    self.bilgilendirmeAlani.setText("Bu SHA-256 adresine sahip herhangi bir kullanıcı bulunamadı.")
            else:
                self.bilgilendirmeAlani.setText("SHA256 adresi 64 birimden oluşur.")
        else:
            self.bilgilendirmeAlani.setText("Lütfen göndericeğiniz kişinin SHA-256 adresini ve göndermek istediğiniz Recycle \nCoin miktarını giriniz.")

        self.baglanti.commit()

# SHA-256
# 043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89
# ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb