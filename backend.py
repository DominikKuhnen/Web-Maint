import json
from functools import lru_cache
from pathlib import Path

CATALOG_PATH = Path(__file__).with_name('katalog_web_v2.json')

@lru_cache(maxsize=1)
def _load_catalog_from_file():
    """Internal helper that actually reads the catalog file."""
    with CATALOG_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

def load_catalog(force_reload: bool = False):
    """Load the JSON catalog file and return its data.

    Args:
        force_reload: If ``True`` the cached catalog is discarded and the
            file is read again. This allows refreshing the cache when the
            underlying JSON file changes.
    """
    if force_reload:
        _load_catalog_from_file.cache_clear()
    return _load_catalog_from_file()

def get_chapter_by_code(code: str):
    """Return a chapter dictionary matching the given code.

    Raises:
        ValueError: If no chapter with the code exists.
    """
    catalog = load_catalog()
    for chapter in catalog.get('chapters', []):
        if chapter.get('code') == code:
            return chapter
    raise ValueError(f'chapter {code} not found')
