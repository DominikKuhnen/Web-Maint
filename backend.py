import json
from pathlib import Path

CATALOG_PATH = Path(__file__).with_name('katalog_web_v2.json')

def load_catalog():
    """Load the JSON catalog file and return its data."""
    with CATALOG_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)

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
