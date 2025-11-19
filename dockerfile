# Choix de l'image de base
FROM python:3.13-slim

# Empêcher la création de fichiers .pyc et forcer l’affichage direct des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Définir le dossier principal dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier tout le projet dans l'image
COPY . /app/

# Collecter les fichiers statiques (production)
RUN python manage.py collectstatic --noinput

# Copie du script d'entrée
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Exposer un port accessible en dehors du conteneur
EXPOSE 8000

# Commande de lancement
CMD ["/app/entrypoint.sh"]