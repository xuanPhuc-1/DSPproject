import sys
import numpy as np
import pywt
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class WaveletDenoisingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wavelet Denoising App")
        self.setGeometry(100, 100, 1920, 1080)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        self.central_widget.setStyleSheet(
            "background-color: rgb(218, 232, 252);")
        # Dropdown list for selecting wavelet
        self.wavelet_label = QLabel("Select Wavelet:")
        self.wavelet_combobox = QComboBox()
        self.wavelet_combobox.addItems(pywt.wavelist())

        # Start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.plot_graph)

        # Matplotlib Figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Amplitude')

        # TextEdit for wavelet description
        self.wavelet_description_label = QLabel("Wavelet Description:")
        self.wavelet_description_textedit = QTextEdit()
        self.wavelet_description_textedit.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.wavelet_label)
        layout.addWidget(self.wavelet_combobox)
        layout.addWidget(self.start_button)
        layout.addWidget(self.canvas)
        layout.addWidget(self.wavelet_description_label)
        layout.addWidget(self.wavelet_description_textedit)
        self.central_widget.setLayout(layout)

        # Initial wavelet description
        self.update_wavelet_description()

    def update_wavelet_description(self):
        selected_wavelet = self.wavelet_combobox.currentText()

        # Get wavelet description
        try:
            wavelet = pywt.Wavelet(selected_wavelet)
            description = f"Advantages: {wavelet.__dir__}\n\n"
        except ValueError:
            description = "No information available for this wavelet."

        # Update the TextEdit
        self.wavelet_description_textedit.setPlainText(description)

    def plot_graph(self):
        wavelet = self.wavelet_combobox.currentText()

        # Create a simple signal with two frequencies
        dt = 0.001
        t = np.arange(0, 1, dt)
        signal = np.sin(2 * np.pi * 50 * t) + \
            np.sin(2 * np.pi * 120 * t)  # Sum of 2
        signal_clean = signal

        signal = signal + 2.5 * np.random.randn(len(t))
        filtered = self.wavelet_denoising(signal, wavelet=wavelet, level=1)

        # Plot the graph
        self.ax.clear()
        self.ax.plot(signal, label='Raw')
        self.ax.plot(filtered, label='Filtered')
        self.ax.legend()
        self.ax.set_title(f"DWT Denoising with {wavelet} Wavelet", size=15)

        # Draw the canvas
        self.canvas.draw()

        # Update wavelet description
        self.update_wavelet_description()

    def wavelet_denoising(self, x, wavelet='db4', level=1):
        coeff = pywt.wavedec(x, wavelet, mode="per")
        sigma = (1/0.6745) * \
            np.mean(np.abs(coeff[-level] - np.mean(coeff[-level])))
        uthresh = sigma * np.sqrt(2 * np.log(len(x)))
        coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard')
                     for i in coeff[1:])
        return pywt.waverec(coeff, wavelet, mode='per')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WaveletDenoisingApp()
    window.show()
    sys.exit(app.exec_())
