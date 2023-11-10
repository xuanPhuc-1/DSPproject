import numpy as np
from scipy import signal
import scipy.io.wavfile as wav

# Đọc tệp âm thanh WAV
fs, audio_data = wav.read('your_audio_file.wav')

# Tính toán mức độ nhiễu trong tín hiệu (ví dụ: thông qua phân tích tín hiệu)
noise_level = calculate_SNR(audio_data)

# Điều chỉnh tần số cắt và num_taps dựa trên mức độ nhiễu
cutoff_freq = calculate_cutoff_frequency(noise_level)
num_taps = calculate_num_taps(noise_level)

# Thiết lập bộ lọc FIR
nyquist = 0.5 * fs
normal_cutoff = cutoff_freq / nyquist
filter_coeffs = signal.firwin(num_taps, normal_cutoff, window='hamming')

# Áp dụng bộ lọc FIR vào tín hiệu âm thanh
filtered_audio = signal.lfilter(filter_coeffs, 1.0, audio_data)

# Lưu kết quả lọc ra tệp mới
wav.write('filtered_audio.wav', fs, filtered_audio)

def calculate_SNR(clean_signal, noisy_signal):
    # Tính toán SNR
    noise_signal = noisy_signal - clean_signal
    RMS_noise = np.sqrt(np.mean(noise_signal ** 2))
    RMS_clean = np.sqrt(np.mean(clean_signal ** 2))
    return 20 * np.log10(RMS_clean / RMS_noise)
