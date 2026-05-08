# 🚀 Phase 3 — Signal Filtering System

This phase introduces one of the most important concepts in Digital Signal Processing (DSP):

# Signal Filtering & Noise Removal

The toolkit can now isolate desired frequencies, remove unwanted noise, and reconstruct filtered signals using inverse FFT.

---

# ✅ Features Implemented

- Low-pass filtering
- High-pass filtering
- Band-pass filtering
- Signal reconstruction using inverse FFT
- Multi-frequency signal generation
- Frequency isolation
- Noise reduction
- FFT before/after filtering visualization
- Dynamic user-configurable DSP inputs
- Nyquist sampling validation warning

---

# 🧠 DSP Concepts Covered

## 1. Signal Filtering

Filtering removes unwanted frequency components from a signal.

This allows:
- noise reduction
- signal isolation
- communication channel separation

---

## 2. Low-Pass Filter

Allows:
- low frequencies

Removes:
- high frequencies

### Example Uses
- audio smoothing
- noise reduction
- sensor filtering

---

## 3. High-Pass Filter

Allows:
- high frequencies

Removes:
- low frequencies

### Example Uses
- edge detection
- drift removal
- rapid signal analysis

---

## 4. Band-Pass Filter

Allows:
- only a selected frequency range

Removes:
- everything outside the band

### Example Uses
- radio tuning
- communication systems
- speech isolation

---

## 5. Frequency Masking

Filtering is performed by creating boolean frequency masks.

Example:

```python
frequencies <= cutoff
```

This selects frequencies to preserve.

---

## 6. Inverse FFT

FFT converts:

```text
Time Domain → Frequency Domain
```

Inverse FFT reconstructs the filtered signal:

```text
Frequency Domain → Time Domain
```

Used function:

```python
np.fft.ifft()
```

---

## 7. Multi-Frequency Signal Composition

The toolkit now supports multiple signal frequencies simultaneously.

Example:

```text
50 Hz + 120 Hz + 300 Hz
```

This allows realistic FFT and filtering demonstrations.

---

## 8. Nyquist Sampling Criterion

The project now validates sampling rate correctness using:

fs ≥ 2fmax

This prevents aliasing and incorrect FFT behavior.

---

# 📂 Files Added / Updated

```text
signal_processing_toolkit/
│
├── processing/
│   ├── fft_analysis.py
│   └── filters.py
│
├── signals/
│   └── generator.py
│
├── visualization/
│   └── plots.py
│
├── main.py
└── README.md
```

---

# 📦 New Functionalities

## Multi-Frequency Signal Generator

Implemented:

```python
generate_multi_signal()
```

This dynamically combines multiple sine waves into a single signal.

---

## Low-Pass Filter

Implemented:

```python
low_pass_filter()
```

Keeps frequencies below selected cutoff.

---

## High-Pass Filter

Implemented:

```python
high_pass_filter()
```

Keeps frequencies above selected cutoff.

---

## Band-Pass Filter

Implemented:

```python
band_pass_filter()
```

Keeps only frequencies inside selected frequency range.

---

# 📊 Current Output

The toolkit now visualizes:

## 1. Noisy Signal
Time-domain noisy waveform.

## 2. FFT Before Filtering
Original frequency spectrum.

## 3. Filtered Signal
Reconstructed filtered waveform.

## 4. FFT After Filtering
Filtered frequency spectrum.

---

# 🔬 Example Workflow

```text
Generate Multi-Frequency Signal
            ↓
Add Noise
            ↓
Apply FFT
            ↓
Apply Frequency Filter
            ↓
Remove Unwanted Frequencies
            ↓
Apply Inverse FFT
            ↓
Reconstruct Signal
            ↓
Visualize Filtered Spectrum
```

---

# 🧠 Key Learnings

After Phase 3, the project can now:

✅ Isolate signal frequencies  
✅ Remove unwanted noise  
✅ Apply low-pass filtering  
✅ Apply high-pass filtering  
✅ Apply band-pass filtering  
✅ Reconstruct filtered signals  
✅ Analyze multi-frequency systems  
✅ Validate Nyquist sampling conditions  

---

# 🏢 Real-World Applications

Filtering systems are heavily used in:

- Audio Processing
- Wireless Communication
- RF Signal Isolation
- Radar Systems
- Biomedical Signal Processing
- Embedded Systems
- Speech Enhancement
- Spectrum Analysis

---

# 🎯 Status

✅ Phase 3 Completed