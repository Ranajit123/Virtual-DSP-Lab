import numpy as np
import matplotlib.pyplot as plt
epsilon = 1e-9

Fs = 16000
F1 = 470
F2 = 3200
Td = 10e-3
n = np.arange(0, int(Td*Fs))
signal = np.sin(2*np.pi*F1*n/Fs) + np.sin(2*np.pi*F2*n/Fs)
plt.figure(figsize=(8, 2))
plt.plot(n, signal)
plt.title('Input signal to LPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.tight_layout()
plt.grid(True)
plt.show()
