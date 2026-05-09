import wave

import numpy as np


class AudioRecorder:

    def __init__(

            self,

            filename="recording.wav",

            sample_rate=44100,

            channels=1
    ):

        self.filename = filename

        self.sample_rate = sample_rate

        self.channels = channels

        self.frames = []

        self.is_recording = False


    def start_recording(self):

        self.frames = []

        self.is_recording = True

        print("\nRecording started...")


    def stop_recording(self):

        self.is_recording = False

        self.save_recording()

        print(
            f"\nRecording saved as {self.filename}"
        )


    def add_audio_data(

            self,

            data
    ):

        if not self.is_recording:

            return

        # =================================
        # Convert to numpy array
        # =================================

        data = np.array(data)

        # =================================
        # Ensure mono audio
        # =================================

        data = np.squeeze(data)

        # =================================
        # Clip safely
        # =================================

        data = np.clip(

            data,

            -1.0,

            1.0
        )

        # =================================
        # Convert float32 → int16 PCM
        # =================================

        audio_int16 = np.int16(

            data * 32767
        )

        # =================================
        # Store audio chunk
        # =================================

        self.frames.append(audio_int16)


    def save_recording(self):

        if len(self.frames) == 0:

            return

        # =================================
        # Merge all chunks
        # =================================

        audio_data = np.concatenate(
            self.frames
        )

        wf = wave.open(

            self.filename,

            'wb'
        )

        wf.setnchannels(
            self.channels
        )

        wf.setsampwidth(2)

        wf.setframerate(
            self.sample_rate
        )

        wf.writeframes(
            audio_data.tobytes()
        )

        wf.close()