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
		self.pushButton.clicked.connect(self.on_click)

	def on_click(self):
		code = self.lineEdit.text()
		if code == "cls":
			self.lineEdit.setText("")#cls
			self.textBrowser.clear()#cls
		else:
			url = "https://raw.githubusercontent.com/MadoiSMind/mindfolderiopetiowp/main/"
			url2 = url + code + ".txt"
			page = requests.get(url2)
			soup = BeautifulSoup(page.text, "html.parser")
			if page.status_code == 200:
				ts = time.time()
				timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
				self.textBrowser.append("[" + timestamp + "] " + "[Connected]")
				ts = time.time()
				timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
				self.textBrowser.append("[" + timestamp + "] Code: " + code + " - founded\n\n" + soup.get_text())
				self.lineEdit.setText("")#cls
			elif page.status_code == 400:
				ts = time.time()
				timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
				self.textBrowser.append("[" + timestamp + "] " + "Code: " + code + " - invalid")
				self.lineEdit.setText("")#cls
			elif page.status_code == 404:
				ts = time.time()
				timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
				self.textBrowser.append("[" + timestamp + "] " + "Code:" + code + " - not found")
				self.lineEdit.setText("")#cls

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()