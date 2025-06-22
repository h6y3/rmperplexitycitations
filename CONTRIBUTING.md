# Contributing to rmperplexitycitations

Thank you for your interest in contributing to rmperplexitycitations! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/rmperplexitycitations.git
   cd rmperplexitycitations
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Run tests to ensure everything works:
   ```bash
   python -m unittest tests.test_main -v
   ```

## 🛠️ Development Workflow

### Setting up your development environment

1. **Fork and clone** the repository
2. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
3. **Make your changes** with tests
4. **Run tests** before committing
5. **Submit a pull request**

### Running Tests

```bash
# Run all tests
python -m unittest tests.test_main -v

# Run specific test
python -m unittest tests.test_main.TestCitationRemoval.test_remove_citations -v
```

### Testing Your Changes

Test the CLI tool manually:
```bash
# Test with file I/O
echo "Test content[1] with citations[2]." > test_input.md
python src/main.py -i test_input.md -o test_output.md
cat test_output.md

# Test with pipx installation
pipx install -e .
rmperplexitycitations --help
```

## 📝 Contribution Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Add type hints where appropriate

### Commit Messages

Use clear, descriptive commit messages:
```
feat: add support for numbered list citations
fix: handle empty clipboard gracefully  
docs: update installation instructions
test: add edge case for malformed citations
```

### Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** if appropriate
5. **Reference any related issues** in your PR description

### Pull Request Template

Your PR should include:
- Clear description of the change
- Motivation for the change
- Testing approach
- Any breaking changes
- Screenshots (if UI-related)

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, please include:
- **Clear title** describing the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Python version)
- **Sample input/output** if relevant
- **Error messages** or logs

### Feature Requests

For new features, please describe:
- **The problem** you're trying to solve
- **Proposed solution** or approach
- **Use cases** and examples
- **Alternative approaches** considered

## 🧪 Testing Guidelines

### Writing Tests

- Add tests for all new functionality
- Test both success and error cases
- Use descriptive test names
- Test edge cases and boundary conditions

### Test Structure

```python
def test_feature_description(self):
    """Test that feature works with specific input."""
    # Arrange
    input_text = "Sample input"
    expected = "Expected output"
    
    # Act
    result = function_to_test(input_text)
    
    # Assert
    self.assertEqual(result, expected)
```

## 📋 Areas for Contribution

We welcome contributions in these areas:

### 🔧 Code Improvements
- Performance optimizations
- Better error handling
- Code refactoring
- Memory usage improvements

### ✨ New Features
- Support for additional citation formats
- New output formats
- Configuration options
- Better regex patterns

### 📚 Documentation
- README improvements
- Code documentation
- Usage examples
- Tutorial content

### 🧪 Testing
- Additional test cases
- Performance benchmarks
- Integration tests
- Edge case coverage

### 🎨 User Experience
- Better error messages
- Progress indicators
- Verbose/debug modes
- Command-line improvements

## 🎯 Development Tips

### Understanding the Codebase

The main components are:
- `src/main.py` - CLI interface and main logic
- `remove_citations()` - Handles inline citation removal
- `remove_citation_sections()` - Removes reference sections
- `remove_perplexity_branding()` - Strips branding text
- `clean_markdown()` - Orchestrates the cleaning process

### Common Patterns

```python
# Regex patterns for citations
citation_pattern = r'\[(?:\d+)\](?:\[(?:\d+)\])*'
# Matches [1], [2], [1][2][3], etc.

# Section detection
if line.strip().lower() in ['sources', 'references', 'citations']:
    # Found citation section start
```

### Debugging

Add debug output:
```python
import sys
print(f"Debug: Processing {len(lines)} lines", file=sys.stderr)
```

## ❓ Questions?

- **General questions**: Open a GitHub Discussion
- **Bug reports**: Open a GitHub Issue  
- **Feature requests**: Open a GitHub Issue with the "enhancement" label
- **Security issues**: Email h6y3@users.noreply.github.com

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold this code.

## 🙏 Recognition

Contributors will be recognized in:
- CHANGELOG.md for their contributions
- README.md contributors section (if significant contributions)
- GitHub's contributor graph

Thank you for helping make rmperplexitycitations better! 🎉