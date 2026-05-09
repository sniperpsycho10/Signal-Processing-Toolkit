import sys

import numpy as np

import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QTimer

from PyQt5 import QtGui


class LiveSpectrogramPlot:

    def __init__(

            self,

            audio_input,

            processor=None
    ):

        self.audio_input = audio_input

        self.processor = processor

        self.sample_rate = audio_input.sample_rate

        self.app = QApplication(sys.argv)

        self.window = pg.GraphicsLayoutWidget(

            title="Realtime Spectrogram"
        )

        self.window.resize(1200, 700)

        self.plot = self.window.addPlot(

            title="Realtime Waterfall Spectrogram"
        )

        self.plot.setLabel(

            'left',

            'Time Frames'
        )

        self.plot.setLabel(

            'bottom',

            'Frequency (Hz)'
        )

        self.image = pg.ImageItem()

        self.plot.addItem(self.image)

        self.history_length = 150

        self.fft_size = 2048

        self.spectrogram = np.zeros(

            (

                self.history_length,

                self.fft_size // 2 + 1
            )
        )

        colormap = pg.colormap.get(

            'inferno'
        )

        self.image.setLookupTable(

            colormap.getLookupTable()
        )

        self.image.setLevels(

            [-80, 0]
        )

        transform = QtGui.QTransform()

        transform.scale(

            self.sample_rate / self.fft_size,

            1
        )

        self.image.setTransform(transform)

        self.timer = QTimer()

        self.timer.timeout.connect(

            self.update
        )

        self.timer.start(60)


    def update(self):

        data = self.audio_input.get_latest_audio()

        if data is None:

            return

        if self.processor is not None:

            data = self.processor.process(data)

        # =================================
        # Recorder support
        # =================================

        if hasattr(self, 'recorder'):

            self.recorder.add_audio_data(data)

        # =================================
        # Remove DC offset
        # =================================

        data = data - np.mean(data)

        # =================================
        # Hann window
        # =================================

        window = np.hanning(len(data))

        data = data * window

        # =================================
        # FFT
        # =================================

        fft_data = np.fft.rfft(

            data,

            n=self.fft_size
        )

        magnitude = np.abs(fft_data)

        magnitude = 20 * np.log10(

            magnitude + 1e-6
        )

        magnitude = np.clip(

            magnitude,

            -80,

            0
        )

        self.spectrogram = np.roll(

            self.spectrogram,

            -1,

            axis=0
        )

        self.spectrogram[-1, :] = magnitude

        self.image.setImage(

            self.spectrogram,

            autoLevels=False
        )


    def start(self):

        self.window.show()

        sys.exit(self.app.exec_())