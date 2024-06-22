from PyQt5 import QtCore
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, butter, buttord
epsilon = 1e-9

Fs = 16000
F1 = 470
F2 = 3200
Td = 10e-3
n = np.arange(0, int(Td*Fs))
signal = np.sin(2*np.pi*F1*n/Fs) + np.sin(2*np.pi*F2*n/Fs)

Fp = 800
Fst = 1200
wp = 2*np.pi*Fp
wst = 2*np.pi*Fst
Ap = 0.5
As = 50
N, wc = buttord(wp, wst, Ap, As, analog=True)
Fc = wc/(2*np.pi)
b, a = butter(N, Fc, btype='lowpass', analog=False, output='ba', fs=Fs)
y_lpf = lfilter(b, a, signal)
plt.figure(figsize=(8, 4))
plt.subplot(2, 1, 1)
plt.plot(n, signal)
plt.title('Input signal to LPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')

plt.subplot(2, 1, 2)
plt.plot(n, y_lpf)
plt.title('Output Signal of LPF')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.tight_layout()
plt.show()