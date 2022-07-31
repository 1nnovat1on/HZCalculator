#1 wavelength in nanometres [nm] = 2.99792458E+17 hertz [Hz]
# f = c/λ

# c = 299792458m/s

# 1 nm = 1e-9 m

def main(wavelength = None):
    inMeters = wavelength * float(1e-9)
    
    # I remember someone showed me this once. At some point, code must include the laws of physics
    
    speedOfLight = 299792458

    hzValue = speedOfLight / inMeters

    print(str(hzValue) + " HZ")

    for twos in range(40):
        hzValue = hzValue/2
    
    print("New HZ = {}".format(hzValue))

main(530)