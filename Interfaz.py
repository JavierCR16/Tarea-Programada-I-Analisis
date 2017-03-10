from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from crearPoblacion import *
from funcionesAdaptavilidad import *
from random import *
import numpy as np
import copy
import time

class Ui_MainWindow(object):

    generaciones = []
    minSimilitud = 0.2
    listo = False
    imagenMeta = ""
    size = width, height = 0, 0
    tamañoPoblacion = 0
    porcentajeCruce = 0
    porcentajeMenosAptos = 0
    poblacion = 0
    mutacion = 0
    arrayPoblacion = []
    comparacion = 0

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.ImagenMeta = QtWidgets.QLabel(self.centralwidget)
        self.ImagenMeta.setGeometry(QtCore.QRect(250, 40, 231, 231))
        self.ImagenMeta.setObjectName("ImagenMeta")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 141, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.PoblacionInicial = QtWidgets.QLineEdit(self.centralwidget)
        self.PoblacionInicial.setGeometry(QtCore.QRect(10, 90, 121, 20))
        self.PoblacionInicial.setObjectName("PoblacionInicial")
        self.PorcentajeMenosAptos = QtWidgets.QLineEdit(self.centralwidget)
        self.PorcentajeMenosAptos.setGeometry(QtCore.QRect(10, 170, 121, 20))
        self.PorcentajeMenosAptos.setObjectName("PorcentajeMenosAptos")
        self.PorcentajeCruce = QtWidgets.QLineEdit(self.centralwidget)
        self.PorcentajeCruce.setGeometry(QtCore.QRect(10, 130, 121, 20))
        self.PorcentajeCruce.setObjectName("PorcentajeCruce")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 181, 16))
        self.label_4.setObjectName("label_4")
        self.saveData = QtWidgets.QPushButton(self.centralwidget)
        self.saveData.setGeometry(QtCore.QRect(10, 240, 81, 23))
        self.saveData.setObjectName("saveData")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100, 240, 141, 21))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 121, 16))
        self.label_6.setObjectName("label_6")
        self.Euclideana = QtWidgets.QRadioButton(self.centralwidget)
        self.Euclideana.setGeometry(QtCore.QRect(140, 280, 84, 19))
        self.Euclideana.setObjectName("Euclideana")
        self.cosenos = QtWidgets.QRadioButton(self.centralwidget)
        self.cosenos.setGeometry(QtCore.QRect(220, 280, 150, 19))
        self.cosenos.setObjectName("Distancia de Minkowski")
        self.JavieryBryan = QtWidgets.QRadioButton(self.centralwidget)
        self.JavieryBryan.setGeometry(QtCore.QRect(355, 280, 91, 19))
        self.JavieryBryan.setObjectName("Javier y Bryan")
        #
        self.similitud = QtWidgets.QLineEdit(self.centralwidget)
        self.similitud.setGeometry(QtCore.QRect(140, 310, 41, 21))
        self.similitud.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.similitud.setObjectName("similitud")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 310, 131, 21))
        self.label_8.setObjectName("label_8")
        #
        self.PorcentajeMutacion = QtWidgets.QLineEdit(self.centralwidget)
        self.PorcentajeMutacion.setGeometry(QtCore.QRect(10, 210, 121, 20))
        self.PorcentajeMutacion.setObjectName("PorcentajeMutacion")
        self.Euclideana.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.home()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tarea Programada"))
        self.label_2.setText(_translate("MainWindow", "Imagen Meta:"))
        self.ImagenMeta.setText(_translate("MainWindow", ""))
        self.groupBox.setTitle(_translate("MainWindow", "Archivo"))
        self.pushButton.setText(_translate("MainWindow", "Abrir"))
        self.label.setText(_translate("MainWindow", "Tamaño de la población"))
        self.label_3.setText(_translate("MainWindow", "Porcentaje de cruce"))
        self.label_4.setText(_translate("MainWindow", "Individuos menos aptos"))
        self.saveData.setText(_translate("MainWindow", "Guardar/Iniciar"))
        self.label_5.setText(_translate("MainWindow", "Porcentaje mutaciones"))
        self.label_6.setText(_translate("MainWindow", "Seleccionar adaptavilidad"))
        self.Euclideana.setText(_translate("MainWindow", "Euclideana"))
        self.cosenos.setText(_translate("MainWindow", "Distancia de Minkowski"))
        self.JavieryBryan.setText(_translate("MainWindow", "Javier y Bryan"))
        self.similitud.setText(_translate("MainWindow","0.2"))
        self.label_8.setText(_translate("MainWindow", "Minimo Indice de similitud: "))

    def home(self):
        self.saveData.setEnabled(True)
        self.PorcentajeCruce.setEnabled(True)
        self.PoblacionInicial.setEnabled(True)
        self.PorcentajeMutacion.setEnabled(True)
        self.PorcentajeMenosAptos.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.similitud.setEnabled(True)
        self.JavieryBryan.setEnabled(True)
        self.Euclideana.setEnabled(True)
        self.cosenos.setEnabled(True)
        self.pushButton.clicked.connect(self.openFile)
        self.saveData.clicked.connect(self.guardarVariables)

    def openFile(self):
        self.label_7.setText("")
        try:
            fileName=self.lineEdit.text()
            self.imagenMeta = Image.open(fileName)
            self.listo=True
            self.lineEdit.setEnabled(False)
            self.pushButton.setEnabled(False)
            pixmap = QtGui.QPixmap(fileName)
            self.ImagenMeta.setPixmap(pixmap)
            self.ImagenMeta.setScaledContents(True)
        except:
            self.lineEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.label_7.setText("Imagen no encontrada")

    def guardarVariables(self):
        self.label_7.setText("")
        try:
            self.tamañoPoblacion = int(self.PoblacionInicial.text())
            self.porcentajeCruce = int(self.PorcentajeCruce.text())
            self.porcentajeMenosAptos = int(self.PorcentajeMenosAptos.text())
            self.mutacion = int(self.PorcentajeMutacion.text())
            self.minSimilitud = float(self.similitud.text())
            if(self.cosenos.isChecked()):
                self.comparacion=1
            elif(self.JavieryBryan.isChecked()):
                self.comparacion=2
            else:
                self.comparacion=0
            if(self.listo):
                self.saveData.setEnabled(False)
                self.PorcentajeCruce.setEnabled(False)
                self.PoblacionInicial.setEnabled(False)
                self.PorcentajeMutacion.setEnabled(False)
                self.PorcentajeMenosAptos.setEnabled(False)
                self.similitud.setEnabled(False)
                self.JavieryBryan.setEnabled(False)
                self.Euclideana.setEnabled(False)
                self.cosenos.setEnabled(False)
                self.label_7.setText("Guardado, Iniciado")
                self.Iniciar()
                self.label_7.setText("Finalizado")
                self.home()
            else:
                self.label_7.setText("Guardado, ingrese una imagen")
        except:
            self.saveData.setEnabled(True)
            self.PorcentajeCruce.setEnabled(True)
            self.PoblacionInicial.setEnabled(True)
            self.PorcentajeMutacion.setEnabled(True)
            self.PorcentajeMenosAptos.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.similitud.setEnabled(True)
            self.JavieryBryan.setEnabled(True)
            self.Euclideana.setEnabled(True)
            self.cosenos.setEnabled(True)
            self.label_7.setText("Error")


    def Iniciar(self):

        self.imagenMeta = self.imagenMeta.convert('L')
        if (((self.imagenMeta.size[0] % 4 != 0) or (
                self.imagenMeta.size[1] % 4 != 0)) and self.JavieryBryan.isChecked()):
            size = width, height = self.imagenMeta.size
            width = math.floor(width / 4) * 4
            height = math.floor(height / 4) * 4
            self.imagenMeta = self.imagenMeta.resize((width, height), Image.ANTIALIAS)
        size = width, height = self.imagenMeta.size
        self.arrayPoblacion = createPopulation(self.tamañoPoblacion, width, height, self.imagenMeta)
        establecerIndicesSimilitud(self.arrayPoblacion, self.imagenMeta, self.comparacion)
        generacion1 = self.arrayPoblacion.copy()
        generacion1[0].imagenGenerada.save(str(0) + "gen.png")
        self.generaciones.append(generacion1.copy())
        print(generacion1[0].indiceSimilitud)
        #Ciclo
        tmp = 1
        while(True):
            generacion1 = cruzar(generacion1, self.porcentajeCruce)
            for i in generacion1:
                i.imagenGenerada = mutacion(i, self.mutacion, self.imagenMeta)
            establecerIndicesSimilitud(generacion1, self.imagenMeta, self.comparacion)
            self.generaciones.append(generacion1.copy())
            generacion1[0].imagenGenerada.save(str(tmp)+"gen.png")
            print(generacion1[0].indiceSimilitud)
            if((generacion1[0].indiceSimilitud <= self.minSimilitud and (self.Euclideana.isChecked() or self.cosenos.isChecked())) or
                   (generacion1[0].indiceSimilitud >= self.minSimilitud and self.JavieryBryan.isChecked())):
                break
            tmp+=1
        tiraImagenes(self.generaciones)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

