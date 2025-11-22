Déploiement
===========

Déploiement via Render
----------------------

Variables d'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~

::

   DEBUG=False
   ALLOWED_HOSTS=<url>
   SENTRY_DSN=<optionnel>

Commande de build
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Commande de démarrage
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT

Mise à jour automatique
-----------------------

Selon la configuration Render :
   Render ne déploie pas à chaque commit.
   Le déploiement n’est déclenché que lorsque les checks CI passent avec succès GitHub Actions.

À chaque push GitHub, Render :

1. re-clone le dépôt  
2. installe les dépendances  
3. applique les migrations  
4. collecte les fichiers statiques  
5. redémarre l'application  