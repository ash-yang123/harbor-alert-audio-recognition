
# Harbor-Alert-Audio-Recognition

## Overview 

Harbor Alert Audio Recognition is a project that uses audio processing to identify and classify different harbor alert signals for the RoboBoat competition. The goal is to identify various frequencies and specific patterns and determine which alert they represent. 

## How it Works

This program processes a WAV file through a couple of different steps:

1. Opens a WAV file and converts the audio file into a NumPy array.
2. Identifies peaks (frequencies) of segments from the array using the Fast Fourier Transform (FFT) algorithm within a 5% accuracy.
3. Classifies each 0.1 second segment as silence or the target frequency
4. Groups together consecutive segments with the same classification (blast or silence).  
5. Looks at the sequence and then determines whether or not a programmed pattern was detected.

## Recognized Signal Patterns

**One Blast Signal**: 1 second blast followed by 2 seconds of silence.
<img width="636" height="477" alt="Screenshot 2026-11-24 at 11 19 46 PM" src="https://github.com/user-attachments/assets/35743d43-6a7f-44c6-abae-44a5aa5d8128" />

**Two Blast Signal**: 0.5 second blast, 0.5 seconds of silence, 0.5 second blast, and then 2 seconds of silence.
<img width="637" height="478" alt="Screenshot 2026-11-24 at 11 20 38 PM" src="https://github.com/user-attachments/assets/a7162b4c-af19-47e3-b8c3-16f33ed80aad" />

## Files

- **main.py**: Reads a WAV recording and runs it through the audio recognition pipeline
- **synthetic_audio.py**: Creates a synthetic audio with adjustable frequency, gap or no gap, repeats, and time of blasts.
- **audio_processing.py**: Has peak finding, segmentation, and classification of blasts functions.












