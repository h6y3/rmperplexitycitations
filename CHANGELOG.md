# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.0.0] - 2025-01-22

### Added
- Initial release of rmperplexitycitations
- CLI tool to remove citations and URLs from Perplexity.ai markdown content
- Support for inline citations removal (`[1]`, `[2]`, `[1][3]` patterns)
- Citation sections removal at document bottom
- Perplexity branding and marketing text removal
- Flexible input/output options:
  - Clipboard to clipboard (default)
  - File to file
  - File to clipboard
  - Clipboard to file
- Cross-platform support (macOS, Linux, Windows)
- pipx installation support
- Comprehensive test suite
- Command-line interface with `click`
- Clipboard integration with `pyperclip`

### Features
- `--input-file` / `-i` option for file input
- `--output-file` / `-o` option for file output
- `--clipboard-input` / `-ci` flag to force clipboard input
- `--clipboard-output` / `-co` flag to force clipboard output
- Preserves markdown formatting (headers, lists, code blocks, emphasis)
- Handles multiple citation formats and patterns
- Automatic detection of "Sources", "References", and "Citations" sections
- Clean error handling and user-friendly messages

### Documentation
- Comprehensive README with installation and usage examples
- MIT License
- Contributing guidelines
- Code of conduct
- GitHub issue templates
- Pull request template
- CI/CD workflow with GitHub Actions

### Development
- Python 3.8+ support
- Type hints and docstrings
- Unit tests with unittest framework
- Cross-platform testing matrix
- Security scanning with bandit
- Code formatting with black
- Import sorting with isort
- Linting with flake8
- Type checking with mypy

---

## Template for future releases

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Now removed features

### Fixed
- Bug fixes

### Security
- Security improvements
```