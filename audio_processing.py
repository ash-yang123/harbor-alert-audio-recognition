import numpy as np
import scipy

sampling_rate = 44100 # data points per second
target_freq = 800 # target frequency

# finds the peak (frequency) of the audio clip inputted
def peak(audio_clip):
    hz = np.fft.rfftfreq(len(audio_clip), 1 / sampling_rate)
    spectrum = np.abs(np.fft.rfft(audio_clip))
    peak_index, prop = scipy.signal.find_peaks(spectrum, threshold = max(spectrum)/1.1)
    
    freq_peaks = []
    for index in peak_index:
        freq_peaks.append(hz[int(index)])
      
    for i in freq_peaks:
        if np.abs(target_freq - i) <= target_freq * 0.05:
            return True
    return False  

# divides the audio sample into 0.1 second clips
def chop(audio):
    n = int(sampling_rate/10)
    pieces = [audio[i:i + n] for i in range(0, len(audio), n)]
    # plt.plot(pieces[0])
    # plt.show()
    outputs = []
    
    for piece in pieces:
            outputs.append(peak(piece))
    return outputs

# groups together consecutive audio segments and classifies them as beeps or silences
def type_of_blast(outputs):
    events = []
    current_type = outputs[0]
    duration_counter = 0
    for value in outputs:
        if value == current_type:
            duration_counter += 1
        else:
            seconds = duration_counter * 0.1
            if current_type == True:
                if np.abs(seconds - 0.5) <= 0.2: # 0.2 margin of error (maybe change later after testing with real mic)
                    events.append('0.5 sec beep')
                elif np.abs(seconds - 1) <= 0.2:
                    events.append('1 sec beep')
            elif current_type == False:
                if np.abs(seconds - 0.5) <= 0.2:
                    events.append('0.5 sec silence')
                elif np.abs(seconds - 2) <= 0.2:
                    events.append('2 sec silence')
            
            current_type = value
            duration_counter = 1
            
    # repeats from above to make sure to add the last part of outputs
            
    seconds = duration_counter * 0.1

    if current_type == True:
        if np.abs(seconds - 0.5) <= 0.2:
            events.append('0.5 sec beep')
        elif np.abs(seconds - 1) <= 0.2:
            events.append('1 sec beep')

    elif current_type == False:
        if np.abs(seconds - 0.5) <= 0.2:
            events.append('0.5 sec silence')
        elif np.abs(seconds - 2) <= 0.2:
            events.append('2 sec silence')
    return events   

# recognizes whether or not the pattern was detected and which one
def interpret_blasts(events):
    for i in range(len(events)):
        if events[i] == '0.5 sec beep':
            if events[i + 1] == '0.5 sec silence':
                if events[i + 2] == '0.5 sec beep':
                    if events[i + 3] == '2 sec silence':
                        return 'two blast signal'
        elif events[i] == '1 sec beep':
            if events[i + 1] == '2 sec silence':
                if events[i - 1] == '2 sec silence':
                    return '1 blast signal'

