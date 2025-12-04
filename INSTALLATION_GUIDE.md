# Installation Guide

This guide explains how to install and run the Villages Event Scraper.

## Quick Start (Recommended)

The simplest way to use the application:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/villages-event-scraper.git
cd villages-event-scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run using the wrapper script
chmod +x villages-events
./villages-events --help
```

## Installation Methods

### Method 1: Wrapper Script (Easiest)

Use the provided `villages-events` wrapper script:

```bash
# Make executable
chmod +x villages-events

# Run from project directory
./villages-events

# Add to PATH to run from anywhere
export PATH="$PATH:$(pwd)"
villages-events
```

**Pros:**
- Simple and straightforward
- No installation required
- Works immediately

**Cons:**
- Must be run from project directory or add to PATH
- Requires chmod +x

### Method 2: Python Module

Run using Python's module syntax:

```bash
# From project directory
python -m src.villages_events

# With arguments
python -m src.villages_events --format json --date-range tomorrow
```

**Pros:**
- No installation required
- Works on all platforms
- Standard Python approach

**Cons:**
- Longer command
- Must be run from project directory

### Method 3: Package Installation

Install as a Python package:

```bash
# Install in development mode
pip install -e .

# Or install normally
pip install .

# Run (requires PYTHONPATH set)
export PYTHONPATH=$(pwd)
villages-events
```

**Pros:**
- Can be run from anywhere (with PYTHONPATH)
- Integrates with Python environment

**Cons:**
- Requires setting PYTHONPATH
- More complex setup

## Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Required packages:
- `requests>=2.31.0` - HTTP library
- `pyyaml>=6.0` - YAML parser

## Configuration

Create a configuration file (optional):

```bash
cp config.yaml.example config.yaml
# Edit config.yaml with your preferences
```

## Usage Examples

### Using Wrapper Script

```bash
./villages-events
./villages-events --format json
./villages-events --date-range tomorrow --preamble "Tomorrow: "
```

### Using Python Module

```bash
python -m src.villages_events
python -m src.villages_events --format json
python -m src.villages_events --date-range tomorrow --preamble "Tomorrow: "
```

### Using Installed Package

```bash
export PYTHONPATH=$(pwd)
villages-events
villages-events --format json
villages-events --date-range tomorrow --preamble "Tomorrow: "
```

## Troubleshooting

### "No module named 'src'" Error

If you get this error when using the installed package:

```bash
# Set PYTHONPATH to project directory
export PYTHONPATH=/path/to/villages-event-scraper
villages-events
```

Or use one of the other methods (wrapper script or python -m).

### Permission Denied

If you get "Permission denied" when running the wrapper script:

```bash
chmod +x villages-events
./villages-events
```

### Import Errors

If you get import errors:

```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Make sure you're in the project directory
cd /path/to/villages-event-scraper
```

## For Developers

### Development Installation

```bash
# Clone repository
git clone https://github.com/yourusername/villages-event-scraper.git
cd villages-event-scraper

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
python -m unittest discover tests -v
```

### Running Tests

```bash
# All tests
python -m unittest discover tests -v

# Specific test file
python -m unittest tests.test_preamble -v

# With coverage
pytest --cov=src --cov-report=term
```

## Platform-Specific Notes

### Linux/macOS

```bash
# Make wrapper executable
chmod +x villages-events

# Run
./villages-events
```

### Windows

```bash
# Use Python module method
python -m src.villages_events

# Or use Python directly
python src/villages_events.py
```

## Summary

**Recommended for most users:** Use the wrapper script (`./villages-events`)

**Recommended for developers:** Use Python module (`python -m src.villages_events`)

**Recommended for system-wide install:** Install package and set PYTHONPATH

Choose the method that best fits your workflow!
