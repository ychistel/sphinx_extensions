Numérotation automatique d'exercices
=======================================

Quand on propose plusieurs exercices, la difficulté de s'y retrouver s'accroit avec le nombre d'exercices. De plus, la numérotation manuelle est à éviter pour éviter toute erreur de numérotation.

Cela m'a amené à réfléchir sur une numérotation automatiquedes exercices. J'ai donc créé une directive ``exercice`` qui contient l'énoncé de l'exercice. Lors de la compilation, les exercices sont numérotés automatiquement sur toutes les pages du projet.

Par exemple, si j'ajoute 2 exercices avec cette directive, on obtient le code suivant:

.. code-block:: reST

    .. exercice::

        Le premier exercice.

    .. exercice::

        Le second exercice.

Ce qui donne après compilation du projet:

.. exercice::

    Le premier exercice.

.. exercice::

    Le second exercice.