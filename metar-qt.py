#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets
import mainwindow

from metar import Metar

try:
	from urllib2 import urlopen
except:
	from urllib.request import urlopen

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"

import metar


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.getMETAR.clicked.connect(self.on_click)
		self.ui.clearButton.clicked.connect(self.cl_clear)
		self.ui.tableWidget.cellClicked.connect(self.decode)
		
	def cl_clear(self):
		self.ui.tableWidget.setRowCount(0)
		self.ui.textBrowserDec.clear()


	def on_click(self):
		apicao = self.ui.lineEdit.text().upper()
		for ap in apicao.split(" "):
			url = "%s/%s.TXT" % (BASE_URL, ap)
			#print("trying to get", url)

			dt = ""
			lines = []
			try:
				urlh = urlopen(url)
				for line in urlh:
					if not isinstance(line, str):
						line = line.decode()  # convert Python3 bytes buffer to string
					line = line.rstrip(" \r\n")
			#		print("line:", line)
					if line.startswith(ap):
						lines.append(line)
					else:
						dt = line
			except:
				import traceback
			#	print(traceback.format_exc())
			#	print("Error retrieving", ap, "data", "\n")

			report = " ".join(lines)
			if len(report) < 4:
			#	print("No data for ", ap, "\n\n")
				continue
			rows = self.ui.tableWidget.rowCount()
			#print("rows:", rows)
			row = max(0, rows)

			self.ui.tableWidget.insertRow(row)
			self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ap)))
			self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(dt)))
			self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(report)))

			self.ui.tableWidget.resizeColumnsToContents()

			#try:
			#	obs = Metar.Metar(report)
			#	#print(obs.string())
			#	#self.ui.tableView.append(report)
			#except Metar.ParserError as exc:
				#print("METAR code: ", line)
				#print(", ".join(exc.args), "\n")
				

			# all is ok
			# ...
	def decode(self, row, column):
		if column != 2:
			column = 2

		line = self.ui.tableWidget.item(row, column).text()
		m = Metar.Metar(line)
		self.ui.textBrowserDec.clear()
		self.ui.textBrowserDec.append(m.string())
		# end on_click()
	# end class

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
