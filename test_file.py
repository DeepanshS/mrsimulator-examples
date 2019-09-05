from mrsimulator import Simulator, Isotopomer, Spectrum
from mrsimulator.methods import one_d_spectrum
import matplotlib.pyplot as plt

Isotopomers = [
    {
        "sites": [
            {
                "isotope": "1H",
                "isotropic_chemical_shift": "0 ppm",
                "shielding_symmetric": {"anisotropy": "13.89 ppm", "asymmetry": 0.25},
            }
        ],
        "abundance": "100 %",
    }
]

spectrum = {
    "direct_dimension": {
        "magnetic_flux_density": "9.4 T",
        "rotor_frequency": "0 kHz",
        "rotor_angle": "54.735 deg",
        "number_of_points": 2048,
        "spectral_width": "25 kHz",
        "reference_offset": "0 Hz",
        "isotope": "1H",
    }
}

sim = Simulator()
sim.isotopomers = [Isotopomer.parse_json_with_units(item) for item in Isotopomers]
sim.spectrum = Spectrum.parse_json_with_units(spectrum)

freq1, amp1 = sim.run(one_d_spectrum, verbose=11)


spectrum = {
    "direct_dimension": {
        "magnetic_flux_density": "9.4 T",
        "rotor_frequency": "1 kHz",
        "rotor_angle": "54.735 deg",
        "number_of_points": 2048,
        "spectral_width": "25 kHz",
        "reference_offset": "0 Hz",
        "isotope": "1H",
    }
}

sim.spectrum = Spectrum.parse_json_with_units(spectrum)
freq2, amp2 = sim.run(one_d_spectrum, verbose=11)

fig, ax = plt.subplots(1, 2)
ax[0].plot(freq1, amp1)
ax[0].set_xlabel("frequency / Hz")
ax[1].plot(freq2, amp2)
ax[1].set_xlabel("frequency / Hz")
plt.show()
