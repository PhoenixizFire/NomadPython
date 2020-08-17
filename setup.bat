@ECHO OFF

:: This batch file will install virtualenv and make a directory wherever requested

TITLE Installation de virtualenv

ECHO Telechargement de virtualenv via PyPi...

python -m pip install virtualenv
ECHO.
ECHO Ou creer l'environnement virtuel ?
set /p CibleChemin="Chemin complet : "
cd %CibleChemin%
ECHO.
ECHO Quel nom donner a votre environnement virtuel ?
set /p NomVenv="Nom du virtualenv : "
virtualenv %NomVenv%
ECHO.
ECHO Environnement virtuel cree
TIMEOUT /T 1 > NUL
ECHO Demarrage de l'environnement virtuel
%NomVenv%\Scripts\activate
ECHO.
TIMEOUT /T 1 > NUL
ECHO Verification de l'implementation de python dans l'environnement virtuel
python -V -V
PAUSE