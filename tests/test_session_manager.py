"""Unit tests for session_manager module."""

import unittest
from unittest.mock import patch, Mock
from src.session_manager import SessionManager
from src.exceptions import SessionError


class TestSessionManager(unittest.TestCase):
    """Test cases for session manager functionality."""

    def test_init_creates_session(self):
        """Test that initialization creates a session."""
        manager = SessionManager()
        session = manager.get_session()
        
        self.assertIsNotNone(session)
        self.assertIn('User-Agent', session.headers)

    def test_establish_session_success(self):
        """Test successful session establishment."""
        manager = SessionManager()
        
        with patch.object(manager._session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response
            
            manager.establish_session("https://example.com/calendar")
            
            mock_get.assert_called_once()
            self.assertIn('Origin', manager._session.headers)
            self.assertIn('Referer', manager._session.headers)

    def test_establish_session_timeout(self):
        """Test timeout error during session establishment."""
        manager = SessionManager()
        
        with patch.object(manager._session, 'get') as mock_get:
            mock_get.side_effect = __import__('requests').exceptions.Timeout()
            
            with self.assertRaises(SessionError) as context:
                manager.establish_session("https://example.com/calendar")
            
            self.assertIn("Timeout", str(context.exception))

    def test_establish_session_request_exception(self):
        """Test request exception during session establishment."""
        manager = SessionManager()
        
        with patch.object(manager._session, 'get') as mock_get:
            mock_get.side_effect = __import__('requests').exceptions.RequestException("Network error")
            
            with self.assertRaises(SessionError) as context:
                manager.establish_session("https://example.com/calendar")
            
            self.assertIn("Failed to establish session", str(context.exception))

    def test_get_session_returns_session(self):
        """Test that get_session returns the session object."""
        manager = SessionManager()
        session = manager.get_session()
        
        self.assertIsNotNone(session)

    def test_get_session_after_close_raises_error(self):
        """Test that get_session raises error after close."""
        manager = SessionManager()
        manager.close()
        
        with self.assertRaises(SessionError) as context:
            manager.get_session()
        
        self.assertIn("closed", str(context.exception))

    def test_close_cleans_up_session(self):
        """Test that close properly cleans up the session."""
        manager = SessionManager()
        manager.close()
        
        self.assertIsNone(manager._session)

    def test_context_manager_closes_session(self):
        """Test that context manager properly closes session."""
        with SessionManager() as manager:
            session = manager.get_session()
            self.assertIsNotNone(session)
        
        self.assertIsNone(manager._session)

    def test_establish_session_after_close_raises_error(self):
        """Test that establish_session raises error after close."""
        manager = SessionManager()
        manager.close()
        
        with self.assertRaises(SessionError) as context:
            manager.establish_session("https://example.com/calendar")
        
        self.assertIn("closed", str(context.exception))


if __name__ == '__main__':
    unittest.main()
