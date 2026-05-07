from signals.generator import (
    generate_sine_wave,
    add_noise
)

from visualization.plots import plot_signal


# Generate signal
t, signal = generate_sine_wave(
    frequency=50,
    amplitude=2,
    duration=1,
    sample_rate=1000
)

# Add noise
noisy_signal = add_noise(
    signal,
    noise_level=1
)

# Plot clean signal
plot_signal(
    t,
    signal,
    title="Clean Signal"
)

# Plot noisy signal
plot_signal(
    t,
    noisy_signal,
    title="Noisy Signal"
)