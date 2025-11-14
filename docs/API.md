# API Documentation

## Module Overview

The Villages Event Scraper is organized into several modules, each with a specific responsibility.

## Core Modules

### `token_fetcher`

Fetches authentication tokens from JavaScript files.

```python
from src.token_fetcher import fetch_auth_token

token = fetch_auth_token(js_url, timeout=10)
```

**Functions:**
- `fetch_auth_token(js_url: str, timeout: int = 10) -> str`
  - Fetches and extracts the authentication token
  - Raises: `TokenFetchError` on failure

### `session_manager`

Manages HTTP sessions and cookies.

```python
from src.session_manager import SessionManager

with SessionManager() as manager:
    manager.establish_session(calendar_url)
    session = manager.get_session()
```

**Class: SessionManager**
- `__init__()` - Initialize session
- `establish_session(calendar_url: str, timeout: int = 10)` - Visit calendar page
- `get_session() -> requests.Session` - Get active session
- `close()` - Close session and cleanup

### `api_client`

Handles authenticated API requests.

```python
from src.api_client import fetch_events

data = fetch_events(session, api_url, auth_token, timeout=10)
```

**Functions:**
- `fetch_events(session, api_url, auth_token, timeout=10) -> Dict[str, Any]`
  - Fetches events from API
  - Raises: `APIError` on failure

### `event_processor`

Processes and transforms event data.

```python
from src.event_processor import EventProcessor

processor = EventProcessor(venue_mappings)
events = processor.process_events(api_response)
```

**Class: EventProcessor**
- `__init__(venue_mappings: Dict[str, str])` - Initialize with venue mappings
- `abbreviate_venue(venue: str) -> str` - Abbreviate venue name
- `process_events(api_response: Dict[str, Any]) -> List[Tuple[str, str]]` - Process events

### `output_formatter`

Formats event data for output.

```python
from src.output_formatter import OutputFormatter

output = OutputFormatter.format_events(events, format_type="json")
```

**Class: OutputFormatter**
- `format_legacy(events) -> str` - Legacy format
- `format_json(events) -> str` - JSON format
- `format_csv(events) -> str` - CSV format
- `format_plain(events) -> str` - Plain text format
- `format_events(events, format_type) -> str` - Dispatcher method

## Configuration

### `config`

Contains all configuration constants.

```python
from src.config import Config

js_url = Config.JS_URL
timeout = Config.DEFAULT_TIMEOUT
```

**Constants:**
- `JS_URL` - JavaScript file URL
- `CALENDAR_URL` - Calendar page URL
- `API_URL` - API endpoint URL
- `DEFAULT_VENUE_MAPPINGS` - Venue abbreviation mappings
- `DEFAULT_TIMEOUT` - HTTP timeout in seconds
- `USER_AGENT` - User agent string
- `VALID_FORMATS` - List of valid output formats
- `DEFAULT_FORMAT` - Default output format

## Exceptions

### `exceptions`

Custom exception hierarchy.

```python
from src.exceptions import VillagesEventError, TokenFetchError

try:
    # code
except TokenFetchError as e:
    print(f"Token fetch failed: {e}")
```

**Exception Classes:**
- `VillagesEventError` - Base exception
- `TokenFetchError` - Token fetching errors
- `SessionError` - Session management errors
- `APIError` - API request errors
- `ProcessingError` - Event processing errors

## Command Line Interface

```bash
# Default (legacy format)
python3 villages_events.py

# JSON format
python3 villages_events.py --format json

# CSV format
python3 villages_events.py --format csv

# Plain text format
python3 villages_events.py --format plain
```

**Exit Codes:**
- `0` - Success
- `1` - Runtime error
- `2` - Invalid arguments
