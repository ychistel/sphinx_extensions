Éditeur Python pour Sphinx
===========================

.. _CodeMirror: https://codemirror.net/
.. _Pyodide: https://pyodide.org/en/stable/index.html

L'extension utilise différents scripts javascript pour créer l'éditeur:

-   CodeMirror_ pour la partie éditeur de texte.
-   Pyodide_ pour l'exécution du code Python.  

Ajouter un éditeur de texte
----------------------------

L'ajout d'un éditeur de code vide se fait avec la directive ``pyscript`` sans aucune option.

.. code-block:: reST

    .. pyscript::

Avec cette directive, on obtient l'éditeur de code suivant :

.. pyscript::

Cet éditeur se décompose en 3 parties.

-   Les boutons d'actions
-   Le corps de l'éditeur pour saisir le code
-   La sortie qui affiche le résultat du code

#.  La partie qui contient les boutons permet d'agir sur l'éditeur:

    -   Le bouton ``Run`` pour lancer l'exécution du code Python.
    -   Le bouton ``Clear Editor`` pour effacer le contenu de l'éditeur.
    -   Le bouton ``Clear Output`` pour effacer les résultats du code exécuté.
    -   Le bouton ``Save`` pour enregistrer le code dans un fichier python.
    -   Le bouton ``Lines +`` pour agrandir l'éditeur.
    -   Le bouton ``Lines -`` pour le réduire.

#.  Le corps de l'éditeur contient le code Python à exécuter. On peut saisir, modifier et effacer le code dans cette partie.

#.  La sortie affiche le résultat de l'exécution du code.

Ajouter un éditeur pré-rempli
------------------------------

Le principal intérêt de cet éditeur est de pouvoir insérer du code Python avant la compilation du document. Ceci est réalisé en ajoutant dans la directive ``pyscript`` le code Python en tant que contenu. On donne l'exemple suivant:

.. code-block::

    .. pyscript::
    
        t = [i**2+1 for i in range(5)]
        print(t)

Après la compilation, le document contient l'éditeur affiché ci-après.

.. pyscript::
    
        t = [i**2+1 for i in range(5)]
        print(t)

On peut également insérer un code Python issu d'un fichier. Cela se réalise en ajoutant des options dans la directive ``pyscript``. Comme exemple, on ajoute le code d'un fichier nommé ``test.py`` précédé du chemin d'accès.

.. code-block:: reST
    
    .. pyscript::
        :file: ../python/test.py

On obtient dans ce cas l'éditeur avec le contenu du fichier Python:

.. pyscript::
    :file: ../python/test.py

Quelques options
-----------------------------

La directive ``pyscript`` possède quelques options.

-   ``:file:`` qui permet de charger le contenu d'un fichier en tant que contenu de l'éditeur.
-   ``:class:`` qui permet d'ajouter le nom d'une classe ``CSS`` définie dans le fichier ``custom.css``.
-   ``:title:`` qui ajoute un titre au-dessus de l'éditeur.

On peut par exemple reprendre l'exemple précédent en lui ajoutant un titre, nue classe et une hauteur.

.. code-block:: reST

    .. pyscript::
        :file: ../python/test.py
        :title: Occurrences dans un tableau
        :class: prog

L'éditeur ci-dessous montre le résultat de la directive précédente.

.. pyscript::
    :file: ../python/test.py
    :title: Occurrences dans un tableau
    :class: prog