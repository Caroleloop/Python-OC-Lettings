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
$PYTHON -m coverage report

# Récupérer la couverture totale avec grep/awk
COV=$($PYTHON -m coverage report | grep TOTAL | awk '{print int($4)}')

REQUIRED=80
echo "Coverage found: $COV%, required: $REQUIRED%"

if [ "$COV" -lt "$REQUIRED" ]; then
  echo "Coverage is $COV%, required is $REQUIRED%"
  exit 1
fi

echo "Coverage OK: $COV%"