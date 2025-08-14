# Platzhalter für Docker-Konfiguration
FROM node:18-alpine
WORKDIR /app
COPY . .
CMD ["node", "backend/app.js"]
