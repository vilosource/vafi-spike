"""Input validation for calculator operations."""


def ensure_numeric(value):
    """Raise TypeError if value is not int or float. Booleans are rejected."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric value, got {type(value).__name__}")
