import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import numpy as np


def plot_signal(
        t,
        signal,
        title="Signal",
        xlabel="Time",
        ylabel="Amplitude"
):

    plt.figure(figsize=(12, 5))

    plt.plot(t, signal)

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_frequency_spectrum(
        frequencies,
        magnitude,
        title="Frequency Spectrum"
):

    plt.figure(figsize=(12, 5))

    plt.plot(frequencies, magnitude)

    plt.title(title)

    plt.xlabel("Frequency (Hz)")

    plt.ylabel("Magnitude")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def compare_signals(
        t,
        original_signal,
        filtered_signal,
        original_title="Original Signal",
        filtered_title="Filtered Signal"
):

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)

    plt.plot(t, original_signal)

    plt.title(original_title)

    plt.grid(True)

    plt.subplot(2, 1, 2)

    plt.plot(t, filtered_signal)

    plt.title(filtered_title)

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_spectrogram(
        frequencies,
        times,
        spectrogram_data,
        title="Spectrogram"
):

    plt.figure(figsize=(12, 6))

    plt.pcolormesh(
        times,
        frequencies,
        spectrogram_data,
        shading='gouraud',
        cmap='inferno'
    )

    plt.title(title)

    plt.ylabel('Frequency (Hz)')

    plt.xlabel('Time (s)')

    plt.colorbar(label='Intensity')

    plt.tight_layout()

    plt.show()


def plot_3d_spectrogram(
        frequencies,
        times,
        spectrogram_data,
        title="3D Spectrogram"
):

    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(111, projection='3d')

    T, F = np.meshgrid(times, frequencies)

    ax.plot_surface(
        T,
        F,
        spectrogram_data,
        cmap='plasma'
    )

    ax.set_title(title)

    ax.set_xlabel('Time (s)')

    ax.set_ylabel('Frequency (Hz)')

    ax.set_zlabel('Intensity')

    plt.tight_layout()

    plt.show()