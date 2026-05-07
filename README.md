# 📡 Signal Processing Toolkit

A modular Python-based Digital Signal Processing (DSP) toolkit for signal generation, visualization, filtering, FFT analysis, spectrograms, and real-time audio processing.

---

# 🚀 Project Goal

This project aims to simulate a real-world DSP workstation capable of:

- Generating signals
- Visualizing waveforms
- Performing FFT analysis
- Filtering noise
- Processing real audio
- Displaying spectrograms
- Supporting real-time microphone input
- Building a professional DSP dashboard GUI

---

# ✅ Current Phase

## Phase 1 — Signal Generation & Visualization

Completed features:

- Time axis generation
- Sine wave generation
- Noise simulation
- Time-domain plotting
- Modular project structure

---

# 🧠 DSP Concepts Covered

## 1. Signals

A signal represents information changing over time.

Examples:
- Audio signals
- Sensor signals
- Wireless communication signals
- ECG signals

---

## 2. Time Domain

Signals are currently visualized in the time domain:

- X-axis → Time
- Y-axis → Amplitude

---

## 3. Sine Waves

Core signal equation:

x(t) = A sin(2πft)

Where:
- A = amplitude
- f = frequency
- t = time

---

## 4. Noise

Random noise is added to simulate real-world signal disturbances such as:
- microphone interference
- electrical noise
- communication noise

---

# 📂 Project Structure

```text
signal_processing_toolkit/
│
├── signals/
│   └── generator.py
│
├── visualization/
│   └── plots.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📦 Libraries Used

| Library | Purpose |
|---|---|
| NumPy | Signal generation & math |
| Matplotlib | Visualization |
| SciPy | DSP utilities |

---

# ▶️ How to Run

## 1. Clone repository

```bash
git clone https://github.com/sniperpsycho10/Signal-Processing-Toolkit.git
```

## 2. Enter project directory

```bash
cd Signal-Processing-Toolkit
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run project

```bash
python main.py
```

---

# 📊 Current Output

The application currently generates:

- Clean sine wave
- Noisy sine wave

and visualizes them using time-domain plots.

---

# 🚀 Future Roadmap

## ✅ Phase 2
FFT & Frequency Analysis

## ✅ Phase 3
Signal Filtering System

## ✅ Phase 4
Spectrogram Visualization

## ✅ Phase 5
Audio File Processing

## ✅ Phase 6
Real-Time Microphone DSP

## ✅ Phase 7
Professional GUI Dashboard

---

# 🎯 Long-Term Vision

Final application goals:

- Real-time DSP workstation
- Interactive GUI dashboard
- Audio filtering & denoising
- Real-time FFT analysis
- Spectrogram visualization
- Communication signal analysis

---

# 🏢 Real-World Applications

- Audio Processing
- Wireless Communication
- Embedded Systems
- Biomedical Signal Processing
- Radar & RF Systems
- Speech Processing

---

# 📌 Status

✅ Phase 1 Completed