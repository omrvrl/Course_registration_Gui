import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QLineEdit
from Form import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import random
from PyQt5.QtGui import QColor, QBrush


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

#DEFAULT RADİO BUTON İTEM                                    -----------------> RADIO
        self.ui.radio_4sinif.setChecked(True)
        self.ui.radio_1sinif_alt.setChecked(True)


#DEFAULT COMBOBOX PROMPT                                    ---------------> COMBOBOX
    
        comboList = ['Mühendislik Mimarlik Fakültesi','Diş Hekimliği Fakültesi','Tip Fakültesi','Hukuk Fakültesi','İktisadi ve İdari Bilimler Fakültesi']
        self.ui.cmb_fakulte.addItems(comboList)
        comboList2 = ['Elektrik Elektronik Muhendisligi','Makina Muhendisligi','Endüstri Muhendisligi','Kimya Muhendisligi','Bilgisayar Muhendisligi']
        self.ui.cmb_bolum.addItems(comboList2)
#Global Variable
        self.ders_listesi=[]
        self.sayi1 = random.randint(1,100)
        self.sayi2 = random.randint(1,100)

        self.ui.lbl_toplamiyazin.setText(f"TOPLAMI YAZIN: {self.sayi1} + {self.sayi2}")
        self.ders_tarihleri=[
            {'Kod': '1512201' , 'row': [1,2,3] , 'col': 1},              #1 -> 9.00  2 -> 10.00 3 -> 11.00 4-> 12.00 5->13.00 6->14.00  ||| pazart 1 salı 2 çarş 3 
            {'Kod': '1512202' , 'row': [5,6,7] , 'col': 1},            #7 -> 15.00 8 -> 16.00 9 -> 17.00 10 -> 18.00 11 -> 19.00          perş 4 cuma 5 cumart 6
            {'Kod': '1512203' , 'row': [8,9] , 'col': 1},           #12 -> 20.00 13 -> 21.00 14 ->22.00 15 -> 23.00 
            {'Kod': '1512204' , 'row': [1,2,3] , 'col': 2},
            {'Kod': '1512205' , 'row': [6,7,8] , 'col': 2},
            {'Kod': '1512206' , 'row': [8,9,10] , 'col': 2},
            {'Kod': '1512207' , 'row': [2,3,4] , 'col': 3},
            {'Kod': '1512208' , 'row': [7,8] , 'col': 3},
            {'Kod': '1512209' , 'row': [5,6,7] , 'col': 3},
            {'Kod': '1512210' , 'row': [1,2,3] , 'col': 4},
            {'Kod': '1512211' , 'row': [1,2,3] , 'col': 4},
            {'Kod': '1512212' , 'row': [6,7] , 'col': 4},
            {'Kod': '1512213' , 'row': [2,3] , 'col': 5},
            {'Kod': '1512214' , 'row': [7,8] , 'col': 5},
            {'Kod': '1512215' , 'row': [6,7] , 'col': 6},
            {'Kod': '1512216' , 'row': [10,11,12] , 'col': 1},
            {'Kod': '1512217' , 'row': [10,11,12] , 'col': 1},
            {'Kod': '1512218' , 'row': [13] , 'col': 1},   
            {'Kod': '1512219' , 'row': [9,10,11] , 'col': 2 },
            {'Kod': '1512220' , 'row': [12] , 'col': 2},
            {'Kod': '1512221' , 'row': [11,12] , 'col': 2},
            {'Kod': '1512222' , 'row': [9,10,11] , 'col': 3},
            {'Kod': '1512223' , 'row': [10,11] , 'col': 3},
            {'Kod': '1512224' , 'row': [10,11] , 'col': 4},
            {'Kod': '1512224' , 'row': [9] , 'col': 4},
            {'Kod': '1512226' , 'row': [11,12] , 'col': 4},
            {'Kod': '1512227' , 'row': [10,11] , 'col': 5},
            {'Kod': '151228' ,  'row': [9,10] , 'col': 5},
            {'Kod': '1512229' , 'row': [6,7] , 'col': 6}]
        


# TABLE WİDGET CONFİGURATION
        self.ui.Table_acilandersler.setRowCount(10)
        self.ui.Table_acilandersler.setColumnCount(4)
        # self.ui.Table_Secilen.setRowCount(10)
        self.ui.Table_Secilen.setColumnCount(4)
        self.ui.Table_acilandersler.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))
        self.ui.Table_acilandersler.setColumnWidth(0,80)
        self.ui.Table_acilandersler.setColumnWidth(1,300)
        self.ui.Table_acilandersler.setColumnWidth(2,90)
        self.ui.Table_acilandersler.setColumnWidth(3,90)
        self.ui.Table_acilandersler.setAlternatingRowColors(True)
        self.ui.Table_acilandersler.setAutoScroll(True)
        self.ui.Table_Secilen.setColumnWidth(0,100)
        self.ui.Table_Secilen.setColumnWidth(1,300)
        self.ui.Table_Secilen.setColumnWidth(2,200)
        self.ui.Table_Secilen.setColumnWidth(3,200)
        self.ui.Table_Secilen.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))
        self.ui.Table_Secilen.setAlternatingRowColors(True)
        row_height = 20  # Set the desired row height
        for row in range(self.ui.Table_acilandersler.rowCount()):
            self.ui.Table_acilandersler.setRowHeight(row, row_height)
            self.ui.Table_Secilen.setRowHeight(row, row_height)
            self.ui.Table_yerinealinabilecekdersler.setRowHeight(row, row_height)
        self.ui.Table_DersProgrami.setColumnCount(7)
        self.ui.Table_DersProgrami.setRowCount(16)
        # self.ui.Table_DersProgrami.setItem(0,0,QTableWidgetItem('Saat'))
        self.ui.Table_DersProgrami.setHorizontalHeaderLabels(['Saat','Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi'])
        self.ui.Table_DersProgrami.setVerticalHeaderLabels(['08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'])
        
        for row in range(self.ui.Table_DersProgrami.rowCount()):
            self.ui.Table_DersProgrami.setRowHeight(row,5)
            for col in range(self.ui.Table_DersProgrami.columnCount()):
                self.ui.Table_DersProgrami.setColumnWidth(row,91)


# CONNECT TO FUNCTİONS                                         
        self.ui.cmb_fakulte.currentIndexChanged.connect(self.ChangedFakulte)        # Loads depertmants
        self.ui.cmb_bolum.currentIndexChanged.connect(self.LoadCoursePackets)            # Ders paketlerini tabloya yükler
        self.ui.radio_1sinif.toggled.connect(self.LoadCoursePackets)
        self.ui.radio_2sinif.toggled.connect(self.LoadCoursePackets)
        self.ui.radio_3sinif.toggled.connect(self.LoadCoursePackets)
        self.ui.radio_4sinif.toggled.connect(self.LoadCoursePackets)
        self.ui.linedit_ara.textChanged.connect(self.SearchFunc)
        self.ui.btn_yenidersekle.clicked.connect(self.YeniDersEkle)
        self.ui.btn_derslerikaydet.clicked.connect(self.DersleriKaydet)

    def DersleriKaydet(self):
        if (self.sayi1 + self.sayi2) ==  int(self.ui.linedit_toplam.text()):
            print('TEBRİKLER DERSLERİNİZ BAŞARIYLA KAYDEDİLDİ.')
        else:
            print('Lütfen girilen sayıları doğru toplayınız.')
        
        

    def YeniDersEkle(self):
        self.ui.Table_Secilen.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))
        
        for item in self.ui.Table_acilandersler.selectedItems():
 
            # print(item.row(),item.column(),item.text())
            rowIndex =self.ui.Table_Secilen.rowCount()
            try:

                self.AddtoDersProgrami(rowIndex)
                if item.text() in [(QTableWidgetItem(self.ui.Table_Secilen.item(row, col))).text() for col in range(self.ui.Table_Secilen.columnCount()) for row in range(self.ui.Table_acilandersler.rowCount())]:

                    raise TypeError('Zaten bu dersi Seçmişsiniz!!!')

                self.ui.Table_Secilen.insertRow(rowIndex)
                if item.column() == 0:
                    self.ui.Table_Secilen.setItem(rowIndex,0,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                    self.ui.Table_Secilen.setItem(rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+1)))
                    self.ui.Table_Secilen.setItem(rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+2)))
                    self.ui.Table_Secilen.setItem(rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+3)))

                elif item.column() == 1:
                    self.ui.Table_Secilen.setItem(rowIndex,0,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    self.ui.Table_Secilen.setItem(rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                    self.ui.Table_Secilen.setItem(rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+1)))
                    self.ui.Table_Secilen.setItem(rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+2)))

                elif item.column() == 2:
                    self.ui.Table_Secilen.setItem(rowIndex,0,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-2)))
                    self.ui.Table_Secilen.setItem(rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    self.ui.Table_Secilen.setItem(rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                    self.ui.Table_Secilen.setItem(rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+1)))
                elif item.column() == 3:
                    self.ui.Table_Secilen.setItem(rowIndex,0,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-3)))
                    self.ui.Table_Secilen.setItem(rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-2)))
                    self.ui.Table_Secilen.setItem(rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    self.ui.Table_Secilen.setItem(rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
            except TypeError as err:
                print(err)

            

    def AddtoDersProgrami(self,rowIndex):
        ders = self.ui.Table_Secilen.item(rowIndex,0)
        print(ders.text())
        brush = QBrush(QColor(200, 243, 178))  # RGB color (red)
        
        for liste in self.ders_listesi:
            if ders.text() == liste['Kod']:
                for ro in liste['row']:
                    self.ui.Table_DersProgrami.setItem(liste['row'],liste['col'],QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
                    self.ui.Table_DersProgrami.item(liste['row'],liste['col']).setBackground(brush)


        # elif ders.text()  == 'INTRODUCTION TO EMBEDDED SYSTEMS':
        #     self.ui.Table_DersProgrami.setItem(1,1,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(2,1,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(3,1,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.item(1,1).setBackground(brush)
        #     self.ui.Table_DersProgrami.item(2,1).setBackground(brush)           
        #     self.ui.Table_DersProgrami.item(3,1).setBackground(brush)           

        # elif ders.text()  == 'DIGITAL SIGNAL PROCESSING':
        #     self.ui.Table_DersProgrami.setItem(7,1,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(8,1,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.item(7,1).setBackground(brush)           
        #     self.ui.Table_DersProgrami.item(8,1).setBackground(brush)       

        # elif ders.text()  == 'POWER SYSTEM ANALYSIS I':
        #     self.ui.Table_DersProgrami.setItem(1,2,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(2,2,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(3,2,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.item(1,2).setBackground(brush)
        #     self.ui.Table_DersProgrami.item(2,2).setBackground(brush)           
        #     self.ui.Table_DersProgrami.item(3,2).setBackground(brush)

        # elif ders.text()  == 'THE ENGINEER AND SOCIETY':
        #     self.ui.Table_DersProgrami.setItem(5,5,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.setItem(6,5,QTableWidgetItem(self.ui.Table_Secilen.item(ders.row(),0)))
        #     self.ui.Table_DersProgrami.item(5,5).setBackground(brush)           
        #     self.ui.Table_DersProgrami.item(6,5).setBackground(brush)
        # else:
        #     print('fail')

    def SearchFunc(self):
        text = self.ui.linedit_ara.text().lower()
        for row in range(self.ui.Table_acilandersler.rowCount()):
            number_item = self.ui.Table_acilandersler.item(row, 0)
            name_item = self.ui.Table_acilandersler.item(row, 1)
            
            if name_item is not None and text.lower() in name_item.text().lower():
                self.ui.Table_acilandersler.setRowHidden(row, False)
            elif number_item is not None and text.lower() in number_item.text().lower():
                self.ui.Table_acilandersler.setRowHidden(row, False)
            else:
                self.ui.Table_acilandersler.setRowHidden(row, True)

    def ChangedFakulte(self):
        Selected_fakulte = self.ui.cmb_fakulte.currentText()
        self.ui.cmb_bolum.clear()
        if Selected_fakulte == 'Mühendislik Mimarlik Fakültesi':
            comboList2 = ['Elektrik Elektronik Muhendisligi','Makina Muhendisligi','Endüstri Muhendisligi','Kimya Muhendisligi','Bilgisayar Muhendisligi']
            self.ui.cmb_bolum.addItems(comboList2)
           
        elif Selected_fakulte == 'Diş Hekimliği Fakültesi':
            comboList2 = ['Ağız Diş ve Çene Cerrahisi','Endonti','Ortodonti','Pedodonti','Protik Diş Tedavisi']
 
        elif Selected_fakulte == 'Tip Fakültesi':
            comboList2 = ['Temel Tıp Bilimleri Bölümü','Dahili Tıp Bilimleri Bölümü','Cerrahi Tıp Bilimleri Bölümü']

        elif Selected_fakulte == 'Hukuk Fakültesi':
            comboList2 = ['Anayasa Hukuku','Roma Hukuku','Ticaret Hukuku','Medeni Hukuk','Ceza Hukuku']

        elif Selected_fakulte == 'İktisadi ve İdari Bilimler Fakültesi':
            comboList2 = ['İşletme Bölümü','Maliye Bölümü','İktisat Bölümü','Siyaset Bilimi ve Kamu Yönetimi Bölümü','Uluslararası İlişkiler Bölümü(%30 İngilizce)']

        self.ui.cmb_bolum.addItems(comboList2)

    def LoadCoursePackets(self):                                                 # Fakültelere yönlendirir. # her fonksiyona changed.connect ten dolayı iki defa giriyor.
        Selected_fakulte = self.ui.cmb_fakulte.currentText()
        if Selected_fakulte == 'Mühendislik Mimarlik Fakültesi': 

            self.fillTAbleforMuhendislik()                                
        elif Selected_fakulte == 'Diş Hekimliği Fakültesi':
            print('diş girildi')
            self.fillTAbleforDis()
        elif Selected_fakulte == 'Tip Fakültesi':
            print('tıp girildi')
            self.fillTAbleforTip()
        elif Selected_fakulte == 'Hukuk Fakültesi':
            print('hukuk girildi')
            self.fillTAbleforHukuk()
        elif Selected_fakulte == 'İktisadi ve İdari Bilimler Fakültesi':
            print('ibf  girildi')
            self.fillTAbleforIbf()
        
    def fillTAbleforMuhendislik(self):
        if self.ui.cmb_bolum.currentText() == 'Elektrik Elektronik Muhendisligi':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
         
        elif self.ui.cmb_bolum.currentText() == 'Makina Muhendisligi':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Endüstri Muhendisligi':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Bilgisayar Muhendisligi':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Kimya Muhendisligi':                                 ##### KİMYA MÜHENDİSLİĞİ               
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable()

    def fillTAbleforDis(self):
        if self.ui.cmb_bolum.currentText() == 'Ağız Diş ve Çene Cerrahisi':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Endonti':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ortodonti':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Pedodonti':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Protik Diş Tedavisi':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable()
     
    def fillTAbleforTip(self):
        print('fillTableTip')
        if self.ui.cmb_bolum.currentText() == 'Temel Tıp Bilimleri Bölümü':     
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Dahili Tıp Bilimleri Bölümü':                              
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Cerrahi Tıp Bilimleri Bölümü':                             
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable()

    def fillTAbleforHukuk(self):
        if self.ui.cmb_bolum.currentText() == 'Anayasa Hukuku':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Roma Hukuku':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ticaret Hukuku':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Medeni Hukuk':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Ceza Hukuku':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable()

    def fillTAbleforIbf(self):

        if self.ui.cmb_bolum.currentText() == 'İşletme Bölümü':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Maliye Bölümü':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        elif self.ui.cmb_bolum.currentText() == 'Siyaset Bilimi ve Kamu Yönetimi Bölümü':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Uluslararası İlişkiler Bölümü(%30 İngilizce)':                                
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '0/50'}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '0/50'}]

        self.InserttoTable()

    def InserttoTable(self):
        self.ui.Table_acilandersler.clear()
        self.ui.Table_acilandersler.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))

        #TABLE WİDGET İNSERT
        rowIndex= 0                     
        for ders in self.ders_listesi:
            
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

