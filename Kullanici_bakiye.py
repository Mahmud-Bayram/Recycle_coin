import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Kullanici_bakiye(QtWidgets.QWidget):
    def __init__(self, SHA256Line):
        super().__init__()

        self.SHA256Line = SHA256Line

        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.arananCarbon = QtWidgets.QLabel("Carbon:")
        self.arananCarbonLine = QtWidgets.QLabel()
        self.arananCoin = QtWidgets.QLabel("Coin:")
        self.arananCoinLine = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.arananCarbon)
        v_box.addWidget(self.arananCarbonLine)
        v_box.addWidget(self.arananCoin)
        v_box.addWidget(self.arananCoinLine)

        self.setLayout(v_box)
        self.cursor.execute("Select Carbon, Coin from KullaniciBilgileri where SHA256 = ?",
                            (self.SHA256Line,))
        kullanici = self.cursor.fetchall()
        carbon = kullanici[0][1]
        coin = kullanici[0][0]
        self.arananCoinLine.setText(str(carbon))
        self.arananCarbonLine.setText(str(coin))

        width = 960
        height = 540
        uygulamaWidth = 100
        uygulamaHeight = 75
        self.setGeometry(width - uygulamaWidth, height - uygulamaHeight, uygulamaWidth * 2, uygulamaHeight * 2)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

# class Kullanici_bakiye(QtWidgets.QWidget):
#     def __init__(self, SHA256Line):
#         super().__init__()
#         self.init_ui()
#
#         self.SHA256Line = SHA256Line
#
#         self.baglanti_olustur()
#
#     def baglanti_olustur(self):
#         self.baglanti = sqlite3.connect("recycle.db")
#         self.cursor = self.baglanti.cursor()
#
#         self.baglanti.commit()
#
#     def init_ui(self):
#         self.arananCarbon = QtWidgets.QLabel("Carbon:")
#         self.arananCarbonLine = QtWidgets.QLabel()
#         self.arananCoin = QtWidgets.QLabel("Coin:")
#         self.arananCoinLine = QtWidgets.QLabel()
#
#         v_box = QtWidgets.QVBoxLayout()
#         v_box.addWidget(self.arananCarbon)
#         v_box.addWidget(self.arananCarbonLine)
#         v_box.addWidget(self.arananCoin)
#         v_box.addWidget(self.arananCoinLine)
#         print(self.ad)
#         self.cursor.execute("Select Carbon, Coin from KullaniciBilgileri Where SHA256 = ?", (self.ad))
#         bakiye = self.cursor.fetchall()
#         print(bakiye[0][0])
#         self.arananCoinLine.setText(bakiye[0][0])
#         self.arananCarbonLine.setText(bakiye[0][1])
#
#         self.setLayout(v_box)
#
#         self.setGeometry(900, 200, 500, 250)
#
#         self.setWindowTitle("Geri Dönüşüm Uygulaması")
#
#         self.show()