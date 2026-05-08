import numpy as np


def low_pass_filter(signal, cutoff, sample_rate):
    """
    Remove high frequencies
    """

    n = len(signal)

    fft_result = np.fft.fft(signal)

    frequencies = np.fft.fftfreq(n, d=1/sample_rate)

    # Create mask
    mask = np.abs(frequencies) <= cutoff

    # Apply filter
    filtered_fft = fft_result * mask

    # Reconstruct signal
    filtered_signal = np.fft.ifft(filtered_fft)

    return np.real(filtered_signal)


def high_pass_filter(signal, cutoff, sample_rate):
    """
    Remove low frequencies
    """

    n = len(signal)

    fft_result = np.fft.fft(signal)

    frequencies = np.fft.fftfreq(n, d=1/sample_rate)

    mask = np.abs(frequencies) >= cutoff

    filtered_fft = fft_result * mask

    filtered_signal = np.fft.ifft(filtered_fft)

    return np.real(filtered_signal)


def band_pass_filter(signal, low_cutoff, high_cutoff, sample_rate):
    """
    Keep only specific frequency range
    """

    n = len(signal)

    fft_result = np.fft.fft(signal)

    frequencies = np.fft.fftfreq(n, d=1/sample_rate)

    mask = (
        (np.abs(frequencies) >= low_cutoff) &
        (np.abs(frequencies) <= high_cutoff)
    )

    filtered_fft = fft_result * mask

    filtered_signal = np.fft.ifft(filtered_fft)

    return np.real(filtered_signal)