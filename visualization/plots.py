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