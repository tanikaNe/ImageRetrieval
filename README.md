# Description
 Content-based Image Retrieval System was created to 
 find similar images in the specified directories using a query image

## Start
 1. Open ImageRetrieval file 
 2. Install requirements using `pip install -r requirements.txt`
 3. Activate the virtual environment using `source venv/bin/activate`   
 4. Run the code using command `python src/runner.py`


Might need additional dependencies on Windows OS


## Usage
### Main Window
 1. drop zone - place to drop a query photo
 2. confirm button - search for results for the uploaded image
 3. directories button - opens dialog with indexed directories to be analysed
 4. results view - display either

    - info with no results
    - clickable top 5 results - after click opens dialog with image in higher resolution
    
### Directories dialog
 Dialog allows managing indexed directories:
 1. preview already indexed directories
 2. remove each of above
 3. add new directory to index
