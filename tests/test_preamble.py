"""Unit tests for preamble feature."""

import unittest
from unittest.mock import patch, Mock
import sys
from io import StringIO

from src.villages_events import main


class TestPreamble(unittest.TestCase):
    """Test cases for preamble functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_js_content = 'dp_AUTH_TOKEN = "Basic dGVzdHRva2VuMTIzNDU2";'
        self.mock_api_response = {
            "events": [
                {
                    "location": {"title": "Brownwood Paddock Square"},
                    "title": "Test Event"
                }
            ]
        }

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py', '--preamble', 'Events: '])
    def test_preamble_with_meshtastic_format(self, mock_token_get, mock_session_get, mock_api_get):
        """Test preamble is added before Meshtastic format output."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify preamble is at the beginning
        self.assertTrue(output.startswith("Events: "))
        
        # Verify event data follows preamble
        self.assertIn("Brownwood,Test Event#", output)

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py', '--preamble', 'Today:\n', '--format', 'json'])
    def test_preamble_with_json_format(self, mock_token_get, mock_session_get, mock_api_get):
        """Test preamble with newline before JSON output."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify preamble with newline
        self.assertTrue(output.startswith("Today:\n"))
        
        # Verify JSON follows
        self.assertIn('"location.title": "Brownwood"', output)

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py', '-p', '=== Events ===\n'])
    def test_preamble_short_option(self, mock_token_get, mock_session_get, mock_api_get):
        """Test preamble using short option -p."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify preamble
        self.assertTrue(output.startswith("=== Events ===\n"))

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py'])
    def test_no_preamble_by_default(self, mock_token_get, mock_session_get, mock_api_get):
        """Test that no preamble is added by default."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify output starts with event data (no preamble)
        self.assertTrue(output.startswith("Brownwood,Test Event#"))

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py', '--preamble', ''])
    def test_empty_preamble(self, mock_token_get, mock_session_get, mock_api_get):
        """Test that empty preamble string adds nothing."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify output starts with event data (no preamble)
        self.assertTrue(output.startswith("Brownwood,Test Event#"))

    @patch('src.api_client.requests.Session.get')
    @patch('src.session_manager.requests.Session.get')
    @patch('src.token_fetcher.requests.get')
    @patch('sys.argv', ['villages_events.py', '--preamble', 'Header: ', '--format', 'csv'])
    def test_preamble_with_csv_format(self, mock_token_get, mock_session_get, mock_api_get):
        """Test preamble with CSV format."""
        # Mock token fetch
        mock_token_response = Mock()
        mock_token_response.text = self.mock_js_content
        mock_token_response.raise_for_status = Mock()
        mock_token_get.return_value = mock_token_response
        
        # Mock session establishment
        mock_session_response = Mock()
        mock_session_response.raise_for_status = Mock()
        mock_session_get.return_value = mock_session_response
        
        # Mock API request
        mock_api_response = Mock()
        mock_api_response.status_code = 200
        mock_api_response.json.return_value = self.mock_api_response
        mock_api_get.return_value = mock_api_response
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            exit_code = main()
            output = captured_output.getvalue()
        finally:
            sys.stdout = sys.__stdout__
        
        # Verify exit code
        self.assertEqual(exit_code, 0)
        
        # Verify preamble before CSV
        self.assertTrue(output.startswith("Header: "))
        
        # Verify CSV follows
        self.assertIn("location.title,title", output)


if __name__ == '__main__':
    unittest.main()
