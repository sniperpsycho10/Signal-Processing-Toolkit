# 🚀 Phase 2 — FFT & Frequency Analysis

This phase introduces the core concept of Digital Signal Processing (DSP):

# Converting signals from the Time Domain to the Frequency Domain

Using Fast Fourier Transform (FFT), the project can now analyze what frequencies exist inside a signal.

---

# ✅ Features Implemented

- FFT computation using NumPy
- Frequency spectrum generation
- Magnitude spectrum analysis
- Frequency-domain visualization
- Dominant frequency detection
- Noisy signal frequency analysis

---

# 🧠 DSP Concepts Covered

## 1. Frequency Domain

In Phase 1, signals were visualized in the time domain:

- X-axis → Time
- Y-axis → Amplitude

Phase 2 introduces the frequency domain:

- X-axis → Frequency
- Y-axis → Magnitude

This allows analysis of the frequencies present inside a signal.

---

## 2. Fourier Transform

Core mathematical idea:

X(f) = ∫ x(t)e^(-j2πft) dt

The Fourier Transform decomposes a signal into its frequency components.

---

## 3. Fast Fourier Transform (FFT)

FFT is a computationally efficient implementation of the Fourier Transform.

Used function:

```python
np.fft.fft()
```

FFT converts:

```text
Time Domain → Frequency Domain
```

---

## 4. Frequency Spectrum

The frequency spectrum visualizes:
- which frequencies exist
- how strong each frequency is

Example:
- A 50 Hz sine wave produces a strong peak near 50 Hz.

---

## 5. Magnitude Spectrum

FFT outputs complex numbers:

```text
a + bj
```

To visualize signal strength, the magnitude is computed using:

```python
np.abs(fft_result)
```

---

## 6. Frequency Axis Generation

FFT output bins are mapped to real frequencies using:

```python
np.fft.fftfreq()
```

This generates accurate frequency labels for visualization.

---

# 📂 Files Added / Updated

```text
signal_processing_toolkit/
│
├── processing/
│   └── fft_analysis.py
│
├── visualization/
│   └── plots.py
│
├── main.py
└── README.md
```

---

# 📦 New Functionalities

## FFT Analysis Engine

Implemented reusable FFT computation module:

```python
compute_fft(signal, sample_rate)
```

Responsibilities:
- compute FFT
- generate frequency axis
- compute magnitude spectrum

---

## Frequency Spectrum Plotting

Added visualization for:
- frequency vs magnitude

This acts as a basic spectrum analyzer.

---

# 📊 Current Output

The system now generates:

## 1. Time-Domain Plot
Displays noisy waveform over time.

## 2. Frequency Spectrum Plot
Displays dominant frequencies inside the signal.

Observed:
- strong peak at signal frequency
- additional noise components across spectrum

---

# 🔬 Example Workflow

```text
Generate Signal
        ↓
Add Noise
        ↓
Apply FFT
        ↓
Extract Frequencies
        ↓
Generate Magnitude Spectrum
        ↓
Plot Frequency Spectrum
```

---

# 🧠 Key Learnings

After Phase 2, the project can now:

✅ Analyze signal frequencies  
✅ Detect dominant frequency peaks  
✅ Visualize frequency spectra  
✅ Understand noisy signal composition  
✅ Perform core DSP frequency analysis  

---

# 🏢 Real-World Applications

FFT is widely used in:

- Audio Processing
- Wireless Communication
- Radar Systems
- RF Signal Analysis
- Biomedical Signal Analysis
- Speech Processing
- Spectrum Analyzers

---

# 🎯 Status

✅ Phase 2 Completed