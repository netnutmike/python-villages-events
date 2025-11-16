# Versioning and Renovate Setup Summary

This document summarizes the versioning and dependency management setup added to the Villages Event Scraper project.

## What Was Added

### 1. Version Management

**Files Created:**
- `VERSION` - Single source of truth for version number (currently 1.0.0)
- `src/__version__.py` - Runtime version access
- `scripts/bump_version.py` - Automated version bumping script
- `CHANGELOG.md` - Version history following Keep a Changelog format

**Files Modified:**
- `setup.py` - Now reads version from VERSION file
- `villages_events.py` - Added `--version` flag

**Usage:**
```bash
# Check version
python villages_events.py --version

# Bump version
python scripts/bump_version.py [major|minor|patch]
```

### 2. Dependency Management with Renovate

**Files Created:**
- `renovate.json` - Main Renovate configuration
- `.github/renovate.json5` - Alternative config with detailed comments
- `.github/dependabot.yml` - Alternative using GitHub Dependabot
- `requirements-dev.txt` - Development dependencies

**Features:**
- Automatic dependency updates via PRs
- Auto-merge for minor/patch updates
- Manual review for major updates
- Security vulnerability alerts
- Weekly update schedule (Monday mornings)
- Grouped updates for related packages

**To Enable:**
1. Choose either Renovate or Dependabot (delete the other config)
2. For Renovate: Install the [Renovate GitHub App](https://github.com/apps/renovate)
3. For Dependabot: It's enabled by default on GitHub

### 3. Continuous Integration

**Files Created:**
- `.github/workflows/ci.yml` - CI workflow for testing
- `.github/workflows/release.yml` - Automated release workflow

**CI Features:**
- Tests on multiple OS (Ubuntu, macOS, Windows)
- Tests on Python 3.8-3.12
- Code formatting checks (Black)
- Linting (Pylint)
- Type checking (MyPy)
- Code coverage reporting

**Release Features:**
- Automatic builds on version tags
- GitHub release creation
- PyPI publishing (requires PYPI_API_TOKEN secret)

### 4. Documentation

**Files Created:**
- `docs/VERSIONING.md` - Comprehensive versioning guide
- `docs/CONTRIBUTING.md` - Contribution guidelines
- `docs/QUICK_START.md` - Quick reference for common tasks
- `.github/PULL_REQUEST_TEMPLATE.md` - PR template

**Files Modified:**
- `README.md` - Added versioning and contributing sections
- `.gitignore` - Added coverage and build artifacts

## How It Works

### Version Bumping Workflow

1. **Bump version:**
   ```bash
   python scripts/bump_version.py patch
   ```

2. **Script automatically:**
   - Updates VERSION file
   - Updates CHANGELOG.md
   - Provides git commands to run

3. **Commit and tag:**
   ```bash
   git add VERSION CHANGELOG.md
   git commit -m "chore: bump version to 1.0.1"
   git tag -a v1.0.1 -m "Release v1.0.1"
   git push origin main --tags
   ```

4. **GitHub Actions automatically:**
   - Builds the package
   - Creates GitHub release
   - Publishes to PyPI (if configured)

### Dependency Update Workflow

1. **Renovate checks for updates** (weekly on Monday mornings)

2. **Creates PRs** for available updates:
   - Minor/patch updates: Auto-merged after CI passes
   - Major updates: Require manual review
   - Security updates: Processed immediately

3. **CI runs tests** on the PR

4. **Auto-merge or manual review** depending on update type

5. **Dependencies stay up to date** automatically

## Configuration Options

### Renovate Configuration

Edit `renovate.json` to customize:

```json
{
  "schedule": ["before 6am on Monday"],  // When to check
  "prConcurrentLimit": 5,                // Max concurrent PRs
  "automerge": true,                     // Auto-merge minor/patch
  "labels": ["dependencies"]             // PR labels
}
```

### CI Configuration

Edit `.github/workflows/ci.yml` to customize:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
```

## Best Practices

### For Version Management

1. **Always update CHANGELOG.md** when making changes
2. **Use semantic versioning** (major.minor.patch)
3. **Test before releasing** (CI must pass)
4. **Tag all releases** with `vX.Y.Z` format
5. **Never edit released versions** - create new version instead

### For Dependency Management

1. **Review major updates** before merging
2. **Keep dependencies up to date** for security
3. **Test after updates** to catch breaking changes
4. **Monitor Renovate dashboard** for issues
5. **Use version ranges** in requirements.txt

### For Contributing

1. **Create feature branches** from main
2. **Write tests** for new functionality
3. **Update documentation** as needed
4. **Follow code style** (Black, Pylint)
5. **Update CHANGELOG.md** with changes

## Quick Commands Reference

```bash
# Version Management
python villages_events.py --version              # Check version
python scripts/bump_version.py patch             # Bump patch version
python scripts/bump_version.py minor             # Bump minor version
python scripts/bump_version.py major             # Bump major version

# Development
pip install -r requirements-dev.txt              # Install dev dependencies
python -m unittest discover tests -v             # Run tests
black .                                          # Format code
pylint src/ villages_events.py                   # Lint code
mypy src/ villages_events.py                     # Type check

# Dependency Management
pip list --outdated                              # Check outdated packages
pip install --upgrade -r requirements.txt        # Update dependencies

# Git Workflow
git checkout -b feature/my-feature               # Create branch
git add . && git commit -m "feat: description"   # Commit changes
git push origin feature/my-feature               # Push branch
```

## Troubleshooting

### Renovate Not Working

- Check Renovate app is installed and has access
- Review configuration file for syntax errors
- Check Renovate dashboard in repository

### CI Failing

- Review CI logs for specific errors
- Test locally with same Python version
- Check for missing dependencies

### Version Conflicts

- Ensure VERSION file is up to date
- Regenerate src/__version__.py if needed
- Check setup.py reads from VERSION file

## Next Steps

1. **Choose dependency manager**: Keep either Renovate or Dependabot config
2. **Enable Renovate**: Install GitHub app if using Renovate
3. **Set up PyPI**: Add PYPI_API_TOKEN secret for publishing
4. **Update repository URL**: Replace `yourusername` in configs
5. **Create first release**: Tag v1.0.0 to test release workflow

## Resources

- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Renovate Documentation](https://docs.renovatebot.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)

## Support

For questions or issues:
- Check documentation in `docs/` directory
- Review CHANGELOG.md for version history
- Open an issue on GitHub
- See CONTRIBUTING.md for contribution guidelines
