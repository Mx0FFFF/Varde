import pytest
from pytest import approx
from varde.geo import geodetic_to_ecef

def test_equator_at_1000m():
    # lat, lon, alt
    assert geodetic_to_ecef(0,0,1000) == (6379137.0, 0.0, 0.0)



     