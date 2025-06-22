# rmperplexitycitations

A Python CLI tool to clean markdown content from Perplexity.ai by removing citations, URLs, and Perplexity-specific formatting.

## Project Overview

This tool processes markdown content (typically from Perplexity.ai) and strips:
- Inline citations like [1], [2], [1][3]
- Citation sections at the bottom of documents
- URLs and links
- Perplexity-specific formatting and attribution
- Extraneous formatting while preserving clean markdown structure

## Installation & Usage

The tool supports multiple installation methods:
- Virtual environment (venv) for development
- pipx for system-wide CLI installation

Input/output options:
- Read from clipboard
- Write to clipboard  
- Read from input files
- Write to output files
- Any combination of the above

## Development Environment

- Platform: macOS
- Python with venv support
- Supports pipx integration for CLI distribution

## Commands

To run linting and type checking:
```bash
# Add specific commands once determined
```

## Project Structure

```
rmperplexitycitations/
├── src/           # Source code
├── tests/         # Test files
├── requirements.txt
├── pyproject.toml # For pipx installation
└── README.md
```