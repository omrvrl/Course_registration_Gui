import sys
from PyQt5 import QtGui, QtWidgets 
from PyQt5.QtWidgets import QLineEdit, QPushButton
from Form import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import random
from PyQt5.QtGui import QColor, QBrush, QPainter, QPen ,QIcon
from PyQt5.QtCore import Qt

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)


#DEFAULT COMBOBOX PROMPT                                    ---------------> COMBOBOX
    
        comboList = ['Mühendislik Mimarlik Fakültesi','Diş Hekimliği Fakültesi','Tip Fakültesi','Hukuk Fakültesi','İktisadi ve İdari Bilimler Fakültesi']
        self.ui.cmb_fakulte.addItems(comboList)
        comboList2 = ['Elektrik Elektronik Muhendisligi','Makina Muhendisligi','Endüstri Muhendisligi','Kimya Muhendisligi','Bilgisayar Muhendisligi']
        self.ui.cmb_bolum.addItems(comboList2)
#Global Variable
        self.ders_listesi=[]
        self.sayi1 = random.randint(1,100)
        self.sayi2 = random.randint(1,100)
        self.toplam_kredi=0
        self.rowIndex =self.ui.Table_Secilen.rowCount()
        self.ui.lbl_toplamiyazin.setText(f"TOPLAMI YAZIN: {self.sayi1} + {self.sayi2}")
        self.ders_tarihleri=[
            {'Kod': '1512201' , 'row': [1,2,3] , 'col': 1},        
            {'Kod': '1512202' , 'row': [5,6,7] , 'col': 1},       
            {'Kod': '1512203' , 'row': [8,9] , 'col': 1},          
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
            {'Kod': '1512231' , 'row': [9,10] , 'col': 1},
            {'Kod': '1512217' , 'row': [2,3,4] , 'col': 1},
            {'Kod': '1512218' , 'row': [11,12] , 'col': 1},   
            {'Kod': '1512234' , 'row': [13,14,15] , 'col': 1},   
            {'Kod': '1512219' , 'row': [4,5,6] , 'col': 2 },
            {'Kod': '1512238' , 'row': [1,2,3] , 'col': 2 },
            {'Kod': '1512220' , 'row': [13,14] , 'col': 1},
            {'Kod': '1512243' , 'row': [12] , 'col': 1},
            {'Kod': '1512242' , 'row': [10,11,12] , 'col': 2},
            {'Kod': '1512240' , 'row': [7,8] , 'col': 2},
            {'Kod': '1512239' , 'row': [9,10,11] , 'col': 3},
            {'Kod': '1512237' , 'row': [1,2,3] , 'col': 3},
            {'Kod': '1512235' , 'row': [7,8] , 'col': 4},
            {'Kod': '1512223' , 'row': [1,2,3] , 'col': 4},
            {'Kod': '1512224' , 'row': [12,13] , 'col': 5},
            {'Kod': '1512225' , 'row': [10,11] , 'col': 5},
            {'Kod': '1512246' , 'row': [9,10] , 'col':6 },
            {'Kod': '1512233' , 'row': [5,6] , 'col': 1},
            {'Kod': '1512226' , 'row': [1,2,3] , 'col': 1},
            {'Kod': '1512232' , 'row': [1,2,3] , 'col': 2},
            {'Kod': '1512227' , 'row': [5,6,7] , 'col': 2},
            {'Kod': '1512230' , 'row': [2,3,4] , 'col': 3},
            {'Kod': '1512221' ,  'row': [9,10] , 'col': 3},
            {'Kod': '1512228' ,  'row': [11,12] , 'col': 3},
            {'Kod': '1512229' , 'row': [8,9,10] , 'col': 4},
            {'Kod': '1512222' , 'row': [6,7] , 'col': 4},
            {'Kod': '1512236' , 'row': [2,3,4] , 'col': 4},
            {'Kod': '1512241' , 'row': [5,6,7] , 'col': 5},
            {'Kod': '1512244' , 'row': [1,2,3] , 'col': 5},
            {'Kod': '1512245' , 'row': [8,9] , 'col': 6}]
            
            
        self.overlapList=[]


# TABLE WİDGET CONFİGURATION
        self.ui.Table_acilandersler.setRowCount(10)
        self.ui.Table_acilandersler.setColumnCount(4)
        # self.ui.Table_Secilen.setRowCount(10)
        self.ui.Table_Secilen.setColumnCount(4)
        self.ui.Table_acilandersler.setHorizontalHeaderLabels(('Ders Kodu','Ders Adi','Teo Uyg Akts','Kontenjan'))
        self.ui.Table_acilandersler.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; }")
        self.ui.Table_acilandersler.setColumnWidth(0,80)
        self.ui.Table_acilandersler.setColumnWidth(1,300)
        self.ui.Table_acilandersler.setColumnWidth(2,90)
        self.ui.Table_acilandersler.setColumnWidth(3,90)
        self.ui.Table_acilandersler.setAlternatingRowColors(True)
        self.ui.Table_acilandersler.setAutoScroll(True)
        self.ui.Table_Secilen.setColumnWidth(0,100)
        self.ui.Table_Secilen.setColumnWidth(1,100)
        self.ui.Table_Secilen.setColumnWidth(2,300)
        self.ui.Table_Secilen.setColumnWidth(3,200)
        self.ui.Table_Secilen.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; }")
        self.ui.Table_Secilen.setHorizontalHeaderLabels(('Silme','Ders Kodu','Ders Adi','Teo Uyg Akts','Yerine'))
        self.ui.Table_Secilen.setAlternatingRowColors(True)
        row_height = 20  # Set the desired row height
        for row in range(self.ui.Table_acilandersler.rowCount()):
            self.ui.Table_acilandersler.setRowHeight(row, row_height)
            self.ui.Table_Secilen.setRowHeight(row, row_height)
            self.ui.Table_yerinealinabilecekdersler.setRowHeight(row, row_height)
        self.ui.Table_DersProgrami.setColumnCount(6)
        self.ui.Table_DersProgrami.setRowCount(16)
        self.ui.Table_DersProgrami.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; }")
        self.ui.Table_DersProgrami.setHorizontalHeaderLabels(['Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi'])
        self.ui.Table_DersProgrami.setVerticalHeaderLabels(['08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'])
        
        for row in range(self.ui.Table_DersProgrami.rowCount()):
            self.ui.Table_DersProgrami.setRowHeight(row,5)
            for col in range(self.ui.Table_DersProgrami.columnCount()):  
                self.ui.Table_DersProgrami.setColumnWidth(row,105)

        self.ui.Table_yerinealinabilecekdersler.setRowCount(1)
        self.ui.Table_yerinealinabilecekdersler.setColumnCount(4)
        self.ui.Table_yerinealinabilecekdersler.setRowHeight(0,5)
        self.ui.Table_yerinealinabilecekdersler.setSpan(0,0,1,self.ui.Table_yerinealinabilecekdersler.columnCount())
        self.ui.Table_yerinealinabilecekdersler.horizontalHeader().setStyleSheet("QHeaderView::section { font-weight: bold; }")
        self.ui.Table_yerinealinabilecekdersler.setHorizontalHeaderLabels(['Ders Kodu','Ders Adı','Harf','Açılan Dersler'])
        text=QTableWidgetItem('Kayıtlı Ders Yok')
        text.setTextAlignment(Qt.AlignCenter)
        self.ui.Table_yerinealinabilecekdersler.setItem(0,0,text)



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

    def OnClicked_Silme(self,row):
        sender_button = self.sender().text()
        # selected_row = 1
        # selected_col = 1

        # # Check if there is an item in the cell
        # if self.ui.Table_Secilen.item(selected_row, selected_col):
        #    self.ui.Table_Secilen.takeItem(selected_row, selected_col)
        print(f"Button clicked in Row {sender_button}")

    def UpdateKredi(self):
            for item in self.ui.Table_acilandersler.selectedItems():
                for ders in self.ders_listesi:
                    if (QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),0)).text()) == str(ders['Ders Kodu']):
                        self.toplam_kredi = self.toplam_kredi + ders['Kredi']
                        self.ui.lbl_kredi_akts.setText(f'KREDİ: {self.toplam_kredi} AKTS: {0}')

    def UpdateKontenjan(self):
        for row in (range(self.ui.Table_Secilen.rowCount())):
            secilen = self.ui.Table_Secilen.item(row,0).text()
            for ders in self.ders_listesi:
                if (str(ders['Ders Kodu']) == str(secilen)):   
                    ders['student_number'] +=1
                    self.InserttoTable()
                    break
        
    def paintEvent(self,event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawLine(0,52,500,52)
        painter.drawLine(0,510,500,510)
        painter.drawLine(540,408,1250,408)

    def DersleriKaydet(self):
        if (self.sayi1 + self.sayi2) ==  int(self.ui.linedit_toplam.text()):
            print('TEBRİKLER DERSLERİNİZ BAŞARIYLA KAYDEDİLDİ.')
            self.UpdateKontenjan()
        else:
            print('DOĞRULAMA GEÇERSİZ.')
    
    def YeniDersEkle(self):
        self.ui.Table_Secilen.setHorizontalHeaderLabels(('Silme','Ders Kodu','Ders Adi','Teo Uyg Akts','Yerine'))
        
        for item in self.ui.Table_acilandersler.selectedItems():
            # print(item.row(),item.column(),item.text())
            rowIndex =self.ui.Table_Secilen.rowCount()
            try:

                if item.text() in [(QTableWidgetItem(self.ui.Table_Secilen.item(row, col))).text() for col in range(self.ui.Table_Secilen.columnCount()) for row in range(self.ui.Table_acilandersler.rowCount())]:
                    raise TypeError('Zaten bu dersi Seçmişsiniz!!!')
                if self.CheckOverlapping(self.rowIndex):
                    raise TypeError('Bu ders seçtiğiniz diğer dersler ile çakışmaktadır!!!!')
                if self.toplam_kredi >= 23:
                    raise TypeError('KREDİNİZİ AŞTINIZ!! MAX KREDİ: 22 ')
                

                btn_sil = QPushButton()
                btn_sil.setIcon(QIcon('delete-icon.jpeg'))
                btn_sil.setStyleSheet("color: white; border: none; padding: 5px;")
                btn_sil.resize(10,10)
                btn_sil.clicked.connect(lambda row=2: self.OnClicked_Silme(row))

                self.UpdateKredi()
                self.ui.Table_Secilen.insertRow(self.rowIndex)
                if item.column() == 0:
                    self.ui.Table_Secilen.setCellWidget(0,0,btn_sil)
                    self.ui.Table_Secilen.setItem(self.rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                    self.ui.Table_Secilen.setItem(self.rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+1)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+2)))

                elif item.column() == 1:
                    self.ui.Table_Secilen.setCellWidget(0,0,btn_sil)
                    self.ui.Table_Secilen.setItem(self.rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                    self.ui.Table_Secilen.setItem(self.rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()+1)))

                elif item.column() == 2:
                    self.ui.Table_Secilen.setCellWidget(0,0,btn_sil)
                    self.ui.Table_Secilen.setItem(self.rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-2)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column())))
                elif item.column() == 3:
                    self.ui.Table_Secilen.setCellWidget(0,0,btn_sil)
                    self.ui.Table_Secilen.setItem(self.rowIndex,1,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-3)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,2,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-2)))
                    self.ui.Table_Secilen.setItem(self.rowIndex,3,QTableWidgetItem(self.ui.Table_acilandersler.item(item.row(),item.column()-1)))
                    
                self.AddtoDersProgrami()

            except TypeError as err:
                print(err)

    def AddtoDersProgrami(self):
        ders = QTableWidgetItem(self.ui.Table_Secilen.item(self.rowIndex,1))
        brush = QBrush(QColor(200, 243, 178))  # RGB color (red)
        for liste in self.ders_tarihleri:
            if liste['Kod'] == ders.text():
                for ro in liste['row']:
                    self.ui.Table_DersProgrami.setItem(ro,liste['col'],QTableWidgetItem(self.ui.Table_Secilen.item(self.rowIndex,1)))
                    self.ui.Table_DersProgrami.item(ro,liste['col']).setBackground(brush)

    def CheckOverlapping(self,rowIndex):
        # ders = QTableWidgetItem(self.ui.Table_Secilen.item(rowIndex,0))
        for liste in self.ders_tarihleri:
            for ders in self.ui.Table_acilandersler.selectedItems():
                # print(QTableWidgetItem(self.ui.Table_acilandersler.item(ders.row(),0)).text())
                if liste['Kod'] == QTableWidgetItem(self.ui.Table_acilandersler.item(ders.row(),0)).text():
                    print(liste['row'])
                    if not any((a in liste['row']) and (b == liste['col']) for a, b in self.overlapList):
                        for ro in liste['row']:
                            self.overlapList.append((ro,liste['col']))
                        return False
                    else:
                        return True    
                else:
                    print('--')

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

            self.fillTAbleforDis()
        elif Selected_fakulte == 'Tip Fakültesi':

            self.fillTAbleforTip()
        elif Selected_fakulte == 'Hukuk Fakültesi':

            self.fillTAbleforHukuk()
        elif Selected_fakulte == 'İktisadi ve İdari Bilimler Fakültesi':

            self.fillTAbleforIbf()
        
    def fillTAbleforMuhendislik(self):
        if self.ui.cmb_bolum.currentText() == 'Elektrik Elektronik Muhendisligi':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 1512201, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512202, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512203, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512205, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512206, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 1512225, 'Ders Adı':'COMMUNICATIONS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50' ,'student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512223, 'Ders Adı':'ELECTRONICS II','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50' ,'student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512233, 'Ders Adı':'LOGIC DESIGN','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50' ,'student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512226, 'Ders Adı':'CONTROL SYSTEMS LABORATORY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512232, 'Ders Adı':'INTRODUCTION TO PROJECT MANAGEMENT','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 1512227, 'Ders Adı':'CIRCUIT ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512230, 'Ders Adı':'CIRCUITS  LABORATORY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512221, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512228, 'Ders Adı':'ELECTROMAGNETIC WAVES','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512229, 'Ders Adı':'SYSTEMS AND SIGNALS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' :1512236, 'Ders Adı':'CALCULUS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512241 , 'Ders Adı':'CHEMISTRY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512244, 'Ders Adı':'INTRODUCTION TO PROGRAMMING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' :1512245 , 'Ders Adı':'ATATÜRK İLKE.VE İNK.TARİHİ I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 1512222, 'Ders Adı':'TECHNICAL  WRITING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
         
        elif self.ui.cmb_bolum.currentText() == 'Makina Muhendisligi':                               ##### MAKINE MÜHENDİSLİĞİ1512227
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220021, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220022, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220023, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220024, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220025, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220026, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220027, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220028, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220029, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220030, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220036, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220037, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220038, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220039, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220040, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220041, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220042, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220043, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220044, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220045, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Endüstri Muhendisligi':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Bilgisayar Muhendisligi':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Kimya Muhendisligi':                                 ##### KİMYA MÜHENDİSLİĞİ               
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        self.InserttoTable()

    def fillTAbleforDis(self):
        if self.ui.cmb_bolum.currentText() == 'Ağız Diş ve Çene Cerrahisi':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Endonti':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ortodonti':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Pedodonti':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Protik Diş Tedavisi':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        self.InserttoTable()
     
    def fillTAbleforTip(self):

        if self.ui.cmb_bolum.currentText() == 'Temel Tıp Bilimleri Bölümü':     
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Dahili Tıp Bilimleri Bölümü':                              
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Cerrahi Tıp Bilimleri Bölümü':                             
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        self.InserttoTable()

    def fillTAbleforHukuk(self):
        if self.ui.cmb_bolum.currentText() == 'Anayasa Hukuku':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Roma Hukuku':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Ticaret Hukuku':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Medeni Hukuk':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Ceza Hukuku':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        self.InserttoTable()

    def fillTAbleforIbf(self):

        if self.ui.cmb_bolum.currentText() == 'İşletme Bölümü':     ##### ELEKTRİK ELEKTRONİKMÜHENDİSLİĞi
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton) 
            for ders in items:
                if ders.text() == '4.Sınıf' and ders.isChecked():                                        
                    self.ders_listesi =[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '3.Sınıf' and ders.isChecked():                                       
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf' and ders.isChecked():                                   
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Maliye Bölümü':                               ##### MAKINE MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:   
                if ders.text() == '4.Sınıf' and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'4.  Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
        
                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'3.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                 
                elif ders.text() == '2.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'2. ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
               
                elif ders.text() == '1.Sınıf' and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.  ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                             ##### ENDÜSTRİ MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'İktisat Bölümü':                           ##### BİLGİSAYAR MÜHENDİSLİĞİ
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'1.sonfı ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

        elif self.ui.cmb_bolum.currentText() == 'Siyaset Bilimi ve Kamu Yönetimi Bölümü':                                ##### KİMYA MÜHENDİSLİĞİ 
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]
                    
        elif self.ui.cmb_bolum.currentText() == 'Uluslararası İlişkiler Bölümü(%30 İngilizce)':                                
            items=self.ui.Group_AcilanDers.findChildren(QtWidgets.QRadioButton)    
            for ders in items:                    
                if ders.text() == '4.Sınıf'and ders.isChecked():
                    self.ders_listesi = [
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 4 Muhendisliginde Tasarım (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Laboratuvarı (I)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Sektörde İş Sağ. ve Güven.','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Makine Muhendisliginde Tasarım (II)','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Project Management','TeoUygKrediAkts': '2 0 2 3', 'Kontenjan': '50','student_number':0,'Kredi':3}]


                elif ders.text() == '3.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'kimya 3 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '2.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'Kimya 2 ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

                elif ders.text() == '1.Sınıf'and ders.isChecked():
                    self.ders_listesi=[
                        {'Ders Kodu' : 151220001, 'Ders Adı':'OBJECT ORIENTED PROGRAMMING I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'INTRODUCTION TO EMBEDDED SYSTEMS','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'DIGITAL SIGNAL PROCESSING','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'POWER SYSTEM ANALYSIS I','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3},
                        {'Ders Kodu' : 151220001, 'Ders Adı':'THE ENGINEER AND SOCIETY','TeoUygKrediAkts': '2  0  2  3', 'Kontenjan': '50','student_number':0,'Kredi':3}]

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
            self.ui.Table_acilandersler.setItem(rowIndex,3,QTableWidgetItem(str(ders['student_number']) + '/' +  ders['Kontenjan']))
            
            rowIndex +=1

def app():
    app= QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()

