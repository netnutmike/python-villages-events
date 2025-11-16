# Quick Start Guide

## For Users

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/villages-event-scraper.git
cd villages-event-scraper

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Get today's events
python villages_events.py

# Get events in JSON format
python villages_events.py --format json

# Get events with custom fields
python villages_events.py --fields location.title,title,start.date --format json

# Check version
python villages_events.py --version
```

## For Contributors

### Setup Development Environment

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m unittest discover tests -v

# Format code
black .

# Run linting
pylint src/ villages_events.py
```

### Making Changes

```bash
# Create a branch
git checkout -b feature/my-feature

# Make changes and test
python -m unittest discover tests -v

# Commit changes
git add .
git commit -m "feat: add my feature"

# Push and create PR
git push origin feature/my-feature
```

### Bumping Version

```bash
# Bump patch version (1.0.0 -> 1.0.1)
python scripts/bump_version.py patch

# Bump minor version (1.0.0 -> 1.1.0)
python scripts/bump_version.py minor

# Bump major version (1.0.0 -> 2.0.0)
python scripts/bump_version.py major
```

## For Maintainers

### Enabling Renovate

1. Install [Renovate GitHub App](https://github.com/apps/renovate)
2. Grant access to repository
3. Renovate will automatically create PRs for dependency updates

### Creating a Release

```bash
# 1. Bump version
python scripts/bump_version.py [major|minor|patch]

# 2. Update CHANGELOG.md with release notes

# 3. Commit and tag
git add VERSION CHANGELOG.md
git commit -m "chore: bump version to X.Y.Z"
git tag -a vX.Y.Z -m "Release vX.Y.Z"

# 4. Push to GitHub
git push origin main --tags
```

### Setting Up PyPI Publishing

1. Create PyPI account and API token
2. Add `PYPI_API_TOKEN` secret to GitHub repository
3. Push a version tag to trigger automatic publishing

## Common Tasks

### Running Tests

```bash
# All tests
python -m unittest discover tests -v

# Specific test file
python -m unittest tests.test_event_processor -v

# With coverage
pytest --cov=src --cov-report=term
```

### Code Quality

```bash
# Format code
black .

# Check formatting
black --check .

# Lint code
pylint src/ villages_events.py

# Type checking
mypy src/ villages_events.py
```

### Updating Dependencies

```bash
# Check for outdated packages
pip list --outdated

# Update all packages
pip install --upgrade -r requirements.txt
pip install --upgrade -r requirements-dev.txt

# Update requirements files
pip freeze > requirements.txt
```

## Troubleshooting

### Tests Failing

```bash
# Run tests with verbose output
python -m unittest discover tests -v

# Run specific test
python -m unittest tests.test_event_processor.TestEventProcessor.test_process_events_success -v
```

### Import Errors

```bash
# Ensure virtual environment is activated
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements-dev.txt
```

### Version Issues

```bash
# Check current version
python villages_events.py --version
python -c "from src.__version__ import __version__; print(__version__)"
cat VERSION
```

## Resources

- [Full Documentation](../README.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Versioning Guide](VERSIONING.md)
- [Changelog](../CHANGELOG.md)
