"""Event processor module for extracting and processing event data."""

import logging
from typing import List, Tuple, Dict, Any

from .exceptions import ProcessingError


logger = logging.getLogger(__name__)


class EventProcessor:
    """Processes event data and applies venue abbreviations."""

    def __init__(self, venue_mappings: Dict[str, str]):
        """
        Initialize with venue abbreviation mappings.

        Args:
            venue_mappings: Dictionary mapping keywords to abbreviations
        """
        self.venue_mappings = venue_mappings

    def abbreviate_venue(self, venue: str) -> str:
        """
        Abbreviates venue name based on keyword matching.

        Args:
            venue: Full venue name

        Returns:
            Abbreviated venue name or original if no match
        """
        if not venue:
            return venue

        # Check if venue contains any keyword from mappings
        for keyword, abbreviation in self.venue_mappings.items():
            if keyword in venue:
                return abbreviation

        # Return original venue if no match found
        return venue

    def process_events(self, api_response: Dict[str, Any]) -> List[Tuple[str, str]]:
        """
        Extracts and processes events from API response.

        Args:
            api_response: Parsed JSON response from API

        Returns:
            List of tuples (abbreviated_venue, event_title)

        Raises:
            ProcessingError: If events array is missing from response
        """
        # Extract events array from response
        if "events" not in api_response:
            raise ProcessingError("Missing 'events' key in API response")

        events = api_response["events"]
        if not isinstance(events, list):
            raise ProcessingError("'events' field is not a list")

        processed_events = []

        for idx, event in enumerate(events):
            try:
                # Extract location.title field
                if "location" not in event:
                    logger.warning(f"Event at index {idx} missing 'location' field, skipping")
                    continue

                location = event["location"]
                if not isinstance(location, dict):
                    logger.warning(f"Event at index {idx} has invalid 'location' field, skipping")
                    continue

                if "title" not in location:
                    logger.warning(f"Event at index {idx} missing 'location.title' field, skipping")
                    continue

                venue = location["title"]

                # Extract event title field
                if "title" not in event:
                    logger.warning(f"Event at index {idx} missing 'title' field, skipping")
                    continue

                event_title = event["title"]

                # Apply venue abbreviation
                abbreviated_venue = self.abbreviate_venue(venue)

                # Add to processed events list
                processed_events.append((abbreviated_venue, event_title))

            except Exception as e:
                logger.warning(f"Error processing event at index {idx}: {e}, skipping")
                continue

        return processed_events
