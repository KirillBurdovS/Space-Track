from skyfield.api import EarthSatellite

def parse_tle(tle_file):
    with open(tle_file, 'r') as f:
        lines = f.readlines()
    satellite = EarthSatellite(lines[1],lines[2],lines[0])
    return satellite
