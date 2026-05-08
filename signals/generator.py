import numpy as np

from scipy.signal import chirp


def generate_time(duration=1.0, sample_rate=1000):

    samples = int(duration * sample_rate)

    t = np.linspace(0, duration, samples)

    return t


def generate_sine_wave(
        frequency=5,
        amplitude=1,
        duration=1,
        sample_rate=1000
):

    t = generate_time(duration, sample_rate)

    signal = amplitude * np.sin(
        2 * np.pi * frequency * t
    )

    return t, signal


def generate_multi_signal(
        frequencies,
        amplitude=1,
        duration=1,
        sample_rate=1000
):

    t = generate_time(duration, sample_rate)

    signal = np.zeros(len(t))

    for freq in frequencies:

        signal += amplitude * np.sin(
            2 * np.pi * freq * t
        )

    return t, signal


def generate_chirp_signal(
        start_frequency,
        end_frequency,
        amplitude=1,
        duration=5,
        sample_rate=1000
):

    t = generate_time(duration, sample_rate)

    signal = amplitude * chirp(
        t,
        f0=start_frequency,
        f1=end_frequency,
        t1=duration,
        method='linear'
    )

    return t, signal


def add_noise(signal, noise_level=0.2):

    noise = np.random.normal(
        0,
        noise_level,
        len(signal)
    )

    noisy_signal = signal + noise

    return noisy_signal