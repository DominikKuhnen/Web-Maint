from main import app


def test_catalog_endpoint():
    client = app.test_client()
    resp = client.get('/catalog')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'chapters' in data


def test_chapter_endpoint_returns_title():
    client = app.test_client()
    resp = client.get('/chapter/1.1')
    assert resp.status_code == 200
    assert resp.get_json()['title'] == 'Linienkenntnisse'


def test_chapter_endpoint_not_found():
    client = app.test_client()
    resp = client.get('/chapter/unknown')
    assert resp.status_code == 404
