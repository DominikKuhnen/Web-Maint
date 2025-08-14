import json
from pathlib import Path
import sys

import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))
import backend

@pytest.fixture
def catalog_path(tmp_path, monkeypatch):
    fixture = Path(__file__).with_name('catalog_fixture.json')
    tmp_file = tmp_path / 'catalog.json'
    tmp_file.write_text(fixture.read_text(encoding='utf-8'), encoding='utf-8')
    monkeypatch.setattr(backend, 'CATALOG_PATH', tmp_file)
    return tmp_file


def test_load_catalog_contains_chapters(catalog_path):
    data = backend.load_catalog()
    assert 'chapters' in data
    assert len(data['chapters']) > 0


def test_get_chapter_by_code_returns_expected_title(catalog_path):
    chapter = backend.get_chapter_by_code('1.1')
    assert chapter['title'] == 'Linienkenntnisse'


def test_get_chapter_by_code_missing_raises(catalog_path):
    with pytest.raises(ValueError):
        backend.get_chapter_by_code('nonexistent')


def test_get_chapter_by_code_with_missing_chapters(tmp_path, monkeypatch):
    tmp_file = tmp_path / 'catalog.json'
    tmp_file.write_text('{}', encoding='utf-8')
    monkeypatch.setattr(backend, 'CATALOG_PATH', tmp_file)
    with pytest.raises(ValueError):
        backend.get_chapter_by_code('1.1')


def test_load_catalog_malformed_json(tmp_path, monkeypatch):
    tmp_file = tmp_path / 'bad.json'
    tmp_file.write_text('{not valid', encoding='utf-8')
    monkeypatch.setattr(backend, 'CATALOG_PATH', tmp_file)
    with pytest.raises(json.JSONDecodeError):
        backend.load_catalog()
