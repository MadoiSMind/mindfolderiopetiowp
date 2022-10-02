from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QFontDatabase
import requests
import time
import sys
import datetime
import os

os.chdir(sys._MEIPASS)
design = 'Summon\\design.ui'
font = 'Summon\\font\\clacon2.ttf'

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__() # Call the inherited classes __init__ method
		uic.loadUi(design, self) # Load the .ui file
		QFontDatabase.addApplicationFont(font)
		self.show() # Show the GUI
		self.checkNet()

	def t(self):
		t = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
		return t

	def checkNet(self):
		try:
			response = requests.get("http://github.com/") #Проверяем сервак гитхаба
			if response.status_code == 200: #Все норм
				self.textBrowser.append(f"[{self.t()}] [Connected]") #Пишем коннектед
				self.pushButton.clicked.connect(self.on_click) #Подключаем кнопку
				return
		except requests.ConnectionError: #Все плохо
			self.textBrowser.append(f"[{self.t()}] [No connetion]") #Пишем но коннектион
			self.lineEdit.setReadOnly(True) #Деактивируем строку ввода, кнопка не активна ибо не поключенна изначально
		
	def create_message(self, page, code):
		if page.status_code == 200:
			self.textBrowser.append(f"[{self.t()}] Code: {code} - founded\n ˅ Read ˅ \n{self.soup.get_text()}")
		elif page.status_code == 400:
			self.textBrowser.append(f"[{self.t()}] Code: {code} - invalid")
		elif page.status_code == 404:
			self.textBrowser.append(f"[{self.t()}] Code: {code} - not found")
		self.lineEdit.setText("")

	def on_click(self):
		code = self.lineEdit.text()
		if code == "cls":
			self.lineEdit.setText("")#cls
			self.textBrowser.clear()#cls
			return
		url = "https://raw.githubusercontent.com/MadoiSMind/mindfolderiopetiowp/main/"
		url2 = url + code + ".txt"
		page = requests.get(url2)
		self.soup = BeautifulSoup(page.text, "html.parser")
		self.create_message(page, code)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()