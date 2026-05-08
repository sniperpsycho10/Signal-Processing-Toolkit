import matplotlib.pyplot as plt


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