# Testing Guide

## Overview

The Villages Event Scraper has comprehensive test coverage including unit tests and integration tests.

## Running Tests

### Run All Tests
```bash
make test
```

### Run with Coverage
```bash
make test-cov
```

### Run Specific Test File
```bash
python3 -m unittest tests.test_token_fetcher -v
```

### Run Specific Test
```bash
python3 -m unittest tests.test_token_fetcher.TestTokenFetcher.test_fetch_auth_token_success -v
```

## Test Structure

```
tests/
├── __init__.py
├── test_token_fetcher.py      # Token fetching tests
├── test_session_manager.py    # Session management tests
├── test_api_client.py          # API client tests
├── test_event_processor.py    # Event processing tests
├── test_output_formatter.py   # Output formatting tests
└── test_integration.py        # End-to-end integration tests
```

## Unit Tests

### Token Fetcher Tests
- Successful token extraction
- Token with single/double quotes
- Pattern not found error
- Network timeout handling
- Request exception handling

### Session Manager Tests
- Session initialization
- Session establishment
- Cookie handling
- Context manager behavior
- Error handling

### API Client Tests
- Successful API requests
- HTTP error codes
- Invalid JSON responses
- Timeout handling
- Request exceptions

### Event Processor Tests
- Venue abbreviation
- Event processing
- Missing fields handling
- Empty events list
- Invalid data structures

### Output Formatter Tests
- Legacy format
- JSON format
- CSV format
- Plain text format
- Invalid format handling
- Empty events handling

## Integration Tests

### End-to-End Tests
- Complete pipeline with all formats
- Empty events list handling
- All HTTP requests mocked

### Error Handling Tests
- Token fetch failures
- Session establishment failures
- API request failures
- Invalid JSON responses
- Missing required fields
- Invalid command-line arguments

## Mocking Strategy

### HTTP Requests
```python
from unittest.mock import patch, Mock

@patch('src.token_fetcher.requests.get')
def test_example(self, mock_get):
    mock_response = Mock()
    mock_response.text = "test content"
    mock_get.return_value = mock_response
```

### Session Objects
```python
@patch('src.session_manager.requests.Session.get')
def test_example(self, mock_session_get):
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_session_get.return_value = mock_response
```

## Test Coverage Goals

- Minimum 80% code coverage
- 100% coverage for critical paths
- All error paths tested
- All output formats tested

## Writing New Tests

### Unit Test Template
```python
import unittest
from unittest.mock import patch, Mock

class TestNewFeature(unittest.TestCase):
    """Test cases for new feature."""
    
    def setUp(self):
        """Set up test fixtures."""
        pass
    
    def test_success_case(self):
        """Test successful operation."""
        # Arrange
        # Act
        # Assert
        pass
    
    def test_error_case(self):
        """Test error handling."""
        # Arrange
        # Act & Assert
        with self.assertRaises(ExpectedException):
            # code that should raise
            pass
```

### Integration Test Template
```python
@patch('src.api_client.requests.Session.get')
@patch('src.session_manager.requests.Session.get')
@patch('src.token_fetcher.requests.get')
@patch('sys.argv', ['villages_events.py', '--format', 'json'])
def test_new_integration(self, mock_token, mock_session, mock_api):
    """Test new integration scenario."""
    # Mock all HTTP requests
    # Run main()
    # Verify output and exit code
    pass
```

## Best Practices

1. **Arrange-Act-Assert** - Structure tests clearly
2. **One Assertion Per Test** - Keep tests focused
3. **Descriptive Names** - Test names explain what they test
4. **Mock External Dependencies** - No real HTTP requests
5. **Test Edge Cases** - Empty inputs, missing data, etc.
6. **Test Error Paths** - Verify error handling works
7. **Use Fixtures** - setUp() for common test data
8. **Clean Up** - Use tearDown() or context managers

## Continuous Integration

Tests run automatically on:
- Every push to main/develop
- Every pull request
- Multiple Python versions (3.8-3.12)
- Multiple operating systems (Linux, macOS, Windows)

See `.github/workflows/ci.yml` for CI configuration.
