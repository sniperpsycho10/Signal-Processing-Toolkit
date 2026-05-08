from signals.generator import (
    generate_multi_signal,
    add_noise
)

from visualization.plots import (
    plot_signal,
    plot_frequency_spectrum,
    compare_signals,
    plot_spectrogram
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
# USER INPUTS
# =====================================

frequency_input = input(
    "Enter signal frequencies separated by commas (example: 50,120,300): "
)

frequencies_list = [
    float(freq.strip())
    for freq in frequency_input.split(",")
]

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
# NYQUIST CHECK
# =====================================

max_frequency = max(frequencies_list)

if sample_rate < 2 * max_frequency:

    print("\nWARNING:")
    print("Sample rate violates Nyquist criterion.")
    print(
        f"Recommended sample rate >= {2 * max_frequency} Hz"
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
# SIGNAL GENERATION
# =====================================

t, signal = generate_multi_signal(
    frequencies=frequencies_list,
    amplitude=amplitude,
    duration=duration,
    sample_rate=sample_rate
)


# =====================================
# ADD NOISE
# =====================================

noisy_signal = add_noise(
    signal,
    noise_level=noise_level
)


# =====================================
# TIME-DOMAIN VISUALIZATION
# =====================================

plot_signal(
    t,
    noisy_signal,
    title="Noisy Signal"
)


# =====================================
# FFT BEFORE FILTERING
# =====================================

frequencies, magnitude = compute_fft(
    noisy_signal,
    sample_rate
)

plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="FFT Before Filtering"
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
# SIGNAL COMPARISON
# =====================================

compare_signals(
    t,
    noisy_signal,
    filtered_signal,
    original_title="Original Noisy Signal",
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
# SPECTROGRAM GENERATION
# =====================================

spectrogram_frequencies, spectrogram_times, spectrogram_data = compute_spectrogram(
    filtered_signal,
    sample_rate
)


# =====================================
# SPECTROGRAM VISUALIZATION
# =====================================

plot_spectrogram(
    spectrogram_frequencies,
    spectrogram_times,
    spectrogram_data,
    title="Signal Spectrogram"
)