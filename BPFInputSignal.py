import numpy as np
import matplotlib.pyplot as plt
epsilon = 1e-9

Fs = 16000
F1 = 2200
F2 = 3100
F3 = 4300
Td = 20e-3
n = np.arange(0, int(Td*Fs))
signal = np.sin(2*np.pi*F1*n/Fs) + np.sin(2*np.pi*F2*n/Fs) + np.sin(2*np.pi*F3*n/Fs)

plt.figure(figsize=(12, 5))
plt.plot(n, signal)
plt.title('Input Signal to BPF')
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.tight_layout()
plt.show()