#!/bin/bash
# Verification script for preamble separator

echo "=== Verifying Preamble Separator ==="
echo

echo "Test 1: Preamble without newline (should add separator)"
echo "Command: python -m src.villages_events --preamble 'TEST:' --version"
output=$(python -m src.villages_events --preamble "TEST:" --version 2>&1)
echo "Output:"
echo "$output" | cat -A  # Show all characters including newlines
echo

if echo "$output" | grep -q "TEST:\$"; then
    echo "✅ PASS: Separator added (newline after TEST:)"
else
    echo "❌ FAIL: No separator found"
fi
echo

echo "Test 2: Preamble with newline (should not add extra separator)"
echo "Command: python -m src.villages_events --preamble \$'TEST:\\n' --version"
output=$(python -m src.villages_events --preamble $'TEST:\n' --version 2>&1)
echo "Output:"
echo "$output" | cat -A
echo

echo "Test 3: Check source code"
echo "Looking for separator logic in src/villages_events.py:"
grep -A 2 "Add separator if preamble" src/villages_events.py
echo

echo "=== Verification Complete ==="
