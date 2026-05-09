import librosa
import soundfile as sf
import numpy as np


def load_audio(audio_path, target_sample_rate=22050):
    """
    Load audio file and convert to mono
    """

    signal, sample_rate = librosa.load(
        audio_path,
        sr=target_sample_rate,
        mono=True
    )

    return signal, sample_rate


def save_audio(output_path, signal, sample_rate):
    """
    Save processed audio
    """

    sf.write(
        output_path,
        signal,
        sample_rate
    )


def generate_time_axis(signal_length, sample_rate):
    """
    Generate time axis for audio plotting
    """

    return np.linspace(
        0,
        signal_length / sample_rate,
        signal_length
    )