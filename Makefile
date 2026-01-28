# Makefile pour automatiser les tâches courantes

.PHONY: help install test lint format clean docker-build docker-up k8s-deploy

help:
	@echo "Commandes disponibles:"
	@echo "  make install       - Installer les dépendances"
	@echo "  make test          - Lancer les tests"
	@echo "  make lint          - Vérifier le code"
	@echo "  make format        - Formater le code"
	@echo "  make clean         - Nettoyer les fichiers temporaires"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-up     - Lancer avec Docker Compose"
	@echo "  make k8s-deploy    - Déployer sur Kubernetes"

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=src --cov-report=html

lint:
	flake8 src/
	pylint src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

docker-build:
	docker build -t rag-it-assistant:latest -f docker/Dockerfile .

docker-up:
	docker-compose -f docker/docker-compose.yml up -d

k8s-deploy:
	kubectl apply -f kubernetes/namespace.yaml
	kubectl apply -f kubernetes/configmap.yaml
	kubectl apply -f kubernetes/secrets.yaml
	kubectl apply -f kubernetes/persistent-volume.yaml
	kubectl apply -f kubernetes/deployment.yaml
	kubectl apply -f kubernetes/service.yaml
