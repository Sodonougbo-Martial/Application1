#!/bin/bash

# Vérifier si un message de commit a été fourni
if [ -z "$1" ]; then
    echo "Erreur: Vous devez fournir un message de commit."
    exit 1
fi

# Récupérer le message de commit
commit_message="$1"

# Ajouter tous les fichiers modifiés
git add .

# Vérifier si des fichiers ont été modifiés
if [ -z "$(git status --porcelain)" ]; then
    echo "Aucun changement à commiter."
    exit 0
fi

# Commiter les changements
git commit -m "$commit_message"

# Pousser les changements vers le dépôt distant
git push origin "$(git rev-parse --abbrev-ref HEAD)"

# Vérifier si le push a réussi
if [ $? -ne 0 ]; then
    echo "Erreur lors du push vers le dépôt distant."
    exit 1
else
    echo "Push réussi !"
fi
