import sys

import numpy as np

import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QTimer


class LiveFFTPlot:

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

            title="Realtime FFT Spectrum"
        )

        self.window.resize(1200, 600)

        self.plot = self.window.addPlot(

            title="Realtime Frequency Spectrum"
        )

        self.plot.showGrid(x=True, y=True)

        self.plot.setLabel(

            'left',

            'Magnitude (dB)'
        )

        self.plot.setLabel(

            'bottom',

            'Frequency (Hz)'
        )

        self.plot.setXRange(

            0,

            8000
        )

        self.plot.setYRange(-100, 10)

        self.curve = self.plot.plot(

            pen='y'
        )

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

        fft_data = np.fft.rfft(data)

        magnitude = np.abs(fft_data)

        magnitude = 20 * np.log10(

            magnitude + 1e-6
        )

        frequencies = np.fft.rfftfreq(

            len(data),

            1 / self.sample_rate
        )

        self.curve.setData(

            frequencies,

            magnitude
        )


    def start(self):

        self.window.show()

        sys.exit(self.app.exec_())