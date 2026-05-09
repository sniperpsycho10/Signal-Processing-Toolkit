import os

from datetime import datetime

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

from signals.realtime_processor import (
    RealtimeDSPProcessor
)

from signals.audio_recorder import (
    AudioRecorder
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

from visualization.live_dashboard import (
    LiveDSPDashboard
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

    t, signal = generate_multi_signal(

        frequencies=frequencies,

        amplitude=amplitude,

        duration=duration,

        sample_rate=sample_rate
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

    t, signal = generate_chirp_signal(

        start_frequency=start_frequency,

        end_frequency=end_frequency,

        amplitude=amplitude,

        duration=duration,

        sample_rate=sample_rate
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

    signal, sample_rate = load_audio(
        file_path
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

    print("4. Full DSP Dashboard")

    choice = input(
        "\nEnter choice: "
    )

    print("\n========= FILTER OPTIONS =========")

    print("1. No Filter")

    print("2. Low-pass Filter")

    print("3. High-pass Filter")

    print("4. Band-pass Filter")

    filter_choice = input(
        "\nEnter filter choice: "
    )

    audio_input = RealTimeAudioInput(

        sample_rate=44100,

        channels=1,

        block_size=1024
    )

    processor = RealtimeDSPProcessor(

        sample_rate=44100
    )

    # =================================
    # FILTER SETUP
    # =================================

    if filter_choice == "2":

        cutoff = float(

            input(
                "Enter low-pass cutoff frequency (Hz): "
            )
        )

        processor.set_lowpass(cutoff)

    elif filter_choice == "3":

        cutoff = float(

            input(
                "Enter high-pass cutoff frequency (Hz): "
            )
        )

        processor.set_highpass(cutoff)

    elif filter_choice == "4":

        lowcut = float(

            input(
                "Enter band-pass LOW cutoff frequency (Hz): "
            )
        )

        highcut = float(

            input(
                "Enter band-pass HIGH cutoff frequency (Hz): "
            )
        )

        processor.set_bandpass(

            lowcut,

            highcut
        )

    else:

        processor.disable_filter()

    # =================================
    # CREATE RECORDINGS DIRECTORY
    # =================================

    os.makedirs(

        "recordings",

        exist_ok=True
    )

    # =================================
    # TIMESTAMPED FILENAME
    # =================================

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"recordings/recording_{timestamp}.wav"
    )

    # =================================
    # RECORDER
    # =================================

    recorder = AudioRecorder(

        filename=filename,

        sample_rate=44100
    )

    audio_input.recorder = recorder

    # =================================
    # START AUDIO STREAM
    # =================================

    audio_input.start_stream()

    try:

        if choice == "1":

            waveform = LiveWaveformPlot(

                audio_input,

                processor
            )

            waveform.start()

        elif choice == "2":

            fft_plot = LiveFFTPlot(

                audio_input,

                processor
            )

            fft_plot.start()

        elif choice == "3":

            spectrogram = LiveSpectrogramPlot(

                audio_input,

                processor
            )

            spectrogram.start()

        elif choice == "4":

            dashboard = LiveDSPDashboard(

                audio_input,

                processor,

                recorder
            )

            dashboard.start()

        else:

            print("\nInvalid choice.")

    finally:

        audio_input.stop_stream()

        if recorder.is_recording:

            recorder.stop_recording()


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

        frequencies, magnitude = compute_fft(

            signal,

            sample_rate
        )

        plot_frequency_spectrum(

            frequencies,

            magnitude,

            "FFT Spectrum"
        )

    elif choice == "3":

        frequencies, times, Sxx = compute_spectrogram(

            signal,

            sample_rate
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