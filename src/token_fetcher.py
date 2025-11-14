"""Token fetcher module for extracting authentication token.

This module fetches the main.js file from The Villages CDN and extracts
the dp_AUTH_TOKEN value using regex pattern matching.
"""

import re
import requests
from src.exceptions import TokenFetchError


def fetch_auth_token(js_url: str, timeout: int = 10) -> str:
    """
    Fetches main.js and extracts the dp_AUTH_TOKEN.
    
    Args:
        js_url: URL to the JavaScript file
        timeout: Request timeout in seconds
        
    Returns:
        Extracted token in format "Basic <base64_string>"
        
    Raises:
        TokenFetchError: If fetching or extraction fails
    """
    try:
        # Fetch the JavaScript file
        response = requests.get(js_url, timeout=timeout)
        response.raise_for_status()
        js_content = response.text
        
    except requests.exceptions.Timeout:
        raise TokenFetchError(f"Timeout while fetching JavaScript file from {js_url}")
    except requests.exceptions.RequestException as e:
        raise TokenFetchError(f"Failed to fetch JavaScript file from {js_url}: {e}")
    
    # Extract the dp_AUTH_TOKEN using regex
    # Pattern matches: dp_AUTH_TOKEN = "Basic <base64>" or dp_AUTH_TOKEN="Basic <base64>"
    pattern = r'dp_AUTH_TOKEN\s*=\s*["\']Basic\s+([a-zA-Z0-9+/=]+)["\']'
    match = re.search(pattern, js_content)
    
    if not match:
        raise TokenFetchError(
            f"Failed to extract dp_AUTH_TOKEN from JavaScript file. "
            f"Pattern not found in response."
        )
    
    # Reconstruct token in "Basic <base64>" format
    base64_token = match.group(1)
    auth_token = f"Basic {base64_token}"
    
    return auth_token
