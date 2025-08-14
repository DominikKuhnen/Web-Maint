const fs = require('fs');
const path = require('path');

describe('katalog_web_v2.json', () => {
  const filePath = path.join(__dirname, '..', 'katalog_web_v2.json');
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

  test('contains chapters array', () => {
    expect(Array.isArray(data.chapters)).toBe(true);
    expect(data.chapters.length).toBeGreaterThan(0);
  });

  test('every chapter has code and title', () => {
    for (const chapter of data.chapters) {
      expect(chapter).toHaveProperty('code');
      expect(chapter).toHaveProperty('title');
    }
  });
});
