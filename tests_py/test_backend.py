import pytest
from backend import load_catalog, get_chapter_by_code

def test_load_catalog_contains_chapters():
    data = load_catalog()
    assert 'chapters' in data
    assert len(data['chapters']) > 0

def test_get_chapter_by_code_returns_expected_title():
    chapter = get_chapter_by_code('1.1')
    assert chapter['title'] == 'Linienkenntnisse'

def test_get_chapter_by_code_missing_raises():
    with pytest.raises(ValueError):
        get_chapter_by_code('nonexistent')
