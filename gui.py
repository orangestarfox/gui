import sys
from PyQt4 import QtCore, QtGui, uic 
from PyQt4.QtCore import *  
from PyQt4.QtGui import   *
import cv2
import dip   
import numpy as np
import pyqtgraph as pg
qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
	        QtGui.QMainWindow.__init__(self)
	        Ui_MainWindow.__init__(self)
	        self.setupUi(self)
		self.actionopen.triggered.connect(self.onOpen)
		self.actionsave.triggered.connect(self.onSave)
		self.actionlaplace.triggered.connect(self.onLaplace)
		self.actioncanny.triggered.connect(self.onCanny)
		self.actiongray.triggered.connect(self.onGray)
		self.actionsobel.triggered.connect(self.onSobel)
		self.actionprewitt.triggered.connect(self.onPrewitt)
		self.actionredo.triggered.connect(self.onRedo)
		self.actiondraw.triggered.connect(self.onDraw)
		self.actionDFT.triggered.connect(self.onDFT)
		self.actionhistogram.triggered.connect(self.onHistogram)
		self.im=[]   
		self.view = pg.GraphicsView(self.graphicsView)
		self.l = pg.GraphicsLayout(border=(100,100,100))
		self.view.setCentralItem(self.l)
		self.view.show()
		self.view.setWindowTitle('Image')
		self.view.resize(640,480)
		self.vb = self.l.addViewBox(lockAspect=True)
		self.img = pg.ImageItem()
		self.vb.addItem(self.img)
		self.vb.autoRange()

	def onOpen(self):
		qpath = QFileDialog.getOpenFileName(self, 'Open file',   '.',"jpg files (*.jpg)")
		path=unicode(qpath.toUtf8(), 'utf-8', 'ignore')
		#self.label.setPixmap(QPixmap(qpath)) 
		im0 = cv2.imread(path)
		self.im=[]
		self.im.append(im0)
		self.im.append(im0)
		I=self.im[1].copy()
			
		self.img.setImage(dip.displayTr(I))
		if self.actionopencv_window.isChecked():
			cv2.namedWindow('origin',cv2.WINDOW_NORMAL)
			cv2.imshow('origin',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
	def onSave(self):
		qpath = QFileDialog.getOpenFileName(self, 'Open file',   '.',"jpg files (*.jpg)")
		path=unicode(qpath.toUtf8(), 'utf-8', 'ignore')
		cv2.imwrite(path,self.im[1] ,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
	def onGray(self):
		self.im[1]=dip.gray(self.im[1],3)
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Gray',cv2.WINDOW_NORMAL)
			cv2.imshow('Gray',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()

		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onLaplace(self):
		k=[[0,-1,0],
		   [-1,4,-1],
		   [0,-1,1]]
		self.im[1]=dip.ImConv(self.im[1],k).astype('uint8')
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Laplace',cv2.WINDOW_NORMAL)
			cv2.imshow('Laplace',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onCanny(self):
		m,n,z=self.im[1].shape
		img=np.zeros((m,n))
		img=cv2.Canny(self.im[1], 50, 150) 
		self.im[1][:,:,0]=img
		self.im[1][:,:,1]=img
		self.im[1][:,:,2]=img
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
			cv2.imshow('Canny',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onRedo(self):
		self.im[1]=self.im[0].copy()
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('origin',cv2.WINDOW_NORMAL)
			cv2.imshow('origin',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onPrewitt(self):
		k=[[-1,0,1],
		   [-1,0,1],
		   [-1,0,1]]
		self.im[1]=dip.ImConv(self.im[1],k).astype('uint8')
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Prewitt',cv2.WINDOW_NORMAL)
			cv2.imshow('Prewitt',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onSobel(self):
		k=[[-1,0,1],
		   [-2,0,2],
		   [-1,0,1]]
		self.im[1]=dip.ImConv(self.im[1],k).astype('uint8')
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Sobel',cv2.WINDOW_NORMAL)
			cv2.imshow('Sobel',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()	
	def onDraw(self):
		self.im[1]=dip.draw(self.im[1])
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('Draw',cv2.WINDOW_NORMAL)
			cv2.imshow('Draw',self.im[1])
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=self.im[1].copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onDFT(self):
		im_fft=dip.fft(self.im[1])
		if self.actionopencv_window.isChecked():
			cv2.destroyAllWindows()
			cv2.namedWindow('DFT',cv2.WINDOW_NORMAL)
			cv2.imshow('DFT',im_fft)
			cv2.waitKey(0)
			cv2.destroyAllWindows()	
		I=im_fft.copy()		
		self.img.setImage(dip.displayTr(I))
		self.vb.addItem(img)
		self.vb.autoRange()
	def onHistogram(self):
		dip.calcAndDrawRgbHist(self.im[1])
		
	
	
    	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()    
	window.show()
        sys.exit(app.exec_())
