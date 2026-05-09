# Phase 7 – Interactive Realtime DSP Workstation

## Overview

Phase 7 upgrades the Signal Processing Toolkit into a complete interactive realtime DSP workstation.

This phase introduces:

- Interactive DSP dashboard
- Realtime filter controls
- GUI-based DSP parameter tuning
- Unified waveform, FFT, and spectrogram visualization
- Professional audio recording system
- Timestamped WAV recordings
- Realtime DSP experimentation environment
- Multi-panel PyQtGraph dashboard
- Interactive realtime signal analysis

The toolkit now behaves similarly to professional DSP software such as:

- Audacity
- SDR#
- GNU Radio visualization panels
- Spectrum analyzers
- Oscilloscope software
- Audio analysis workstations

---

# Major Features Implemented

---

# 1. Unified Realtime DSP Dashboard

Implemented a complete realtime DSP dashboard using:

- PyQt5
- PyQtGraph
- Multi-panel GUI layouts

The dashboard simultaneously displays:

- Realtime waveform
- Realtime FFT spectrum
- Realtime waterfall spectrogram

All visualizations are synchronized using a shared realtime audio pipeline.

---

# 2. Interactive DSP Control Panel

Added a professional GUI control panel for realtime DSP interaction.

Features include:

- Filter type selection
- Live DSP control switching
- Realtime cutoff tuning
- Interactive parameter adjustment
- Reset filter controls

Supported filters:

- No Filter
- Low-pass Filter
- High-pass Filter
- Band-pass Filter

This allows realtime DSP experimentation directly from the GUI.

---

# 3. Realtime DSP Filtering System

Implemented a realtime DSP processing engine using:

- Butterworth filters
- Streaming audio pipelines
- Realtime filter processing

Implemented filters:

## Low-pass Filter
Removes high-frequency components while preserving low frequencies.

## High-pass Filter
Removes low-frequency components while preserving high frequencies.

## Band-pass Filter
Isolates a selected frequency range.

Realtime filter changes instantly affect:

- Waveform
- FFT spectrum
- Spectrogram

---

# 4. Professional Realtime Recording System

Implemented a callback-based realtime audio recording architecture.

Features include:

- Realtime WAV recording
- Callback-based audio capture
- Timestamped recordings
- Automatic recordings folder generation
- GUI recording controls
- Start/Stop recording buttons
- Live recording status indicator
- Recording duration timer

Recordings are saved in:

```text
recordings/
```

with timestamped filenames:

```text
recording_YYYYMMDD_HHMMSS.wav
```

---

# 5. Realtime FFT Spectrum Analyzer

Implemented a realtime FFT spectrum analyzer with:

- Live FFT computation
- dB-scaled magnitude display
- Hann window preprocessing
- DC offset removal
- Realtime spectral visualization

This allows:

- Frequency analysis
- Harmonic observation
- DSP filter verification
- Speech frequency analysis

---

# 6. Realtime Waterfall Spectrogram

Implemented a realtime scrolling spectrogram system.

Features:

- Waterfall visualization
- Time-frequency analysis
- Dynamic spectrogram updates
- Inferno colormap visualization
- Frequency evolution tracking

This enables visualization of:

- Speech harmonics
- Chirps
- Frequency sweeps
- Filter behavior over time

---

# 7. Optimized Realtime DSP Performance

Improved realtime DSP stability using:

- Reduced GUI update rate
- Optimized FFT sizes
- Reduced spectrogram history size
- Callback-based recording architecture
- Efficient PyQtGraph rendering

This significantly improved:

- Realtime responsiveness
- Recording stability
- FFT smoothness
- Spectrogram performance

---

# 8. Professional DSP Architecture

The system now uses a professional realtime DSP architecture:

```text
Microphone Input
        ↓
Realtime Audio Callback
        ↓
Audio Buffer
        ↓
DSP Processor
        ↓
Waveform / FFT / Spectrogram
```

Recording operates independently using callback-based audio capture.

---

# Project Architecture

```text
signal_processing_toolkit/

│── signals/
│   ├── generator.py
│   ├── audio_loader.py
│   ├── real_time_input.py
│   ├── realtime_processor.py
│   ├── audio_recorder.py
│
│── processing/
│   ├── fft_analysis.py
│   ├── spectrogram.py
│   ├── filters.py
│
│── visualization/
│   ├── plots.py
│   ├── live_graphs.py
│   ├── live_fft.py
│   ├── live_spectrogram.py
│   ├── live_dashboard.py
│
│── recordings/
│
│── main.py
│── phase6_main.py
```

---

# Technologies Used

- Python
- NumPy
- SciPy
- PyQt5
- PyQtGraph
- SoundDevice
- Matplotlib

---

# DSP Concepts Learned

This phase introduced several advanced DSP and software engineering concepts:

- Realtime DSP pipelines
- Streaming audio systems
- Interactive DSP controls
- Callback-based recording
- FFT analysis
- Time-frequency analysis
- Waterfall spectrograms
- DSP filter design
- Low-pass filtering
- High-pass filtering
- Band-pass filtering
- GUI event systems
- Realtime synchronization
- Audio buffering
- Realtime visualization systems

---

# How To Run

## Install Dependencies

```bash
pip install numpy scipy matplotlib pyqtgraph PyQt5 sounddevice
```

---

# Run DSP Toolkit

```bash
python phase6_main.py
```

---

# Available Modes

```text
1. Synthetic Signal
2. Chirp Signal
3. Audio File
4. Live Microphone
```

---

# Realtime Visualization Modes

```text
1. Realtime Waveform
2. Realtime FFT Spectrum
3. Realtime Spectrogram
4. Full DSP Dashboard
```

---

# DSP Dashboard Features

The realtime DSP dashboard supports:

- Live waveform visualization
- Live FFT analysis
- Live spectrogram visualization
- Interactive DSP filters
- Realtime cutoff tuning
- GUI-based DSP controls
- Live audio recording
- Timestamped WAV export

---

# Recommended DSP Experiments

## Low-pass Filter

Try:

```text
1000 Hz
```

Observe:
- High frequencies disappear
- FFT compresses toward lower frequencies

---

## High-pass Filter

Try:

```text
2000 Hz
```

Observe:
- Low frequencies disappear
- Speech becomes sharper

---

## Band-pass Filter

Try:

```text
300 Hz → 3000 Hz
```

Observe:
- Speech frequencies become isolated
- Background frequencies disappear

---

# Key Achievements

Successfully built:

- Interactive realtime DSP workstation
- Unified DSP dashboard
- Professional realtime audio pipeline
- Interactive DSP control system
- Realtime FFT analyzer
- Realtime waterfall spectrogram
- Professional WAV recording system
- GUI-controlled DSP experimentation platform

This phase marks the transition from:

- Realtime DSP visualization

to:

- Professional interactive DSP software engineering.