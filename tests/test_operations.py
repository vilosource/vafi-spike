"""Tests for calc.operations."""

import pytest
from src.calc.operations import add, subtract, multiply


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_mixed_signs(self):
        assert add(-1, 3) == 2

    def test_zeros(self):
        assert add(0, 0) == 0

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_invalid_input_raises_type_error(self):
        with pytest.raises(TypeError):
            add("a", 1)


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_zeros(self):
        assert subtract(0, 0) == 0

    def test_floats(self):
        assert subtract(5.5, 2.5) == 3.0

    def test_invalid_input_raises_type_error(self):
        with pytest.raises(TypeError):
            subtract(None, 1)


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_mixed_signs(self):
        assert multiply(-2, 3) == -6

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0

    def test_invalid_input_raises_type_error(self):
        with pytest.raises(TypeError):
            multiply([], 1)
