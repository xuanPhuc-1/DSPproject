# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\VADWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf
import numpy as np
import os
from threading import Thread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import pyaudio
import wave


class MplCanvas(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackground('w')  # Set background color to white


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color:    rgb(218, 232, 252)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnInput.setGeometry(QtCore.QRect(40, 120, 111, 41))
        self.btnInput.setObjectName("btnInput")
        self.inputPath = QtWidgets.QTextEdit(self.centralwidget)
        self.inputPath.setGeometry(QtCore.QRect(190, 130, 281, 31))
        self.inputPath.setObjectName("inputPath")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 140, 31, 16))
        self.label.setObjectName("label")
        self.outputPath = QtWidgets.QTextEdit(self.centralwidget)
        self.outputPath.setGeometry(QtCore.QRect(190, 180, 281, 31))
        self.outputPath.setObjectName("outputPath")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 190, 31, 16))
        self.label_2.setObjectName("label_2")
        self.btnOutput = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutput.setGeometry(QtCore.QRect(40, 170, 111, 41))
        self.btnOutput.setObjectName("btnOutput")
        self.sample_window_slider = QtWidgets.QSlider(self.centralwidget)
        self.sample_window_slider.setGeometry(QtCore.QRect(220, 370, 160, 22))
        self.sample_window_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sample_window_slider.setObjectName("sample_window_slider")
        self.sample_overlap_slider = QtWidgets.QSlider(self.centralwidget)
        self.sample_overlap_slider.setGeometry(QtCore.QRect(220, 430, 160, 22))
        self.sample_overlap_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sample_overlap_slider.setObjectName("sample_overlap_slider")
        self.window_size_slider = QtWidgets.QSlider(self.centralwidget)
        self.window_size_slider.setGeometry(QtCore.QRect(130, 590, 22, 160))
        self.window_size_slider.setOrientation(QtCore.Qt.Vertical)
        self.window_size_slider.setObjectName("window_size_slider")
        self.energy_threshold_slider = QtWidgets.QSlider(self.centralwidget)
        self.energy_threshold_slider.setGeometry(
            QtCore.QRect(270, 590, 22, 160))
        self.energy_threshold_slider.setOrientation(QtCore.Qt.Vertical)
        self.energy_threshold_slider.setObjectName("energy_threshold_slider")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(510, 130, 91, 31))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(510, 180, 91, 31))
        self.btnStop.setObjectName("btnStop")
        self.btnPlay = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(300, 220, 91, 31))
        self.btnPlay.setObjectName("btnPlay")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(300, 260, 91, 31))
        self.btnSave.setObjectName("btnSave")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 370, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 430, 81, 20))
        self.label_6.setObjectName("label_6")
        self.sample_widow_value = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value.setGeometry(QtCore.QRect(390, 370, 121, 16))
        self.sample_widow_value.setObjectName("sample_widow_value")
        self.sample_overlap_value = QtWidgets.QLabel(self.centralwidget)
        self.sample_overlap_value.setGeometry(QtCore.QRect(390, 430, 111, 20))
        self.sample_overlap_value.setObjectName("sample_overlap_value")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 760, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 760, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(500, 760, 121, 16))
        self.label_9.setObjectName("label_9")
        self.stop_band_slider = QtWidgets.QSlider(self.centralwidget)
        self.stop_band_slider.setGeometry(QtCore.QRect(530, 590, 22, 160))
        self.stop_band_slider.setOrientation(QtCore.Qt.Vertical)
        self.stop_band_slider.setObjectName("stop_band_slider")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 760, 101, 16))
        self.label_10.setObjectName("label_10")
        self.start_band_slider = QtWidgets.QSlider(self.centralwidget)
        self.start_band_slider.setGeometry(QtCore.QRect(410, 590, 22, 160))
        self.start_band_slider.setOrientation(QtCore.Qt.Vertical)
        self.start_band_slider.setObjectName("start_band_slider")
        self.sample_widow_value_2 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_2.setGeometry(QtCore.QRect(100, 570, 121, 16))
        self.sample_widow_value_2.setObjectName("sample_widow_value_2")
        self.sample_widow_value_3 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_3.setGeometry(QtCore.QRect(230, 570, 121, 16))
        self.sample_widow_value_3.setObjectName("sample_widow_value_3")
        self.sample_widow_value_4 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_4.setGeometry(QtCore.QRect(390, 570, 61, 16))
        self.sample_widow_value_4.setObjectName("sample_widow_value_4")
        self.sample_widow_value_5 = QtWidgets.QLabel(self.centralwidget)
        self.sample_widow_value_5.setGeometry(QtCore.QRect(510, 570, 61, 16))
        self.sample_widow_value_5.setObjectName("sample_widow_value_5")
        self.pg1 = pg.PlotWidget(self.centralwidget)
        self.pg1.setGeometry(QtCore.QRect(610, 0, 1301, 311))
        self.pg1.setStyleSheet("")
        self.pg1.setObjectName("pg1")
        self.pg2 = pg.PlotWidget(self.centralwidget)
        self.pg2.setGeometry(QtCore.QRect(610, 320, 1301, 311))
        self.pg2.setStyleSheet("")
        self.pg2.setObjectName("pg2")
        self.pg3 = pg.PlotWidget(self.centralwidget)
        self.pg3.setGeometry(QtCore.QRect(610, 640, 1301, 331))
        self.pg3.setStyleSheet("")
        self.pg3.setObjectName("pg3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(110, 860, 451, 120))
        self.listView.setObjectName("listView")
        # add text to list view
        self.model = QtGui.QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.model.appendRow(QtGui.QStandardItem(
            "Change the parameters to see the effect on the plot"))
        self.model.appendRow(QtGui.QStandardItem(
            "The default parameters are:"))
        self.model.appendRow(QtGui.QStandardItem("Sample window: 20 ms"))
        self.model.appendRow(QtGui.QStandardItem("Sample overlap: 10 ms"))
        self.model.appendRow(QtGui.QStandardItem("Speech window size: 500 ms"))
        self.model.appendRow(QtGui.QStandardItem(
            "Speech energy threshold: 0.2"))
        self.model.appendRow(QtGui.QStandardItem("Speech start band: 300"))
        self.model.appendRow(QtGui.QStandardItem("Speech end band: 3000"))
        self.lbFFT_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_3.setGeometry(QtCore.QRect(190, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_3.setFont(font)
        self.lbFFT_3.setStyleSheet("")
        self.lbFFT_3.setObjectName("lbFFT_3")
        self.lbFFT_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_4.setGeometry(QtCore.QRect(230, 320, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_4.setFont(font)
        self.lbFFT_4.setStyleSheet("")
        self.lbFFT_4.setObjectName("lbFFT_4")
        self.lbFFT_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_5.setGeometry(QtCore.QRect(200, 500, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_5.setFont(font)
        self.lbFFT_5.setStyleSheet("")
        self.lbFFT_5.setObjectName("lbFFT_5")
        self.lbFFT_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbFFT_6.setGeometry(QtCore.QRect(290, 820, 110, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbFFT_6.setFont(font)
        self.lbFFT_6.setStyleSheet("")
        self.lbFFT_6.setObjectName("lbFFT_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.vad = VoiceActivityDetector(self)
        self.setup_connection()

    def setup_connection(self):
        self.btnInput.clicked.connect(self.vad.on_click_input)
        self.btnOutput.clicked.connect(self.vad.on_click_output)
        self.btnStart.clicked.connect(self.vad.on_click_start)
        self.btnStop.clicked.connect(self.vad.on_click_stop)
        self.btnSave.clicked.connect(self.vad.on_click_save)
        self.btnPlay.clicked.connect(self.vad.on_click_play)
        # SET UP SLIDER WITH MIN VALUE IS 0.01 AND MAX VALUE IS 0.5
        self.sample_window_slider.setMinimum(1)
        self.sample_window_slider.setMaximum(50)
        # CONNECT SLIDER WITH FUNCTION
        self.sample_window_slider.valueChanged.connect(
            self.vad.update_sample_window)

        # SET UP SLIDER WITH MIN VALUE IS 0.01 AND MAX VALUE IS 0.5
        self.sample_overlap_slider.setMinimum(1)
        self.sample_overlap_slider.setMaximum(50)
        # CONNECT SLIDER WITH FUNCTION
        self.sample_overlap_slider.valueChanged.connect(
            self.vad.update_sample_overlap)

        self.window_size_slider.setMinimum(1)
        self.window_size_slider.setMaximum(100)
        self.window_size_slider.valueChanged.connect(
            self.vad.update_speech_window)

        self.energy_threshold_slider.setMinimum(1)
        self.energy_threshold_slider.setMaximum(400)
        self.energy_threshold_slider.valueChanged.connect(
            self.vad.update_speech_energy_threshold)

        self.start_band_slider.setMinimum(1)
        self.start_band_slider.setMaximum(10000)
        self.start_band_slider.valueChanged.connect(
            self.vad.update_speech_start_band)

        self.stop_band_slider.setMinimum(1)
        self.stop_band_slider.setMaximum(10000)
        self.stop_band_slider.valueChanged.connect(
            self.vad.update_speech_end_band)

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
        self.lbFFT_3.setText(_translate(
            "MainWindow", "Voice Activity Detector (VAD)"))
        self.lbFFT_4.setText(_translate("MainWindow", "Window parameters"))
        self.lbFFT_5.setText(_translate(
            "MainWindow", "Signal Analysis Parameters"))
        self.lbFFT_6.setText(_translate("MainWindow", "Description"))


class VoiceActivityDetector:
    def __init__(self, ui, wave_input_filename=None):

        self.ui = ui
        self.data = None
        self.rate = 0
        self.sample_window = 0.02  # 20 ms
        self.sample_overlap = 0.01  # 10ms
        self.speech_window = 0.5  # half a second
        self.speech_energy_threshold = 0.2  # 50% of energy in voice band
        self.speech_start_band = 300
        self.speech_end_band = 3000
        self.speech_label = []
        self.raw_detection = []

    def on_click_input(self):
        # Sử dụng self.ui để truy cập thành phần của Ui_MainWindow
        file_dialog = QtWidgets.QFileDialog()
        wave_input_filename, _ = file_dialog.getOpenFileName()
        if wave_input_filename:
            self.ui.inputPath.setPlainText(wave_input_filename)
            # self._read_wav(wave_input_filename)._convert_to_mono()
            # Thực hiện các thao tác khác cần thiết khi chọn tệp âm thanh

    def on_click_output(self):
        # Sử dụng self.ui để truy cập thành phần của Ui_MainWindow
        file_dialog = QtWidgets.QFileDialog()
        wave_output_filename, _ = file_dialog.getOpenFileName()
        if wave_output_filename:
            self.ui.outputPath.setPlainText(wave_output_filename)
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

    def update_sample_overlap(self):
        self.vad.sample_overlap = self.ui.sample_overlap_slider.value() / 1000
        print(self.vad.sample_overlap)
        self.update_plot_and_params()

    def update_speech_window(self):
        self.vad.speech_window = self.ui.window_size_slider.value() / 1000
        print(self.vad.speech_window)
        self.update_plot_and_params()

    def update_speech_energy_threshold(self):
        self.vad.speech_energy_threshold = self.ui.energy_threshold_slider.value() / \
            1000
        print(self.vad.speech_energy_threshold)
        self.update_plot_and_params()

    def update_speech_start_band(self):
        self.vad.speech_start_band = self.ui.start_band_slider.value() / 1000
        print(self.vad.speech_start_band)
        self.update_plot_and_params()

    def update_speech_end_band(self):
        self.vad.speech_end_band = self.ui.stop_band_slider.value() / 1000
        print(self.vad.speech_end_band)
        self.update_plot_and_params()

    def update_plot_and_params(self):
        self.vad.update_plot()
        self.vad.update_parameters_value_for_slider()
        self.vad.plot_detected_speech_regions()
        self.raw_detection = self.vad.detect_speech()
        self.speech_labels = self.vad.convert_windows_to_readible_labels(
            self.raw_detection)
        self.vad.plot_readible_labels(self.speech_labels)

    def update_plot(self):
        # use matplotlib to plot with interact mode to get change in real time
        self.plot_detected_speech_regions()

    def on_click_save(self):
        # save only speech file
        # open file dialog to select output file
        # get the text from output path
        outputfile = self.ui.outputPath.toPlainText()
        # print(outputfile)
        self.save_only_speech_file(outputfile)

    def on_click_play(self):
        self.plot_the_output_file()
        # get file path from output path
        file_path = self.ui.outputPath.toPlainText()
        # Mở file WAV
        wave_file = wave.open(file_path, 'rb')

        # Tạo một đối tượng PyAudio
        p = pyaudio.PyAudio()

        # Cài đặt thông số cho stream
        stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                        channels=wave_file.getnchannels(),
                        rate=wave_file.getframerate(),
                        output=True)

        # Đọc dữ liệu từ file WAV và gửi đến stream
        data = wave_file.readframes(1024)
        while data:
            stream.write(data)
            data = wave_file.readframes(1024)

        # Đóng stream và đối tượng PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Đóng file WAV
        wave_file.close()

    def on_click_start(self):
        wave_input_filename = self.ui.inputPath.toPlainText()
        self.vad = VoiceActivityDetector(self.ui, wave_input_filename)
        # start processing
        self.vad._read_wav(wave_input_filename)._convert_to_mono()
        self.raw_detection = self.vad.detect_speech()
        self.speech_labels = self.vad.convert_windows_to_readible_labels(
            self.raw_detection)

        self.vad.plot_detected_speech_regions()
        self.vad.plot_readible_labels(self.speech_labels)

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

        self.ui.pg1.clear()

        # Plot the original signal
        self.ui.pg1.plot(data, pen='b', name='Speech signal')

        # Plot the speech regions
        self.ui.pg1.plot(data_speech, pen='r', name='Speech regions')

        # Add a legend
        self.ui.pg1.addLegend()

        # Set axis labels
        self.ui.pg1.setLabel('left', 'Amplitude')
        self.ui.pg1.setLabel('bottom', 'Time (seconds)')

    def plot_readible_labels(self, speech_labels):
        # use pg to plot the speech labels
        data = self.data
        self.ui.pg2.clear()

        # Plot the original signal
        self.ui.pg2.plot(data, pen='b', name='Speech signal')

        # Create a list to store the speech regions
        speech_regions = []

        # Plot the speech regions
        for label in speech_labels:
            start = int(label['speech_begin'] * self.rate)
            end = int(label['speech_end'] * self.rate)
            region = pg.LinearRegionItem(
                values=[start, end], brush=(255, 0, 0, 50))
            speech_regions.append(region)
            self.ui.pg2.addItem(region)

        # Add a legend (Note: PyqtGraph doesn't have a built-in legend, so you may need to implement it separately)

        # Set axis labels
        self.ui.pg2.setLabel('left', 'Amplitude')
        self.ui.pg2.setLabel('bottom', 'Time (seconds)')

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

    def save_only_speech_file(self, input_file, output_file):
        # Mở file WAV gốc để đọc dữ liệu
        with wave.open(input_file, 'rb') as input_wf:
            # Tạo một đối tượng mới để ghi dữ liệu vào file đầu ra
            with wave.open(output_file, 'wb') as output_wf:
                # Cài đặt các thông số của file đầu ra dựa trên file gốc
                output_wf.setnchannels(input_wf.getnchannels())
                output_wf.setsampwidth(input_wf.getsampwidth())
                output_wf.setframerate(input_wf.getframerate())
                # Đặt số frame ban đầu là 0, sẽ cập nhật sau
                output_wf.setnframes(0)

                for label in self.speech_labels:
                    start_frame = int(
                        label['speech_begin'] * input_wf.getframerate())
                    end_frame = int(label['speech_end']
                                    * input_wf.getframerate())

                    # Đọc dữ liệu từ file gốc
                    input_wf.setpos(start_frame)
                    frames = input_wf.readframes(end_frame - start_frame)

                    # Ghi dữ liệu vào file đầu ra
                    output_wf.writeframes(frames)

    def plot_the_output_file(self):
        # plot the output file
        # get the output file path
        outputfile = self.ui.outputPath.toPlainText()
        # use pg3 to plot the output file
        self.ui.pg3.clear()
        # Mở file WAV để đọc dữ liệu
        wf = wave.open(outputfile, 'rb')

        # Đọc dữ liệu âm thanh
        frames = wf.readframes(wf.getnframes())
        wf.close()

        # Chuyển đổi dữ liệu thành mảng numpy
        data = np.frombuffer(frames, dtype=np.int16)

        self.ui.pg3.plot(data, pen='b', name='Speech signal output')
        # Set axis labels
        self.ui.pg3.setLabel('left', 'Amplitude')
        self.ui.pg3.setLabel('bottom', 'Time (seconds)')
        # Add a legend
        self.ui.pg3.addLegend()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
