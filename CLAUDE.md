# CLAUDE.md

## Project

A simple Python calculator library used for testing vafi agent execution.

## Structure

```
src/calc/
  __init__.py          # Package init
  operations.py        # Arithmetic functions (add, subtract, multiply, ...)
  validators.py        # Input validation (ensure_numeric)
tests/
  test_operations.py   # Tests for operations
  test_validators.py   # Tests for validators
```

## Conventions

- Each operation is a standalone function in `operations.py`
- All operations validate inputs via `validators.ensure_numeric()` before operating
- Each operation has its own test class in `test_operations.py`
- Tests cover: positive numbers, negative numbers, zeros, floats, invalid input
- Invalid input tests assert `TypeError` is raised

## Running tests

```bash
python -m pytest tests/ -v
```

## Adding a new operation

1. Add the function to `src/calc/operations.py` following the existing pattern
2. Add a test class to `tests/test_operations.py` following the existing pattern
3. Run tests to verify
