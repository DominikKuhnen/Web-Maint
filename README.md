# Web-Maint

## Prerequisites

- Python 3 installed.
- Install dependencies with `pip install -r requirements.txt`.
- Ensure the `katalog_web_v2.json` file is present in the project root.

## Example Usage

```python
>>> from backend import load_catalog, get_chapter_by_code
>>> catalog = load_catalog()
>>> get_chapter_by_code("1.1")["title"]
'Linienkenntnisse'
```

## Testing

Run the test suite to verify functionality:

```bash
python3 -m pytest -q
```

