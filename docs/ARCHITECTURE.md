# Architecture

## Overview

The Villages Event Scraper follows a modular architecture with clear separation of concerns. Each module has a single responsibility and communicates through well-defined interfaces.

## System Architecture

```
┌─────────────────┐
│  CLI Interface  │
│ villages_events │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│           Main Pipeline                 │
│  1. Token Fetch                         │
│  2. Session Establishment               │
│  3. API Request                         │
│  4. Event Processing                    │
│  5. Output Formatting                   │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│         Module Layer                    │
│                                         │
│  ┌──────────────┐  ┌──────────────┐   │
│  │TokenFetcher  │  │SessionManager│   │
│  └──────────────┘  └──────────────┘   │
│                                         │
│  ┌──────────────┐  ┌──────────────┐   │
│  │  APIClient   │  │EventProcessor│   │
│  └──────────────┘  └──────────────┘   │
│                                         │
│  ┌──────────────┐                      │
│  │OutputFormat  │                      │
│  └──────────────┘                      │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│      External Dependencies              │
│  - requests (HTTP)                      │
│  - json (parsing)                       │
│  - re (regex)                           │
└─────────────────────────────────────────┘
```

## Module Responsibilities

### Token Fetcher
- Fetches JavaScript file from CDN
- Extracts authentication token using regex
- Handles network errors and timeouts

### Session Manager
- Creates and manages HTTP session
- Establishes session by visiting calendar page
- Captures cookies for authenticated requests
- Implements context manager for cleanup

### API Client
- Makes authenticated requests to API
- Validates HTTP response codes
- Parses JSON responses
- Handles API-specific errors

### Event Processor
- Validates API response structure
- Extracts event data (venue, title)
- Abbreviates venue names
- Handles missing or malformed data

### Output Formatter
- Formats events in multiple formats
- Supports legacy, JSON, CSV, and plain text
- Validates format types

## Data Flow

```
JavaScript File → Token → Session → API Response → Events → Formatted Output
     (CDN)                (Cookies)   (JSON)      (Tuples)    (String)
```

## Error Handling Strategy

1. **Custom Exception Hierarchy**
   - Base: `VillagesEventError`
   - Specific: `TokenFetchError`, `SessionError`, `APIError`, `ProcessingError`

2. **Error Propagation**
   - Modules raise specific exceptions
   - Main function catches and logs errors
   - Returns appropriate exit codes

3. **Graceful Degradation**
   - Skip malformed events
   - Log warnings for non-critical issues
   - Continue processing when possible

## Configuration Management

- Centralized in `config.py`
- Constants for URLs, timeouts, mappings
- Easy to modify without code changes
- Type-safe configuration access

## Testing Strategy

### Unit Tests
- Test each module in isolation
- Mock external dependencies
- Focus on core logic

### Integration Tests
- Test complete pipeline
- Mock all HTTP requests
- Verify error handling paths
- Test all output formats

## Design Patterns

1. **Context Manager** - SessionManager for resource cleanup
2. **Strategy Pattern** - Multiple output formatters
3. **Dependency Injection** - Pass dependencies to functions
4. **Single Responsibility** - Each module has one job
5. **Fail Fast** - Validate early, raise exceptions immediately

## Performance Considerations

- Single HTTP session reused for all requests
- Minimal data transformation
- Streaming output (no buffering)
- Configurable timeouts

## Security Considerations

- No credentials stored in code
- Token extracted from public JavaScript
- HTTPS for all requests
- Proper error message sanitization
