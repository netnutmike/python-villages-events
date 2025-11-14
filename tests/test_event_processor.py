"""Unit tests for event_processor module."""

import unittest
from src.event_processor import EventProcessor
from src.exceptions import ProcessingError


class TestEventProcessor(unittest.TestCase):
    """Test cases for event processor functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.venue_mappings = {
            "Brownwood": "Brownwood",
            "Sawgrass": "Sawgrass",
            "Spanish Springs": "Spanish Springs",
            "Lake Sumter": "Lake Sumter"
        }
        self.processor = EventProcessor(self.venue_mappings)

    def test_abbreviate_venue_with_match(self):
        """Test venue abbreviation with matching keyword."""
        result = self.processor.abbreviate_venue("Brownwood Paddock Square")
        self.assertEqual(result, "Brownwood")

    def test_abbreviate_venue_no_match(self):
        """Test venue abbreviation with no matching keyword."""
        result = self.processor.abbreviate_venue("Unknown Venue Location")
        self.assertEqual(result, "Unknown Venue Location")

    def test_abbreviate_venue_empty_string(self):
        """Test venue abbreviation with empty string."""
        result = self.processor.abbreviate_venue("")
        self.assertEqual(result, "")

    def test_process_events_success(self):
        """Test successful event processing."""
        api_response = {
            "events": [
                {
                    "location": {"title": "Brownwood Paddock Square"},
                    "title": "Artist One"
                },
                {
                    "location": {"title": "Spanish Springs Town Square"},
                    "title": "Artist Two"
                }
            ]
        }
        
        result = self.processor.process_events(api_response)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], ("Brownwood", "Artist One"))
        self.assertEqual(result[1], ("Spanish Springs", "Artist Two"))

    def test_process_events_missing_events_key(self):
        """Test error when events key is missing."""
        api_response = {"data": []}
        
        with self.assertRaises(ProcessingError) as context:
            self.processor.process_events(api_response)
        
        self.assertIn("Missing 'events' key", str(context.exception))

    def test_process_events_not_a_list(self):
        """Test error when events is not a list."""
        api_response = {"events": "not a list"}
        
        with self.assertRaises(ProcessingError) as context:
            self.processor.process_events(api_response)
        
        self.assertIn("not a list", str(context.exception))

    def test_process_events_empty_list(self):
        """Test processing empty events list."""
        api_response = {"events": []}
        
        result = self.processor.process_events(api_response)
        
        self.assertEqual(result, [])

    def test_process_events_missing_location(self):
        """Test skipping event with missing location field."""
        api_response = {
            "events": [
                {"title": "Artist One"},
                {
                    "location": {"title": "Brownwood Paddock Square"},
                    "title": "Artist Two"
                }
            ]
        }
        
        result = self.processor.process_events(api_response)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("Brownwood", "Artist Two"))

    def test_process_events_missing_title(self):
        """Test skipping event with missing title field."""
        api_response = {
            "events": [
                {
                    "location": {"title": "Brownwood Paddock Square"},
                    "title": "Artist One"
                },
                {
                    "location": {"title": "Sawgrass Grove"}
                }
            ]
        }
        
        result = self.processor.process_events(api_response)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ("Brownwood", "Artist One"))


if __name__ == '__main__':
    unittest.main()
