from scipy.signal import spectrogram


def compute_spectrogram(signal, sample_rate):
    """
    Compute spectrogram using STFT
    """

    frequencies, times, spectrogram_data = spectrogram(
        signal,
        fs=sample_rate
    )

    return frequencies, times, spectrogram_data