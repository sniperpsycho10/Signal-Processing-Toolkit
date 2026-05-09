import sys

import time

import numpy as np

import pyqtgraph as pg

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QComboBox
)

from PyQt5.QtCore import Qt, QTimer

from PyQt5 import QtGui


class LiveDSPDashboard:

    def __init__(
            self,
            audio_input,
            processor=None,
            recorder=None
    ):

        self.audio_input = audio_input

        self.processor = processor

        self.recorder = recorder

        self.sample_rate = audio_input.sample_rate

        self.fft_size = 1024

        self.history_length = 150

        self.recording_start_time = None

        # =================================
        # Qt App
        # =================================

        self.app = QApplication(sys.argv)

        # =================================
        # Main Window
        # =================================

        self.window = QWidget()

        self.window.setWindowTitle(
            "Interactive DSP Workstation"
        )

        self.window.resize(1500, 1000)

        # =================================
        # Main Layout
        # =================================

        self.main_layout = QHBoxLayout()

        self.window.setLayout(
            self.main_layout
        )

        # =================================
        # LEFT CONTROL PANEL
        # =================================

        self.control_panel = QVBoxLayout()

        self.main_layout.addLayout(
            self.control_panel,
            1
        )

        # =================================
        # RIGHT VISUALIZATION PANEL
        # =================================

        self.graphics = pg.GraphicsLayoutWidget()

        self.main_layout.addWidget(
            self.graphics,
            4
        )

        # =================================
        # RECORDING STATUS
        # =================================

        self.recording_status = QLabel(
            "● Not Recording"
        )

        self.control_panel.addWidget(
            self.recording_status
        )

        # =================================
        # RECORDING TIMER
        # =================================

        self.recording_timer = QLabel(
            "00:00:00"
        )

        self.control_panel.addWidget(
            self.recording_timer
        )

        # =================================
        # START RECORD BUTTON
        # =================================

        self.start_button = QPushButton(
            "Start Recording"
        )

        self.control_panel.addWidget(
            self.start_button
        )

        self.start_button.clicked.connect(
            self.start_recording
        )

        # =================================
        # STOP RECORD BUTTON
        # =================================

        self.stop_button = QPushButton(
            "Stop Recording"
        )

        self.control_panel.addWidget(
            self.stop_button
        )

        self.stop_button.clicked.connect(
            self.stop_recording
        )

        # =================================
        # FILTER TYPE
        # =================================

        self.filter_label = QLabel(
            "Filter Type"
        )

        self.control_panel.addWidget(
            self.filter_label
        )

        self.filter_selector = QComboBox()

        self.filter_selector.addItems([
            "No Filter",
            "Low-pass",
            "High-pass",
            "Band-pass"
        ])

        self.control_panel.addWidget(
            self.filter_selector
        )

        self.filter_selector.currentIndexChanged.connect(
            self.update_filter
        )

        # =================================
        # LOW CUTOFF
        # =================================

        self.low_label = QLabel(
            "Low Cutoff: 1000 Hz"
        )

        self.control_panel.addWidget(
            self.low_label
        )

        self.low_slider = QSlider(Qt.Horizontal)

        self.low_slider.setMinimum(50)

        self.low_slider.setMaximum(8000)

        self.low_slider.setValue(1000)

        self.control_panel.addWidget(
            self.low_slider
        )

        self.low_slider.valueChanged.connect(
            self.update_filter
        )

        # =================================
        # HIGH CUTOFF
        # =================================

        self.high_label = QLabel(
            "High Cutoff: 3000 Hz"
        )

        self.control_panel.addWidget(
            self.high_label
        )

        self.high_slider = QSlider(Qt.Horizontal)

        self.high_slider.setMinimum(100)

        self.high_slider.setMaximum(12000)

        self.high_slider.setValue(3000)

        self.control_panel.addWidget(
            self.high_slider
        )

        self.high_slider.valueChanged.connect(
            self.update_filter
        )

        # =================================
        # RESET BUTTON
        # =================================

        self.reset_button = QPushButton(
            "Reset Filter"
        )

        self.control_panel.addWidget(
            self.reset_button
        )

        self.reset_button.clicked.connect(
            self.reset_filter
        )

        # =================================
        # WAVEFORM PANEL
        # =================================

        self.waveform_plot = self.graphics.addPlot(
            title="Realtime Waveform"
        )

        self.waveform_plot.showGrid(
            x=True,
            y=True
        )

        self.waveform_plot.setYRange(-1, 1)

        self.waveform_curve = self.waveform_plot.plot(
            pen='c'
        )

        # =================================
        # FFT PANEL
        # =================================

        self.graphics.nextRow()

        self.fft_plot = self.graphics.addPlot(
            title="Realtime FFT Spectrum"
        )

        self.fft_plot.showGrid(
            x=True,
            y=True
        )

        self.fft_plot.setXRange(0, 8000)

        self.fft_plot.setYRange(-100, 10)

        self.fft_curve = self.fft_plot.plot(
            pen='y'
        )

        # =================================
        # SPECTROGRAM PANEL
        # =================================

        self.graphics.nextRow()

        self.spectrogram_plot = self.graphics.addPlot(
            title="Realtime Spectrogram"
        )

        self.spectrogram_image = pg.ImageItem()

        self.spectrogram_plot.addItem(
            self.spectrogram_image
        )

        self.spectrogram_data = np.zeros(
            (
                self.history_length,
                self.fft_size // 2 + 1
            )
        )

        colormap = pg.colormap.get(
            'inferno'
        )

        self.spectrogram_image.setLookupTable(
            colormap.getLookupTable()
        )

        self.spectrogram_image.setLevels(
            [-80, 0]
        )

        transform = QtGui.QTransform()

        transform.scale(
            self.sample_rate / self.fft_size,
            1
        )

        self.spectrogram_image.setTransform(
            transform
        )

        # =================================
        # TIMER
        # =================================

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_dashboard
        )

        self.timer.start(60)


    def start_recording(self):

        if self.recorder is None:

            return

        self.recorder.start_recording()

        self.recording_start_time = time.time()

        self.recording_status.setText(
            "● Recording"
        )


    def stop_recording(self):

        if self.recorder is None:

            return

        self.recorder.stop_recording()

        self.recording_status.setText(
            "● Not Recording"
        )

        self.recording_timer.setText(
            "00:00:00"
        )


    def update_filter(self):

        if self.processor is None:

            return

        filter_type = self.filter_selector.currentText()

        low_cutoff = self.low_slider.value()

        high_cutoff = self.high_slider.value()

        self.low_label.setText(
            f"Low Cutoff: {low_cutoff} Hz"
        )

        self.high_label.setText(
            f"High Cutoff: {high_cutoff} Hz"
        )

        if filter_type == "No Filter":

            self.processor.disable_filter()

        elif filter_type == "Low-pass":

            self.processor.set_lowpass(
                low_cutoff
            )

        elif filter_type == "High-pass":

            self.processor.set_highpass(
                low_cutoff
            )

        elif filter_type == "Band-pass":

            self.processor.set_bandpass(
                low_cutoff,
                high_cutoff
            )


    def reset_filter(self):

        self.filter_selector.setCurrentIndex(0)

        self.low_slider.setValue(1000)

        self.high_slider.setValue(3000)


    def update_dashboard(self):

        data = self.audio_input.get_latest_audio()

        if data is None:

            return

        # =================================
        # RECORD TIMER
        # =================================

        if (
            self.recorder is not None
            and self.recorder.is_recording
            and self.recording_start_time
        ):

            elapsed = int(
                time.time() -
                self.recording_start_time
            )

            hours = elapsed // 3600

            minutes = (
                elapsed % 3600
            ) // 60

            seconds = elapsed % 60

            self.recording_timer.setText(
                f"{hours:02}:{minutes:02}:{seconds:02}"
            )

        # =================================
        # APPLY FILTER
        # =================================

        if self.processor is not None:

            data = self.processor.process(data)

        # =================================
        # REMOVE DC OFFSET
        # =================================

        data = data - np.mean(data)

        # =================================
        # NORMALIZE
        # =================================

        max_val = np.max(
            np.abs(data)
        ) + 1e-6

        normalized = (
            data / max_val
        ) * 0.8

        # =================================
        # UPDATE WAVEFORM
        # =================================

        self.waveform_curve.setData(
            normalized
        )

        # =================================
        # FFT
        # =================================

        window = np.hanning(
            len(data)
        )

        fft_input = data * window

        fft_data = np.fft.rfft(
            fft_input,
            n=self.fft_size
        )

        magnitude = np.abs(fft_data)

        magnitude_db = 20 * np.log10(
            magnitude + 1e-6
        )

        frequencies = np.fft.rfftfreq(
            self.fft_size,
            1 / self.sample_rate
        )

        self.fft_curve.setData(
            frequencies,
            magnitude_db
        )

        # =================================
        # SPECTROGRAM
        # =================================

        magnitude_db = np.clip(
            magnitude_db,
            -80,
            0
        )

        self.spectrogram_data = np.roll(
            self.spectrogram_data,
            -1,
            axis=0
        )

        self.spectrogram_data[-1, :] = (
            magnitude_db
        )

        self.spectrogram_image.setImage(
            self.spectrogram_data,
            autoLevels=False
        )


    def start(self):

        self.window.show()

        sys.exit(self.app.exec_())