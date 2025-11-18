#!/bin/bash
set -e

# Détecte python disponible
PYTHON=python3


echo "Using $PYTHON"

# Lancer les tests avec coverage
echo "Running tests with coverage..."
$PYTHON -m coverage run -m pytest

# Générer le rapport texte
echo "Generating coverage report..."
$PYTHON -m coverage report --fail-under=80

echo "Coverage threshold met"
