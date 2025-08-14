from flask import Flask, jsonify, abort
from backend import load_catalog, get_chapter_by_code

app = Flask(__name__)

@app.route('/catalog')
def catalog():
    """Return the entire catalog as JSON."""
    return jsonify(load_catalog())

@app.route('/chapter/<code>')
def chapter(code):
    """Return a single chapter by its code."""
    try:
        data = get_chapter_by_code(code)
    except ValueError:
        abort(404, description=f'chapter {code} not found')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
