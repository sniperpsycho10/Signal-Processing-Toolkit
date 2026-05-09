import pyqtgraph as pg

from pyqtgraph.Qt import (
    QtWidgets,
    QtCore
)

import numpy as np


class LiveFFTPlot:

    def __init__(self, audio_input):

        self.audio_input = audio_input

        self.sample_rate = (
            self.audio_input.sample_rate
        )

        self.block_size = (
            self.audio_input.block_size
        )

        # =================================
        # Frequency axis
        # =================================

        self.frequencies = np.fft.rfftfreq(

            self.block_size,

            d=1 / self.sample_rate
        )

        # =================================
        # FFT smoothing buffer
        # =================================

        self.smoothed_fft = np.zeros(
            len(self.frequencies)
        )

        # =================================
        # Create Qt app
        # =================================

        self.app = QtWidgets.QApplication([])

        # =================================
        # Main window
        # =================================

        self.window = pg.GraphicsLayoutWidget(

            title="Realtime FFT Spectrum"
        )

        self.window.resize(1200, 600)

        self.window.show()

        # =================================
        # Plot
        # =================================

        self.plot = self.window.addPlot(

            title="Realtime Frequency Spectrum"
        )

        self.plot.setLabel(

            'bottom',

            'Frequency',

            units='Hz'
        )

        self.plot.setLabel(

            'left',

            'Magnitude (dB)'
        )

        self.plot.showGrid(

            x=True,

            y=True
        )

        # =================================
        # Better voice-focused range
        # =================================

        self.plot.setXRange(

            0,

            5000
        )

        self.plot.setYRange(

            -80,

            0
        )

        # =================================
        # FFT curve
        # =================================

        self.curve = self.plot.plot(
            pen='y'
        )

        # =================================
        # Timer
        # =================================

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(
            self.update_plot
        )

        self.timer.start(30)


    def update_plot(self):

        audio_data = (
            self.audio_input.get_latest_audio()
        )

        # =================================
        # Remove DC offset
        # =================================

        audio_data = (
            audio_data - np.mean(audio_data)
        )

        # =================================
        # Gentle normalization
        # =================================

        max_val = np.max(
            np.abs(audio_data)
        ) + 1e-6

        audio_data = (
            audio_data / max_val
        )

        # =================================
        # Hann window
        # =================================

        window = np.hanning(
            len(audio_data)
        )

        audio_data = (
            audio_data * window
        )

        # =================================
        # FFT
        # =================================

        fft_data = np.fft.rfft(
            audio_data
        )

        magnitude = np.abs(
            fft_data
        )

        # =================================
        # dB scaling
        # =================================

        magnitude = 20 * np.log10(
            magnitude + 1e-6
        )

        # =================================
        # Stable clipping
        # =================================

        magnitude = np.clip(

            magnitude,

            -80,

            0
        )

        # =================================
        # STRONGER smoothing
        # =================================

        alpha = 0.93

        self.smoothed_fft = (

            alpha * self.smoothed_fft +

            (1 - alpha) * magnitude
        )

        # =================================
        # Update graph
        # =================================

        self.curve.setData(

            self.frequencies,

            self.smoothed_fft
        )


    def start(self):

        QtWidgets.QApplication.instance().exec_()