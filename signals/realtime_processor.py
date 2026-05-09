import numpy as np

from processing.filters import (

    lowpass_filter,

    highpass_filter,

    bandpass_filter
)


class RealtimeDSPProcessor:

    def __init__(

            self,

            sample_rate=44100
    ):

        self.sample_rate = sample_rate

        self.filter_type = None

        self.low_cutoff = 300

        self.high_cutoff = 3000


    def set_lowpass(

            self,

            cutoff
    ):

        self.filter_type = "lowpass"

        self.low_cutoff = cutoff


    def set_highpass(

            self,

            cutoff
    ):

        self.filter_type = "highpass"

        self.low_cutoff = cutoff


    def set_bandpass(

            self,

            lowcut,

            highcut
    ):

        self.filter_type = "bandpass"

        self.low_cutoff = lowcut

        self.high_cutoff = highcut


    def disable_filter(self):

        self.filter_type = None


    def process(

            self,

            audio_data
    ):

        if self.filter_type == "lowpass":

            return lowpass_filter(

                audio_data,

                self.low_cutoff,

                self.sample_rate
            )

        elif self.filter_type == "highpass":

            return highpass_filter(

                audio_data,

                self.low_cutoff,

                self.sample_rate
            )

        elif self.filter_type == "bandpass":

            return bandpass_filter(

                audio_data,

                self.low_cutoff,

                self.high_cutoff,

                self.sample_rate
            )

        return audio_data