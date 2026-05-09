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
            block_size
        )

        self.stream = None

        # =================================
        # Use Linux default microphone
        # =================================

        self.device_id = sd.default.device[0]

        print(
            f"\nUsing input device: "
            f"{self.device_id}"
        )


    def audio_callback(

            self,

            indata,

            frames,

            time,

            status
    ):

        if status:

            print(status)

        self.latest_audio = (
            indata[:, 0]
        )


    def start_stream(self):

        self.stream = sd.InputStream(

            samplerate=self.sample_rate,

            channels=self.channels,

            blocksize=self.block_size,

            callback=self.audio_callback,

            device=self.device_id
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