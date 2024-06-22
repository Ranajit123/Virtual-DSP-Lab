import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, lfilter, firwin
epsilon = 1e-9

Fs = 16000
F1 = 2200
F2 = 3100
F3 = 4300
Td = 20e-3
n = np.arange(0, int(Td*Fs))
signal = np.sin(2*np.pi*F1*n/Fs) + np.sin(2*np.pi*F2*n/Fs) + np.sin(2*np.pi*F3*n/Fs)

tap = 101
fc = [2800, 3400]
win = 'hann'
h = firwin(tap, fc, pass_zero='bandpass', window=win, fs = Fs)
b = h
a = [1]
y_bpf = lfilter(b, a, signal)

plt.subplot(2, 1, 1)
plt.plot(n, signal)
plt.title('Input Signal to BPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')

plt.subplot(2, 1, 2)
plt.plot(n, y_bpf)
plt.title('Output Signal of BPF')
plt.ylabel('Aplitude')
plt.xlabel('Samples')
plt.tight_layout()
plt.show()