from signals.generator import (
    generate_sine_wave,
    add_noise
)

from visualization.plots import (
    plot_signal,
    plot_frequency_spectrum,
    compare_signals
)

from processing.fft_analysis import compute_fft

from processing.filters import (
    low_pass_filter,
    high_pass_filter,
    band_pass_filter
)


# Generate signal
t, signal = generate_sine_wave(
    frequency=50,
    amplitude=1,
    duration=1,
    sample_rate=1000
)

# Add noise
noisy_signal = add_noise(
    signal,
    noise_level=0.5
)

# Plot noisy signal
plot_signal(
    t,
    noisy_signal,
    title="Noisy Signal"
)

# FFT before filtering
frequencies, magnitude = compute_fft(
    noisy_signal,
    sample_rate=1000
)

plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="FFT Before Filtering"
)

# Apply low-pass filter
filtered_signal = low_pass_filter(
    noisy_signal,
    cutoff=100,
    sample_rate=1000
)

# Compare signals
compare_signals(
    t,
    noisy_signal,
    filtered_signal,
    original_title="Original Noisy Signal",
    filtered_title="Low-Pass Filtered Signal"
)

# FFT after filtering
filtered_frequencies, filtered_magnitude = compute_fft(
    filtered_signal,
    sample_rate=1000
)

plot_frequency_spectrum(
    filtered_frequencies,
    filtered_magnitude,
    title="FFT After Filtering"
)