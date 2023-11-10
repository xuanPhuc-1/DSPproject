import numpy as np
import matplotlib.pyplot as plt

def median_filter_for_continuous_data(data, window_size):
    """ Apply median filter to continuous data.
    Parameters:
    - data: The input signal
    - window_size: The size of the window
    """
    data_filtered = np.zeros(len(data))
    for i in range(len(data)):
        start = max(0, i - window_size)
        end = min(len(data), i + window_size)
        data_filtered[i] = np.median(data[start:end])
    return data_filtered



def main():
    dt = 0.001
    t = np.arange(0, 1, dt)
    f = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)  # Sum of 2
    f_clean = f

    f = f + 2.5 * np.random.randn(len(t))
    #convert f to 2d array
    f = np.reshape(f, (1, len(f)))
    #apply median filter
    f_filtered = median_filter_for_continuous_data(f, 10)
    #convert f_filtered to continuous data
    f_filtered = np.reshape(f_filtered, (len(f_filtered),))
    #plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, f, label='Raw')
    plt.plot(t, f_filtered, label='Filtered')
    plt.legend()
    plt.title(f"Median Filter", size=15)
    plt.show()
    
    
    

if __name__ == '__main__':
    main()