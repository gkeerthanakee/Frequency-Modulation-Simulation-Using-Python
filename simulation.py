import numpy as np
import matplotlib.pyplot as plt

# Sampling configuration
fs = 100000  # Sampling frequency in Hz
t = np.arange(0, 0.01, 1/fs)  # Time vector (10 ms duration)

# Signal definitions
Am = 1        # Amplitude of message signal
fm = 500      # Frequency of message signal
Ac = 1        # Amplitude of carrier signal
fc = 5000     # Frequency of carrier signal
kf = 75       # Frequency sensitivity (Hz per volt)

# Message signal
m_t = Am * np.sin(2 * np.pi * fm * t)

# FM modulated signal
integral_m_t = np.cumsum(m_t) / fs  # Approximate integral
s_t = Ac * np.cos(2 * np.pi * fc * t + 2 * np.pi * kf * integral_m_t)

# Frequency deviation
delta_f = kf * np.max(np.abs(m_t))  # Maximum deviation
print(f"Maximum Frequency Deviation: {delta_f} Hz")
print(f"Minimum Frequency Deviation: {-delta_f} Hz")

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t[0:1000], s_t[0:1000])  # Display only the first 1000 samples
plt.title("FM Modulated Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
	
