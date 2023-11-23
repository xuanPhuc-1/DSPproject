from pylab import plot, show, xlabel, ylabel, subplot
from scipy import fft
import plotSpectrum
import numpy
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

sampleCount = 8192          # Sampling Frequency
R = 1000                    # R Ohm
C = 100e-9                  # C Farad
Ts = 1.0 / sampleCount      # sampling interval
freq1 = 1000                # freq Hz input signal
freq2 = 2000                # freq Hz input signal
freq3 = 3000                # freq Hz input signal

inputSignal = [0] * sampleCount
outputSignal = [0] * sampleCount

t = numpy.arange(0, 1, Ts)


class LowPassFilter(object):
    def __init__(self, x, R, C, period):
        self.__R = R
        self.__C = C
        self.__T = period
        self.__x = x
        self.__y = [0] * len(x)

        self.__K1 = (self.__T / (self.__T + 2 * self.__R * self.__C))
        self.__K2 = (self.__T / (self.__T + 2 * self.__R * self.__C))
        self.__K3 = ((self.__T - 2 * self.__R * self.__C) /
                     (self.__T + 2 * self.__R * self.__C))

    def FilterApply(self):
        for i in range(len(self.__x)):
            self.__y[i] = (self.__x[i] * self.__K1) + (self.__x[i - 1]
                                                       * self.__K2) - (self.__y[i - 1] * self.__K3)
        return (self.__y)

    def GetFrequency(self):
        return (1 / (2 * numpy.pi * self.__R * self.__C))

    def GetWarping(self):
        return (2 / self.__T) * numpy.arctan(2 * numpy.pi * self.GetFrequency() * self.__T / 2) / (2 * numpy.pi)

    def plot_frequency_response(R, C, Ts, sampleCount):
        # Tính toán tần số cắt
        fc = 1 / (2 * np.pi * R * C)

        # Tạo bộ lọc
        num, den = signal.butter(1, fc / (1.0 / (2 * Ts)),
                                 btype='low', analog=False)

        # Tính toán đáp ứng tần số
        w, h = signal.freqz(num, den, worN=sampleCount)

        # Chuyển đổi tần số sang Hz
        freq = w * (1.0 / Ts) / (2 * np.pi)

        # Vẽ đáp ứng tần số
        plt.plot(freq, 20 * np.log10(abs(h)))
        plt.title('Frequency Response')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain (dB)')
        plt.grid(True)
        plt.show()


inputSignal = numpy.sin(2 * numpy.pi * freq1 * t) + numpy.sin(2 *
                                                              numpy.pi * freq2 * t) + numpy.sin(2 * numpy.pi * freq3 * t)

myFilter = LowPassFilter(inputSignal, R, C, Ts)

outputSignal = myFilter.FilterApply()

print("CutOff Frequency : " + str(myFilter.GetFrequency()))
print("Frequency Warping : " + str(myFilter.GetWarping()))

subplot(2, 1, 1)
plot(t, outputSignal)
xlabel('Time')
ylabel('Amplitude')
subplot(2, 1, 2)
# plot the spectrum
plotSpectrum.plot_spectrum(outputSignal, sampleCount)
show()

LowPassFilter.plot_frequency_response(R, C, Ts, sampleCount)
