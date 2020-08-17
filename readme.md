# NomadPython project

### Notice pour reproduire la création de ce projet. Si besoin de télécharger ce repo uniquement, passer directement à l'étape 8.

##### Ce projet s'inscrit dans une démarche de contournement des machines où Python ne peut pas être installé pour des raisons professionnelles. ATTENTION : Guide pour Windows 10.

## Etape 1 :

Installer Python sur une machine qui peut installer Python. Exemple, un ordinateur personnel.
Penser à ajouter Python au PATH (variables d'environnement) pour ne pas se faire surprendre à la prochaine étape.

## Etape 2 :

Faire (dans CMD ou Powershell) un `pip install virtualenv` ou `python -m pip install virtualenv` pour récupérer l'utilitaire de création d'environnement virtuel.

## Etape 3 :

Faire (dans CMD ou Powershell) un `virtualenv <NOM_DE_L_ENVIRONNEMENT_VIRTUEL>`.

## Etape 4 :

Lancer l'environnement virtuel : Faire (dans CMD ou Powershell) un `<NOM_DE_L_ENVIRONNEMENT_VIRTUEL>\Scripts\activate`.

## Etape 5 :

S'assurer que python fonctionne avec la commande `python`. Quitter le compileur avec `quit()`.

## Etape 6 :

Installer les packages souhaités avec la commande suivante, soit avec `pip`, soit avec `python -m pip` :
`pip install --target=<NOM_DE_L_ENVIRONNEMENT_VIRTUEL>\Scripts\ --ignore-installed <NOM_DU_PACKAGE>`.

Possibilité de créer un dossier spécifique dans Scripts, et d'en faire la source par la suite. La commande ici reflète le contenu de ce repository git.

## Etape 7 :

Push le dossier sur git, ne rien ignorer de particulier, surtout ne pas ignorer l'environnement virtuel (éventuellement créer un fichier .gitignore vide pour être sûr de ne pas rencontrer de soucis).

## Etape 8 :

Pull le dossier via git sur la machine qui ne peut pas installer Python.

## Etape 9 :

Dans le dossier contenant l'environnement virtuel, refaire les étapes 4 et 5 pour s'assurer que python fonctionne sur la nouvelle machine.

## Etape 10 :

Définir la variable d'environnement système ou user (système de préférence) PYTHONPATH avec le chemin donné en target à l'étape 6. Exemple : C:\Users\Moi\Documents\MonEnvironnementVirtuel\Scripts\ .

Si l'accès aux variables d'environnement est verrouillé, une solution de contournement existe via CMD.

Dans CMD, taper `echo %PATH%` pour voir les chemins attribués au PATH. Taper `echo %PYTHONPATH%` pour voir si quelque chose est déjà dans PYTHONPATH, pour ne pas l'écraser.

Pour __ajouter__ une variable au PATH via CMD, voici la commande (avec le chemin en exemple) :
`set PATH=%PATH%;C:\Users\Moi\Documents\MonEnvironnementVirtuel\Scripts\`

Pour __écraser__ une variable au PATH via CMD, voici la commande (avec le chemin en exemple) :
`set PYTHONPATH=C:\Users\Moi\Documents\MonEnvironnementVirtuel\Scripts`

## Etape 11 :

Maintenant, tout devrait fonctionner, répéter encore une fois les étapes 4 et 5 pour tester python, et dans le compileur, tester un des packages installés lors de l'étape 6. Liste des packages pour test via ce repository : numpy, pandas.

Pour tester les packages, dans le compileur, faire `import numpy` par exemple. Si le package n'est pas détécté, une erreur du type `ModuleNotFoundError: No module named 'numpy'` apparaîtra. Si rien n'apparait, alors le package est détécté. Pour vérification, taper `numpy.__path__`. Normalement, le chemin correspondant à l'endroit où le package est installé devrait apparaître.

####################################################################################################

Si d'autres erreurs devaient arriver, ouvrir un ticket ou me contacter à edwyn.beauvery@gmail.com.

### Possibles erreurs connues :
- <b>ModuleNotFoundError: No module named 'runpy'</b> : Ce problème vient d'un souci de création de l'environnement virtuel sur la machine actuelle.