import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import backend
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


def test_load_catalog_uses_cache(monkeypatch):
    """Successive calls should not reread the file."""
    opens = 0
    from pathlib import Path
    original_open = Path.open

    def counting_open(self, *args, **kwargs):
        nonlocal opens
        if self == backend.CATALOG_PATH:
            opens += 1
        return original_open(self, *args, **kwargs)

    monkeypatch.setattr(Path, "open", counting_open)

    # Ensure cache is empty and first call reads the file
    load_catalog(force_reload=True)
    assert opens == 1

    # Subsequent calls should use the cached data
    load_catalog()
    get_chapter_by_code('1.1')
    assert opens == 1
