# rmperplexitycitations

A Python CLI tool to clean markdown content from Perplexity.ai by removing citations, URLs, and Perplexity-specific formatting.

## What it does

This tool processes markdown content (typically from Perplexity.ai) and removes:
- ✂️ Inline citations like `[1]`, `[2]`, `[1][3]`
- 🗑️ Citation sections at the bottom of documents  
- 🔗 URLs and reference links
- 🏷️ Perplexity-specific branding and attribution
- 🧹 Extraneous formatting while preserving clean markdown structure

## Before & After Example

**Input (from Perplexity):**
```markdown
# California mDL Guide

The TSA accepts mobile licenses[1][2] at 27 airports.

- LAX accepts mDL[3]
- SFO supports the system[4]

Sources
[1] https://example.com/tsa-announcement
[2] https://perplexity.ai/mobile-licenses  
[3] https://lax.com/mobile-id
```

**Output (cleaned):**
```markdown
# California mDL Guide

The TSA accepts mobile licenses at 27 airports.

- LAX accepts mDL
- SFO supports the system
```

## Installation

### Option 1: pipx (Recommended)
```bash
pipx install git+https://github.com/h6y3/rmperplexitycitations
```

### Option 2: pip with virtual environment
```bash
git clone https://github.com/h6y3/rmperplexitycitations
cd rmperplexitycitations
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

## Usage

### Default: Clipboard to Clipboard
```bash
# Copy Perplexity content to clipboard, then run:
rmperplexitycitations
# Cleaned content is now in your clipboard
```

### File Input/Output
```bash
# File to file
rmperplexitycitations -i input.md -o output.md

# File to clipboard  
rmperplexitycitations -i input.md

# Clipboard to file
rmperplexitycitations -o output.md
```

### All Options
```bash
rmperplexitycitations --help
```

```
Usage: rmperplexitycitations [OPTIONS]

  Remove citations and URLs from Perplexity.ai markdown content.

Options:
  -i, --input-file PATH    Input file path (default: read from clipboard)
  -o, --output-file PATH   Output file path (default: write to clipboard)  
  -ci, --clipboard-input   Force read from clipboard
  -co, --clipboard-output  Force write to clipboard
  --help                   Show this message and exit.
```

## Features

- 📋 **Flexible I/O**: Any combination of clipboard and file input/output
- 🎯 **Preserves formatting**: Keeps headers, lists, code blocks, emphasis
- ⚡ **Fast processing**: Handles large documents efficiently  
- 🖥️ **Cross-platform**: Works on macOS, Linux, and Windows
- 🔧 **Easy installation**: Single command with pipx
- ✅ **Well tested**: Comprehensive test suite

## Requirements

- Python 3.8+
- macOS, Linux, or Windows
- Dependencies: `pyperclip`, `click` (installed automatically)

## Development

### Setup
```bash
git clone https://github.com/h6y3/rmperplexitycitations
cd rmperplexitycitations
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run tests
```bash
python -m unittest tests.test_main -v
```

### Run from source
```bash
python src/main.py --help
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Why this tool?

Perplexity.ai generates excellent research content, but the citations and references can clutter the markdown when you want to use the content elsewhere. This tool preserves the valuable information while removing the academic formatting, giving you clean, readable markdown perfect for documentation, notes, or further editing.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.