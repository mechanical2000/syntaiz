# syntax=docker/dockerfile:1.4

# Utiliser l'image PyTorch stable, optimisée pour GPU CUDA 11.8
# (Cette image est uniquement disponible pour linux/amd64)
FROM --platform=linux/amd64 pytorch/pytorch:2.2.2-cuda11.8-cudnn8-runtime

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Mettre à jour pip et installer les dépendances nécessaires
RUN pip install --upgrade pip && \
    pip install transformers accelerate exllama fastapi uvicorn

# Copier le code de l'API FastAPI dans le conteneur
COPY app.py /app/app.py

# Exposer le port 8000 pour accéder à l'API
EXPOSE 8000

# Commande par défaut pour lancer l'API FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
