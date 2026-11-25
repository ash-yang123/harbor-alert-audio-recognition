import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 44100 #data points per second
target_freq = 800 #target frequency

def sound(freq, gap, num_repeats, blast_time):
    signal = []
    t = np.linspace(0,blast_time,int(sampling_rate*blast_time))
    tone = np.sin(2*np.pi*freq*t)
    
    #add different silences
    silence05 = np.zeros(int(sampling_rate/2))
    silence2 = np.zeros(int(sampling_rate*2))
    
    signal = []
    if gap:
        signal = np.concatenate([tone, silence05, tone, silence2]) 
    else:
        signal = np.concatenate([tone, silence2])        
    repeatSignal = []
    
    for i in range(num_repeats):
        repeatSignal = np.concatenate([repeatSignal, signal])
        
    repeatSignal = repeatSignal + np.random.normal(0, 0.1, len(repeatSignal)) #adds the gaussion noise to better simulate the real world

    #plots the synthetic audio (optional)
    plt.plot(repeatSignal)
    plt.show()
    
    return repeatSignal
    
