
import pytest
from src.core.content_generator import ContentGenerator

def test_generate_content():
    generator = ContentGenerator()
    content = generator.generate_content("Test Topic", 100, "formal")
    assert isinstance(content, str)
    assert len(content) > 0

def test_refine_content():
    generator = ContentGenerator()
    original_content = "This is a test content."
    refined_content = generator.refine_content(original_content, {"simplify": True})
    assert isinstance(refined_content, str)
    assert len(refined_content) > 0
    assert refined_content != original_content
