from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import numpy as np
import pywt
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pyqtgraph as pg

wavelet_description = """
        A wavelet is a mathematical function that is characterized by its ability to oscillate and decay rapidly.
        Unlike traditional Fourier analysis, which uses sine and cosine functions to represent signals, wavelet analysis
        allows for the examination of localized features within a signal. This localization in both time and frequency
        domains makes wavelets particularly useful for analyzing signals with non-stationary or time-varying
        characteristics.

        The term "wavelet" is derived from "wave" and "let," emphasizing its nature as a small wave. Wavelets come in
        various shapes and sizes, each suited for specific types of signal analysis. They are often used in applications
        such as signal processing, image compression, and data compression.

        Wavelet analysis involves decomposing a signal into different frequency components represented by wavelets at
        various scales. This decomposition results in a detailed representation of the signal's behavior at different time
        intervals. The decomposition process can be performed using a technique called wavelet transform.

        One key advantage of wavelet analysis is its ability to provide both low-frequency and high-frequency
        information simultaneously. This enables the identification and extraction of relevant features within a signal,
        making wavelets valuable in applications such as denoising, compression, and feature detection.

        Wavelet analysis has found wide applications in diverse fields, including signal processing, image analysis,
        medical imaging, and pattern recognition. Its adaptability to capture localized information and its ability to
        handle signals with dynamic characteristics contribute to its popularity in various scientific and engineering
        disciplines.
        """


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color:    rgb(218, 232, 252)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(pywt.wavelist())
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.plot_graph)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(340, 20, 1051, 681))
        self.graphicsView.setObjectName("graphicsView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 180, 321, 521))
        self.textBrowser.setObjectName("textBrowser")
        # set text for textBrowser
        self.textBrowser.setText(wavelet_description)
        self.lbFFT_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_3.setGeometry(QtCore.QRect(130, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_3.setFont(font)
        self.lbFFT_3.setStyleSheet("")
        self.lbFFT_3.setObjectName("lbFFT_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wavelet Window"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.lbFFT_3.setText(_translate("MainWindow", "Wavelet "))

    def plot_graph(self):
        wavelet = self.comboBox.currentText()

        # Create a simple signal with two frequencies
        dt = 0.001
        t = np.arange(0, 1, dt)
        signal = np.sin(2 * np.pi * 50 * t) + \
            np.sin(2 * np.pi * 120 * t)  # Sum of 2
        signal_clean = signal

        signal = signal + 2.5 * np.random.randn(len(t))
        filtered = self.wavelet_denoising(signal, wavelet=wavelet, level=1)

        # Plot the graph using pyqtgraph
        self.graphicsView.clear()

        # Set different line widths
        self.graphicsView.plot(t, signal_clean, pen={
                               'color': 'r', 'width': 1}, name="Original Signal")
        self.graphicsView.plot(
            t, signal, pen={'color': 'b', 'width': 1}, name="Noisy Signal")
        self.graphicsView.plot(
            t, filtered, pen={'color': 'w', 'width': 2}, name="Denoised Signal")
        # Add legend
        self.graphicsView.addLegend()

    def wavelet_denoising(self, x, wavelet='db4', level=1):
        coeff = pywt.wavedec(x, wavelet, mode="per")
        sigma = (1/0.6745) * \
            np.mean(np.abs(coeff[-level] - np.mean(coeff[-level])))
        uthresh = sigma * np.sqrt(2 * np.log(len(x)))
        coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard')
                     for i in coeff[1:])
        return pywt.waverec(coeff, wavelet, mode='per')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
