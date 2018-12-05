#!/usr/bin/env python3

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

import sinesum


def test_f():
    """Test function to check if f function in cw08 module works correctly"""
    assert sinesum.f(0) == 0
    assert sinesum.f(0.3*math.pi*2,100) == 1
    assert math.isclose(sinesum.f(-1),1)

def test_Sn():
    """Test Function to check if Sn functino in cw08 module works correctly"""
    assert math.isclose(sinesum.Sn(math.pi*2*0.25,100),1)
