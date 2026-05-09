import pyqtgraph as pg

from pyqtgraph.Qt import (
    QtWidgets,
    QtCore
)

import numpy as np


class LiveWaveformPlot:

    def __init__(self, audio_input):

        self.audio_input = audio_input

        self.app = QtWidgets.QApplication([])

        self.window = pg.GraphicsLayoutWidget(

            title="Realtime DSP Waveform"
        )

        self.window.resize(1200, 600)

        self.window.show()

        self.plot = self.window.addPlot(

            title="Realtime Microphone Waveform"
        )

        self.plot.setLabel(
            'bottom',
            'Samples'
        )

        self.plot.setLabel(
            'left',
            'Amplitude'
        )

        self.plot.showGrid(
            x=True,
            y=True
        )

        self.plot.setYRange(
            -1,
            1
        )

        self.curve = self.plot.plot(
            pen='c'
        )

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(
            self.update_plot
        )

        self.timer.start(20)


    def update_plot(self):

        audio_data = (
            self.audio_input.get_latest_audio()
        )

        # Remove DC offset
        audio_data = (
            audio_data - np.mean(audio_data)
        )

        # Normalize
        max_val = np.max(
            np.abs(audio_data)
        ) + 1e-6

        audio_data = (
            audio_data / max_val
        ) * 0.8

        self.curve.setData(
            audio_data
        )


    def start(self):

        QtWidgets.QApplication.instance().exec_()