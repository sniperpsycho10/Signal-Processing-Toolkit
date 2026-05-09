import pyqtgraph as pg

from pyqtgraph.Qt import (
    QtWidgets,
    QtCore,
    QtGui
)

import numpy as np


class LiveSpectrogramPlot:

    def __init__(self, audio_input):

        self.audio_input = audio_input

        self.sample_rate = (
            self.audio_input.sample_rate
        )

        self.block_size = (
            self.audio_input.block_size
        )

        # =================================
        # Display only useful speech range
        # =================================

        self.max_frequency = 8000

        # =================================
        # FFT bins
        # =================================

        self.frequency_bins = (
            self.block_size // 2 + 1
        )

        # =================================
        # Frequency axis
        # =================================

        self.frequencies = np.fft.rfftfreq(

            self.block_size,

            d=1 / self.sample_rate
        )

        # =================================
        # Keep only useful frequencies
        # =================================

        self.valid_bins = np.where(

            self.frequencies <= self.max_frequency

        )[0]

        self.display_bins = len(
            self.valid_bins
        )

        # =================================
        # Waterfall buffer
        # =================================

        self.history_length = 300

        self.spectrogram_data = np.zeros(

            (
                self.history_length,

                self.display_bins
            )
        )

        # =================================
        # Qt Application
        # =================================

        self.app = QtWidgets.QApplication([])

        # =================================
        # Main Window
        # =================================

        self.window = pg.GraphicsLayoutWidget(

            title="Realtime Spectrogram"
        )

        self.window.resize(1200, 700)

        self.window.show()

        # =================================
        # Plot
        # =================================

        self.plot = self.window.addPlot(

            title="Realtime Waterfall Spectrogram"
        )

        self.plot.setLabel(

            'bottom',

            'Frequency',

            units='Hz'
        )

        self.plot.setLabel(

            'left',

            'Time Frames'
        )

        self.plot.showGrid(

            x=True,

            y=True
        )

        # =================================
        # Proper display range
        # =================================

        self.plot.setXRange(

            0,

            self.max_frequency
        )

        # =================================
        # Image item
        # =================================

        self.image = pg.ImageItem()

        self.plot.addItem(
            self.image
        )

        # =================================
        # Correct image scaling
        # =================================

        freq_resolution = (

            self.max_frequency

        ) / self.display_bins

        transform = QtGui.QTransform()

        transform.scale(

            freq_resolution,

            1
        )

        self.image.setTransform(
            transform
        )

        # =================================
        # Better colormap
        # =================================

        colormap = pg.colormap.get(
            'inferno'
        )

        self.image.setColorMap(
            colormap
        )

        # =================================
        # Update timer
        # =================================

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(
            self.update_plot
        )

        self.timer.start(40)


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
        # Stronger noise gate
        # =================================

        threshold = 0.04

        audio_data[
            np.abs(audio_data) < threshold
        ] = 0

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
        # Keep only useful bins
        # =================================

        magnitude = magnitude[
            self.valid_bins
        ]

        # =================================
        # dB scaling
        # =================================

        magnitude = 20 * np.log10(
            magnitude + 1e-6
        )

        # =================================
        # Better dynamic range
        # =================================

        magnitude = np.clip(

            magnitude,

            -55,

            -15
        )

        # =================================
        # Normalize
        # =================================

        magnitude = (

            magnitude + 55

        ) / 40

        # =================================
        # Shift waterfall
        # =================================

        self.spectrogram_data[:-1] = (

            self.spectrogram_data[1:]
        )

        # =================================
        # Add newest FFT row
        # =================================

        self.spectrogram_data[-1] = (
            magnitude
        )

        # =================================
        # Update image
        # =================================

        self.image.setImage(

            self.spectrogram_data.T,

            autoLevels=False,

            levels=(0, 1)
        )


    def start(self):

        QtWidgets.QApplication.instance().exec_()