import sounddevice as sd

import numpy as np


class RealTimeAudioInput:

    def __init__(

            self,

            sample_rate=44100,

            channels=1,

            block_size=1024
    ):

        self.sample_rate = sample_rate

        self.channels = channels

        self.block_size = block_size

        self.latest_audio = np.zeros(
            block_size,
            dtype=np.float32
        )

        self.stream = None

        self.recorder = None


    def audio_callback(

            self,

            indata,

            frames,

            time,

            status
    ):

        if status:

            print(status)

        # =================================
        # Convert to mono
        # =================================

        audio_data = indata[:, 0].copy()

        # =================================
        # Store latest audio
        # =================================

        self.latest_audio = audio_data

        # =================================
        # Recording support
        # =================================

        if self.recorder is not None:

            self.recorder.add_audio_data(
                audio_data
            )


    def start_stream(self):

        self.stream = sd.InputStream(

            samplerate=self.sample_rate,

            channels=self.channels,

            blocksize=self.block_size,

            callback=self.audio_callback
        )

        self.stream.start()

        print(
            "\nRealtime microphone stream started..."
        )


    def stop_stream(self):

        if self.stream is not None:

            self.stream.stop()

            self.stream.close()

            print(
                "\nRealtime microphone stream stopped."
            )


    def get_latest_audio(self):

        return self.latest_audio