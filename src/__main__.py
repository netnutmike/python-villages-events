#!/usr/bin/env python3
"""
Command-line entry point for Villages Event Scraper.
"""

from .villages_events import main

if __name__ == "__main__":
    import sys
    sys.exit(main())
