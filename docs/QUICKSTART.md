# Quick Start Guide

Get up and running with Villages Event Scraper in 5 minutes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Internet connection

## Installation

### 1. Get the Code

```bash
git clone https://github.com/yourusername/villages-event-scraper.git
cd villages-event-scraper
```

Or download and extract the ZIP file.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! Only one dependency: `requests`

## Basic Usage

### Run with Default Settings

```bash
python3 villages_events.py
```

Output (legacy format):
```
Brownwood,John Doe#Spanish Springs,Jane Smith#
```

### Try Different Formats

**JSON:**
```bash
python3 villages_events.py --format json
```

**CSV:**
```bash
python3 villages_events.py --format csv
```

**Plain Text:**
```bash
python3 villages_events.py --format plain
```

## Common Use Cases

### Save to File

```bash
python3 villages_events.py --format json > events.json
```

### Use in Shell Script

```bash
#!/bin/bash
events=$(python3 villages_events.py --format legacy)
echo "Today's events: $events"
```

### Cron Job

Add to crontab to run daily at 8 AM:
```bash
0 8 * * * cd /path/to/villages-event-scraper && python3 villages_events.py --format json > /path/to/events.json
```

### Parse JSON in Python

```python
import subprocess
import json

result = subprocess.run(
    ['python3', 'villages_events.py', '--format', 'json'],
    capture_output=True,
    text=True
)

events = json.loads(result.stdout)
for event in events:
    print(f"{event['venue']}: {event['title']}")
```

## What's Next?

- Read the [full README](../README.md) for detailed documentation
- Check out [API documentation](API.md) to understand the modules
- Review [Architecture](ARCHITECTURE.md) to understand the design
- See [Testing Guide](TESTING.md) to run tests
- Read [Contributing Guide](../CONTRIBUTING.md) to contribute

## Troubleshooting

### Command Not Found

If `python3` doesn't work, try:
```bash
python villages_events.py
```

### Module Not Found

Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### No Output

This is normal if there are no events scheduled for today. Try again on a different day.

### Network Errors

Check your internet connection and verify you can access:
- https://cdn.thevillages.com
- https://www.thevillages.com

## Getting Help

- Check the [README troubleshooting section](../README.md#troubleshooting)
- Review the [documentation](.)
- Open an issue on GitHub
