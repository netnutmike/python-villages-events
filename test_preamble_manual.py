#!/usr/bin/env python3
"""Manual test for preamble separator."""

# Test the logic
preamble = "Events:"
print("Testing preamble logic:")
print(f"Preamble: {repr(preamble)}")
print(f"Ends with newline: {preamble.endswith('\\n')}")
print()

print("Output:")
print(preamble, end='')
if not preamble.endswith('\n'):
    print()  # Add newline separator
print("Data here", end='')
print()
print()

# Test with newline
preamble2 = "Events:\n"
print("Testing with newline:")
print(f"Preamble: {repr(preamble2)}")
print(f"Ends with newline: {preamble2.endswith('\\n')}")
print()

print("Output:")
print(preamble2, end='')
if not preamble2.endswith('\n'):
    print()  # Add newline separator
print("Data here", end='')
