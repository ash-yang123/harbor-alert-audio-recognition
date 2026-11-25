import numpy as np
import wave
from harbor_alert_with_fake_audio import interpret_blasts, type_of_blast, chop

#update target_freq in other file
spf = wave.open("800Hz_1blast_loop3.wav", "r")

signal = spf.readframes(-1)
signal = np.frombuffer(signal, np.int16)
