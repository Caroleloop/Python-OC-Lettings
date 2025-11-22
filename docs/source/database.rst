Base de données et modèles
==========================

Modèle Profile
--------------

- user_id : relation vers User
- favorite_city : ville préférée

Modèle Address
--------------

- number, street, city, state, zip_code

Modèle Letting
--------------

- title : nom de la location
- address : relation vers Address

Schéma simplifié
----------------

Profile --> User  
Letting --> Address