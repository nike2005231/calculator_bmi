from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 275)
        MainWindow.setStyleSheet("background-color: rgb(198, 224, 255);")
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 187, 151, 41))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.lineEdit_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_weight.setGeometry(QtCore.QRect(190, 110, 41, 22))
        self.lineEdit_weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_weight.setText("")
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.lineEdit_weight.setMaxLength(3)

        self.lineEdit_height = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_height.setGeometry(QtCore.QRect(190, 140, 41, 22))
        self.lineEdit_height.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.lineEdit_height.setMaxLength(3)

        self.label_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_weight.setGeometry(QtCore.QRect(140, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_weight.setFont(font)
        self.label_weight.setStyleSheet("")
        self.label_weight.setObjectName("label_weight")

        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setGeometry(QtCore.QRect(140, 140, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_height.setFont(font)
        self.label_height.setObjectName("label_height")

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(40, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)

        self.label_imt = QtWidgets.QLabel(self.centralwidget)
        self.label_imt.setGeometry(QtCore.QRect(140, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_imt.setFont(font)
        self.label_imt.setObjectName("label_imt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_imt.setAlignment(QtCore.Qt.AlignCenter)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        def calc_imt():
            try:
                num_weight, num_height = float(self.lineEdit_weight.text()), float(self.lineEdit_height.text()[0] + "." + self.lineEdit_height.text()[1:])
                imt = round(num_weight / (num_height * num_height), 1)
                self.label_imt.setText(f"ИМТ = {imt}")
                if float(imt) < 16:
                    self.label_info.setText("Выраженный дефицит массы тела")
                elif 16 < float(imt) < 18.5:
                    self.label_info.setText("Недостаточная масса тела")
                elif 18.6 < float(imt) < 24.9:
                    self.label_info.setText("Норма")
                elif 25 < float(imt) < 30:
                    self.label_info.setText("Избыточная масса тела")
                elif 30.1 < float(imt) < 35:
                    self.label_info.setText("Ожирение первой степени")
                elif 35.1 < float(imt) < 40:
                    self.label_info.setText("Ожирение второй степени")
                elif float(imt) > 40.1:
                    self.label_info.setText("Ожирение третьей степени")
                else:
                    self.label_info.setText("Что-то пошло не так")
            except:
                self.label_info.setText("Введены не правильные значения")
                self.label_imt.setText("ИМТ")

        self.pushButton.clicked.connect(calc_imt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор ИМТ"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label_weight.setText(_translate("MainWindow", "Вес"))
        self.label_height.setText(_translate("MainWindow", "Рост"))
        self.label_info.setText(_translate("MainWindow", "Информация о вашем весе"))
        self.label_imt.setText(_translate("MainWindow", "ИМТ"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
