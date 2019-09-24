from mrsimulator import Simulator, Isotopomer, SpectroscopicDimension
from mrsimulator.methods import one_d_spectrum
import matplotlib.pyplot as plt

# setting isotopomers
Isotopomers = [
    {
        "sites": [
            {
                "isotope": "1H",
                "isotropic_chemical_shift": "0 ppm",
                "shielding_symmetric": {"zeta": "13.89 ppm", "eta": 0.25},
            }
        ],
        "abundance": "100 %",
    }
]

# static spectrum setup
dimension = {
    "magnetic_flux_density": "9.4 T",
    "rotor_frequency": "0 kHz",
    "rotor_angle": "54.735 deg",
    "number_of_points": 2048,
    "spectral_width": "25 kHz",
    "reference_offset": "0 Hz",
    "isotope": "1H",
}

sim = Simulator()
sim.isotopomers = [Isotopomer.parse_dict_with_units(item) for item in Isotopomers]
sim.spectrum = [SpectroscopicDimension.parse_dict_with_units(dimension)]

freq1, amp1 = sim.run(one_d_spectrum, verbose=11)

# magic angle spinning (MAS) spectrum setup
dimension = {
    "magnetic_flux_density": "9.4 T",
    "rotor_frequency": "1 kHz",
    "rotor_angle": "54.735 deg",
    "number_of_points": 2048,
    "spectral_width": "25 kHz",
    "reference_offset": "0 Hz",
    "isotope": "1H",
}

sim.spectrum = [SpectroscopicDimension.parse_dict_with_units(dimension)]
freq2, amp2 = sim.run(one_d_spectrum, verbose=11)

# plot of the two spectrum
fig, ax = plt.subplots(1, 2, figsize=(6, 3))
ax[0].plot(freq1, amp1, linewidth=1.0, color="k")
ax[0].set_xlabel(f"frequency ratio / {freq2.unit}")
ax[0].grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
ax[0].set_title("Static")
ax[1].plot(freq2, amp2, linewidth=1.0, color="k")
ax[1].set_xlabel(f"frequency ratio / {freq2.unit}")
ax[1].grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
ax[1].set_title("MAS")
plt.tight_layout(h_pad=0, w_pad=0, pad=0)
plt.show()
