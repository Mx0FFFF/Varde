import math

# Constant values according to WGS 84 (World Geodetic System)
A = 6378137.0
F = 1/298.257223563
E2 = 2*F - F**2

def geodetic_to_ecef(lat_deg, lon_deg, alt_m):

    if not -90 <= lat_deg <= 90:
        raise ValueError("Latitude must be betweeen -90 and 90 degrees")

    lat_rad = math.radians(lat_deg)
    lon_rad = math.radians(lon_deg)
    N = A / math.sqrt(1-E2 * math.sin(lat_rad)**2)
    X = (N + alt_m) * math.cos(lat_rad) * math.cos(lon_rad)
    Y = (N + alt_m) * math.cos(lat_rad) * math.sin(lon_rad)
    Z = (N * (1 - E2) + alt_m) * math.sin(lat_rad)
    return (X,Y,Z)


if __name__ == "__main__":
    cases = [
        (0,0,0),
        (90,0,0),
        (0,90,0),
        (48.8562, 2.3508, 67.4),
    ]

    for lat, lon, alt in cases:
        x, y, z = geodetic_to_ecef(lat, lon, alt)
        print(f"{lat:>9.4f} {lon:>9.4f} {alt:>8.1f} -> {x:15.2f} {y:15.2f} {z:15.2f}")