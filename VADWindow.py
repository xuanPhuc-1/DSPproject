from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf
import numpy as np
import os
from threading import Thread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pyqtgraph import PlotWidget
import pyqtgraph as pg


class MplCanvas(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')  # Set background color to white


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btnInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnInput.setGeometry(QtCore.QRect(70, 70, 111, 41))
        self.btnInput.setObjectName("btnInput")
        self.inputPath = QtWidgets.QTextEdit(self.centralwidget)
        self.inputPath.setGeometry(QtCore.QRect(220, 80, 341, 31))
        self.inputPath.setObjectName("inputPath")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 90, 31, 16))
        self.label.setObjectName("label")
        self.outputPath = QtWidgets.QTextEdit(self.centralwidget)
        self.outputPath.setGeometry(QtCore.QRect(220, 130, 341, 31))
        self.outputPath.setObjectName("outputPath")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 140, 31, 16))
        self.label_2.setObjectName("label_2")
        self.btnOutput = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutput.setGeometry(QtCore.QRect(70, 120, 111, 41))
        self.btnOutput.setObjectName("btnOutput")
        self.sample_window_slider = QtWidgets.QSlider(self.centralwidget)
        self.sample_window_slider.setGeometry(QtCore.QRect(270, 300, 160, 22))
        self.sample_window_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sample_window_slider.setObjectName("sample_window_slider")
        self.sample_overlap_slider = QtWidgets.QSlider(self.centralwidget)
        self.sample_overlap_slider.setGeometry(QtCore.QRect(270, 360, 160, 22))
        self.sample_overlap_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sample_overlap_slider.setObjectName("sample_overlap_slider")
        self.window_size_slider = QtWidgets.QSlider(self.centralwidget)
        self.window_size_slider.setGeometry(QtCore.QRect(150, 470, 22, 160))
        self.window_size_slider.setOrientation(QtCore.Qt.Vertical)
        self.window_size_slider.setObjectName("window_size_slider")
        self.energy_threshold_slider = QtWidgets.QSlider(self.centralwidget)
        self.energy_threshold_slider.setGeometry(
            QtCore.QRect(290, 470, 22, 160))
        self.energy_threshold_slider.setOrientation(QtCore.Qt.Vertical)
        self.energy_threshold_slider.setObjectName("energy_threshold_slider")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(610, 80, 91, 31))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(610, 130, 91, 31))
        self.btnStop.setObjectName("btnStop")
        self.btnPlay = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(330, 170, 91, 31))
        self.btnPlay.setObjectName("btnPlay")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(330, 210, 91, 31))
        self.btnSave.setObjectName("btnSave")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 260, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 410, 181, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 300, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 360, 81, 20))
        self.label_6.setObjectName("label_6")
        self.sample_widow_value = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value.setGeometry(QtCore.QRect(440, 300, 121, 16))
        self.sample_widow_value.setObjectName("sample_widow_value")
        self.sample_overlap_value = QtWidgets.QLabel(self.centralwidget)
        self.sample_overlap_value.setGeometry(QtCore.QRect(440, 360, 111, 20))
        self.sample_overlap_value.setObjectName("sample_overlap_value")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 640, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 640, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(520, 640, 121, 16))
        self.label_9.setObjectName("label_9")
        self.stop_band_slider = QtWidgets.QSlider(self.centralwidget)
        self.stop_band_slider.setGeometry(QtCore.QRect(550, 470, 22, 160))
        self.stop_band_slider.setOrientation(QtCore.Qt.Vertical)
        self.stop_band_slider.setObjectName("stop_band_slider")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 640, 101, 16))
        self.label_10.setObjectName("label_10")
        self.start_band_slider = QtWidgets.QSlider(self.centralwidget)
        self.start_band_slider.setGeometry(QtCore.QRect(430, 470, 22, 160))
        self.start_band_slider.setOrientation(QtCore.Qt.Vertical)
        self.start_band_slider.setObjectName("start_band_slider")
        self.sample_widow_value_2 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_2.setGeometry(QtCore.QRect(120, 450, 121, 16))
        self.sample_widow_value_2.setObjectName("sample_widow_value_2")
        self.sample_widow_value_3 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_3.setGeometry(QtCore.QRect(250, 450, 121, 16))
        self.sample_widow_value_3.setObjectName("sample_widow_value_3")
        self.sample_widow_value_4 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_4.setGeometry(QtCore.QRect(410, 450, 61, 16))
        self.sample_widow_value_4.setObjectName("sample_widow_value_4")
        self.sample_widow_value_5 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_5.setGeometry(QtCore.QRect(530, 450, 61, 16))
        self.sample_widow_value_5.setObjectName("sample_widow_value_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Đặt tên tệp âm thanh khi cần
        self.vad = VoiceActivityDetector(self)
        self.setup_connection()
        # self.vad = VoiceActivityDetector(self.inputPath.toPlainText())

        # set up connection

    def setup_connection(self):
        self.btnInput.clicked.connect(self.vad.on_click_input)
        self.btnOutput.clicked.connect(self.vad.on_click_output)
        self.btnStart.clicked.connect(self.vad.on_click_start)
        self.btnStop.clicked.connect(self.vad.on_click_stop)
        # SET UP SLIDER WITH MIN VALUE IS 0.01 AND MAX VALUE IS 0.5
        self.sample_window_slider.setMinimum(1)
        self.sample_window_slider.setMaximum(50)
        # CONNECT SLIDER WITH FUNCTION
        self.sample_window_slider.valueChanged.connect(
            self.vad.update_sample_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnInput.setText(_translate("MainWindow", "Select Input Audio"))
        self.label.setText(_translate("MainWindow", "PATH"))
        self.label_2.setText(_translate("MainWindow", "PATH"))
        self.btnOutput.setText(_translate("MainWindow", "Select Output Audio"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.btnPlay.setText(_translate("MainWindow", "Play"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Window Parameters"))
        self.label_4.setText(_translate(
            "MainWindow", "Signal Analysis Parameters"))
        self.label_5.setText(_translate("MainWindow", "Sample window"))
        self.label_6.setText(_translate("MainWindow", "Sample overlap"))
        self.sample_widow_value.setText(
            _translate("MainWindow", "sample_window_value"))
        self.sample_overlap_value.setText(
            _translate("MainWindow", "sample_overlap_value"))
        self.label_7.setText(_translate("MainWindow", "Speech Window Size"))
        self.label_8.setText(_translate(
            "MainWindow", "Speech Energy Threshold"))
        self.label_9.setText(_translate("MainWindow", "Speech Stop Band"))
        self.label_10.setText(_translate("MainWindow", "Speech Start Band"))
        self.sample_widow_value_2.setText(
            _translate("MainWindow", "window_size_value"))
        self.sample_widow_value_3.setText(
            _translate("MainWindow", "energy_threshold_value"))
        self.sample_widow_value_4.setText(
            _translate("MainWindow", "start_band"))
        self.sample_widow_value_5.setText(
            _translate("MainWindow", "stop_band"))


class VoiceActivityDetector:
    def __init__(self, ui, wave_input_filename=None):

        self.ui = ui
        self.data = None
        self.rate = 0
        self.sample_window = 0.02
        self.sample_overlap = 0.01
        self.speech_window = 0.5
        self.speech_energy_threshold = 0.2
        self.speech_start_band = 300
        self.speech_end_band = 3000

    def on_click_input(self):
        # Sử dụng self.ui để truy cập thành phần của Ui_MainWindow
        file_dialog = QtWidgets.QFileDialog()
        wave_input_filename, _ = file_dialog.getOpenFileName()
        if wave_input_filename:
            self.ui.inputPath.setPlainText(wave_input_filename)
            # self._read_wav(wave_input_filename)._convert_to_mono()
            # Thực hiện các thao tác khác cần thiết khi chọn tệp âm thanh

    def update_parameters_value_for_slider(self):

        # update value on label
        self.ui.sample_widow_value.setText(str(self.sample_window))
        self.ui.sample_overlap_value.setText(str(self.sample_overlap))
        self.ui.sample_widow_value_2.setText(str(self.speech_window))
        self.ui.sample_widow_value_3.setText(str(self.speech_energy_threshold))
        self.ui.sample_widow_value_4.setText(str(self.speech_start_band))
        self.ui.sample_widow_value_5.setText(str(self.speech_end_band))

    def update_sample_window(self):
        self.vad.sample_window = self.ui.sample_window_slider.value() / 1000
        print(self.vad.sample_window)
        self.update_plot_and_params()

    def update_plot_and_params(self):
        self.vad.update_plot()
        self.vad.update_parameters_value_for_slider()

    def update_plot(self):
        # use matplotlib to plot with interact mode to get change in real time
        self.plot_detected_speech_regions()
        # self.vad.plot_only_speech_file()

    def on_click_output(self):
        # open file dialog to select output file
        self.outputPath.setText(QtWidgets.QFileDialog.getOpenFileName())

    def on_click_start(self):
        wave_input_filename = self.ui.inputPath.toPlainText()
        self.vad = VoiceActivityDetector(self.ui, wave_input_filename)
        # start processing
        self.vad._read_wav(wave_input_filename)._convert_to_mono()
        raw_detection = self.vad.detect_speech()
        speech_labels = self.vad.convert_windows_to_readible_labels(
            raw_detection)

        self.vad.plot_detected_speech_regions()

        self.update_parameters_value_for_slider()

    def on_click_stop(self):
        # stop processing
        pass

    def _read_wav(self, wave_file):
        if not os.path.isfile(wave_file):
            print(f"Error: File '{wave_file}' does not exist.")
            return self
        self.rate, self.data = wf.read(wave_file)
        print(self.rate, self.data)
        self.channels = len(self.data.shape)
        self.filename = wave_file
        return self
        # ...

    def _convert_to_mono(self):
        if self.channels == 2:
            self.data = np.mean(self.data, axis=1, dtype=self.data.dtype)
            self.channels = 1
        return self

    def _calculate_frequencies(self, audio_data):
        data_freq = np.fft.fftfreq(len(audio_data), 1.0/self.rate)
        data_freq = data_freq[1:]
        return data_freq

    def _calculate_amplitude(self, audio_data):
        data_ampl = np.abs(np.fft.fft(audio_data))
        data_ampl = data_ampl[1:]
        return data_ampl

    def _calculate_energy(self, data):
        data_amplitude = self._calculate_amplitude(data)
        data_energy = data_amplitude ** 2
        return data_energy

    def _znormalize_energy(self, data_energy):
        energy_mean = np.mean(data_energy)
        energy_std = np.std(data_energy)
        energy_znorm = (data_energy - energy_mean) / energy_std
        return energy_znorm

    def _connect_energy_with_frequencies(self, data_freq, data_energy):
        energy_freq = {}
        for (i, freq) in enumerate(data_freq):
            if abs(freq) not in energy_freq:
                energy_freq[abs(freq)] = data_energy[i] * 2
        return energy_freq

    def _calculate_normalized_energy(self, data):
        data_freq = self._calculate_frequencies(data)
        data_energy = self._calculate_energy(data)
        # data_energy = self._znormalize_energy(data_energy) #znorm brings worse results
        energy_freq = self._connect_energy_with_frequencies(
            data_freq, data_energy)
        return energy_freq

    def _sum_energy_in_band(self, energy_frequencies, start_band, end_band):
        sum_energy = 0
        for f in energy_frequencies.keys():
            if start_band < f < end_band:
                sum_energy += energy_frequencies[f]
        return sum_energy

    def _median_filter(self, x, k):
        assert k % 2 == 1, "Median filter length must be odd."
        assert x.ndim == 1, "Input must be one-dimensional."
        k2 = (k - 1) // 2
        y = np.zeros((len(x), k), dtype=x.dtype)
        y[:, k2] = x
        for i in range(k2):
            j = k2 - i
            y[j:, i] = x[:-j]
            y[:j, i] = x[0]
            y[:-j, -(i+1)] = x[j:]
            y[-j:, -(i+1)] = x[-1]
        return np.median(y, axis=1)

    def _smooth_speech_detection(self, detected_windows):  # cửa sổ
        median_window = int(self.speech_window/self.sample_window)
        if median_window % 2 == 0:
            median_window = median_window-1  # nếu là số chẵn thì trừ đi 1
        median_energy = self._median_filter(
            detected_windows[:, 1], median_window)
        return median_energy

    def convert_windows_to_readible_labels(self, detected_windows):
        """ Takes as input array of window numbers and speech flags from speech
        detection and convert speech flags to time intervals of speech.
        Output is array of dictionaries with speech intervals.
        """
        speech_time = []
        is_speech = 0
        for window in detected_windows:
            if (window[1] == 1.0 and is_speech == 0):  # nếu là speech và chưa có speech nào
                is_speech = 1
                speech_label = {}
                speech_time_start = window[0] / self.rate  # chuyển về giây
                # lưu thời gian bắt đầu
                speech_label['speech_begin'] = speech_time_start
                print(window[0], speech_time_start)  # in ra thời gian bắt đầu
                # speech_time.append(speech_label)
            # nếu là non-speech và có speech trước đó
            if (window[1] == 0.0 and is_speech == 1):
                is_speech = 0  # đánh dấu là đã có speech
                speech_time_end = window[0] / self.rate  # chuyển về giây
                # lưu thời gian kết thúc
                speech_label['speech_end'] = speech_time_end
                speech_time.append(speech_label)  # lưu vào mảng
                print(window[0], speech_time_end)
        return speech_time

    def plot_detected_speech_regions(self):
        data = self.data
        detected_windows = self.detect_speech()
        data_speech = np.zeros(len(data))

        for start, is_speech in detected_windows:
            data_speech[int(start):int(start + len(data_speech) * self.sample_window)] = data[int(
                start):int(start + len(data_speech) * self.sample_window)] * is_speech

        self.ui.graphicsView.clear()

        # Plot the original signal
        self.ui.graphicsView.plot(data, pen='b', name='Speech signal')

        # Plot the speech regions
        self.ui.graphicsView.plot(data_speech, pen='r', name='Speech regions')

        # Add a legend
        self.ui.graphicsView.addLegend()

        # Set axis labels
        self.ui.graphicsView.setLabel('left', 'Amplitude')
        self.ui.graphicsView.setLabel('bottom', 'Time (seconds)')

    def handle_close(self, evt):
        QtGui.QApplication.quit()

    def detect_speech(self):
        """ Detects speech regions based on ratio between speech band energy
        and total energy.
        Output is array of window numbers and speech flags (1 - speech, 0 - nonspeech).
        """
        detected_windows = np.array([])
        sample_window = int(self.rate * self.sample_window)
        sample_overlap = int(self.rate * self.sample_overlap)
        data = self.data
        sample_start = 0
        start_band = self.speech_start_band
        end_band = self.speech_end_band
        while (sample_start < (len(data) - sample_window)):
            sample_end = sample_start + sample_window
            if sample_end >= len(data):
                sample_end = len(data)-1
            data_window = data[sample_start:sample_end]
            energy_freq = self._calculate_normalized_energy(data_window)
            sum_voice_energy = self._sum_energy_in_band(
                energy_freq, start_band, end_band)
            sum_full_energy = sum(energy_freq.values())
            speech_ratio = sum_voice_energy/sum_full_energy
            # Hipothesis is that when there is a speech sequence we have ratio of energies more than Threshold
            speech_ratio = speech_ratio > self.speech_energy_threshold
            detected_windows = np.append(
                detected_windows, [sample_start, speech_ratio])
            sample_start += sample_overlap
        detected_windows = detected_windows.reshape(
            int(len(detected_windows)/2), 2)
        detected_windows[:, 1] = self._smooth_speech_detection(
            detected_windows)
        return detected_windows

    def save_only_speech_file(self, outputfile, speech_labels):
        # crop the file at speech labels and save to a output file
        data = self.data
        for label in speech_labels:
            start = int(label['speech_begin'] * self.rate)
            end = int(label['speech_end'] * self.rate)
            wf.write(outputfile, self.rate, data[start:end])
        return self

    def plot_only_speech_file(self, outputfile, speech_labels):
        # crop the file at speech labels and save to a output file
        data = self.data
        for label in speech_labels:
            start = int(label['speech_begin'] * self.rate)
            end = int(label['speech_end'] * self.rate)
            plt.plot(data[start:end])
        plt.show()
        return self


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
