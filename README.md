# Web-Maint

Einfache Weboberfläche zur Verwaltung von Weiterbildungskapiteln.

## Struktur

- `templates/` – HTML-Seiten (Start, Login, Dashboard)
- `static/` – CSS- und JavaScript-Assets
- `backend/` – serverseitige Logik
- `db/` – Datenbankschema
- `tests/` – Testfälle
- `docs/` – Dokumentation

Weitere Dateien wie `Dockerfile`, `docker-compose.yml` und `.env.example` dienen als Ausgangspunkt für Deployment und Konfiguration.

## Nutzung

Die Startseite `templates/index.html` lädt die Kapitel aus `katalog_web_v2.json` und zeigt sie als Liste an.
Die Login-Seite speichert den eingegebenen Benutzernamen lokal und leitet anschließend auf das Dashboard weiter.
