# Description
 System was designed to easily using image recognition in searching similar photos to given in pre-indexed dataset.

## Start
 1. `pip install -r requirements.txt` sprawdź czy nazwa się zgadza
 2. `python runner.py` nie pamiętam gdzie to leży

## Usage
### Main Window
 1. drop zone - place to drop photo to process
 2. confirm button - confirms computation
 3. directories button - opens dialog with indexed directories
 4. results view - shows after first photo processed, shows either:

    - info with no results
    - clickable top 5 results - after click opens dialog with image in higher resolution
    
### Directories dialog
 Dialog allows managing indexed directories:
 1. preview already indexed directories
 2. remove each of above
 3. add new directory to index

