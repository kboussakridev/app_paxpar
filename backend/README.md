# création d'une application Paxpar.light
## Coté backend avec FastAPI et Poetry

Ce projet est un exemple de configuration et d'utilisation de FastAPI avec Poetry sur Windows.

## Prérequis

- Python 3.9 ou supérieur doit être installé sur votre machine.
- PowerShell (inclus par défaut avec Windows).

## Installation de Poetry

1. Ouvrez PowerShell et exécutez la commande suivante pour installer Poetry :

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```

2. Ajoutez Poetry à votre PATH :

    1. Ouvrez les Paramètres Système Avancés (recherchez "variables d'environnement" dans le menu Démarrer).
    2. Cliquez sur "Variables d'environnement".
    3. Sous "Variables système", trouvez et sélectionnez la variable "Path", puis cliquez sur "Modifier".
    4. Ajoutez un nouveau chemin : `C:\Users\<VotreNomUtilisateur>\AppData\Roaming\Python\Scripts\`.
   
       Remplacez `<VotreNomUtilisateur>` par votre nom d'utilisateur Windows.

3. Vérifiez l'installation de Poetry :

    ```powershell
    poetry --version
    ```

## Création d'un Nouveau Projet

1. Naviguez vers le répertoire où vous souhaitez créer votre projet :

    ```powershell
    cd C:\chemin\vers\votre\projet
    ```

2. Initialisez un nouveau projet :

    ```powershell
    poetry init
    ```

    Répondez aux questions pour configurer votre projet.

## Ajouter les Dépendances

Ajoutez FastAPI et Uvicorn à votre projet :

```powershell
poetry add fastapi uvicorn
```
## Créer la Structure de Votre Projet
1. Créez la structure de votre projet :

```powershell
mkdir app
New-Item -Path app\main.py -ItemType File

```
2. Ouvrez app\main.py et ajoutez le code suivant :

```python
# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


```
## Activer l'Environnement Virtuel

Poetry crée et gère automatiquement un environnement virtuel pour votre projet. Pour activer cet environnement virtuel, utilisez :

```powershell
poetry shell

```
## Lancer l'Application FastAPI
Avec l'environnement virtuel activé, lancez votre application FastAPI en utilisant Uvicorn :
```powershell
puvicorn app.main:app --reload


```
Vous devriez voir la sortie indiquant que le serveur Uvicorn est en cours d'exécution. Vous pouvez maintenant accéder à votre application à l'adresse http://127.0.0.1:8000.
## Gestion des Dépendances
Pour ajouter d'autres dépendances à votre projet, utilisez poetry add. Par exemple, pour ajouter SQLAlchemy :
```powershell
poetry add sqlalchemy

```
Pour mettre à jour les dépendances, utilisez :

```powershell
poetry update

```
