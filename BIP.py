# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Goruntu_Isleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ModulFeatures import Feature
import functools

class Ui_MainWindow(object):
    features = None
    def setupUi(self, MainWindow):
## Main Window GUI ##
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 852)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
## Central Widget GUI ##
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);\n"
                                            "font: 25 12pt \"Calibri Light\";")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
## Scroll Area GUI ##
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 400))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.HLine)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
## Image View GUI ##
        self.imageView = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageView.setEnabled(True)
        self.imageView.setToolTip("Click to view original image")
        self.imageView.setToolTipDuration(1)
        self.imageView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageView.setLineWidth(0)
        self.pixMap = QtGui.QPixmap("default.jpg")
        self.imageView.setPixmap(self.pixMap)
        self.imageView.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView.setObjectName("imageView")
        self.imageView.mouseReleaseEvent = self.clickImagePreview
        self.verticalLayout.addWidget(self.imageView)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

## Tab Widget GUI ##
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
    ## LoadTab ##
        self.tabLoadSave = QtWidgets.QWidget()
        self.tabLoadSave.setObjectName("tabLoadSave")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabLoadSave)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        ## Image Upload - Load Button ##
        self.loadBtn = QtWidgets.QPushButton(self.tabLoadSave)
        self.loadBtn.setMinimumSize(QtCore.QSize(200, 100))
        self.loadBtn.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "border-color: rgb(0, 0, 0);")
        self.loadBtn.setDefault(True)
        self.loadBtn.setFlat(True)
        self.loadBtn.setObjectName("loadBtn")
        self.loadBtn.clicked.connect(self.clickLoad) # load Click
        self.gridLayout_3.addWidget(self.loadBtn, 1, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        ## Image Save - Save Button ##
        self.saveBtn = QtWidgets.QPushButton(self.tabLoadSave)
        self.saveBtn.setMinimumSize(QtCore.QSize(200, 100))
        self.saveBtn.setSizeIncrement(QtCore.QSize(200, 100))
        self.saveBtn.setBaseSize(QtCore.QSize(200, 100))
        self.saveBtn.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "border-color: rgb(0, 0, 0);")
        self.saveBtn.setDefault(True)
        self.saveBtn.setFlat(True)
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.clickSave) # save Click
        self.gridLayout_3.addWidget(self.saveBtn, 1, 4, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tabLoadSave, "")
    
    ## FeaturesTab ##
        self.tabFeatures = QtWidgets.QWidget()
        self.tabFeatures.setObjectName("tabFeatures")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabFeatures)
        self.gridLayout_4.setObjectName("gridLayout_4")

    
    ## FeaturesTab - Increase Brightness ##
        self.IncreaseBrightBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.IncreaseBrightBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.IncreaseBrightBtn.setDefault(True)
        self.IncreaseBrightBtn.setFlat(True)
        self.IncreaseBrightBtn.setObjectName("IncreaseBrightBtn")
        self.IncreaseBrightBtn.clicked.connect(functools.partial(self.clickBrightness,"Increase")) #click Increase Brightness
        self.gridLayout_4.addWidget(self.IncreaseBrightBtn, 0, 4, 1, 1)
   
    ## FeaturesTab - Decrease Brightness ##
        self.DecreaseBrightBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.DecreaseBrightBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.DecreaseBrightBtn.setDefault(True)
        self.DecreaseBrightBtn.setFlat(True)
        self.DecreaseBrightBtn.setObjectName("DecreaseBrightBtn")
        self.DecreaseBrightBtn.clicked.connect(functools.partial(self.clickBrightness,"Decrease")) #click Decrease Brightness
        self.gridLayout_4.addWidget(self.DecreaseBrightBtn, 0, 5, 1, 1)

    ## FeaturesTab - Increase Contrast ##
        self.IncreaseConrasttBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.IncreaseConrasttBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.IncreaseConrasttBtn.setDefault(True)
        self.IncreaseConrasttBtn.setFlat(True)
        self.IncreaseConrasttBtn.setObjectName("IncreaseConrasttBtn")
        self.IncreaseConrasttBtn.clicked.connect(functools.partial(self.clickContrast,"Increase")) #click Increase Contrast
        self.gridLayout_4.addWidget(self.IncreaseConrasttBtn, 1, 4, 1, 1)

    ## FeaturesTab - Decrease Contrast ##
        self.DecreaseContrastBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.DecreaseContrastBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.DecreaseContrastBtn.setDefault(True)
        self.DecreaseContrastBtn.setFlat(True)
        self.DecreaseContrastBtn.setObjectName("DecreaseContrastBtn")
        self.DecreaseContrastBtn.clicked.connect(functools.partial(self.clickContrast,"Decrease")) #click Decrease Contrast
        self.gridLayout_4.addWidget(self.DecreaseContrastBtn, 1, 5, 1, 1)

    ## FeaturesTab - GrayScale ##
        self.GrayScaleBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.GrayScaleBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.GrayScaleBtn.setMaximumSize(QtCore.QSize(160, 80))
        self.GrayScaleBtn.setDefault(True)
        self.GrayScaleBtn.setFlat(True)
        self.GrayScaleBtn.setObjectName("GrayScaleBtn")
        self.GrayScaleBtn.clicked.connect(self.clickGrayscale) # click Grayscale 
        self.gridLayout_4.addWidget(self.GrayScaleBtn, 0, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)

    ## FeaturesTab - Black white ##
        self.BlcakWhiteBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.BlcakWhiteBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.BlcakWhiteBtn.setMaximumSize(QtCore.QSize(160, 80))
        self.BlcakWhiteBtn.setDefault(True)
        self.BlcakWhiteBtn.setFlat(True)
        self.BlcakWhiteBtn.setObjectName("BlcakWhiteBtn")
        self.BlcakWhiteBtn.clicked.connect(self.clickBlackWhite)# Click Black white
        self.gridLayout_4.addWidget(self.BlcakWhiteBtn, 0, 2, 1, 1)

    ## FeaturesTab - Negative ##
        self.NegativeBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.NegativeBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.NegativeBtn.setMaximumSize(QtCore.QSize(160, 80))
        self.NegativeBtn.setDefault(True)
        self.NegativeBtn.setFlat(True)
        self.NegativeBtn.setObjectName("NegativeBtn")
        self.NegativeBtn.clicked.connect(self.clickNegative) # click Negative
        self.gridLayout_4.addWidget(self.NegativeBtn, 1, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)

    ## FeaturesTab - Histogram Equlization ##
        self.HistogramEqualizationBtn = QtWidgets.QPushButton(self.tabFeatures)
        self.HistogramEqualizationBtn.setMinimumSize(QtCore.QSize(160, 80))
        self.HistogramEqualizationBtn.setMaximumSize(QtCore.QSize(160, 80))
        self.HistogramEqualizationBtn.setDefault(True)
        self.HistogramEqualizationBtn.setFlat(True)
        self.HistogramEqualizationBtn.setObjectName("HistogramEqualizationBtn")
        self.HistogramEqualizationBtn.clicked.connect(self.clickHistogramEqu) #click Histogram Equlization
        self.gridLayout_4.addWidget(self.HistogramEqualizationBtn, 1, 2, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 6, 1, 1)

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabFeatures, "")

    ## RotateTab ##
        self.tabRotate = QtWidgets.QWidget()
        self.tabRotate.setObjectName("tabRotate")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabRotate)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 2, 1, 1, 1)
   
    ## RotateTab - Frame ##
        self.frame = QtWidgets.QFrame(self.tabRotate)
        self.frame.setStyleSheet("border-color: rgb(10, 94, 189);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(-1, 0, 10, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
   
    ## RotateTab - Zoom Out ##
        self.zoomOutBtn = QtWidgets.QPushButton(self.frame)
        self.zoomOutBtn.setDefault(True)
        self.zoomOutBtn.setFlat(True)
        self.zoomOutBtn.setObjectName("zoomOutBtn")
        self.zoomOutBtn.clicked.connect(self.clickZoomOUT) #click Zoom Out
        self.gridLayout_5.addWidget(self.zoomOutBtn, 3, 0, 1, 1)

    ## RotateTab - Zoom In ##
        self.zoomInBtn = QtWidgets.QPushButton(self.frame)
        self.zoomInBtn.setAutoFillBackground(False)
        self.zoomInBtn.setCheckable(False)
        self.zoomInBtn.setAutoDefault(False)
        self.zoomInBtn.setDefault(True)
        self.zoomInBtn.setFlat(True)
        self.zoomInBtn.setObjectName("zoomInBtn")
        self.zoomInBtn.clicked.connect(self.clickZoomIN) #click Zoom In
        self.gridLayout_5.addWidget(self.zoomInBtn, 2, 0, 1, 1)

    ## RotateTab - Resize ##
        self.resizeBtn = QtWidgets.QPushButton(self.frame)
        self.resizeBtn.setDefault(True)
        self.resizeBtn.setFlat(True)
        self.resizeBtn.setObjectName("resizeBtn")
        # self.resizeBtn.clicked.connect() #click Resize
        self.gridLayout_5.addWidget(self.resizeBtn, 4, 2, 1, 1)

    ## RotateTab - Height Label ##
        self.heightLbl = QtWidgets.QLabel(self.frame)
        self.heightLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.heightLbl.setAutoFillBackground(False)
        self.heightLbl.setLineWidth(0)
        self.heightLbl.setScaledContents(False)
        self.heightLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.heightLbl.setObjectName("heightLbl")
        self.gridLayout_5.addWidget(self.heightLbl, 3, 1, 1, 1)

    ## RotateTab - Height TextBox ##
        self.heightTxtBox = QtWidgets.QLineEdit(self.frame)
        self.heightTxtBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.heightTxtBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.heightTxtBox.setObjectName("heightTxtBox")
        self.gridLayout_5.addWidget(self.heightTxtBox, 3, 2, 1, 1)

    ## RotateTab - Width Label  ##
        self.widthLbl = QtWidgets.QLabel(self.frame)
        self.widthLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widthLbl.setAutoFillBackground(False)
        self.widthLbl.setLineWidth(0)
        self.widthLbl.setScaledContents(False)
        self.widthLbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.widthLbl.setObjectName("widthLbl")
        self.gridLayout_5.addWidget(self.widthLbl, 2, 1, 1, 1)

    ## RotateTab - Width TextBox ##
        self.widthTxtBox = QtWidgets.QLineEdit(self.frame)
        self.widthTxtBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.widthTxtBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.widthTxtBox.setObjectName("widthTxtBox")
        self.gridLayout_5.addWidget(self.widthTxtBox, 2, 2, 1, 1)

    ## RotateTab - Zoom/Crop Label  ##
        self.zoomCropLbl = QtWidgets.QLabel(self.frame)
        self.zoomCropLbl.setMinimumSize(QtCore.QSize(353, 0))
        self.zoomCropLbl.setMaximumSize(QtCore.QSize(16777215, 30))
        self.zoomCropLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.zoomCropLbl.setObjectName("zoomCropLbl")
        self.gridLayout_5.addWidget(self.zoomCropLbl, 1, 0, 1, 3)

        self.gridLayout_6.addWidget(self.frame, 2, 2, 1, 1)

        self.frame_2 = QtWidgets.QFrame(self.tabRotate)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

    ## RotateTab - Rotate/Mirror Label  ##
        self.rotateMirrorLbl = QtWidgets.QLabel(self.frame_2)
        self.rotateMirrorLbl.setMinimumSize(QtCore.QSize(210, 0))
        self.rotateMirrorLbl.setMaximumSize(QtCore.QSize(12312312, 30))
        self.rotateMirrorLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rotateMirrorLbl.setAutoFillBackground(False)
        self.rotateMirrorLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rotateMirrorLbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rotateMirrorLbl.setLineWidth(0)
        self.rotateMirrorLbl.setScaledContents(False)
        self.rotateMirrorLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.rotateMirrorLbl.setObjectName("rotateMirrorLbl")
        self.gridLayout_4.addWidget(self.rotateMirrorLbl, 0, 0, 1, 2)

    ## RotateTab - Rotate Left  ##
        self.rotateLeftBtn = QtWidgets.QPushButton(self.frame_2)
        self.rotateLeftBtn.setDefault(True)
        self.rotateLeftBtn.setFlat(True)
        self.rotateLeftBtn.setObjectName("rotateLeftBtn")
        self.rotateLeftBtn.clicked.connect(functools.partial(self.clickRotateImage,"left")) #click Rotate left
        self.gridLayout_4.addWidget(self.rotateLeftBtn, 1, 0, 1, 1)

    ## RotateTab - Rotate Right  ##
        self.rotateRightBtn = QtWidgets.QPushButton(self.frame_2)
        self.rotateRightBtn.setDefault(True)
        self.rotateRightBtn.setFlat(True)
        self.rotateRightBtn.setObjectName("rotateRightBtn")
        self.rotateRightBtn.clicked.connect(functools.partial(self.clickRotateImage,"right")) #click Rotate Right
        self.gridLayout_4.addWidget(self.rotateRightBtn, 1, 1, 1, 1)

    ## RotateTab - Horizontal Flip  ##
        self.horizontalFlipBtn = QtWidgets.QPushButton(self.frame_2)
        self.horizontalFlipBtn.setDefault(True)
        self.horizontalFlipBtn.setFlat(True)
        self.horizontalFlipBtn.setObjectName("horizontalFlipBtn")
        self.horizontalFlipBtn.clicked.connect(functools.partial(self.clickFlipImage,"horizontal")) #click Horizontal
        self.gridLayout_4.addWidget(self.horizontalFlipBtn, 2, 0, 1, 1)

    ## RotateTab - Vertical Flip  ##
        self.verticalFlipBtn = QtWidgets.QPushButton(self.frame_2)
        self.verticalFlipBtn.setDefault(True)
        self.verticalFlipBtn.setFlat(True)
        self.verticalFlipBtn.setObjectName("verticalFlipBtn")
        self.verticalFlipBtn.clicked.connect(functools.partial(self.clickFlipImage,"vertical")) #click Vertical
        self.gridLayout_4.addWidget(self.verticalFlipBtn, 2, 1, 1, 1)

        self.gridLayout_6.addWidget(self.frame_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabRotate, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.features = Feature(self)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadBtn.setText(_translate("MainWindow", "Load"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLoadSave), _translate("MainWindow", "Load/Save"))
        self.DecreaseContrastBtn.setText(_translate("MainWindow", "Decrease Contrast"))
        self.IncreaseBrightBtn.setText(_translate("MainWindow", "Increase Brightness"))
        self.IncreaseConrasttBtn.setText(_translate("MainWindow", "Increase Contrast"))
        self.DecreaseBrightBtn.setText(_translate("MainWindow", "Decrease Brightness"))
        self.GrayScaleBtn.setText(_translate("MainWindow", "GrayScale"))
        self.BlcakWhiteBtn.setText(_translate("MainWindow", "Blackwhite"))
        self.NegativeBtn.setText(_translate("MainWindow", "Negative"))
        self.HistogramEqualizationBtn.setText(_translate("MainWindow", "Histogram Equ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFeatures), _translate("MainWindow", "Features"))
        self.zoomOutBtn.setText(_translate("MainWindow", "Zoom Out"))
        self.heightLbl.setText(_translate("MainWindow", "Height"))
        self.zoomInBtn.setText(_translate("MainWindow", "Zoom In"))
        self.resizeBtn.setText(_translate("MainWindow", "Resize"))
        self.widthLbl.setText(_translate("MainWindow", "Width "))
        self.zoomCropLbl.setText(_translate("MainWindow", "Zoom/Crop"))
        self.rotateMirrorLbl.setText(_translate("MainWindow", "Rotate/Mirror"))
        self.rotateLeftBtn.setText(_translate("MainWindow", "To Left"))
        self.rotateRightBtn.setText(_translate("MainWindow", "To Right"))
        self.horizontalFlipBtn.setText(_translate("MainWindow", "Horizontal"))
        self.verticalFlipBtn.setText(_translate("MainWindow", "Vertical"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRotate), _translate("MainWindow", "Rotate/Crop"))


## Funcs ##
    def clickLoad(self):
         self.features.uploadImage()

    def clickSave(self):
        self.features.save()
    
    def clickImagePreview(self,event):
        self.features.previewImage()

    def clickZoomIN(self):
        self.features.zoomIN()
        width, height = self.features.getSize()
        title = str(width) + "x" + str(height)
        MainWindow.setWindowTitle("MainWindow   Zoom: " + title)

    def clickZoomOUT(self):
        self.features.zoomOUT()
        width, height = self.features.getSize()
        title = str(width) + "x" + str(height)
        MainWindow.setWindowTitle("MainWindow   Zoom: " + title)

    def clickFlipImage(self,direction):
        self.features.flipImage(direction)

    def clickRotateImage(self,direction):
        self.features.rotateImage(direction)
    
    def clickResize(self):
        pass ## Improving

    def clickHistogramEqu(self):
        self.features.histEqualize()
    
    def clickNegative(self):
        self.features.convert2Negative()

    def clickBlackWhite(self):
        self.features.convert2Blackwhite()
    
    def clickGrayscale(self):
        self.features.convert2Gray()

    def clickBrightness(self,value):
        self.features.changeBrightness(value)
    
    def clickContrast(self,value):
        self.features.changeContrast(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())