"""
Program: test_rotation_utils.py
Name: Elijah Drakeford
Purpose: This program verifies that the adjust rotation in rotation_utils is working properly
Date: April 5, 2026
"""

import pytest
from rotation_utils import adjust_rotation

def test_input_100():
    assert adjust_rotation(100) == 100

def test_input_460():
    assert adjust_rotation(460) == 100

def test_input_820():
    assert adjust_rotation(820) == 100

def test_input_negative_100():
    assert adjust_rotation(-100) == 260

def test_input_negative_460():
    assert adjust_rotation(-460) == 260

def test_input_negative_820():
    assert adjust_rotation(-820) == 260

def test_non_numeric_input():
    with pytest.raises(TypeError):
        adjust_rotation("abc")
