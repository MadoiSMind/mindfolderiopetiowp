from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic, QtTest, QtGui
from PyQt5.QtGui import QFontDatabase
from randomizer import random_text_unicode
import requests
import time
import sys
import datetime
import os
import random


os.chdir(sys._MEIPASS)
design = 'Summon\\design.ui'
font = 'Summon\\font\\clacon2.ttf'
icon = 'Summon\\images\\icon.ico'


class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()  # Call the inherited classes __init__ method
		uic.loadUi(design, self)  # Load the .ui file
		QFontDatabase.addApplicationFont(font)
		self.setWindowIcon(QtGui.QIcon(icon))
		self.show()  # Show the GUI
		self.checkNet()

	def checkNet(self):
		try:
			response = requests.get("http://github.com/")  # Проверяем сервак гитхаба
			if response.status_code == 200:  # Все норм
				self.textBrowser.append(f"[{self.t()}] [Соединенно]")  # Пишем коннектед
				self.textBrowser.append(f"[{self.t()}] [Напишите help для вызыва помощи или about]")
				self.control(True)  # Подключаем кнопку
				return
		except requests.ConnectionError:  # Все плохо
			self.textBrowser.append(f"[{self.t()}] [Нет соединения]")  # Пишем но коннектион
			self.lineEdit.setReadOnly(True)  # Деактивируем строку ввода, кнопка не активна ибо не поключенна изначально

	def t(self):
		t = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
		return t

	def cls(self):
		self.lineEdit.setText("")  # cls
		self.textBrowser.clear()  # cls
		self.control(True)


	def control(self, state):
		if state:
			self.pushButton.clicked.connect(self.on_click)
		else:
			self.pushButton.clicked.disconnect(self.on_click)
		self.lineEdit.setReadOnly(not state)


	def create_message(self, page, code):
		if page.status_code == 200:
			self.textBrowser.append(f"[{self.t()}] Код: {code} - найден. Чтение...")
			QtTest.QTest.qWait(random.randint(1000, 3000))
			self.textBrowser.append(f"[{self.t()}] ˅ Прочитанно ˅ \n\n{self.soup.get_text()}\n")
			self.control(True)
		elif page.status_code == 400:
			self.textBrowser.append(f"[{self.t()}] Код: {code} - не верный")
			self.control(True)
		elif page.status_code == 404:
			self.textBrowser.append(f"[{self.t()}] Код: {code} - не найден")
			self.control(True)


	def about(self):
		Madoi = """==============++********++++++++++++++++
=-===+====+##%%%%%##*********+++***++***
==-=====*@@@%%%%%%%##***************+***
+=--==+%@@@@@%%%%%%%##******************
++===*%#%@@@@%%@%%%%####*****##*********
=+===####%@@@@%@@%@@%#####****##******+*
-===*%%%##%@@@%%%%%@@%#####*######**+*++
--==#%%%%#%@@@%%%%%%%%#**#**#######*++++
--==#%%%%#%%@@@%%%%%%%###*****#####*++++
---=%@@@%%%%@@@@%%%%%%####*****####*++++
---*%%@@@@%%@@@@@%%%%##%###*****###*++++
--++#%%@@@@%%@@@@%@@@%%%********###*++++
----+%%@@@@%%@@@@@@@@%%%####*****##*=++=
----+%@@@@%%%%@@@@@@@@%%@%%%#****###==+=
----*%%@@@@%%%%@@@@@@@@%@@%%%#***##*====
:---===%%@@@@%%@@@@@@@@@@%%#######**====
-------==*#=#%@%@@@@@%%###++++++=++=====
====--====--=*@%@@@@@@@%%*+======++=====
--====+=++*%@@@@@@@@@@@@@%%@%**+++++====
==-=+*##%%#%%%%%%@@@@@@@@%%%%%@%#**+====
"""
		by = random_text_unicode(10)
		self.textBrowser.append(f"{Madoi}\nСделанно: {by}")
		self.control(True)


	def help(self):
		self.textBrowser.append("В качестве кода выступают различные названия, к примеру: dream summoner pill")
		self.control(True)


	def on_click(self):
		self.control(False)
		code = self.lineEdit.text().lower()
		self.lineEdit.setText("")
		if code == "cls":
			self.cls()
			return
		elif code == "about":
			self.about()
			return
		elif code == "help":
			self.help()
			return
		url = "https://raw.githubusercontent.com/MadoiSMind/mindfolderiopetiowp/main/Memory/"
		url2 = url + code + ".txt"
		page = requests.get(url2)
		self.soup = BeautifulSoup(page.text, "html.parser")
		self.create_message(page, code)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
