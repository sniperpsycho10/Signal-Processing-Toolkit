from signals.generator import (
    generate_sine_wave,
    add_noise
)

from visualization.plots import (
    plot_signal,
    plot_frequency_spectrum
)

from processing.fft_analysis import compute_fft


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
    noise_level=0.3
)

# Plot time-domain signal
plot_signal(
    t,
    noisy_signal,
    title="Noisy Signal"
)

# Compute FFT
frequencies, magnitude = compute_fft(
    noisy_signal,
    sample_rate=1000
)

# Plot frequency spectrum
plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="FFT Frequency Spectrum"
)