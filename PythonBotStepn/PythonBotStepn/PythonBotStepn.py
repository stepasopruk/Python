from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtGui, QtWidgets

import pyscreenshot
import pyautogui
from PIL import Image, ImageGrab
from time import sleep
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import tkinter.messagebox
import tkinter as tk
import threading

Form, Window = uic.loadUiType("A:/PythonBot/PythonApplication1/PythonApplication1/interface01.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

compliteSetting = False
process = True
processUpdate = True
complitePrice = False
complitePriceIdButtonBuy = None
recordedPrice = False
refreshComplited = True

def clickSaveSetting():
    global pathProgramm, pathTesseract, pathRefreshImg_1, pathRefreshImg_2, pathBuyButton, pathConfirmButton, PriceBuy
    global coordSneakers_x1_1, coordSneakers_y1_1, coordSneakers_x2_1, coordSneakers_y2_1
    global coordSneakers_x1_2, coordSneakers_y1_2, coordSneakers_x2_2, coordSneakers_y2_2
    global coordSneakers_x1_3, coordSneakers_y1_3, coordSneakers_x2_3, coordSneakers_y2_3
    global coordSneakers_x1_4, coordSneakers_y1_4, coordSneakers_x2_4, coordSneakers_y2_4
    global coordPrice_x1_1, coordPrice_y1_1, coordPrice_x2_1, coordPrice_y2_1
    global coordPrice_x1_2, coordPrice_y1_2, coordPrice_x2_2, coordPrice_y2_2
    global coordPrice_x1_3, coordPrice_y1_3, coordPrice_x2_3, coordPrice_y2_3
    global coordPrice_x1_4, coordPrice_y1_4, coordPrice_x2_4, coordPrice_y2_4
    global compliteSetting
    #-------------------------------------------------------------------------------------------
    pathProgramm = form.pathProgrammText.text()
    pathTesseract = form.pathTesseractText.text()
    pathRefreshImg_1 = form.pathRefreshImgText1.text()
    pathRefreshImg_2 = form.pathRefreshImgText2.text()
    pathBuyButton = form.pathBuyButtonText.text()
    pathConfirmButton = form.pathConfirmButtonText.text()
    PriceBuy = form.PriceBuyText.text()
    #-------------------------------------------------------------------------------------------
    coordSneakers_x1_1 = form.coordSneakersText_x1_1.text()
    coordSneakers_y1_1 = form.coordSneakersText_y1_1.text()
    coordSneakers_x2_1 = form.coordSneakersText_x2_1.text()
    coordSneakers_y2_1 = form.coordSneakersText_y2_1.text()

    coordSneakers_x1_2 = form.coordSneakersText_x1_2.text()
    coordSneakers_y1_2 = form.coordSneakersText_y1_2.text()
    coordSneakers_x2_2 = form.coordSneakersText_x2_2.text()
    coordSneakers_y2_2 = form.coordSneakersText_y2_2.text()

    coordSneakers_x1_3 = form.coordSneakersText_x1_3.text()
    coordSneakers_y1_3 = form.coordSneakersText_y1_3.text()
    coordSneakers_x2_3 = form.coordSneakersText_x2_3.text()
    coordSneakers_y2_3 = form.coordSneakersText_y2_3.text()

    coordSneakers_x1_4 = form.coordSneakersText_x1_4.text()
    coordSneakers_y1_4 = form.coordSneakersText_y1_4.text()
    coordSneakers_x2_4 = form.coordSneakersText_x2_4.text()
    coordSneakers_y2_4 = form.coordSneakersText_y2_4.text()
    #-------------------------------------------------------------------------------------------
    coordPrice_x1_1 = form.coordPriceText_x1_1.text()
    coordPrice_y1_1 = form.coordPriceText_y1_1.text()
    coordPrice_x2_1 = form.coordPriceText_x2_1.text()
    coordPrice_y2_1 = form.coordPriceText_y2_1.text()

    coordPrice_x1_2 = form.coordPriceText_x1_2.text()
    coordPrice_y1_2 = form.coordPriceText_y1_2.text()
    coordPrice_x2_2 = form.coordPriceText_x2_2.text()
    coordPrice_y2_2 = form.coordPriceText_y2_2.text()

    coordPrice_x1_3 = form.coordPriceText_x1_3.text()
    coordPrice_y1_3 = form.coordPriceText_y1_3.text()
    coordPrice_x2_3 = form.coordPriceText_x2_3.text()
    coordPrice_y2_3 = form.coordPriceText_y2_3.text()

    coordPrice_x1_4 = form.coordPriceText_x1_4.text()
    coordPrice_y1_4 = form.coordPriceText_y1_4.text()
    coordPrice_x2_4 = form.coordPriceText_x2_4.text()
    coordPrice_y2_4 = form.coordPriceText_y2_4.text()
    #-------------------------------------------------------------------------------------------
    print(pathProgramm)
    print(pathTesseract)
    print(pathRefreshImg_1)
    print(pathRefreshImg_2)
    print(float(PriceBuy))
    #-------------------------------------------------------------------------------------------    
    compliteSetting = True


def WorkingProcess():
    global process, complitePriceIdButtonBuy, processUpdate, recordedPrice, refreshComplited
    global pathProgramm, pathTesseract, pathRefreshImg_1, pathRefreshImg_2, pathBuyButton, pathConfirmButton, PriceBuy

    while process:
        print("----------------------")
        def ClickRefresh():
            global process, pathRefreshImg_1, pathRefreshImg_2
            if process:
                try:    
                    templateFilter = pyautogui.locateCenterOnScreen(pathRefreshImg_1, confidence=0.7)
                except:
                    process = False
                    print("Error, code: Ex02")
                    tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex02")

            sleep(0.1)

            if process:
                try:
                    pyautogui.click(templateFilter[0], templateFilter[1])
                except:
                    process = False
                    print("Error, code: Ex03")
                    tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex03")

            if process:
                try:
                    templateConfirm = pyautogui.locateCenterOnScreen(pathRefreshImg_2, confidence=0.7)
                except:
                    process = False
                    print("Error, code: Ex04")
                    tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex04")

            sleep(0.1)

            if process:
                try:
                    pyautogui.click(templateConfirm[0], templateConfirm[1])
                except:
                    process = False
                    print("Error, code: Ex05")
                    tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex05")
            sleep(0.5)
        
        if process:
            if processUpdate:
                if recordedPrice:
                    ClickRefresh()
                    refreshComplited = True
                    recordedPrice = False

        if process:
            if processUpdate == False:
                ButtonsBuy = list(pyautogui.locateAllOnScreen(pathBuyButton, confidence=0.95))

        def PriceCheckBuy(idButtonBuy):
            global process     
            try:
                ButtonsBuy[idButtonBuy] = pyautogui.center(ButtonsBuy[idButtonBuy])
                pyautogui.click(ButtonsBuy[idButtonBuy])
                sleep(1)
                ButtonConfirm = pyautogui.locateCenterOnScreen(pathConfirmButton, confidence=0.5)
                print(ButtonConfirm)
                pyautogui.click(ButtonConfirm)
                sleep(1)
                #--- ≈ще один клик ---
                print('Complete')
                tkinter.messagebox.showinfo(title = "Complete", message = "Complete")
                process = False
            except:
                process = False
                print("Error, code: Ex11")
                tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex11")
        
        if process:
            if processUpdate == False:
                PriceCheckBuy(complitePriceIdButtonBuy)


def ConstantlyUpdated():
    global processUpdate, process, refreshComplited, recordedPrice
    while processUpdate:
        print("++++++++++++++++++++++++++++++")
        def SaveImageSneakersAndPrice():
            global processUpdate, process
            global coordPrice_x1_1, coordPrice_y1_1, coordPrice_x2_1, coordPrice_y2_1
            global coordPrice_x1_2, coordPrice_y1_2, coordPrice_x2_2, coordPrice_y2_2
            global coordPrice_x1_3, coordPrice_y1_3, coordPrice_x2_3, coordPrice_y2_3
            global coordPrice_x1_4, coordPrice_y1_4, coordPrice_x2_4, coordPrice_y2_4
            try:
                scr1Price = pyscreenshot.grab(bbox = (int(coordPrice_x1_1),int(coordPrice_y1_1),int(coordPrice_x2_1),int(coordPrice_y2_1)))
                scr1Price.save('scr1Price.png')
                scr2Price = pyscreenshot.grab(bbox = (int(coordPrice_x1_2),int(coordPrice_y1_2),int(coordPrice_x2_2),int(coordPrice_y2_2)))
                scr2Price.save('scr2Price.png')
                scr3Price = pyscreenshot.grab(bbox = (int(coordPrice_x1_3),int(coordPrice_y1_3),int(coordPrice_x2_3),int(coordPrice_y2_3)))
                scr3Price.save('scr3Price.png')
                scr4Price = pyscreenshot.grab(bbox = (int(coordPrice_x1_4),int(coordPrice_y1_4),int(coordPrice_x2_4),int(coordPrice_y2_4)))
                scr4Price.save('scr4Price.png')
                print('Complited Saving Image Price')
            except:
                processUpdate = False
                process = False
                print("Error, code: Ex07")
                tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex07")
    
        def imgToString(img, Price_cv):
            ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
            rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))
            dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
            cv2.imwrite('dilation_image.jpg',dilation)
            contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                rect=cv2.rectangle(Price_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cropped = Price_cv[y:y + h, x:x + w]
                cv2.imwrite('rectanglebox.jpg',rect)
                text = pytesseract.image_to_string(cropped)
                return text

        def ImageReadingAndGrayscaleConversion():
            global processUpdate, process
            global Price_cv_1, Price_cv_2, Price_cv_3, Price_cv_4
            global grayPrice_cv_1, grayPrice_cv_2, grayPrice_cv_3, grayPrice_cv_4
            try:
                Price_cv_1 = cv2.imread('scr1Price.png')
                Price_cv_2 = cv2.imread('scr2Price.png')
                Price_cv_3 = cv2.imread('scr3Price.png')
                Price_cv_4 = cv2.imread('scr4Price.png')
                grayPrice_cv_1 = cv2.cvtColor(Price_cv_1, cv2.COLOR_BGR2GRAY)
                grayPrice_cv_2 = cv2.cvtColor(Price_cv_2, cv2.COLOR_BGR2GRAY)
                grayPrice_cv_3 = cv2.cvtColor(Price_cv_3, cv2.COLOR_BGR2GRAY)
                grayPrice_cv_4 = cv2.cvtColor(Price_cv_4, cv2.COLOR_BGR2GRAY)
            except:
                processUpdate = False
                process = False
                print("Error, code: Ex08")
                tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex08")

        def PriceToString():
            global processUpdate, process
            global Price_1, Price_2, Price_3, Price_4
            global Price_cv_1, Price_cv_2, Price_cv_3, Price_cv_4
            global grayPrice_cv_1, grayPrice_cv_2, grayPrice_cv_3, grayPrice_cv_4
            try:
                Price_1 = imgToString(grayPrice_cv_1, Price_cv_1)
                Price_2 = imgToString(grayPrice_cv_2, Price_cv_2)
                Price_3 = imgToString(grayPrice_cv_3, Price_cv_3)
                Price_4 = imgToString(grayPrice_cv_4, Price_cv_4)
                print('Price_1 ')
                print(Price_1)
                print('Price_2 ')
                print(Price_2)
                print('Price_3 ')
                print(Price_3)
                print('Price_4 ')
                print(Price_4)
            except:
                processUpdate = False
                process = False
                print("Error, code: Ex09")
                tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex09")

        def DelExcessString(string):
            if string != None:
                string = string.replace(' ', '')
                string = string.replace('S', '')
                string = string.replace('O', '')
                string = string.replace('L', '')
                string = string.replace(',', '.')
                string = string.replace('(', '')
                string = string.replace(')', '')
                string = string.replace("'", '')
                string = string.replace('|', '')
                string = string.replace("`", '')
                return string
            else:
                return None

        def PriceRecord():
            global processUpdate, process
            global Price_1, Price_2, Price_3, Price_4
            try:
                Price_1 = DelExcessString(Price_1)
                Price_2 = DelExcessString(Price_2)
                Price_3 = DelExcessString(Price_3)
                Price_4 = DelExcessString(Price_4)
                print('The price of the first: ')
                print(Price_1)
                print('The price of the second ')
                print(Price_2)
                print('The price of the third: ')
                print(Price_3)
                print('The price of the fourth: ')
                print(Price_4)
            except:
                processUpdate = False
                process = False
                print("Error, code: Ex10")
                tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex10")

        def is_float(value):
            try:
                float(value)
                return True
            except:
                return False

        def PriceCheckBuy(price, idButtonBuy):
            global processUpdate, complitePrice, complitePriceIdButtonBuy
            if is_float(price): 
                if float(price) <= float(PriceBuy):
                    processUpdate = False
                    complitePrice = True
                    complitePriceIdButtonBuy = idButtonBuy
                    print("!!!!!!!!!!!!!!!")
    
        if refreshComplited:
            refreshComplited = False
            if processUpdate:
                SaveImageSneakersAndPrice()
            if processUpdate:
                ImageReadingAndGrayscaleConversion()
            if processUpdate:          
                PriceToString()
            if processUpdate:
                PriceRecord()
            if processUpdate:
                PriceCheckBuy(Price_1, 0)
            if processUpdate:
                PriceCheckBuy(Price_2, 1)
            if processUpdate:
                PriceCheckBuy(Price_3, 2)
            if processUpdate:
                PriceCheckBuy(Price_4, 3)
            recordedPrice = True




def clickStart():
    global pathTesseract
    if compliteSetting:
        try:
            pytesseract.pytesseract.tesseract_cmd = pathTesseract
        except:
            print("Error, code: Ex01")
            tkinter.messagebox.showerror(title = "Error", message = "Error, code: Ex01")
            exit(0)

        t = threading.Thread(target=WorkingProcess, args=())
        t.start()
        l = threading.Thread(target=ConstantlyUpdated, args=())
        l.start()
    else:
        tkinter.messagebox.showinfo(title = "SaveSetting", message = "Please, save setting")
    

def clickExit():
    global process, processUpdate
    process = False
    processUpdate = False
    print("Exit")

form.startButton.clicked.connect(clickStart)
form.exitButton.clicked.connect(clickExit)
form.saveSettingButton.clicked.connect(clickSaveSetting)

app.exec()
