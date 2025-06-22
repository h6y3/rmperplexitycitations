#!/usr/bin/env python3
"""Tests for rmperplexitycitations"""

import unittest
from src.main import remove_citations, remove_citation_sections, remove_perplexity_branding, clean_markdown


class TestCitationRemoval(unittest.TestCase):
    
    def test_remove_single_citations(self):
        """Test removal of single citations like [1], [2]"""
        text = "This is a test[1] with citations[2] in it."
        expected = "This is a test with citations in it."
        result = remove_citations(text)
        self.assertEqual(result, expected)
    
    def test_remove_multiple_citations(self):
        """Test removal of multiple citations like [1][2][3]"""
        text = "This has multiple[1][2] citations[3][4][5] here."
        expected = "This has multiple citations here."
        result = remove_citations(text)
        self.assertEqual(result, expected)
    
    def test_remove_citation_sections(self):
        """Test removal of citation sections at bottom"""
        text = """This is the main content.

More content here.

[1] https://example.com/source1
[2] https://example.com/source2
3. https://example.com/source3"""
        
        expected = """This is the main content.

More content here."""
        
        result = remove_citation_sections(text)
        self.assertEqual(result.strip(), expected.strip())
    
    def test_remove_perplexity_branding(self):
        """Test removal of Perplexity branding text"""
        text = "Great content here. Powered by Perplexity. Ask Perplexity for more."
        expected = "Great content here. "
        result = remove_perplexity_branding(text)
        self.assertEqual(result, expected)
    
    def test_clean_markdown_full(self):
        """Test full cleaning process"""
        text = """# Title

This is content[1] with citations[2][3].

More content here.

Powered by Perplexity

[1] https://example.com/source1
[2] https://example.com/source2
[3] https://example.com/source3"""
        
        expected = """# Title

This is content with citations.

More content here."""
        
        result = clean_markdown(text)
        self.assertEqual(result.strip(), expected.strip())
    
    def test_preserve_markdown_formatting(self):
        """Test that markdown formatting is preserved"""
        text = """# Header

**Bold text**[1] and *italic text*[2].

- List item 1[3]
- List item 2

```python
code_block()[4]
```

[1] https://example.com/1
[2] https://example.com/2
[3] https://example.com/3
[4] https://example.com/4"""
        
        expected = """# Header

**Bold text** and *italic text*.

- List item 1
- List item 2

```python
code_block()
```"""
        
        result = clean_markdown(text)
        self.assertEqual(result.strip(), expected.strip())


if __name__ == '__main__':
    unittest.main()