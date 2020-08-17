@ECHO OFF

TITLE Configuration du Path pour Virtualenv

ECHO Verification de python
python -V -V

TIMEOUT /T 1 > NUL

ECHO Quel est le chemin de Python ?
set /p CheminPython
ECHO Quel est le chemin des packages ?
set /p CheminPackages

set PATH=%PATH%;%CheminPython%
set PYTHONPATH=%CheminPackages%

ECHO Quel est le chemin du dossier du virtualenv ?
set /p CheminVirtual

ECHO Lancement du virtualenv
%CheminVirtual%\Scripts\activate

ECHO Verification de python dans le virtualenv
python -V -V