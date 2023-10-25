import numpy as np
import pywt
import matplotlib.pyplot as plt
def madev(d, axis=None):
    """ Mean absolute deviation of a signal """
    return np.mean(np.absolute(d - np.mean(d, axis)), axis)
def wavelet_denoising(x, wavelet='db4', level=1):
    coeff = pywt.wavedec(x, wavelet, mode="per")
    sigma = (1/0.6745) * madev(coeff[-level])
    uthresh = sigma * np.sqrt(2 * np.log(len(x)))
    coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard') for i in coeff[1:])
    return pywt.waverec(coeff, wavelet, mode='per')

for wav in pywt.wavelist():
    try:
        # Create a simple signal with two frequencies
        dt = 0.001
        t = np.arange(0, 1, dt)
        signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)  # Sum of 2
        signal_clean = signal

        signal = signal + 2.5 * np.random.randn(len(t))
        filtered = wavelet_denoising(signal, wavelet=wav, level=1)
    except:
        pass
    
    plt.figure(figsize=(10, 6))
    plt.plot(signal, label='Raw')
    plt.plot(filtered, label='Filtered')
    plt.legend()
    plt.title(f"DWT Denoising with {wav} Wavelet", size=15)
    plt.show()
    
#pick the best wavelet for denoising