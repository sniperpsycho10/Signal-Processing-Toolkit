import sys

import numpy as np

import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import QTimer


class LiveWaveformPlot:

    def __init__(

            self,

            audio_input,

            processor=None
    ):

        self.audio_input = audio_input

        self.processor = processor

        self.app = QApplication(sys.argv)

        self.window = pg.GraphicsLayoutWidget(

            title="Realtime DSP Waveform"
        )

        self.window.resize(1200, 600)

        self.plot = self.window.addPlot(

            title="Live Microphone Waveform"
        )

        self.plot.showGrid(x=True, y=True)

        self.plot.setLabel(

            'left',

            'Amplitude'
        )

        self.plot.setLabel(

            'bottom',

            'Samples'
        )

        self.plot.setYRange(-1, 1)

        self.curve = self.plot.plot(
            pen='c'
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
        # Remove DC offset
        # =================================

        data = data - np.mean(data)

        # =================================
        # Normalize
        # =================================

        max_val = np.max(
            np.abs(data)
        ) + 1e-6

        data = (
            data / max_val
        ) * 0.8

        self.curve.setData(data)


    def start(self):

        self.window.show()

        sys.exit(self.app.exec_())