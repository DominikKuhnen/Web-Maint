import json
import logging
from pathlib import Path

CATALOG_PATH = Path(__file__).with_name('katalog_web_v2.json')

logger = logging.getLogger(__name__)


def load_catalog():
    """Load the JSON catalog file and return its data.

    Raises:
        RuntimeError: If the catalog file is missing or contains invalid JSON.
    """
    try:
        with CATALOG_PATH.open('r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as exc:
                logger.exception("Malformed catalog file: %s", CATALOG_PATH)
                raise RuntimeError(f"Catalog file {CATALOG_PATH} is malformed") from exc
    except FileNotFoundError as exc:
        logger.exception("Catalog file not found: %s", CATALOG_PATH)
        raise RuntimeError(f"Catalog file {CATALOG_PATH} not found") from exc

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
