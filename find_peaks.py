import numpy as np
from scipy.signal import argrelextrema

a = np.loadtxt("yvalues.txt", dtype=float)

# Here you should fine tune parameters to get what you want
#peaks = find_peaks(a, prominence=1.5)
#print("Peaks position:", peaks[0])

# Plotting
#plt.plot(a)
#plt.title("Finding Peaks")
y = argrelextrema(a, np.greater)
print(len(y[0]))


#[plt.axvline(p, c='C3', linewidth=0.3) for p in peaks[0]]

#plt.show()