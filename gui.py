import sys
from PyQt4 import QtCore, QtGui, uic 
from PyQt4.QtCore import *  
from PyQt4.QtGui import   *
import cv2   
qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
	self.actionopen.triggered.connect(self.onOpen)
    def onOpen(self):
	qpath = QFileDialog.getOpenFileName(self, 'Open file',   '.',"jpg files (*.jpg)")
	path=unicode(qpath.toUtf8(), 'utf-8', 'ignore')
	self.label.setPixmap(QPixmap(qpath)) 
	im0 = cv2.imread(path) 
	cv2.imshow('orgin',im0)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
    	
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
