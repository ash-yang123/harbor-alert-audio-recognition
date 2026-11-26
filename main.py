import numpy as np
import wave
from audio_processing import interpret_blasts, type_of_blast, chop

#update target_freq in other file
spf = wave.open("test_audio_files.wav", "r") # change for whichever file you want to test in test_audio_files folder

signal = spf.readframes(-1)
signal = np.frombuffer(signal, np.int16)
