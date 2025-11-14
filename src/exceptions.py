"""Custom exception classes for Villages Event Scraper.

This module defines the exception hierarchy for better error handling
throughout the application.
"""


class VillagesEventError(Exception):
    """Base exception for Villages Event Scraper."""
    pass


class TokenFetchError(VillagesEventError):
    """Raised when token fetching or extraction fails."""
    pass


class SessionError(VillagesEventError):
    """Raised when session establishment fails."""
    pass


class APIError(VillagesEventError):
    """Raised when API request fails."""
    pass


class ProcessingError(VillagesEventError):
    """Raised when event processing fails."""
    pass
