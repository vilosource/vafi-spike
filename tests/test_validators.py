"""Tests for calc.validators."""

import pytest
from src.calc.validators import ensure_numeric


class TestEnsureNumeric:
    def test_int_passes(self):
        ensure_numeric(42)

    def test_float_passes(self):
        ensure_numeric(3.14)

    def test_zero_passes(self):
        ensure_numeric(0)

    def test_negative_passes(self):
        ensure_numeric(-5)

    def test_string_raises(self):
        with pytest.raises(TypeError, match="Expected numeric value"):
            ensure_numeric("hello")

    def test_none_raises(self):
        with pytest.raises(TypeError):
            ensure_numeric(None)

    def test_list_raises(self):
        with pytest.raises(TypeError):
            ensure_numeric([1, 2])

    def test_bool_raises(self):
        with pytest.raises(TypeError):
            ensure_numeric(True)
