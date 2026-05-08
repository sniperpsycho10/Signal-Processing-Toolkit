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
# SIGNAL TYPE SELECTION
# =====================================

print("Select Signal Type")
print("1. Multi-Frequency Signal")
print("2. Chirp Signal")

signal_choice = input(
    "Enter choice (1/2): "
)


# =====================================
# COMMON INPUTS
# =====================================

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


# =====================================
# SIGNAL GENERATION
# =====================================

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


# =====================================
# ADD NOISE
# =====================================

noisy_signal = add_noise(
    signal,
    noise_level=noise_level
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
# FILTERING
# =====================================

if filter_choice == "1":

    cutoff = float(
        input("Enter low-pass cutoff frequency: ")
    )

    filtered_signal = low_pass_filter(
        noisy_signal,
        cutoff=cutoff,
        sample_rate=sample_rate
    )

    filter_title = "Low-Pass Filtered Signal"


elif filter_choice == "2":

    cutoff = float(
        input("Enter high-pass cutoff frequency: ")
    )

    filtered_signal = high_pass_filter(
        noisy_signal,
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
        noisy_signal,
        low_cutoff=low_cutoff,
        high_cutoff=high_cutoff,
        sample_rate=sample_rate
    )

    filter_title = "Band-Pass Filtered Signal"

else:

    print("Invalid filter choice")
    exit()


# =====================================
# VISUALIZATION
# =====================================

plot_signal(
    t,
    noisy_signal,
    title="Noisy Signal"
)

compare_signals(
    t,
    noisy_signal,
    filtered_signal,
    original_title="Original Noisy Signal",
    filtered_title=filter_title
)


# =====================================
# FFT ANALYSIS
# =====================================

frequencies, magnitude = compute_fft(
    filtered_signal,
    sample_rate
)

plot_frequency_spectrum(
    frequencies,
    magnitude,
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