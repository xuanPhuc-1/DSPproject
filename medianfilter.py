import numpy as np
from scipy.signal import medfilt

def median_filter(signal, window_size):
    # Sử dụng medfilt từ thư viện scipy để áp dụng bộ lọc trung vị
    filtered_signal = medfilt(signal, kernel_size=window_size)
    return filtered_signal

# Ví dụ về cách sử dụng
if __name__ == "__main__":
    # Tạo một tín hiệu âm thanh mẫu (có nhiễu)
    signal_with_noise = np.array([1, 3, 5, 10, 20, 18, 15, 12, 7, 5])

    # Cài đặt kích thước cửa sổ cho bộ lọc trung vị
    window_size = 3

    # Áp dụng bộ lọc trung vị
    filtered_signal = median_filter(signal_with_noise, window_size)

    # In tín hiệu gốc và tín hiệu đã lọc
    print("Tín hiệu gốc: ", signal_with_noise)
    print("Tín hiệu đã lọc: ", filtered_signal)
