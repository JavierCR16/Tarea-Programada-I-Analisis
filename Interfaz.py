from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from crearPoblacion import createPopulation

class Ui_MainWindow(object):

    listo = False
    imagenMeta = ""
    size = width, height = 0, 0
    tamañoPoblacion = 0
    porcentajeCruce = 0
    porcentajeMenosAptos = 0
    poblacion = 0
    mutacion = 0
    arrayPoblacion = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 325)
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
        self.PorcentajeMutacion = QtWidgets.QLineEdit(self.centralwidget)
        self.PorcentajeMutacion.setGeometry(QtCore.QRect(10, 210, 121, 20))
        self.PorcentajeMutacion.setObjectName("PorcentajeMutacion")
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
        self.label_4.setText(_translate("MainWindow", "Porcentaje de individos menos aptos"))
        self.saveData.setText(_translate("MainWindow", "Guardar/Iniciar"))
        self.label_5.setText(_translate("MainWindow", "Porcentaje de genes a mutar"))

    def home(self):
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
            if(self.listo):
                self.saveData.setEnabled(False)
                self.PorcentajeCruce.setEnabled(False)
                self.PoblacionInicial.setEnabled(False)
                self.PorcentajeMutacion.setEnabled(False)
                self.PorcentajeMenosAptos.setEnabled(False)
                self.label_7.setText("Guardado, Iniciado")
                self.Iniciar()
            else:
                self.label_7.setText("Guardado, ingrese una imagen")
        except:
            self.label_7.setText("Solo números enteros")

    def Iniciar(self):
        size = width, height = self.imagenMeta.size
        self.arrayPoblacion = createPopulation(self.tamañoPoblacion, width, height)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
