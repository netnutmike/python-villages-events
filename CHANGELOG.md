# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-11-16

### Added
- Initial release of Villages Event Scraper
- Fetch events from The Villages API
- Support for multiple output formats (Meshtastic, JSON, CSV, Plain)
- Configurable output fields with dot notation support
- Date range filtering (today, tomorrow, this-week, next-week, this-month, next-month, all)
- Category filtering (entertainment, arts-and-crafts, health-and-wellness, recreation, social-clubs, special-events, sports, all)
- Location filtering (town-squares, specific venues, all)
- Venue abbreviation support
- YAML configuration file support
- Command-line interface with argparse
- Comprehensive test suite with 128+ tests
- Documentation and examples

### Security
- Secure token fetching and session management
- Input validation for all user-provided parameters

[Unreleased]: https://github.com/yourusername/villages-event-scraper/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/villages-event-scraper/releases/tag/v1.0.0
