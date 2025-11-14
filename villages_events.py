#!/usr/bin/env python3
"""
Villages Event Scraper - Main entry point

Fetches entertainment events from The Villages API and outputs formatted event data.
"""

import sys
import argparse
import logging

from src.config import Config
from src.token_fetcher import fetch_auth_token
from src.session_manager import SessionManager
from src.api_client import fetch_events
from src.event_processor import EventProcessor
from src.output_formatter import OutputFormatter
from src.exceptions import VillagesEventError


def main() -> int:
    """
    Main entry point for the application.
    Returns exit code (0 for success, non-zero for failure).
    """
    # Configure logging
    logging.basicConfig(
        level=logging.WARNING,
        format='[%(levelname)s] %(message)s',
        stream=sys.stderr
    )
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Fetch and format entertainment events from The Villages API'
    )
    parser.add_argument(
        '--format',
        choices=Config.VALID_FORMATS,
        default=Config.DEFAULT_FORMAT,
        help=f'Output format (default: {Config.DEFAULT_FORMAT})'
    )
    
    try:
        args = parser.parse_args()
    except SystemExit as e:
        # argparse calls sys.exit() on error or --help
        # Return exit code 2 for invalid arguments, 0 for --help
        return 2 if e.code != 0 else 0
    
    try:
        # Initialize Config and load venue mappings
        venue_mappings = Config.DEFAULT_VENUE_MAPPINGS
        
        # Step 1: Fetch authentication token
        logging.debug("Fetching authentication token...")
        auth_token = fetch_auth_token(Config.JS_URL, timeout=Config.DEFAULT_TIMEOUT)
        
        # Step 2: Establish session with context manager for cleanup
        with SessionManager() as session_manager:
            logging.debug("Establishing session...")
            session_manager.establish_session(Config.CALENDAR_URL, timeout=Config.DEFAULT_TIMEOUT)
            session = session_manager.get_session()
            
            # Step 3: Fetch events from API
            logging.debug("Fetching events from API...")
            api_response = fetch_events(
                session=session,
                api_url=Config.API_URL,
                auth_token=auth_token,
                timeout=Config.DEFAULT_TIMEOUT
            )
            
            # Step 4: Process events
            logging.debug("Processing events...")
            processor = EventProcessor(venue_mappings)
            processed_events = processor.process_events(api_response)
            
            # Step 5: Format output
            logging.debug(f"Formatting output as {args.format}...")
            formatted_output = OutputFormatter.format_events(
                processed_events,
                format_type=args.format
            )
            
            # Step 6: Print formatted output to stdout
            print(formatted_output, end='')
        
        # Success
        return 0
        
    except VillagesEventError as e:
        # Handle all application-specific errors
        logging.error(str(e))
        return 1
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
