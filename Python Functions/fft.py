import numpy as np
import matplotlib.pyplot as plt


def generate_signal(t, amplitude_1, frequency_1, amplitude_2, frequency_2, noise_coefficient):
    f = amplitude_1 * np.sin(2 * np.pi * frequency_1 * t) + \
        amplitude_2 * np.sin(2 * np.pi * frequency_2 * t)
    f_clean = f

    f = f + noise_coefficient * np.random.randn(len(t))

    return f, f_clean


def compute_fft(t, f):
    n = len(t)
    fhat = np.fft.fft(f, n)
    PSD = fhat * np.conj(fhat) / n  # Power spectrum (power per freq)
    freq = (1 / (dt * n)) * np.arange(n)
    L = np.arange(1, np.floor(n / 2), dtype='int')

    return fhat, PSD, freq, L


def filter_noise(fhat, PSD, threshold=100):
    indices = PSD > threshold  # Find all freqs with large power
    PSDclean = PSD * indices  # Zero out all others
    fhat = indices * fhat  # Zero out small Fourier coeffs. in Y

    return fhat, PSDclean


def inverse_fft(fhat):
    ffilt = np.fft.ifft(fhat)  # Inverse FFT for filtered time signal
    return ffilt


def plot_signal(t, f, f_clean, ffilt):
    plt.subplot(4, 1, 1)
    plt.plot(t, f_clean)
    plt.title('Clean Signal')

    plt.subplot(4, 1, 2)
    plt.plot(t, f)
    plt.title('Noisy Signal')

    plt.subplot(4, 1, 3)
    plt.plot(t, np.real(ffilt))
    plt.title('Filtered Signal')

    plt.subplot(4, 1, 4)
    plt.plot(t, np.real(ffilt), 'r', label='Filtered')
    plt.plot(t, f_clean, 'g', label='Clean')
    plt.legend()
    plt.title('Comparison of Clean and Filtered Signals')

    plt.tight_layout()
    plt.show()


def plot_frequency_coefficients(freq, PSD, L):
    plt.plot(freq[L], PSD[L], 'b')  # plot frequency coefficients
    plt.title('Frequency Coefficients')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.show()


def real_time_plot(t, f, f_clean):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(10, 6))

    threshold = 100
    while True:
        fhat, PSD, freq, L = compute_fft(t, f)
        fhat, PSDclean = filter_noise(fhat, PSD, threshold)
        ffilt = inverse_fft(fhat)

        ax.clear()
        ax.plot(t, f_clean, label='Clean Signal')
        ax.plot(t, f, label='Noisy Signal')
        ax.plot(t, np.real(ffilt), label='Filtered Signal')
        ax.legend()
        ax.set_title(
            f'Comparison of Clean, Noisy, and Filtered Signals (Threshold = {threshold})')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')

        plt.pause(0.1)

        try:
            threshold = float(
                input("Enter the threshold value (press Ctrl+C to exit): "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the threshold.")


# Main program
dt = 0.001
t = np.arange(0, 1, dt)

# # amplitude_1 = float(input("Enter amplitude for the first signal: "))
# frequency_1 = float(input("Enter frequency for the first signal: "))
# amplitude_2 = float(input("Enter amplitude for the second signal: "))
# frequency_2 = float(input("Enter frequency for the second signal: "))
# noise_coefficient = float(input("Enter the noise coefficient: "))

# f, f_clean = generate_signal(
#     t, amplitude_1, frequency_1, amplitude_2, frequency_2, noise_coefficient)

# real_time_plot(t, f, f_clean)
