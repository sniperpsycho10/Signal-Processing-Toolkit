import numpy as np

from scipy.signal import butter, lfilter


def butter_lowpass(

        cutoff,

        sample_rate,

        order=5
):

    nyquist = 0.5 * sample_rate

    normal_cutoff = cutoff / nyquist

    b, a = butter(

        order,

        normal_cutoff,

        btype='low',

        analog=False
    )

    return b, a


def lowpass_filter(

        data,

        cutoff,

        sample_rate,

        order=5
):

    b, a = butter_lowpass(

        cutoff,

        sample_rate,

        order
    )

    filtered = lfilter(

        b,

        a,

        data
    )

    return filtered


def butter_highpass(

        cutoff,

        sample_rate,

        order=5
):

    nyquist = 0.5 * sample_rate

    normal_cutoff = cutoff / nyquist

    b, a = butter(

        order,

        normal_cutoff,

        btype='high',

        analog=False
    )

    return b, a


def highpass_filter(

        data,

        cutoff,

        sample_rate,

        order=5
):

    b, a = butter_highpass(

        cutoff,

        sample_rate,

        order
    )

    filtered = lfilter(

        b,

        a,

        data
    )

    return filtered


def butter_bandpass(

        lowcut,

        highcut,

        sample_rate,

        order=5
):

    nyquist = 0.5 * sample_rate

    low = lowcut / nyquist

    high = highcut / nyquist

    b, a = butter(

        order,

        [low, high],

        btype='band'
    )

    return b, a


def bandpass_filter(

        data,

        lowcut,

        highcut,

        sample_rate,

        order=5
):

    b, a = butter_bandpass(

        lowcut,

        highcut,

        sample_rate,

        order
    )

    filtered = lfilter(

        b,

        a,

        data
    )

    return filtered