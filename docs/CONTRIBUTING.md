# Contributing to Villages Event Scraper

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account

### Setting Up Development Environment

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/yourusername/villages-event-scraper.git
   cd villages-event-scraper
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Run tests to verify setup**:
   ```bash
   python -m unittest discover tests -v
   ```

## Development Workflow

### 1. Create a Branch

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test improvements
- `chore/` - Maintenance tasks

### 2. Make Your Changes

- Write clear, concise code
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Keep commits focused and atomic

### 3. Run Tests and Linting

Before committing, ensure all tests pass and code is properly formatted:

```bash
# Run all tests
python -m unittest discover tests -v

# Run with coverage
pytest --cov=src --cov-report=term

# Format code with Black
black .

# Run linting
pylint src/ villages_events.py

# Run type checking
mypy src/ villages_events.py
```

### 4. Update CHANGELOG.md

Add your changes to the `[Unreleased]` section of CHANGELOG.md:

```markdown
## [Unreleased]

### Added
- New feature description

### Fixed
- Bug fix description
```

### 5. Commit Your Changes

Write clear, descriptive commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: resolve issue with X"
```

Commit message types:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Test additions or changes
- `chore:` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub:
1. Go to the repository on GitHub
2. Click "Pull requests" → "New pull request"
3. Select your branch
4. Fill out the PR template
5. Submit the pull request

## Code Style Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use Black for code formatting (line length: 100)
- Use type hints where appropriate
- Write docstrings for all public functions and classes

### Example

```python
def process_event(event: Dict[str, Any], config: Config) -> Dict[str, str]:
    """
    Process a single event from the API response.
    
    Args:
        event: Raw event data from API
        config: Configuration object
        
    Returns:
        Processed event dictionary with extracted fields
        
    Raises:
        ProcessingError: If event data is invalid
    """
    # Implementation here
    pass
```

### Testing Guidelines

- Write tests for all new functionality
- Aim for high test coverage (>80%)
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Mock external dependencies

### Example Test

```python
def test_process_event_with_valid_data(self):
    """Test processing event with valid data."""
    # Arrange
    event = {"title": "Test Event", "location": {"title": "Test Venue"}}
    processor = EventProcessor(venue_mappings={})
    
    # Act
    result = processor.process_events({"events": [event]})
    
    # Assert
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]["title"], "Test Event")
```

## Documentation

### Updating Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add examples for new features
- Update CHANGELOG.md for all changes

### Documentation Structure

- `README.md` - Main documentation and usage guide
- `docs/VERSIONING.md` - Versioning and dependency management
- `docs/CONTRIBUTING.md` - This file
- `CHANGELOG.md` - Version history and changes

## Pull Request Process

### Before Submitting

- [ ] All tests pass
- [ ] Code is formatted with Black
- [ ] Linting passes (Pylint)
- [ ] Type checking passes (MyPy)
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Commit messages follow conventions

### PR Review Process

1. **Automated Checks**: CI will run tests on multiple platforms and Python versions
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, your PR will be merged

### After Merge

- Your changes will be included in the next release
- You'll be credited in the release notes
- Thank you for contributing!

## Reporting Issues

### Bug Reports

When reporting bugs, include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Relevant logs or error messages

### Feature Requests

When requesting features, include:
- Clear description of the feature
- Use case and motivation
- Proposed implementation (if any)
- Examples of similar features elsewhere

## Questions and Support

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Email**: For private inquiries

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other unprofessional conduct

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (GNU General Public License v3.0).

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes
- CHANGELOG.md (for significant contributions)

Thank you for contributing to Villages Event Scraper! 🎉
