# Quick Test Guide - Preamble Separator

## TL;DR

The separator works! Just don't test with `--version` or `--help`.

## Quick Verification (30 seconds)

```bash
# Run the tests
python -m unittest tests.test_preamble -v
```

Expected output: `Ran 6 tests in X.XXXs` with `OK`

## Why `--version` Doesn't Show Preamble

```python
# In src/villages_events.py:
parser.add_argument('--version', action='version', ...)  # Line 70
# ↑ This exits immediately, before line 208 where preamble is printed
```

## Test Commands That WILL Show Preamble

```bash
# Test 1: Simple preamble (separator auto-added)
villages-events --preamble "Events:" --date-range today

# Test 2: Preamble with newline (no extra separator)
villages-events --preamble $'Events:\n' --date-range today

# Test 3: Multi-line preamble
villages-events --preamble $'Schedule\n--------\n' --date-range today
```

## Expected Output Format

### Without Preamble
```
Brownwood,Jazz Band#Spanish Springs,Comedy Show#...
```

### With Preamble (no newline)
```
Events:
Brownwood,Jazz Band#Spanish Springs,Comedy Show#...
```

### With Preamble (with newline)
```
Events:
Brownwood,Jazz Band#Spanish Springs,Comedy Show#...
```

## Troubleshooting

### "I still don't see it"

1. Clear cache:
   ```bash
   find . -type d -name "__pycache__" -exec rm -rf {} +
   ```

2. Reinstall:
   ```bash
   pip install -e .
   ```

3. Test with events (not --version):
   ```bash
   villages-events --preamble "TEST:" --date-range today
   ```

### "Tests fail"

Check Python version:
```bash
python --version  # Should be 3.7+
```

Run full test suite:
```bash
python -m unittest discover -s tests -v
```

## Files to Review

- Implementation: `src/villages_events.py` (lines 208-218)
- Tests: `tests/test_preamble.py`
- Status: `PREAMBLE_SEPARATOR_STATUS.md`
- Clarification: `SEPARATOR_CLARIFICATION.md`

## Summary

✅ Feature implemented  
✅ Tests pass (6/6)  
✅ Works with all formats  
✅ Automatic separator logic correct  

**The feature is complete and working!**
