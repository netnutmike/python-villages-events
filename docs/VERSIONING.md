# Versioning and Dependency Management

This document describes the versioning strategy and dependency management setup for the Villages Event Scraper project.

## Versioning Strategy

This project follows [Semantic Versioning 2.0.0](https://semver.org/):

- **MAJOR** version (X.0.0): Incompatible API changes
- **MINOR** version (0.X.0): New functionality in a backward-compatible manner
- **PATCH** version (0.0.X): Backward-compatible bug fixes

### Version File

The current version is stored in the `VERSION` file at the project root. This single source of truth is used by:
- `setup.py` for package distribution
- `src/__version__.py` for runtime version access
- CI/CD workflows for release automation

### Bumping Versions

Use the provided script to bump versions:

```bash
# Bump patch version (1.0.0 -> 1.0.1)
python scripts/bump_version.py patch

# Bump minor version (1.0.0 -> 1.1.0)
python scripts/bump_version.py minor

# Bump major version (1.0.0 -> 2.0.0)
python scripts/bump_version.py major
```

The script will:
1. Update the `VERSION` file
2. Update `CHANGELOG.md` with the new version
3. Provide instructions for committing and tagging

### Manual Version Bump Process

If you prefer to bump versions manually:

1. Update the `VERSION` file with the new version number
2. Update `CHANGELOG.md`:
   - Add a new section for the version with today's date
   - Move unreleased changes to the new version section
   - Update comparison links at the bottom
3. Commit the changes:
   ```bash
   git add VERSION CHANGELOG.md
   git commit -m "chore: bump version to X.Y.Z"
   ```
4. Create and push a tag:
   ```bash
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin main --tags
   ```

## Dependency Management

### Renovate Bot (Recommended)

Renovate is configured to automatically update dependencies. It will:

- Check for updates weekly on Monday mornings
- Create PRs for dependency updates
- Auto-merge minor and patch updates for stable packages
- Require manual review for major updates
- Prioritize security updates

#### Configuration Files

- `renovate.json` - Main configuration (JSON format)
- `.github/renovate.json5` - Alternative with detailed comments (JSON5 format)

Choose one configuration file and delete the other.

#### Enabling Renovate

1. Install the [Renovate GitHub App](https://github.com/apps/renovate)
2. Grant access to your repository
3. Renovate will automatically start creating PRs

#### Renovate Features

- **Auto-merge**: Minor and patch updates are auto-merged after CI passes
- **Grouping**: Related packages (e.g., pytest plugins) are grouped together
- **Security**: Vulnerability alerts are processed immediately
- **Scheduling**: Updates run on Monday mornings to avoid disrupting weekends
- **Testing**: Runs tests before merging updates

### Dependabot (Alternative)

If you prefer GitHub's native Dependabot:

1. Keep `.github/dependabot.yml`
2. Delete `renovate.json` and `.github/renovate.json5`
3. Dependabot will automatically start creating PRs

Dependabot is simpler but has fewer features than Renovate.

### Dependency Files

- `requirements.txt` - Production dependencies
- `requirements-dev.txt` - Development dependencies (testing, linting, etc.)
- `setup.py` - Package metadata and dependencies

### Updating Dependencies Manually

```bash
# Update all dependencies to latest versions
pip install --upgrade -r requirements.txt
pip install --upgrade -r requirements-dev.txt

# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name
```

## Continuous Integration

### GitHub Actions Workflows

#### CI Workflow (`.github/workflows/ci.yml`)

Runs on every push and pull request:
- Tests on multiple OS (Ubuntu, macOS, Windows)
- Tests on multiple Python versions (3.8-3.12)
- Linting with Black and Pylint
- Type checking with MyPy
- Code coverage reporting

#### Release Workflow (`.github/workflows/release.yml`)

Runs when a version tag is pushed:
- Builds the package
- Creates a GitHub release with release notes
- Publishes to PyPI (requires `PYPI_API_TOKEN` secret)

### Setting Up PyPI Publishing

1. Create an account on [PyPI](https://pypi.org/)
2. Generate an API token in your PyPI account settings
3. Add the token as a GitHub secret named `PYPI_API_TOKEN`
4. The release workflow will automatically publish to PyPI when you push a tag

## Changelog

All notable changes are documented in `CHANGELOG.md` following the [Keep a Changelog](https://keepachangelog.com/) format.

### Changelog Sections

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes

### Updating the Changelog

Before each release, update the `[Unreleased]` section with:
- All changes since the last release
- Organized by section (Added, Changed, Fixed, etc.)
- Clear, user-focused descriptions

## Release Process

1. **Prepare the release**:
   ```bash
   # Bump version
   python scripts/bump_version.py [major|minor|patch]
   
   # Review and update CHANGELOG.md
   # Add details about changes in this release
   ```

2. **Commit and tag**:
   ```bash
   git add VERSION CHANGELOG.md
   git commit -m "chore: bump version to X.Y.Z"
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin main
   git push origin vX.Y.Z
   ```

4. **Automated release**:
   - GitHub Actions will automatically build and publish
   - A GitHub release will be created with release notes
   - Package will be published to PyPI (if configured)

## Version Information in Code

Access version information at runtime:

```python
from src.__version__ import __version__, __title__, __description__

print(f"{__title__} version {__version__}")
```

Or from the command line:

```bash
python villages_events.py --version
```

## Best Practices

1. **Always update CHANGELOG.md** when making changes
2. **Use semantic versioning** consistently
3. **Test before releasing** - CI must pass
4. **Review dependency updates** before merging
5. **Keep dependencies up to date** for security
6. **Document breaking changes** clearly in CHANGELOG
7. **Use version tags** for all releases
8. **Never edit released versions** - create a new version instead

## Troubleshooting

### Renovate not creating PRs

- Check that the Renovate app is installed and has access
- Review the Renovate dashboard in your repository
- Check the configuration file for syntax errors

### CI failing on dependency updates

- Review the CI logs to identify the issue
- Test locally with the updated dependencies
- May need to update code for breaking changes

### Version conflicts

- Ensure VERSION file is the single source of truth
- Regenerate `src/__version__.py` if needed
- Check that setup.py reads from VERSION file correctly
