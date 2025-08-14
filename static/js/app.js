async function loadChapters() {
  const res = await fetch('../katalog_web_v2.json');
  if (!res.ok) throw new Error('Katalog nicht gefunden');
  const data = await res.json();
  return data.chapters || [];
}

function renderList(id, chapters) {
  const ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = '';
  chapters.forEach(ch => {
    const li = document.createElement('li');
    li.textContent = `${ch.code} – ${ch.title}`;
    ul.appendChild(li);
  });
}

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const chapters = await loadChapters();
    renderList('chapterList', chapters);
    renderList('dashChapters', chapters);
  } catch (err) {
    console.error(err);
  }

  const welcome = document.getElementById('welcome');
  if (welcome) {
    const user = localStorage.getItem('user');
    if (user) welcome.textContent = `Willkommen, ${user}!`;
  }

  const form = document.getElementById('loginForm');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const user = document.getElementById('user').value.trim();
      if (user) {
        localStorage.setItem('user', user);
        window.location.href = 'dashboard.html';
      }
    });
  }
});
