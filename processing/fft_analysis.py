import numpy as np


def compute_fft(signal, sample_rate):
    """
    Compute FFT and return positive frequencies only
    """

    n = len(signal)

    fft_result = np.fft.fft(signal)

    frequencies = np.fft.fftfreq(n, d=1/sample_rate)

    magnitude = np.abs(fft_result)

    # Keep only positive frequencies
    positive_indices = frequencies >= 0

    frequencies = frequencies[positive_indices]

    magnitude = magnitude[positive_indices]

    return frequencies, magnitude