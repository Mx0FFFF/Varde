import pytest
from pytest import approx
from varde.geo import geodetic_to_ecef

def test_equator_at_1000m():
    # lat, lon, alt
    assert geodetic_to_ecef(0,0,1000) == (6379137.0, 0.0, 0.0)


def test_equator_at_90_east():
    assert geodetic_to_ecef(0,90,0) == approx((0,6378137.0,0), abs=0.001)


def test_north_pole():
    assert geodetic_to_ecef(90,0,0) == approx((0.0, 0.0, 6356752.314245), abs=0.001)

def test_south_pole():
    assert geodetic_to_ecef(-90,0,0) == approx((0.0,0.0,-6356752.314245), abs=0.001)