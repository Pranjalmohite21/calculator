# calculator.py

def add(x, y):
    """Return x + y."""
    return x + y

def subtract(x, y):
    """Return x − y."""
    return x - y

def divide(x, y):
    """Return x ÷ y; raise ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
