import numpy as np
import scipy.signal
import librosa
import librosa.display
import matplotlib.pyplot as plt

def compute_snr(clean_signal, noisy_signal):
    """
    Tính toán SNR (Signal-to-Noise Ratio) giữa tín hiệu sạch và tín hiệu nhiễu.

    Parameters:
        clean_signal (np.ndarray): Tín hiệu sạch.
        noisy_signal (np.ndarray): Tín hiệu nhiễu.

    Returns:
        snr (float): Giá trị SNR tính bằng dB.
    """
    clean_power = np.mean(clean_signal ** 2)
    noise = clean_signal - noisy_signal
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(clean_power / noise_power)
    return snr

def compute_sdr(reference_signal, estimated_signal):
    """
    Tính toán SDR (Source-to-Distortion Ratio) giữa tín hiệu tham chiếu và tín hiệu ước tính.

    Parameters:
        reference_signal (np.ndarray): Tín hiệu tham chiếu (sạch).
        estimated_signal (np.ndarray): Tín hiệu ước tính (có nhiễu).

    Returns:
        sdr (float): Giá trị SDR tính bằng dB.
    """
    reference_energy = np.mean(reference_signal ** 2)
    distortion = reference_signal - estimated_signal
    distortion_energy = np.mean(distortion ** 2)
    sdr = 10 * np.log10(reference_energy / distortion_energy)
    return sdr

def plot_audio_and_spectrogram(audio, title):
    """
    Vẽ biểu đồ tín hiệu âm thanh và biểu đồ spectrogram của tín hiệu.

    Parameters:
        audio (np.ndarray): Tín hiệu âm thanh.
        title (str): Tiêu đề biểu đồ.
    """
    "Hiển thị cả 2 đồ thị của noisy và clean cùng 1 cửa sổ"
    fig, ax = plt.subplots(2, 1, figsize=(12, 6))
    fig.suptitle(title, fontsize=16)
    librosa.display.waveshow(audio, sr=16000, ax=ax[0])
    ax[0].set_title("Audio Signal")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)
    
    spectrogram = librosa.stft(audio)
    spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))
    librosa.display.specshow(spectrogram_db, sr=16000, ax=ax[1], x_axis='time', y_axis='hz')
    ax[1].set_title("Spectrogram")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Frequency")
    ax[1].grid(True)
    plt.show()
    
# Đọc tệp âm thanh đã qua xử lý và âm thanh có nhiễu
clean_audio, _ = librosa.load('test1.wav', sr=None)
noisy_audio, _ = librosa.load('test1.wav', sr=None)

# Đo SNR và SDR
snr_value = compute_snr(clean_audio, noisy_audio)
sdr_value = compute_sdr(clean_audio, noisy_audio)

# In giá trị SNR và SDR
print(f'SNR: {snr_value} dB')
print(f'SDR: {sdr_value} dB')

# Vẽ biểu đồ tín hiệu âm thanh và spectrogram
plot_audio_and_spectrogram(clean_audio, "Clean Audio")
plot_audio_and_spectrogram(noisy_audio, "Noisy Audio")
