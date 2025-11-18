#!/bin/bash
set -e

# Détecte python disponible
if command -v python3 &>/dev/null; then
    PYTHON=python3
else
    PYTHON=python
fi

echo "Using $PYTHON"

# Lancer les tests avec coverage
echo "Running tests with coverage..."
$PYTHON -m coverage run -m pytest

# Générer le rapport texte
echo "Generating coverage report..."
$PYTHON -m coverage report --fail-under=80

echo "Coverage threshold met"