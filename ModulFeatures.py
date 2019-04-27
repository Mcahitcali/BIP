from math import cos, pi, sin

from numba import jit, prange
from PIL import Image, ImageEnhance, ImageOps
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap


class Feature():
    def __init__(self, MainWindow):
        self.mainWindow = MainWindow
        self.qLabel = MainWindow.imageView #ImageViewer
        self.fileName = "rody.jpg" # default Image
        self.pillImage = Image.open(self.fileName).convert("RGB")
        self.imageWidth, self.imageHeight = self.pillImage.size
        self.qImage = None #Set Image
        self.currentImage = "temp" #preview Image
        self.tempData = list(self.pillImage.getdata())
        self.orgData =  list(self.pillImage.getdata())

    def defaultImageView(self):
        self.setImage(self.pillImage,state="default")

    def uploadImage(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self.mainWindow.centralwidget, ("Open Image"),
                                       "//untitled.png",
                                       ("Images *.png *.jpg"))

        self.fileName = str(file[0]) if file[0] != '' else self.fileName #set current image when dont selected new image
        self.setImage(state="upload")
        
    def save(self):
        image = self.getImage(self.orgData)
        
        file = QtWidgets.QFileDialog.getSaveFileName(self.mainWindow.centralwidget, ("Save Image"),
                                       "//untitled.png",
                                       ("Images *.png *.jpg"))

        image.save(str(file[0])) if file[0] else print("clicked Cancel")
    
    def setImage(self,qImage=None,state="upload",cImage="originally",scale = True):
        if state == "upload":
            self.pillImage = Image.open(self.fileName).convert("RGB")
            self.imageWidth, self.imageHeight = self.pillImage.size
            self.tempData = self.orgData = list(self.pillImage.getdata())
            qImage = self.pillImage
        if cImage == "temp":
            self.tempData = list(qImage.getdata())
            self.imageWidth, self.imageHeight = qImage.size
        
        
        self.qImage = ImageQt(qImage.convert("RGBA"))
        pixMap = QPixmap.fromImage(self.qImage)

        self.qLabel.setPixmap(pixMap)
       
    def previewImage(self):
        newImage = self.getImage(self.tempData)
        if self.currentImage == "temp":
            self.setImage(qImage=self.pillImage,state="preview",cImage="originally")
            self.currentImage = "originally"
        else:
            self.setImage(qImage=newImage,state="preview",cImage="temp")
            self.currentImage = "temp"

    def getImage(self,tempData,mode="RGB"):
        newImage = Image.new(mode,(self.imageWidth,self.imageHeight))
        newImage.putdata([tuple(pixel) for pixel in self.tempData])
        if mode == "RGB":
            return newImage
        else:
            return newImage.convert(mode)

    def getSize(self):
        size = (self.imageWidth, self.imageHeight)
        return size

    def convert2Blackwhite(self):
        data = self.tempData
        for i in range(len(data)):
            r,g,b = data[i]
            value = int(r*0.299 + g*0.587 + b*0.114)
            if value < 128:
                value = 0   ### for BLACk - WHITE
            else:
                value = 255
            data[i] = list(data[i])
            for j in range(3):
                self.tempData[i][j] = value
        newImage = self.getImage(self.tempData)
        self.setImage(newImage, state="edit",cImage="temp")

    def convert2Negative(self):
        newImage = self.getImage(self.tempData)
        for x in range(newImage.size[0]):
            for y in range(newImage.size[1]):
                r,g,b = newImage.getpixel((x,y))
                newImage.putpixel((x,y),(255-r,255-g,255-b))
                
        self.setImage(newImage, state="edit",cImage="temp")
    
    def convert2Gray(self):
           data = self.tempData
           for i in range(len(data)):
               r,g,b = data[i]
               value = int(r*0.299 + g*0.587 + b*0.114)
               # if value < 122:
               #     value = 0   ### for BLACk - WHITE
               # else:
               #     value = 255
               data[i] = list(data[i])
               for j in range(3):
                   self.tempData[i][j] = value
           newImage = self.getImage(self.tempData)
           self.setImage(newImage, state="edit",cImage="temp")

    def changeBrightness (self, value):
        newImage = self.getImage(self.tempData)
        
        if value == "Increase":
            factor = 25
        else :
            factor = -25

        for x in range(newImage.size[0]):
            for y in range(newImage.size[1]):
                r,g,b = newImage.getpixel((x,y))
                newImage.putpixel((x,y),(r+factor,g+factor,b+factor))
                    
        
        self.setImage(newImage, state="edit",cImage="temp")
    
    def getMinMaxPix(self):
        temp,min, max = 0,0,255
        newImage = self.getImage(self.tempData,"L")
        for x in range(newImage.size[0]):
            for y in range(newImage.size[1]):
                r,g,b = newImage.getpixel((x,y))
                
    def changeContrast(self,value):
        newImage = self.getImage(self.tempData) #Convert To Gray
        data = list(newImage.getdata())

        def validFactor(factor):
            return 0 if factor < 0 else 255 if factor > 255 else int(factor)

        if value == "Increase":
            factor = 25
        else :
            factor = -25

        factor = (259 * (factor + 255)) / (255 * (259 - factor))
            
        # for i in range(len(data)):
        #     pix = data[i]
        #     newPix = pix * factor
        #     data[i] = newPix

        for x in range(newImage.size[0]):
            for y in range(newImage.size[1]):
                r,g,b = newImage.getpixel((x,y))
                r = validFactor(factor= (factor * r - 128)) + 128
                g = validFactor(factor * g - 128) + 128
                b = validFactor(factor * b - 128) + 128

                newImage.putpixel((x,y),(r,g,b))

        
        self.setImage(newImage, state="edit",cImage="temp")

    def histEqualize(self):
        newImage = self.getImage(self.tempData)
        newImage = ImageOps.equalize(newImage)
        self.setImage(newImage, state="edit",cImage="temp")
    
    def rotateImage(self, direction):
        newImage = self.getImage(self.tempData)
        width,height = newImage.size
        dataImage = Image.new("RGB", (width,height) )
        
        if direction == "left":
            angle = -(pi / 2) # angle in radian (270)
        else:
            angle = (pi / 2) # angle in radian
        
        center_x = width / 2 ## width = 1280 => 640
        center_y = height / 2 ## height = 720 => 360

        for x in range(width):
            for y in range(height):
                xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x) ## 1000 - y  
                yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y) ## 280 + x
                r,g,b = newImage.getpixel((x,y))

                if 0 <= xp < width and 0 <= yp < height:
                    dataImage.putpixel((xp,yp),(r,g,b))

        newImage.close()
        self.setImage(qImage=dataImage,state="edit",cImage="temp")

    def flipImage(self, direction):
        newImage = self.getImage(self.tempData)
        width,height = newImage.size
        dataImage = Image.new("RGB",(width,height))
        
        if direction == "vertical":
            for x in range(width - 1):
                for y  in range(height - 1):
                    r,g,b = newImage.getpixel((x,y))
                    dataImage.putpixel((x,((height-1)-y)),(r,g,b))
        else: ##Horiz
            for x in range(width - 1):
                for y  in range(height - 1):
                    r,g,b = newImage.getpixel((x,y))
                    dataImage.putpixel(((width-1)-x,y),(r,g,b))
        
        
        newImage.close()
        self.setImage(qImage=dataImage,state="edit",cImage="temp")

    def zoomOUT(self):
        newImage = self.getImage(self.tempData)
        width , height = newImage.size
        size = (int(round(0.9 * width)), 
                int(round(0.9 * height)))
        if size[0] < 5 or size[1] < 5:
            size = (5,5)
        newImage = newImage.resize(size, Image.LANCZOS)
        self.setImage(qImage=newImage,state="edit",cImage="temp")

    def zoomIN(self):
        newImage = self.getImage(self.tempData)
        width , height = newImage.size
        size = (int(round(1.1 * width)), 
                int(round(1.1 * height)))

        newImage = newImage.resize(size, Image.LANCZOS)
        self.setImage(qImage=newImage,state="edit",cImage="temp")
