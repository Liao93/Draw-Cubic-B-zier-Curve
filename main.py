import numpy as np
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import ui.bezierUi as ui

def bernstein(n, t):
    #B0=(1-t)^3
    if n==0:
        return (1-t) ** 3
    #B1=3t(1-t)^2
    elif n==1:
        return 3 * t * (1-t) ** 2
    #B2=3t^2(1-t)
    elif n==2:
        return (3 * t ** 2) * (1-t)
    #B3=t^3
    elif n==3:
        return t ** 3
    else:
        return 0

class Main(QMainWindow, ui.Ui_MainWindow):
    win_name = 'Draw Bezier curve'
    controlP = []
    background = 50

    def __init__(self):
         super().__init__()
         self.setupUi(self)
         
         self.imgToShow = np.zeros((1000, 1000, 3), np.uint8)
         self.imgToShow.fill(self.background)
         
         self.resetButton.clicked.connect(self.resetBtn)
         self.drawButton.clicked.connect(self.drawBtn)
         
         
         cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
         cv2.setMouseCallback(self.win_name, self.addPoint)
         cv2.resizeWindow(self.win_name, 1000, 1000)
         cv2.imshow(self.win_name, self.imgToShow)
         
    def showWin(self):
        cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
        cv2.setMouseCallback(self.win_name, self.addPoint)
        cv2.resizeWindow(self.win_name, 1000, 1000)
        cv2.imshow(self.win_name, self.imgToShow)
         
    def resetBtn(self):
        self.controlP.clear()
        self.p1_info.setText('')
        self.p2_info.setText('')
        self.p3_info.setText('')
        self.p4_info.setText('')
        self.imgToShow.fill(self.background)
        self.showWin()
    
    def drawBtn(self, imgs): 
        if len(self.controlP) == 4:
            #Draw lines between control points
            for i in range(3):
                cv2.line(self.imgToShow, self.controlP[i], self.controlP[i+1], (255,0,0), 5)
            #Find the point on curve at t=a
            a = 0.33
            p_a = self.findPa(a)
            #Draw bezier curve
            self.drawCurve()
            #draw the point on curve at t=a
            self.drawPa(p_a, a)
            self.showWin()

    def addPoint(self, event, x, y, flags, param):
       global mouseX, mouseY
       if event== cv2.EVENT_LBUTTONDBLCLK:
            if len(self.controlP)<4:
                # Add a control point to list
                self.controlP.append((x, y))
                
                #Show information of control point
                if len(self.controlP) == 1:
                    text = 'P1: (' + str(x) + ', ' + str(y) + ')'
                    self.p1_info.setText(text)
                elif len(self.controlP) == 2:
                    text = 'P2: (' + str(x) + ', ' + str(y) + ')'
                    self.p2_info.setText(text)
                elif len(self.controlP) == 3:
                    text = 'P3: (' + str(x) + ', ' + str(y) + ')'
                    self.p3_info.setText(text)
                elif len(self.controlP) == 4:
                    text = 'P4: (' + str(x) + ', ' + str(y) + ')'
                    self.p4_info.setText(text)
                    
                # Draw control point and show
                # color: BGR
                cv2.circle(self.imgToShow, (x,y), 5, (255,0,0), -1)
                self.showWin()

            mouseX, mouseY = x,y
            
    def findPa(self, a=0.5):
        #Use subdividing to find p(a)
        P0 = self.controlP[0]
        P1 = self.controlP[1]
        P2 = self.controlP[2]
        P3 = self.controlP[3]
        P01 = (round((1-a)*P0[0] + a*P1[0]), round((1-a)*P0[1] + a*P1[1]))
        P11 = (round((1-a)*P1[0] + a*P2[0]), round((1-a)*P1[1] + a*P2[1]))
        P21 = (round((1-a)*P2[0] + a*P3[0]), round((1-a)*P2[1] + a*P3[1]))
        cv2.line(self.imgToShow, P01, P11, (0,255,0), 3)
        cv2.line(self.imgToShow, P11, P21, (0,255,0), 3)
        P02 = (round((1-a)*P01[0] + a*P11[0]), round((1-a)*P01[1] + a*P11[1]))
        P12 = (round((1-a)*P11[0] + a*P21[0]), round((1-a)*P11[1] + a*P21[1]))
        cv2.line(self.imgToShow, P02, P12, (0,255,0), 3)
        return (round((1-a)*P02[0] + a*P12[0]), round((1-a)*P02[1] + a*P12[1]))
    
    def drawPa(self, p_a, a):
        #Draw p(a)
        cv2.circle(self.imgToShow, p_a, 5, (0,0,0), -1)
        text = 'a = ' + str(a)
        cv2.putText(self.imgToShow, text, (850, 925), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
    def drawCurve(self, N=300):
        # N: segements # of curve
        for i in range(N+1):
            t = i/N
            x, y = 0, 0
            # p(t) = p0*B0(t) + p1*B1(t) + p2*B2(t) + p3*B3(t)
            for j in range(4):
                x += bernstein(j, t) * self.controlP[j][0]
                y += bernstein(j, t) * self.controlP[j][1]
            x = round(x)
            y = round(y)
            cv2.circle(self.imgToShow, (x,y) ,3, (0,0,255), -1)
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())




