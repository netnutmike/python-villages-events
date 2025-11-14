# Contributing to Villages Event Scraper

Thank you for your interest in contributing! Here are some guidelines to help you get started.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/villages-event-scraper.git
cd villages-event-scraper
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install development dependencies:
```bash
make install-dev
```

## Running Tests

Run all tests:
```bash
make test
```

Run tests with coverage:
```bash
make test-cov
```

## Code Quality

Format code with Black:
```bash
make format
```

Run linters:
```bash
make lint
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all public functions and classes
- Keep line length to 100 characters
- Use meaningful variable and function names

## Testing

- Write unit tests for all new functionality
- Maintain or improve code coverage
- Use mocks for external dependencies (HTTP requests)
- Follow the existing test structure

## Pull Request Process

1. Create a new branch for your feature or bugfix
2. Make your changes and add tests
3. Ensure all tests pass and linters are happy
4. Update documentation if needed
5. Submit a pull request with a clear description

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Add detailed description if needed

## Questions?

Feel free to open an issue for any questions or concerns.
