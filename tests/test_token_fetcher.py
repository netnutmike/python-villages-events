"""Unit tests for token_fetcher module."""

import unittest
from unittest.mock import patch, Mock
from src.token_fetcher import fetch_auth_token
from src.exceptions import TokenFetchError


class TestTokenFetcher(unittest.TestCase):
    """Test cases for token fetcher functionality."""

    def test_fetch_auth_token_success(self):
        """Test successful token extraction."""
        mock_js_content = '''
        var someCode = "test";
        dp_AUTH_TOKEN = "Basic YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=";
        var moreCode = "test";
        '''
        
        with patch('src.token_fetcher.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = mock_js_content
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            token = fetch_auth_token("https://example.com/main.js")
            
            self.assertEqual(token, "Basic YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=")
            mock_get.assert_called_once_with("https://example.com/main.js", timeout=10)

    def test_fetch_auth_token_with_single_quotes(self):
        """Test token extraction with single quotes."""
        mock_js_content = "dp_AUTH_TOKEN = 'Basic dGVzdHRva2VuMTIzNDU2Nzg5MA==';"
        
        with patch('src.token_fetcher.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = mock_js_content
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            token = fetch_auth_token("https://example.com/main.js")
            
            self.assertEqual(token, "Basic dGVzdHRva2VuMTIzNDU2Nzg5MA==")

    def test_fetch_auth_token_pattern_not_found(self):
        """Test error when token pattern is not found."""
        mock_js_content = "var someCode = 'no token here';"
        
        with patch('src.token_fetcher.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.text = mock_js_content
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            with self.assertRaises(TokenFetchError) as context:
                fetch_auth_token("https://example.com/main.js")
            
            self.assertIn("Pattern not found", str(context.exception))

    def test_fetch_auth_token_timeout(self):
        """Test timeout error handling."""
        with patch('src.token_fetcher.requests.get') as mock_get:
            mock_get.side_effect = __import__('requests').exceptions.Timeout()
            
            with self.assertRaises(TokenFetchError) as context:
                fetch_auth_token("https://example.com/main.js")
            
            self.assertIn("Timeout", str(context.exception))

    def test_fetch_auth_token_request_exception(self):
        """Test general request exception handling."""
        with patch('src.token_fetcher.requests.get') as mock_get:
            mock_get.side_effect = __import__('requests').exceptions.RequestException("Network error")
            
            with self.assertRaises(TokenFetchError) as context:
                fetch_auth_token("https://example.com/main.js")
            
            self.assertIn("Failed to fetch", str(context.exception))


if __name__ == '__main__':
    unittest.main()
