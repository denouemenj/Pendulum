import numpy as np
import fit_black_box as bb


def quadratic(t, a, b, c):
    return a * t ** 2 + b * t + c


filename = "periodamp.txt"
x, y, xerr, yerr = bb.load_data(filename)

init_guess = (-0.5, 0, +0.5)
font_size = 12
xlabel = "Releasing Amplitude (radian)"
ylabel = "Period (second)"

bb.plot_fit(quadratic, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, xlabel=xlabel, ylabel=ylabel)


def damped(t, a, b, c, d):
    return a * np.exp(-t / b) * np.cos(2 * np.pi * t / c + d)


filename = "qfactor.txt"
x, y, xerr, yerr = bb.load_data(filename)
init_guess = (0.095781592, 100, 1.031, 0)
font_size = 12
xlabel = "Time (second)"
ylabel = "Amplitude (radian)"

bb.plot_fit(damped, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, xlabel=xlabel, ylabel=ylabel)

filename = "specificqfactor.txt"
x, y, xerr, yerr = bb.load_data(filename)
init_guess = (0.095781592, 100, 1.031, 0)
font_size = 12
xlabel = "Time (second)"
ylabel = "Amplitude (radian)"

bb.plot_fit(damped, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, xlabel=xlabel, ylabel=ylabel)

# Best fit parameters, with uncertainties, but not rounded off properly:
# 0.0632239065407082 +/- 0.0025238656120603886
# -0.00039321016339176595 +/- 0.001842735401466339
# 1.0075142875798548 +/- 0.0025458057834517795

# Best fit parameters, with uncertainties, but not rounded off properly:
# -0.3125717478936253 +/- 0.0021113346218110322
# 91.66974737574103 +/- 0.8898317674212124
# 1.0025832329580984 +/- 1.6952772193593762e-05
# -0.13585075212473005 +/- 0.006765486155422607

# Best fit parameters, with uncertainties, but not rounded off properly:
# 0.25372279529831143 +/- 0.08996166386786343
# 0.25 / 0.09
# 144.28694792381657 +/- 69.20628831028856
# 144 / 70
# 1.0023042060684506 +/- 0.0005467136036460165
# 1.0023 / 0.0005
# -16.186410461688308 +/- 0.3648766881712546
# -16.2 / -0.4
