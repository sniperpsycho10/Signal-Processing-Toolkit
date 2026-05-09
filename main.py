from signals.audio_loader import (
    load_audio,
    save_audio,
    generate_time_axis
)

from signals.generator import (
    generate_multi_signal,
    generate_chirp_signal,
    add_noise
)

from visualization.plots import (
    plot_signal,
    plot_frequency_spectrum,
    compare_signals,
    plot_spectrogram,
    plot_3d_spectrogram
)

from processing.fft_analysis import compute_fft

from processing.filters import (
    low_pass_filter,
    high_pass_filter,
    band_pass_filter
)

from processing.spectrogram import (
    compute_spectrogram
)


# =====================================
# MODE SELECTION
# =====================================

print("Select Input Mode")
print("1. Synthetic Signal")
print("2. Real Audio File")

mode_choice = input(
    "Enter choice (1/2): "
)


# =====================================
# SYNTHETIC SIGNAL MODE
# =====================================

if mode_choice == "1":

    print("\nSelect Signal Type")
    print("1. Multi-Frequency Signal")
    print("2. Chirp Signal")

    signal_choice = input(
        "Enter choice (1/2): "
    )

    amplitude = float(
        input("Enter signal amplitude: ")
    )

    duration = float(
        input("Enter signal duration (seconds): ")
    )

    sample_rate = int(
        input("Enter sample rate (Hz): ")
    )

    noise_level = float(
        input("Enter noise level: ")
    )

    # ---------------------------------
    # Multi-Frequency Signal
    # ---------------------------------

    if signal_choice == "1":

        frequency_input = input(
            "Enter frequencies separated by commas: "
        )

        frequencies_list = [
            float(freq.strip())
            for freq in frequency_input.split(",")
        ]

        max_frequency = max(frequencies_list)

        if sample_rate < 2 * max_frequency:

            print("\nWARNING:")
            print("Sample rate violates Nyquist criterion.")

        t, signal = generate_multi_signal(
            frequencies=frequencies_list,
            amplitude=amplitude,
            duration=duration,
            sample_rate=sample_rate
        )

    # ---------------------------------
    # Chirp Signal
    # ---------------------------------

    elif signal_choice == "2":

        start_frequency = float(
            input("Enter chirp start frequency: ")
        )

        end_frequency = float(
            input("Enter chirp end frequency: ")
        )

        max_frequency = max(
            start_frequency,
            end_frequency
        )

        if sample_rate < 2 * max_frequency:

            print("\nWARNING:")
            print("Sample rate violates Nyquist criterion.")

        t, signal = generate_chirp_signal(
            start_frequency=start_frequency,
            end_frequency=end_frequency,
            amplitude=amplitude,
            duration=duration,
            sample_rate=sample_rate
        )

    else:

        print("Invalid signal choice")
        exit()

    # ---------------------------------
    # Add Noise
    # ---------------------------------

    signal = add_noise(
        signal,
        noise_level=noise_level
    )


# =====================================
# REAL AUDIO MODE
# =====================================

elif mode_choice == "2":

    audio_path = input(
        "Enter path to audio file (.wav or .mp3): "
    )

    signal, sample_rate = load_audio(audio_path)

    print("\nAudio Loaded Successfully")

    print(f"Sample Rate: {sample_rate} Hz")

    print(f"Signal Length: {len(signal)} samples")

    t = generate_time_axis(
        len(signal),
        sample_rate
    )


else:

    print("Invalid mode choice")
    exit()


# =====================================
# SIGNAL VISUALIZATION
# =====================================

plot_signal(
    t,
    signal,
    title="Input Signal"
)


# =====================================
# FFT BEFORE FILTERING
# =====================================

frequencies, magnitude = compute_fft(
    signal,
    sample_rate
)

plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="FFT Before Filtering"
)


# =====================================
# FILTER SELECTION
# =====================================

print("\nSelect Filter Type")
print("1. Low-Pass Filter")
print("2. High-Pass Filter")
print("3. Band-Pass Filter")

filter_choice = input(
    "Enter choice (1/2/3): "
)


# =====================================
# APPLY FILTER
# =====================================

if filter_choice == "1":

    cutoff = float(
        input("Enter low-pass cutoff frequency: ")
    )

    filtered_signal = low_pass_filter(
        signal,
        cutoff=cutoff,
        sample_rate=sample_rate
    )

    filter_title = "Low-Pass Filtered Signal"


elif filter_choice == "2":

    cutoff = float(
        input("Enter high-pass cutoff frequency: ")
    )

    filtered_signal = high_pass_filter(
        signal,
        cutoff=cutoff,
        sample_rate=sample_rate
    )

    filter_title = "High-Pass Filtered Signal"


elif filter_choice == "3":

    low_cutoff = float(
        input("Enter low cutoff frequency: ")
    )

    high_cutoff = float(
        input("Enter high cutoff frequency: ")
    )

    filtered_signal = band_pass_filter(
        signal,
        low_cutoff=low_cutoff,
        high_cutoff=high_cutoff,
        sample_rate=sample_rate
    )

    filter_title = "Band-Pass Filtered Signal"

else:

    print("Invalid filter choice")
    exit()


# =====================================
# SIGNAL COMPARISON
# =====================================

compare_signals(
    t,
    signal,
    filtered_signal,
    original_title="Original Signal",
    filtered_title=filter_title
)


# =====================================
# FFT AFTER FILTERING
# =====================================

filtered_frequencies, filtered_magnitude = compute_fft(
    filtered_signal,
    sample_rate
)

plot_frequency_spectrum(
    filtered_frequencies,
    filtered_magnitude,
    title="FFT After Filtering"
)


# =====================================
# SPECTROGRAM
# =====================================

spectrogram_frequencies, spectrogram_times, spectrogram_data = compute_spectrogram(
    filtered_signal,
    sample_rate
)

plot_spectrogram(
    spectrogram_frequencies,
    spectrogram_times,
    spectrogram_data,
    title="2D Spectrogram"
)

plot_3d_spectrogram(
    spectrogram_frequencies,
    spectrogram_times,
    spectrogram_data,
    title="3D Spectrogram"
)


# =====================================
# SAVE AUDIO (ONLY FOR REAL AUDIO)
# =====================================

if mode_choice == "2":

    save_choice = input(
        "\nDo you want to save filtered audio? (y/n): "
    )

    if save_choice.lower() == "y":

        output_path = input(
            "Enter output file name (example: cleaned_audio.wav): "
        )

        save_audio(
            output_path,
            filtered_signal,
            sample_rate
        )

        print("\nFiltered audio saved successfully")