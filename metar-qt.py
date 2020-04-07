#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
import mainwindow

try:
	from metar import Metar
except:
	pass

try:
	from urllib2 import urlopen
except:
	from urllib.request import urlopen

BASE_URL = "http://tgftp.nws.noaa.gov/data/observations/metar/stations"
TAF_URL = "http://tgftp.nws.noaa.gov/data/forecasts/taf/stations"

import metar


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = mainwindow.Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.getMETAR.clicked.connect(self.on_click)
		self.ui.clearButton.clicked.connect(self.cl_clear)
		self.ui.tableWidget.cellClicked.connect(self.decode)
		self.ui.tableWidget.setSortingEnabled(True)
		self.ui.lineEdit.returnPressed.connect(self.on_click)

	def cl_clear(self):
		self.ui.tableWidget.setRowCount(0)
		self.ui.textBrowser.clear()


	def on_click(self):
		apicao = self.ui.lineEdit.text().upper()
		for ap in apicao.split(" "):
			if len(ap) < 4:
				continue
			#METAR
			url = "%s/%s.TXT" % (BASE_URL, ap)
			#print("trying to get", url)

			lines = []
			try:
				urlh = urlopen(url)
				for line in urlh:
					if not isinstance(line, str):
						line = line.decode()  # convert Python3 bytes buffer to string
					lines.append(line.rstrip(" \r\n"))
			except:
				import traceback
				print(traceback.format_exc())
				print("Error retrieving", ap, "data", "\n")
				continue

			dt = lines[0]
			report = " ".join(lines[1:])
			if len(report) < 4:
				print("No data for:", ap)
				continue
			if not report.startswith(ap):
				print("ICAO name mismatch for %s: %s" % (ap, report[:4]))
				continue
			rows = self.ui.tableWidget.rowCount()
			#print("rows:", rows)
			row = max(0, rows)

			sorting_toggle = self.ui.tableWidget.isSortingEnabled()
			self.ui.tableWidget.setSortingEnabled(False)
			self.ui.tableWidget.insertRow(row)
			self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ap)))
			self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(dt)))
			self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(report)))
			self.ui.tableWidget.setSortingEnabled(sorting_toggle)
			self.ui.tableWidget.resizeColumnsToContents()
			
			#TAF
			taf_url = "%s/%s.TXT" % (TAF_URL, ap)
			taf_lines = []
			try:
				taf_urlh = urlopen(taf_url)
				
				for taf_line in taf_urlh:
					if not isinstance(taf_line, str):
						taf_line = taf_line.decode()  # convert Python3 bytes buffer to string
					taf_lines.append(taf_line.rstrip(" "))
			except:
				import traceback
				print(traceback.format_exc())
				print("Error retrieving", ap, "data", "\n")
				continue
			
			dt = taf_lines[0]
			report = " ".join(taf_lines[1:])
			print(report)
			self.ui.textBrowser_3.append(report)
			
			
			
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

		try:
			line = self.ui.tableWidget.item(row, column).text()
		except AttributeError:
			# skip empty contents
			return

		self.ui.textBrowser.clear()
		m = "NO MODULE: METAR"
		if 'Metar' not in globals():
			self.ui.textBrowser.append(m)
			return

		m = Metar.Metar(line)
		self.ui.textBrowser.append(m.string())
		# end on_click()
	# end class

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
