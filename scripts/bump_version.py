#!/usr/bin/env python3
"""
Version bumping script for Villages Event Scraper.

Usage:
    python scripts/bump_version.py [major|minor|patch]
"""

import sys
import re
from pathlib import Path


def read_version():
    """Read current version from VERSION file."""
    version_file = Path(__file__).parent.parent / "VERSION"
    with open(version_file, "r", encoding="utf-8") as f:
        return f.read().strip()


def write_version(version):
    """Write new version to VERSION file."""
    version_file = Path(__file__).parent.parent / "VERSION"
    with open(version_file, "w", encoding="utf-8") as f:
        f.write(f"{version}\n")


def parse_version(version_string):
    """Parse version string into major, minor, patch components."""
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version_string)
    if not match:
        raise ValueError(f"Invalid version format: {version_string}")
    return tuple(map(int, match.groups()))


def bump_version(version_string, bump_type):
    """Bump version based on type (major, minor, patch)."""
    major, minor, patch = parse_version(version_string)
    
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}. Use major, minor, or patch.")
    
    return f"{major}.{minor}.{patch}"


def update_changelog(old_version, new_version):
    """Update CHANGELOG.md with new version."""
    changelog_file = Path(__file__).parent.parent / "CHANGELOG.md"
    
    with open(changelog_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get today's date
    from datetime import date
    today = date.today().strftime("%Y-%m-%d")
    
    # Replace [Unreleased] with new version
    unreleased_section = "## [Unreleased]"
    new_section = f"## [Unreleased]\n\n## [{new_version}] - {today}"
    
    content = content.replace(unreleased_section, new_section, 1)
    
    # Update comparison links at bottom
    old_link_pattern = f"[Unreleased]: https://github.com/yourusername/villages-event-scraper/compare/v{old_version}...HEAD"
    new_links = f"""[Unreleased]: https://github.com/yourusername/villages-event-scraper/compare/v{new_version}...HEAD
[{new_version}]: https://github.com/yourusername/villages-event-scraper/compare/v{old_version}...v{new_version}"""
    
    content = content.replace(old_link_pattern, new_links)
    
    with open(changelog_file, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python scripts/bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    bump_type = sys.argv[1].lower()
    
    if bump_type not in ["major", "minor", "patch"]:
        print(f"Error: Invalid bump type '{bump_type}'. Use major, minor, or patch.")
        sys.exit(1)
    
    try:
        # Read current version
        current_version = read_version()
        print(f"Current version: {current_version}")
        
        # Bump version
        new_version = bump_version(current_version, bump_type)
        print(f"New version: {new_version}")
        
        # Write new version
        write_version(new_version)
        print(f"✓ Updated VERSION file")
        
        # Update changelog
        update_changelog(current_version, new_version)
        print(f"✓ Updated CHANGELOG.md")
        
        print(f"\nVersion bumped from {current_version} to {new_version}")
        print(f"\nNext steps:")
        print(f"1. Review and update CHANGELOG.md with changes")
        print(f"2. Commit changes: git add VERSION CHANGELOG.md && git commit -m 'chore: bump version to {new_version}'")
        print(f"3. Create tag: git tag -a v{new_version} -m 'Release v{new_version}'")
        print(f"4. Push changes: git push && git push --tags")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
