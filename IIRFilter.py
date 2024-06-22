import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
import AudioRec

sec = 2
def IIRaudioPlot(sec):
   AudioRec.audioPlot(sec)
   times = AudioRec.times
   audio_array = AudioRec.audio_array

   def butter_bandpass(lowcut, highcut, fs, order = 5):
     nyq = 0.5*fs
     low = lowcut/nyq
     high = highcut/nyq
     b, a = butter(order, [low, high], btype='band')
     return b, a
  
   def apply_filter(data, lowcut, highcut, fs, order=5):
     b, a = butter_bandpass(lowcut, highcut, fs, order=order)
     y = lfilter(b, a, data)
     return y
  
   lowcut = 100
   highcut = 1000
   order = 4
   fs = 44100
   filtered_signal = apply_filter(audio_array, lowcut, highcut, fs, order=order)
   print("Filtered Signal: ", filtered_signal)
    
   plt.figure(figsize=(10, 6))
   plt.subplot(2, 1, 1)
   plt.plot(times, audio_array)
   plt.xlabel('Time (s)')
   plt.ylabel('Amplitude')
   plt.title('Original Audio Signal')
   plt.grid(True)

   plt.subplot(2, 1, 2)
   plt.plot(times, filtered_signal)
   plt.xlabel('Time (s)')
   plt.ylabel('Amplitude')
   plt.title('IIR Filtered Audio Signal')
   plt.xlim([0.5,0.8])
   plt.grid(True)
   plt.tight_layout()
   plt.show()
  