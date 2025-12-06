# Preamble Separator Fix - Format-Specific Separators

## Issue

The preamble was using a newline separator for all formats, but Meshtastic format uses `#` as the separator between events, not newlines.

## Solution

Updated the separator logic to be format-specific:
- **Meshtastic format**: Uses `#` separator
- **Other formats** (JSON, CSV, plain): Use newline separator

## Code Changes

### File: `src/villages_events.py`

```python
# Add preamble if provided
if args.preamble:
    print(args.preamble, end='')
    # Add separator based on format type
    # Meshtastic uses # separator, other formats use newline
    if args.format == 'meshtastic':
        # For meshtastic, add # separator if preamble doesn't end with it
        if not args.preamble.endswith('#'):
            print('#', end='')
    else:
        # For other formats, add newline if preamble doesn't end with one
        if not args.preamble.endswith('\n'):
            print()
print(formatted_output, end='')
```

## Test Updates

### File: `tests/test_preamble.py`

1. Updated `test_preamble_with_meshtastic_format` to expect `#` separator
2. Added new test `test_preamble_with_hash_separator` to verify no double `##`

## Test Results

All 135 tests pass (added 1 new test):

```
✅ test_preamble_with_meshtastic_format - Expects # separator
✅ test_preamble_with_hash_separator - No double ## when preamble ends with #
✅ test_preamble_with_json_format - Newline separator for JSON
✅ test_preamble_with_csv_format - Newline separator for CSV
✅ test_preamble_short_option - Short -p option works
✅ test_no_preamble_by_default - No preamble by default
✅ test_empty_preamble - Empty string handled correctly
```

## Examples

### Meshtastic Format (Default)

**Without separator in preamble:**
```bash
./villages-events --preamble "Events:" --date-range today
# Output: Events:#Spanish Springs,Scooter The DJ#Lake Sumter,The Brothers Jukebox#...
```

**With separator in preamble:**
```bash
./villages-events --preamble "Events:#" --date-range today
# Output: Events:#Spanish Springs,Scooter The DJ#Lake Sumter,The Brothers Jukebox#...
# (no double ##)
```

### JSON Format

**Without newline in preamble:**
```bash
./villages-events --preamble "Events:" --date-range today --format json
# Output:
# Events:
# [
#   {"location.title": "Spanish Springs", ...}
# ]
```

**With newline in preamble:**
```bash
./villages-events --preamble $'Events:\n' --date-range today --format json
# Output:
# Events:
# [
#   {"location.title": "Spanish Springs", ...}
# ]
# (no extra newline)
```

### CSV Format

```bash
./villages-events --preamble "Schedule:" --date-range today --format csv
# Output:
# Schedule:
# location.title,title
# Spanish Springs,Scooter The DJ
# ...
```

## Summary

✅ Fixed separator to match output format  
✅ Meshtastic uses `#` separator  
✅ JSON/CSV/plain use newline separator  
✅ No duplicate separators  
✅ All 135 tests pass  
✅ Backward compatible with existing usage  

The preamble feature now correctly uses format-specific separators!
