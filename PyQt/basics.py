import sys
from PyQt4 import QtCore, QtGui

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 640, 360)
		self.setWindowTitle("Yo does work?")

		extractAction = QtGui.QAction("Quit", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave The App")
		extractAction.triggered.connect(self.quit)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(self.quit)
		btn.resize(80, 30)
		btn.move(10, 80)

		self.toolBar = self.addToolBar("Toolbar")
		self.toolBar.setMovable(False)

		extractAction = QtGui.QAction(QtGui.QIcon("saveicon.png"), "Save", self)
		extractAction.triggered.connect(self.quit)
		self.toolBar.addAction(extractAction)

		extractAction = QtGui.QAction(QtGui.QIcon("lemonsmall.png"), "Lemon?", self)
		extractAction.triggered.connect(self.quit)
		self.toolBar.addAction(extractAction)

		checkBox = QtGui.QCheckBox("Thing", self)
		checkBox.move(10, 110)
		checkBox.stateChanged.connect(self.enlarge_window)

		self.show()

	def quit(self):
		sys.exit()

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)

def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()