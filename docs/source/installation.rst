Installation du projet
======================

Prérequis
---------

- Python 3.6 ou supérieur
- Git
- SQLite3
- Accès au repository GitHub du projet

Cloner le dépôt
---------------

.. code-block:: bash

   git clone https://github.com/Caroleloop/Python-OC-Lettings.git
   cd Python-OC-Lettings

Créer l'environnement virtuel
-----------------------------

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

Installer les dépendances
-------------------------

.. code-block:: bash

   pip install -r requirements.txt

Lancer l'application
--------------------

.. code-block:: bash

   python manage.py runserver

Se rendre sur :

``http://localhost:8000``