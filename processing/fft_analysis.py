import numpy as np


def compute_fft(signal, sample_rate):
    """
    Compute FFT and frequency spectrum
    """

    # Number of samples
    n = len(signal)

    # Apply FFT
    fft_result = np.fft.fft(signal)

    # Generate frequency axis
    frequencies = np.fft.fftfreq(n, d=1/sample_rate)

    # Compute magnitude spectrum
    magnitude = np.abs(fft_result)

    return frequencies, magnitude