# Preamble Feature Summary

## Overview

Added the ability to prefix output with a custom preamble string using the `-p, --preamble` command-line option.

## Feature Details

### Command-Line Option

```bash
-p PREAMBLE, --preamble PREAMBLE
    Preamble string to prefix output (default: '')
```

### Usage Examples

```bash
# Simple label
python villages_events.py --preamble "Events: "

# Header with newline
python villages_events.py --preamble "=== Today's Events ===\n" --format json

# Short option
python villages_events.py -p "Schedule: " --format meshtastic

# Multiple lines
python villages_events.py -p "Report\n------\n" --format csv

# Combined with other options
python villages_events.py --date-range tomorrow --preamble "Tomorrow: "
```

### Configuration File Support

The preamble can be set in `config.yaml`:

```yaml
# config.yaml
preamble: "Events:\n"
```

Command-line argument takes precedence over config file setting.

## Implementation

### Files Modified

1. **villages_events.py**
   - Added `--preamble` argument to argparse
   - Load default preamble from config file
   - Print preamble before formatted output

2. **src/config.py**
   - Added `DEFAULT_PREAMBLE = ""`

3. **config.yaml.example**
   - Added preamble configuration example with documentation

4. **README.md**
   - Added "Adding a Preamble" section with examples

### Files Created

1. **tests/test_preamble.py**
   - 6 comprehensive tests for preamble functionality
   - Tests all output formats
   - Tests both short and long options
   - Tests default behavior (no preamble)
   - Tests empty preamble

## Testing

All tests pass (134 total, 6 new):

```bash
python -m unittest tests.test_preamble -v
# 6 tests passed ✅

python -m unittest discover tests -v
# 134 tests passed ✅
```

### Test Coverage

- ✅ Preamble with Meshtastic format
- ✅ Preamble with JSON format
- ✅ Preamble with CSV format
- ✅ Preamble with newlines
- ✅ Short option `-p`
- ✅ Long option `--preamble`
- ✅ Default behavior (no preamble)
- ✅ Empty preamble string

## Use Cases

### 1. Adding Headers

```bash
python villages_events.py --preamble "# Events Report\n" --format csv > report.csv
```

Output:
```
# Events Report
location.title,title
Brownwood,Jazz Band
Spanish Springs,Rock Group
```

### 2. Labeling Output

```bash
python villages_events.py --preamble "Today: " --format meshtastic
```

Output:
```
Today: Brownwood,Jazz Band#Spanish Springs,Rock Group#
```

### 3. Formatting for Scripts

```bash
#!/bin/bash
events=$(python villages_events.py --preamble "EVENTS=" --format meshtastic)
echo "$events"
```

Output:
```
EVENTS=Brownwood,Jazz Band#Spanish Springs,Rock Group#
```

### 4. Multi-line Headers

```bash
python villages_events.py --preamble "=== Villages Events ===\nDate: $(date)\n\n" --format plain
```

Output:
```
=== Villages Events ===
Date: Sat Nov 16 17:00:00 EST 2025

location.title: Brownwood, title: Jazz Band
location.title: Spanish Springs, title: Rock Group
```

### 5. JSON with Context

```bash
python villages_events.py --preamble "// Generated on $(date)\n" --format json
```

Output:
```json
// Generated on Sat Nov 16 17:00:00 EST 2025
[
  {
    "location.title": "Brownwood",
    "title": "Jazz Band"
  }
]
```

## Configuration Precedence

1. **Command-line argument** (highest priority)
   ```bash
   python villages_events.py --preamble "CLI: "
   ```

2. **Config file setting**
   ```yaml
   # config.yaml
   preamble: "Config: "
   ```

3. **Default** (empty string, no preamble)

## Backward Compatibility

- ✅ Default behavior unchanged (no preamble)
- ✅ All existing tests still pass
- ✅ No breaking changes to API or output
- ✅ Optional feature, doesn't affect existing usage

## Documentation

Updated documentation in:
- ✅ README.md - Added "Adding a Preamble" section
- ✅ config.yaml.example - Added preamble configuration
- ✅ --help output - Shows preamble option

## Technical Details

### Implementation Logic

```python
# In villages_events.py

# 1. Load default from config
default_preamble = ConfigLoader.get_default(
    yaml_config, 'preamble', Config.DEFAULT_PREAMBLE
)

# 2. Add argument with default
parser.add_argument(
    '-p', '--preamble',
    type=str,
    default=default_preamble,
    help=f'Preamble string to prefix output (default: {repr(default_preamble)})'
)

# 3. Print preamble before output
if args.preamble:
    print(args.preamble, end='')
print(formatted_output, end='')
```

### Special Characters

The preamble supports escape sequences:
- `\n` - Newline
- `\t` - Tab
- `\\` - Backslash

Example:
```bash
python villages_events.py --preamble "Line 1\nLine 2\n"
```

## Future Enhancements

Possible future additions:
- Postamble/footer option
- Template variables (e.g., `{date}`, `{count}`)
- Conditional preambles based on output format
- Multi-line preamble from file

## Status

✅ **Feature Complete**
✅ **All Tests Passing**
✅ **Documentation Updated**
✅ **Ready for Use**

---

**Feature Added**: November 16, 2025  
**Tests Added**: 6  
**Total Tests**: 134  
**Status**: Complete ✅
