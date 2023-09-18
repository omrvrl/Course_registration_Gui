import sys
from PyQt5 import QtWidgets
from Form import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

#DEFAULT RADİO BUTON İTEM                                    -----------------> RADIO
        self.ui.radio_4sinif.setChecked(True)
        self.ui.radio_1sinif_alt.setChecked(True)


#DEFAULT COMBOBOX PROMPT                                    ---------------> COMBOBOX
    
        comboList = ['Mühendislik Mimarlık Fakültesi','Diş Hekimliği Fakültesi','Tıp Fakültesi','Hukuk Fakültesi','İktisadi ve İdari Bilimler Fakültesi']
        self.ui.cmb_fakulte.addItems(comboList)
        comboList2 = ['Elektrik Elektronik Mühendisliği','Makina Mühendisliği','Endüstri Mühendisliği','Kimya Mühendisliği','Bilgisayar Mühendisliği']
        self.ui.cmb_bolum.addItems(comboList2)


# TABLE WİDGET CONFİGURATION
        self.ui.Table_acilandersler.setRowCount(5)
        self.ui.Table_acilandersler.setColumnCount(4)
        self.ui.Table_acilandersler.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))
        self.ui.Table_acilandersler.setColumnWidth(0,150)
        self.ui.Table_acilandersler.setColumnWidth(1,200)
        
#CONNECT TO FUNCTİONS                                         
        self.ui.cmb_fakulte.currentIndexChanged.connect(self.SelectFakulte)
        self.ui.cmb_bolum.currentIndexChanged.connect(self.SelectFakulte)
        self.ui.radio_1sinif.toggled.connect(self.SelectFakulte)
        self.ui.radio_2sinif.toggled.connect(self.SelectFakulte)
        self.ui.radio_3sinif.toggled.connect(self.SelectFakulte)
        self.ui.radio_4sinif.toggled.connect(self.SelectFakulte)

    def SelectYear(self):
        


    def SelectFakulte(self):
        self.ui.cmb_bolum.clear()
        Selected_fakulte = self.ui.cmb_fakulte.currentText()

        if Selected_fakulte == 'Mühendislik Mimarlık Fakültesi':
            comboList2 = ['Elektrik Elektronik Mühendisliği','Makina Mühendisliği','Endüstri Mühendisliği','Kimya Mühendisliği','Bilgisayar Mühendisliği']
            self.ui.cmb_bolum.addItems(comboList2)
            print('mühendislik girildi')
            self.fillTAbleforMühendislik()
        elif Selected_fakulte == 'Diş Hekimliği Fakültesi':
            comboList2 = ['Ağız Diş ve Çene Cerrahisi','Endonti','Ortodonti','Pedodonti','Protik Diş Tedavisi']
            self.ui.cmb_bolum.addItems(comboList2)
            print('diş girildi')
            self.fillTAbleforDis()
        elif Selected_fakulte == 'Tıp Fakültesi':
            comboList2 = ['Temel Tıp Bilimleri Bölümü','Dahili Tıp Bilimleri Bölümü','Cerrahi Tıp Bilimleri Bölümü']
            self.ui.cmb_bolum.addItems(comboList2)
            print('tıp girildi')
            self.fillTAbleforTip()
        elif Selected_fakulte == 'Hukuk Fakültesi':
            comboList2 = ['Anayasa Hukuku','Roma Hukuku','Ticaret Hukuku','Medeni Hukuk','Ceza Hukuku']
            self.ui.cmb_bolum.addItems(comboList2)
            print('hukuk girildi')
            self.fillTAbleforHukuk()
        elif Selected_fakulte == 'İktisadi ve İdari Bilimler Fakültesi':
            comboList2 = ['İşletme Bölümü','Maliye Bölümü','İktisat Bölümü','Siyaset Bilimi ve Kamu Yönetimi Bölümü','Uluslararası İlişkiler Bölümü(%30 İngilizce)']
            self.ui.cmb_bolum.addItems(comboList2)
            print('ibf  girildi')
            self.fillTAbleforIbf()
        
    def fillTAbleforMühendislik(self):
        if self.ui.cmb_bolum.currentText() == 'Elektrik Elektronik Mühendisliği':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                # print(ders.text())   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                
        elif self.ui.cmb_bolum.currentText() == 'Makina Mühendisliği':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Endüstri Mühendisliği':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Bilgisayar Mühendisliği':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Kimya Mühendisliği':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

            self.InserttoTable()
        
        self.InserttoTable(ders_listesi)

    def fillTAbleforDis(self):
        if self.ui.cmb_bolum.currentText() == 'Ağız Diş ve Çene Cerrahisi':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                # print(ders.text())   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Endonti':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ortodonti':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Pedodonti':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Protik Diş Tedavisi':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable(ders_listesi)
     
    def fillTAbleforTip(self):
        print('fillTableTip')
        if self.ui.cmb_bolum.currentText() == 'Temel Tıp Bilimleri Bölümü':     
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                # print(ders.text())   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Dahili Tıp Bilimleri Bölümü':                              
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Cerrahi Tıp Bilimleri Bölümü':                             
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable(ders_listesi)

    def fillTAbleforHukuk(self):
        if self.ui.cmb_bolum.currentText() == 'Anayasa Hukuku':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                # print(ders.text())   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Roma Hukuku':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ticaret Hukuku':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Medeni Hukuk':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Ceza Hukuku':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable(ders_listesi)

    def fillTAbleforIbf(self):

        
        if self.ui.cmb_bolum.currentText() == 'İşletme Bölümü':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                # print(ders.text())   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Maliye Bölümü':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Siyaset Bilimi ve Kamu Yönetimi Bölümü':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Uluslararası İlişkiler Bölümü(%30 İngilizce)':                                
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Mühendisliğinde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Mühendisliğinde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
                self.InserttoTable(ders_listesi)

        self.InserttoTable(ders_listesi)

    def InserttoTable(self,liste):
        self.ui.Table_acilandersler.clear()
        #TABLE WİDGET İNSERT
        rowIndex= 1                     
        for ders in liste:
            
            self.ui.Table_acilandersler.setItem(rowIndex,0,QTableWidgetItem(str(ders['Ders Kodu'])))
            self.ui.Table_acilandersler.setItem(rowIndex,1,QTableWidgetItem(ders['Ders Adı']))
            self.ui.Table_acilandersler.setItem(rowIndex,2,QTableWidgetItem(ders['TeoUygKrediAkts']))
            self.ui.Table_acilandersler.setItem(rowIndex,3,QTableWidgetItem(ders['Kontenjan']))
            
            rowIndex +=1






def app():
    app= QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()



#FUNCTİONS #START
    # def LoadtoComboBox(self,liste):
    #     liste = self.ui.cmb_fakulte.currentText()
    #     self.ui.cmb_bolum.clear()

    #     if liste == 'Mühendislik Mimarlık Fakültesi':
    #         comboList2 = ['Elektrik Elektronik Mühendisliği','Makina Mühendisliği','Endüstri Mühendisliği','Kimya Mühendisliği','Bilgisayar Mühendisliği']
            
    #     elif liste == 'Diş Hekimliği Fakültesi':
    #         comboList2 = ['Ağız Diş ve Çene Cerrahisi','Endonti','Ortodonti','Pedodonti','Protik Diş Tedavisi']
            
    #     elif liste == 'Tıp Fakültesi':
    #         comboList2 = ['Temel Tıp Bilimleri Bölümü','Dahili Tıp Bilimleri Bölümü','Cerrahi Tıp Bilimleri Bölümü']

    #     elif liste == 'Hukuk Fakültesi':
    #         comboList2 = ['Anayasa Hukuku','Roma Hukuku','Ticaret Hukuku','Medeni Hukuk','Ceza Hukuku']
        
    #     elif liste == 'İktisadi ve İdari Bilimler Fakültesi':
    #         comboList2 = ['İşletme Bölümü','Maliye Bölümü','İktisat Bölümü','Siyaset Bilimi ve Kamu Yönetimi Bölümü','Uluslararası İlişkiler Bölümü(%30 İngilizce)']
            
    #     self.ui.cmb_bolum.addItems(comboList2)