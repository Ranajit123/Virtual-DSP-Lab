import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter, firwin
epsilon = 1e-9

Fs = 16000
F1 = 470
F2 = 3200
Td = 10e-3
n = np.arange(0, int(Td*Fs))
signal = np.sin(2*np.pi*F1*n/Fs) + np.sin(2*np.pi*F2*n/Fs)

tap = 21
fc = [(F1+F2)/2]
win = 'hann'
h = firwin(tap, fc, pass_zero='lowpass', window=win, fs=Fs)
b = h
a = [1]

y_lpf = lfilter(b, a, signal)

plt.figure(figsize=(8, 4))
plt.subplot(2, 1, 1)
plt.plot(n, signal)
plt.title('Input signal of LPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')

plt.subplot(2, 1, 2)
plt.plot(n, y_lpf)
plt.title('Output signal of LPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.tight_layout()
plt.show()