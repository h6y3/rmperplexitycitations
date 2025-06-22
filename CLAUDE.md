# rmperplexitycitations

A Python CLI tool to clean markdown content from Perplexity.ai by removing citations, URLs, and Perplexity-specific formatting.

## Project Status

**Current Version:** 1.0.0
**Repository:** https://github.com/h6y3/rmperplexitycitations  
**Status:** Production-ready, open source, accepting contributions
**CI/CD:** GitHub Actions (minor import sorting issue needs fix)

## Project Overview

This tool processes markdown content (typically from Perplexity.ai) and strips:
- Inline citations like [1], [2], [1][3] 
- Citation sections at the bottom of documents (detects "Sources", "References", "Citations" headers)
- URLs and reference links
- Perplexity-specific branding and attribution (powered by perplexity, ask perplexity, etc.)
- Extraneous formatting while preserving clean markdown structure

## Key Technical Details

### Core Functions (src/main.py)
- `remove_citations()` - Regex pattern: `r"\[(?:\d+)\](?:\[(?:\d+)\])*"` for [1], [2], [1][3] 
- `remove_citation_sections()` - Detects "Sources" headers and citation URL patterns
- `remove_perplexity_branding()` - Removes marketing text with regex patterns
- `clean_markdown()` - Orchestrates all cleaning functions

### Installation Methods
1. **pipx (Production)**: `pipx install git+https://github.com/h6y3/rmperplexitycitations`
2. **Development**: Clone repo, create venv, `pip install -r requirements.txt`

### CLI Usage Patterns
```bash
# Default: clipboard to clipboard
rmperplexitycitations

# File combinations
rmperplexitycitations -i input.md -o output.md  # file to file
rmperplexitycitations -i input.md               # file to clipboard  
rmperplexitycitations -o output.md              # clipboard to file
```

## Development Environment

### Author Information
- **Name:** Han Yuan
- **Email:** h6y3@users.noreply.github.com  
- **GitHub:** h6y3
- **License:** MIT

### Platform Support
- **Primary:** macOS (development environment)
- **Supported:** Linux, Windows (via GitHub Actions CI)
- **Python:** 3.8+ (tested on 3.8, 3.9, 3.10, 3.11, 3.12)

### Dependencies
- **Runtime:** pyperclip>=1.8.2, click>=8.0.0
- **Development:** black, isort, flake8, mypy, bandit, safety, pytest, pre-commit

## Project Structure

```
rmperplexitycitations/
├── .github/
│   ├── ISSUE_TEMPLATE/          # Bug reports & feature requests (YAML)
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml               # Multi-platform CI/CD
├── src/
│   ├── __init__.py
│   └── main.py                  # Main CLI application
├── tests/
│   ├── __init__.py
│   └── test_main.py             # Comprehensive test suite
├── .gitignore                   # Python + project-specific exclusions
├── .pre-commit-config.yaml      # Code quality automation
├── CHANGELOG.md                 # Version history
├── CLAUDE.md                    # This file - agent knowledge base
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT license
├── README.md                    # User documentation with examples
├── pyproject.toml               # Package config + tool settings
├── requirements.txt             # Runtime dependencies
├── requirements-dev.txt         # Development dependencies
└── venv/                        # Virtual environment (excluded from git)
```

## Testing & Quality Assurance

### Test Coverage
- Unit tests for all core functions using unittest framework
- Real-world test data validation (Perplexity output samples)
- Cross-platform installation testing (pipx)
- CLI functionality testing

### CI/CD Pipeline (.github/workflows/ci.yml)
- **Matrix Testing:** 3 OS × 5 Python versions = 15 combinations
- **Linting:** black (formatting), isort (imports), flake8 (style), mypy (types)
- **Security:** bandit (code security), safety (dependency vulnerabilities) 
- **Installation:** pipx install and functionality testing

### Development Commands
```bash
# Setup development environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt

# Code quality
black src/ tests/                # Format code
isort src/ tests/                # Sort imports
flake8 src/ tests/               # Lint code
mypy src/                        # Type checking

# Testing
python -m unittest tests.test_main -v

# Run from source
python src/main.py --help
```

## Known Issues & Fixes

### CI/CD Issues Resolved
1. **Black formatting** - Fixed code style (quotes, spacing, line length)
2. **Import sorting** - Fixed with isort (alphabetical + separation)
3. **Cross-platform compatibility** - Verified on Ubuntu, Windows, macOS

### Current Status
- All core functionality working
- pipx installation tested and verified
- Real-world Perplexity content successfully processed
- Open source documentation complete

## GitHub Repository Details

### Branch Strategy
- **main** - Production branch with releases
- Feature branches for new development

### Issue Management
- Bug reports via GitHub issue templates (YAML format)
- Feature requests with priority and contribution willingness tracking
- Pull requests use structured template with testing requirements

### Release Management
- Semantic versioning (1.0.0 = initial stable release)
- CHANGELOG.md tracks all changes following keepachangelog.com format
- No automated PyPI publishing (GitHub-only distribution)

## Future Agent Context

### Important Implementation Notes
1. **Citation Patterns:** Uses comprehensive regex to handle various Perplexity citation formats
2. **Sources Detection:** Looks for "Sources", "References", "Citations" section headers (case-insensitive)
3. **Branding Removal:** Pattern-based removal of Perplexity marketing text
4. **Markdown Preservation:** Carefully preserves headers, lists, code blocks, emphasis
5. **Error Handling:** User-friendly error messages for file I/O and clipboard operations

### Configuration Files
- **pyproject.toml** - Complete package configuration with tool settings for all dev tools
- **.pre-commit-config.yaml** - Automated code quality hooks
- **requirements-dev.txt** - All development dependencies

### Testing Strategy
- Unit tests cover all core functions with edge cases
- Manual testing includes real Perplexity content
- CI tests installation on multiple platforms and Python versions

### Code Quality Standards
- Black formatting (88 char line length, double quotes)
- Import sorting with isort (alphabetical, separated standard/third-party/local)
- Type hints required (mypy checking)
- Security scanning (bandit + safety)

This project is ready for production use and external contributions. All tooling, documentation, and CI/CD is in place for collaborative development.