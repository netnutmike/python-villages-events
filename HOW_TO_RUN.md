# How to Run Villages Event Scraper

## From Current Directory

You're in: `/Users/mikemyers/Documents/Development/python/python-villages-events`

### Method 1: Wrapper Script (Recommended)
```bash
./villages-events --version
./villages-events --date-range today
./villages-events --preamble "Events:" --date-range today
```

### Method 2: Python Module
```bash
python -m src.villages_events --version
python -m src.villages_events --date-range today
python -m src.villages_events --preamble "Events:" --date-range today
```

### Method 3: Direct Python (if installed with pip)
```bash
# First install in development mode
pip install -e .

# Then run from anywhere
villages-events --version
villages-events --date-range today
```

## Example Commands

### Basic Usage
```bash
# Get today's events
./villages-events --date-range today

# Get this week's events in JSON format
./villages-events --date-range this-week --format json

# Get entertainment events at town squares
./villages-events --category entertainment --location town-squares
```

### With Preamble
```bash
# Simple preamble (automatic separator added)
./villages-events --preamble "Today's Events:" --date-range today

# Preamble with explicit newline (no extra separator)
./villages-events --preamble $'Events:\n' --date-range today

# Multi-line preamble
./villages-events --preamble $'Schedule\n--------\n' --date-range today
```

### Different Output Formats
```bash
# Meshtastic format (default)
./villages-events --date-range today

# JSON format
./villages-events --date-range today --format json

# CSV format
./villages-events --date-range today --format csv

# Plain text format
./villages-events --date-range today --format text
```

### Custom Fields
```bash
# Show only specific fields
./villages-events --fields "location.title,title,start.date"

# Show all available fields
./villages-events --fields "location.title,title,start.date,start.time,end.date,end.time,description"
```

### Raw API Response
```bash
# Get raw JSON from API (for debugging)
./villages-events --raw --date-range today
```

## Configuration File

You can also set defaults in `config.yaml`:

```yaml
format: json
date_range: today
category: entertainment
location: town-squares
preamble: "Today's Events:\n"
timeout: 10

output_fields:
  - location.title
  - title
  - start.date
  - start.time

venue_mappings:
  "Brownwood Paddock Square": "Brownwood"
  "Spanish Springs Town Square": "Spanish Springs"
  "Lake Sumter Landing Market Square": "Lake Sumter"
```

Then just run:
```bash
./villages-events  # Uses config.yaml defaults
```

## Testing

### Run All Tests
```bash
python -m unittest discover -s tests -v
```

### Run Specific Test Suite
```bash
python -m unittest tests.test_preamble -v
python -m unittest tests.test_integration -v
```

### Run Single Test
```bash
python -m unittest tests.test_preamble.TestPreamble.test_preamble_with_json_format -v
```

## Current Version

```bash
./villages-events --version
# Output: villages_events.py 1.1.0
```

## Help

```bash
./villages-events --help
```

Shows all available options and their defaults.

## Summary

✅ **Easiest**: `./villages-events --date-range today`  
✅ **With preamble**: `./villages-events --preamble "Events:" --date-range today`  
✅ **JSON output**: `./villages-events --format json --date-range today`  
✅ **Custom fields**: `./villages-events --fields "location.title,title"`  

The application is ready to use! 🎉
