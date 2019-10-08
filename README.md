# Science-NLP
A project designed to demonstrate NLP techniques, like named entity recognition, topic modeling, and data engineering flows, like converting PDF documents to `.txt` files. 

I store my personal collection of publications, (mostly clustered around space science and related fields) in the `pdf_files` folder.
The `process_and_store.py` script converts these pdf files to `.txt` files, stores them in the `txt_files` folder, and proceeds to process them using the Processor object contained in the `Processing.py` file. It then collects all the data created and stores it as a JSON file.

## To use this repo for your own collection of PDF documents:
### First clone the repo

```git clone https://github.com/mkirby1995/Science-NLP```

### Then run `process_and_store.py`

```python process_and_store.py```

#### Note: It might be in the users interest to delete all the `.pdf` files and `.txt` files contained in the `txt_files` and `pdf_files` folders, along with `documents.json` before doing this with their own PDF documents.
