import numpy as np

from signals.generator import (
    generate_multi_signal,
    generate_chirp_signal,
    add_noise
)

from signals.audio_loader import (
    load_audio
)

from signals.real_time_input import (
    RealTimeAudioInput
)

from processing.fft_analysis import (
    compute_fft
)

from processing.spectrogram import (
    compute_spectrogram
)

from visualization.plots import (
    plot_signal,
    plot_frequency_spectrum,
    plot_spectrogram
)

from visualization.live_graphs import (
    LiveWaveformPlot
)

from visualization.live_fft import (
    LiveFFTPlot
)

from visualization.live_spectrogram import (
    LiveSpectrogramPlot
)


def synthetic_signal_menu():

    print("\n========= SYNTHETIC SIGNAL =========")

    amplitude = float(
        input("Enter amplitude: ")
    )

    duration = float(
        input("Enter duration (seconds): ")
    )

    sample_rate = int(
        input("Enter sample rate: ")
    )

    noise_level = float(
        input("Enter noise level: ")
    )

    print(
        "\nUsing default frequencies:"
        " 50 Hz, 120 Hz, 300 Hz"
    )

    frequencies = [50, 120, 300]

    t, signal = (
        generate_multi_signal(

            frequencies=frequencies,

            amplitude=amplitude,

            duration=duration,

            sample_rate=sample_rate
        )
    )

    signal = add_noise(

        signal,

        noise_level=noise_level
    )

    visualization_menu(

        signal,

        sample_rate,

        t
    )


def chirp_signal_menu():

    print("\n========= CHIRP SIGNAL =========")

    amplitude = float(
        input("Enter amplitude: ")
    )

    duration = float(
        input("Enter duration (seconds): ")
    )

    sample_rate = int(
        input("Enter sample rate: ")
    )

    noise_level = float(
        input("Enter noise level: ")
    )

    start_frequency = float(
        input("Enter start frequency: ")
    )

    end_frequency = float(
        input("Enter end frequency: ")
    )

    t, signal = (
        generate_chirp_signal(

            start_frequency=start_frequency,

            end_frequency=end_frequency,

            amplitude=amplitude,

            duration=duration,

            sample_rate=sample_rate
        )
    )

    signal = add_noise(

        signal,

        noise_level=noise_level
    )

    visualization_menu(

        signal,

        sample_rate,

        t
    )


def audio_file_menu():

    print("\n========= AUDIO FILE =========")

    file_path = input(
        "Enter audio file path: "
    )

    signal, sample_rate = (
        load_audio(file_path)
    )

    t = np.linspace(

        0,

        len(signal) / sample_rate,

        len(signal)
    )

    visualization_menu(

        signal,

        sample_rate,

        t
    )


def live_microphone_menu():

    print("\n========= LIVE MICROPHONE =========")

    print("1. Realtime Waveform")

    print("2. Realtime FFT Spectrum")

    print("3. Realtime Spectrogram")

    choice = input(
        "\nEnter choice: "
    )

    audio_input = RealTimeAudioInput(

        sample_rate=44100,

        channels=1,

        block_size=2048
    )

    audio_input.start_stream()

    try:

        if choice == "1":

            waveform = (
                LiveWaveformPlot(
                    audio_input
                )
            )

            waveform.start()

        elif choice == "2":

            fft_plot = (
                LiveFFTPlot(
                    audio_input
                )
            )

            fft_plot.start()

        elif choice == "3":

            spectrogram = (
                LiveSpectrogramPlot(
                    audio_input
                )
            )

            spectrogram.start()

        else:

            print("\nInvalid choice.")

    finally:

        audio_input.stop_stream()


def visualization_menu(

        signal,

        sample_rate,

        t
):

    print("\n========= VISUALIZATION =========")

    print("1. Waveform")

    print("2. FFT Spectrum")

    print("3. Spectrogram")

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        plot_signal(

            t,

            signal,

            "Signal Waveform"
        )

    elif choice == "2":

        frequencies, magnitude = (
            compute_fft(

                signal,

                sample_rate
            )
        )

        plot_frequency_spectrum(

            frequencies,

            magnitude,

            "FFT Spectrum"
        )

    elif choice == "3":

        frequencies, times, Sxx = (
            compute_spectrogram(

                signal,

                sample_rate
            )
        )

        plot_spectrogram(

            frequencies,

            times,

            Sxx,

            "Spectrogram"
        )

    else:

        print("\nInvalid choice.")


def main():

    print("\n========= DSP TOOLKIT =========")

    print("1. Synthetic Signal")

    print("2. Chirp Signal")

    print("3. Audio File")

    print("4. Live Microphone")

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        synthetic_signal_menu()

    elif choice == "2":

        chirp_signal_menu()

    elif choice == "3":

        audio_file_menu()

    elif choice == "4":

        live_microphone_menu()

    else:

        print("\nInvalid choice.")


if __name__ == "__main__":

    main()