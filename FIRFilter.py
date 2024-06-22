import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter
import AudioRec

sec = 2
def FIRaudioPlot(sec):
   AudioRec.audioPlot(sec)
   times = AudioRec.times
   audio_array = AudioRec.audio_array

   sample_frequency = 16000
   nyq = 0.5*sample_frequency
   cutoff = 1000
   num_taps = 101
   b = firwin(num_taps, cutoff/nyq)
   filtered_signal = lfilter(b, 1.0, audio_array)
   print("Filtered Signal: ", filtered_signal)

   # F1 = 470
   # F2 = 3200

   # tap = 21
   # fc = [(F1+F2)/2]
   # win = 'hann'
   # h = firwin(tap, fc, pass_zero='lowpass', window=win, fs=sample_frequency)
   # b = h
   # a = [1]
   # y_lpf = lfilter(b, a, audio_array)
    
   plt.figure(figsize=(10, 6))
   plt.subplot(2, 1, 1)
   plt.plot(times, audio_array)
   plt.xlabel('Time (s)')
   plt.ylabel('Amplitude')
   plt.title('Original Audio Signal')
   plt.grid(True)

   plt.subplot(2, 1, 2)
   plt.plot(times, filtered_signal)
   # plt.plot(times, y_lpf)
   plt.xlabel('Time (s)')
   plt.ylabel('Amplitude')
   plt.title('FIR Filtered Audio Signal')
   plt.xlim([0.5,0.8])
   plt.grid(True)
   plt.tight_layout()
   plt.show()
  