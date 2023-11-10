import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(y, Fs):
    """
    Plots a Single-Sided Amplitude Spectrum of y(t).

    Parameters:
    - y: The input signal
    - Fs: Sampling frequency (number of samples per second)
    """
    n = len(y)  # Length of the signal
    k = np.arange(n)
    T = n / Fs
    frq = k / T  # Two-sided frequency range
    frq = frq[:int(n / 2)]  # One-sided frequency range

    Y = np.fft.fft(y) / n  # FFT computation and normalization
    Y = Y[:int(n / 2)]

    plt.plot(frq, abs(Y), 'r')  # Plotting the spectrum
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('|Y(freq)|')

if __name__ == "__main__":
    # Example usage
    sample_count = 8192
    Fs = 1000  # Sampling frequency
    t = np.arange(0, 1, 1 / Fs)
    input_signal = np.sin(2 * np.pi * 100 * t) + np.sin(2 * np.pi * 200 * t)
    
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, input_signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    
    plt.subplot(2, 1, 2)
    plot_spectrum(input_signal, Fs)
    
    plt.show()
