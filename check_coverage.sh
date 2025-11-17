# Exit si une commande échoue
set -e

# Chemin vers python du venv
PYTHON="./venv/Scripts/python.exe"

# Lancer les tests avec coverage
echo "Running tests with coverage..."
$PYTHON -m coverage run -m pytest

# Générer le rapport texte
echo "Generating coverage report..."
$PYTHON -m coverage report

# Récupérer le pourcentage de couverture de la dernière ligne
COV=$($PYTHON -m coverage report | tail -n1 | awk '{print $4}' | sed 's/%//' | awk '{printf "%d\n",$1}')
REQUIRED=80


# Vérifier si la couverture est suffisante
compare=$(echo "$COV >= $REQUIRED" | bc)
if [ "$compare" -ne 1 ]; then
  echo "Coverage is $COV%, required is $REQUIRED%"
  exit 1
fi

echo "Coverage OK: $COV%"