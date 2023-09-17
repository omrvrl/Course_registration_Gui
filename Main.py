import sys
from PyQt5 import QtWidgets
from Form import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

#default radio seçeneğini set et                                                                    ------------> Radio
        self.ui.radio_1sinif.setChecked(True)
        self.ui.radio_1sinif_alt.setChecked(True)

        self.ui.cmb_fakulte.

#load comboBox items
    
        comboList = ['Mühendislik Mimarlık Fakültesi','Diş Hekimliği Fakültesi','Tıp Fakültesi','Hukuk Fakültesi','İktisadi ve İdari Bilimler Fakültesi']
        self.ui.cmb_fakulte.addItems(comboList)
        # if self.ui.cmb_fakulte.c
        self.LoadtoComboBox(self.ui.cmb_fakulte.currentText())

    

    def LoadtoComboBox(self,liste):

        if liste == 'Mühendislik Mimarlık Fakültesi':
            comboList2 = ['Elektik Elektronik Mühendisliği','Makina Mühendisliği','Endüstri Mühendisliği','Kimya Mühendisliği','Bilgisayar Mühendisliği']
            
        elif liste == 'Diş Hekimliği Fakültesi':
            comboList2 = ['AĞIZ, DİŞ VE ÇENE CERRAHİSİ','ENDODONTİ','ORTODONTİ','PEDODONTİ','PROTETİK DİŞ TEDAVİSİ']
            
        elif liste == 'Tıp Fakültesi':
            comboList2 = ['Temel Tıp Bilimleri Bölümü','Dahili Tıp Bilimleri Bölümü','Cerrahi Tıp Bilimleri Bölümü']

        elif liste == 'Hukuk Fakültesi':
            comboList2 = ['Anayasa Hukuku','Roma Hukuku','Ticaret Hukuku','Medeni Hukuk','Ceza Hukuku']
        
        elif liste == 'İktisadi ve İdari Bilimler Fakültesi':
            comboList2 = ['İşletme Bölümü','Maliye Bölümü','İktisat Bölümü','Siyaset Bilimi ve Kamu Yönetimi Bölümü','Uluslararası İlişkiler Bölümü(%30 İngilizce)']
            
        self.ui.cmb_bolum.addItems(comboList2)


    



def app():
    app= QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()

