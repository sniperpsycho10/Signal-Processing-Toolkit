# Phase 6 – Real-Time Interactive DSP System

## Overview

Phase 6 transforms the Signal Processing Toolkit from an offline DSP application into a real-time interactive DSP workstation.

This phase introduces:

- Real-time microphone signal acquisition
- Live waveform visualization
- Real-time FFT spectrum analysis
- Live waterfall spectrogram visualization
- PyQtGraph accelerated rendering
- Zooming and panning support
- Integrated DSP toolkit combining:
  - Synthetic signals
  - Chirp signals
  - Audio file processing
  - Live microphone DSP

The toolkit now supports both:

- Offline DSP analysis
- Real-time DSP visualization

similar to professional:
- Oscilloscopes
- Spectrum analyzers
- SDR (Software Defined Radio) tools
- Audio analysis software

---

# Features Implemented

## 1. Real-Time Microphone Processing

Implemented a real-time audio streaming system using:

- `sounddevice`
- Callback-based audio capture
- Streaming audio buffers

Features:
- Automatic Linux default microphone handling
- Support for:
  - Laptop microphone
  - Wired 3.5mm headset microphone
  - External audio devices

---

## 2. Real-Time Waveform Visualization

Implemented a live waveform viewer using:

- `PyQtGraph`
- Real-time GUI rendering
- Continuous waveform updates

Features:
- Live amplitude vs time display
- Smooth rendering
- Zooming support
- Panning support
- Low-latency visualization

---

## 3. Real-Time FFT Spectrum Analyzer

Implemented a real-time frequency spectrum analyzer.

Features:
- Real-time FFT computation
- Frequency-domain visualization
- dB-scaled magnitude display
- FFT smoothing
- Hann window preprocessing
- DC offset removal

This allows:
- Voice frequency analysis
- Harmonic visualization
- Real-time spectral analysis

---

## 4. Real-Time Waterfall Spectrogram

Implemented a live scrolling spectrogram system.

Features:
- Waterfall frequency visualization
- Time-frequency analysis
- Real-time spectrogram updates
- Inferno color mapping
- Noise gating
- Dynamic range tuning

This visualizes:
- Speech harmonics
- Whistling frequencies
- Frequency changes over time

---

## 5. DSP Signal Conditioning

Added professional DSP preprocessing techniques:

### Implemented:
- DC offset removal
- Hann windowing
- FFT smoothing
- Noise gating
- Dynamic range clipping
- dB scaling

These significantly improve:
- FFT stability
- Spectrogram clarity
- Noise suppression

---

## 6. PyQtGraph Accelerated Rendering

Migrated real-time visualization from:
- Matplotlib

to:
- PyQtGraph

Benefits:
- Faster rendering
- Smooth GUI interaction
- Realtime responsiveness
- Built-in zooming and panning

---

## 7. Unified DSP Toolkit

Integrated all previous phases into one unified launcher.

The toolkit now supports:

### Offline DSP
- Synthetic multi-frequency signals
- Chirp signal generation
- Audio file analysis (.wav/.mp3)

### Real-Time DSP
- Live microphone waveform
- Live FFT spectrum
- Live spectrogram

---

# Project Architecture

signal_processing_toolkit/

│── signals/  
│   ├── generator.py  
│   ├── audio_loader.py  
│   ├── real_time_input.py  

│── processing/  
│   ├── fft_analysis.py  
│   ├── spectrogram.py  

│── visualization/  
│   ├── plots.py  
│   ├── live_graphs.py  
│   ├── live_fft.py  
│   ├── live_spectrogram.py  

│── phase6_main.py  

---

# Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib
- PyQtGraph
- PyQt5
- SoundDevice

---

# Real-Time DSP Concepts Learned

This phase introduced important DSP engineering concepts:

- Streaming DSP
- Audio buffering
- Callback systems
- Real-time FFT analysis
- Waterfall spectrograms
- Time-frequency analysis
- GUI rendering systems
- Low-latency visualization
- Signal conditioning
- Dynamic range control

---

# How to Run

## Install Dependencies

```bash
pip install numpy scipy matplotlib pyqtgraph PyQt5 sounddevice