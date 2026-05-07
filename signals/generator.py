import numpy as np


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

    signal = amplitude * np.sin(2 * np.pi * frequency * t)

    return t, signal


def add_noise(signal, noise_level=0.2):

    noise = np.random.normal(0, noise_level, len(signal))

    noisy_signal = signal + noise

    return noisy_signal