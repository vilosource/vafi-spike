"""Basic arithmetic operations.

Each function takes two numeric arguments and returns a numeric result.
All functions validate inputs via validators.ensure_numeric() before operating.
"""

from .validators import ensure_numeric


def add(a, b):
    """Return the sum of a and b."""
    ensure_numeric(a)
    ensure_numeric(b)
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    ensure_numeric(a)
    ensure_numeric(b)
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    ensure_numeric(a)
    ensure_numeric(b)
    return a * b
