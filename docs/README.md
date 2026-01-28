# RAG IT Support Assistant

## Description
Assistant intelligent interne pour répondre aux questions des techniciens IT à partir d'un PDF de support.

## Architecture
Voir `docs/ARCHITECTURE.md` pour l'architecture détaillée.

## Installation

### Prérequis
- Python 3.10+
- Docker & Docker Compose
- Kubernetes (Lens Desktop)
- PostgreSQL

### Installation locale
```bash
# Cloner le repo
git clone <repo-url>
cd rag-it-support-assistant

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs
```

## Utilisation

### Initialiser la base de données
```bash
python src/scripts/initialize_db.py
```

### Charger le PDF dans la base vectorielle
```bash
python src/scripts/load_pdf_to_vectordb.py
```

### Lancer l'API
```bash
uvicorn src.api.main:app --reload
```

### Lancer avec Docker Compose
```bash
docker-compose up -d
```

## Tests
```bash
pytest tests/
```

## Déploiement
Voir `docs/DEPLOYMENT_GUIDE.md`

## License
MIT
