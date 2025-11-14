"""Configuration module for Villages Event Scraper.

This module contains all configuration constants including URLs,
venue mappings, HTTP settings, and valid output formats.
"""


class Config:
    """Application configuration and constants."""
    
    # URLs
    JS_URL = "https://cdn.thevillages.com/web_components/myvillages-auth-forms/main.js"
    CALENDAR_URL = "https://www.thevillages.com/calendar/#/?dateRange=today&categories=entertainment&locationCategories=town-squares"
    API_URL = "https://api.v2.thevillages.com/events/?cancelled=false&startRow=0&endRow=24&dateRange=today&categories=entertainment&locationCategories=town-squares&subcategoriesQueryType=and"
    
    # Default venue mappings
    DEFAULT_VENUE_MAPPINGS = {
        "Brownwood": "Brownwood",
        "Sawgrass": "Sawgrass",
        "Spanish Springs": "Spanish Springs",
        "Lake Sumter": "Lake Sumter"
    }
    
    # HTTP settings
    DEFAULT_TIMEOUT = 10
    USER_AGENT = "Mozilla/5.0"
    
    # Output formats
    VALID_FORMATS = ["legacy", "json", "csv", "plain"]
    DEFAULT_FORMAT = "legacy"
