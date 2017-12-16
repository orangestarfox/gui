#coding:utf-8
import numpy as np
import cv2
import scipy
from skimage import data,restoration 
from scipy.signal import convolve2d as conv2
from scipy import fftpack
def ImConv(I0,kernel):
	m,n,z=I0.shape
	I=np.zeros((m,n,3))
	I[:,:,0]=conv2(I0[:,:,0],kernel,boundary='symm',mode='same') 
	I[:,:,1]=conv2(I0[:,:,1],kernel,boundary='symm',mode='same') 
	I[:,:,2]=conv2(I0[:,:,2],kernel,boundary='symm',mode='same') 
	I=I.astype('uint8')
	return I
def convolve(star, psf):
	star_fft = fftpack.fftshift(fftpack.fftn(star))
    	psf_fft = fftpack.fftshift(fftpack.fftn(psf))
        ret=fftpack.fftshift(fftpack.ifftn(fftpack.ifftshift(star_fft*psf_fft)))
	return ret.real.astype('uint8')
def deconvolve(star, psf):
	star_fft = fftpack.fftshift(fftpack.fftn(star))
    	psf_fft = fftpack.fftshift(fftpack.fftn(psf))
        ret=fftpack.fftshift(fftpack.ifftn(fftpack.ifftshift(star_fft/psf_fft)))
	return abs(ret).astype('uint8')
def gray(array,a=1):
	m,n,z=array.shape
	R=array[:,:,0]
	G=array[:,:,1]
	B=array[:,:,2]
	gray = R*0.299 + G*0.587 + B*0.114
	gray=gray.astype('uint8')
	
	if a==3:
		gray3=np.zeros((m,n,3))
		gray3[:,:,0]=gray
		gray3[:,:,1]=gray
		gray3[:,:,2]=gray
		return gray3.astype('uint8')
	return gray
def draw(array):
	a =gray(array)
	depth = 10.  # (0-100)
	grad = np.gradient(a)  # 取图像灰度的梯度值
	grad_x, grad_y = grad  # 分别取横纵图像梯度值
	grad_x = grad_x * depth / 100.
	grad_y = grad_y * depth / 100.
	A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
	uni_x = grad_x / A
	uni_y = grad_y / A
	uni_z = 1. / A
	vec_el = np.pi / 2.2  
	vec_az = np.pi / 4. 
	dx = np.cos(vec_el) * np.cos(vec_az)  
	dy = np.cos(vec_el) * np.sin(vec_az) 
	dz = np.sin(vec_el)  
	b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  
	b = b.clip(0, 255)
	m,n=b.shape
	B=np.zeros((m,n,3))
	B[:,:,0]=b
	B[:,:,1]=b
	B[:,:,2]=b	
	return B.astype('uint8')
def displayTr(arr0):
	
	arr1=arr0[:,:,::-1]
	m,n,z=arr1.shape
	arr2=np.zeros((n,m,z))
	arr2[:,:,0]=arr1[:,:,0].T
	arr2[:,:,1]=arr1[:,:,1].T
	arr2[:,:,2]=arr1[:,:,2].T   
	arr2[:,:,0]=arr2[:,:,0][:,::-1]
	arr2[:,:,1]=arr2[:,:,1][:,::-1]
	arr2[:,:,2]=arr2[:,:,2][:,::-1]
	return arr2
def fft(img):
	m,n,z=img.shape
	img_fft=np.zeros((m,n,z))
	for i in range(3):
		img_fft[:,:,i] = fftpack.fftshift(fftpack.fftn(img[:,:,i]))	
		img_fft[:,:,i]=np.log(np.abs(img_fft[:,:,i])+1)
		img_fft[:,:,i]=255*img_fft[:,:,i]/np.max(img_fft[:,:,i])
	return img_fft.astype('uint8')

def calcAndDrawHist(image, color):    
	hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])    
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
	histImg = np.zeros([256,256,3], np.uint8)    
   	hpt = int(0.9* 256);    
        
    	for h in range(256):    
        	intensity = int(hist[h]*hpt/maxVal)    
       		cv2.line(histImg,(h,256), (h,256-intensity), color)                
    	return histImg; 
def calcAndDrawRgbHist(img):
	b, g, r = cv2.split(img)        
   	histImgB = calcAndDrawHist(b, [255, 0, 0])    
    	histImgG = calcAndDrawHist(g, [0, 255, 0])    
    	histImgR = calcAndDrawHist(r, [0, 0, 255])  
	cv2.imshow("histImgB", histImgB)    
   	cv2.imshow("histImgG", histImgG)    
   	cv2.imshow("histImgR", histImgR)
	#return histImgR,histImgG,histImgB
	























