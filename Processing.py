import spacy
import pandas as pd
import json
import re


class Processor:
    """
    Class for handeling conversion and processing of txt documents
    """

    def __init__(self, nlp, error_method = 'replace'):
        self.error_method = error_method
        self.nlp = nlp


    def extract_string(self, filepath):
        """Takes a plaintext file as input and returns a string of text"""
        with open(filepath, 'rb') as f:
            contents = f.read()

        contents = contents.decode(encoding="utf-8", errors = self.error_method)
        
        contents = contents.replace('\n', '') 

        return contents


    def named_entity_extraction(self, contents):
        """
        Takes a string and returns a dataframe of named entities
        """
        doc = self.nlp(contents)

        text = [entity.text for entity in doc.ents]
        labels = [entity.label_ for entity in doc.ents]

        df = pd.DataFrame({'text': text, 'labels':labels})

        return df


    def create_exportable(self, filename, contents, named_entities):
        """
        Takes the documnet name, text and named_entities and returns a dict
        """
        people = named_entities['text']\
            .where(named_entities['labels'] == 'PERSON')\
            .dropna()\
            .tolist()
        places = named_entities['text']\
            .where(named_entities['labels'] == 'GPE')\
            .dropna()\
            .tolist()
        institutions = named_entities['text']\
            .where(named_entities['labels'] == 'ORG')\
            .dropna()\
            .tolist()
        emails = re.findall('\S+@\S+', contents)

        export_dict = {
            'filename': filename,
            'contents': contents,
            'people': people,
            'places': places,
            'institutions': institutions,
            'emails': emails
        }

        return export_dict


    def process(self, filepath, export = True):
        """
        Takes a plaintext documnet as input and exports a JSON file
        """
        print(filepath)

        contents = self.extract_string(filepath)
        print('\tText extracted')

        named_entities = self.named_entity_extraction(contents)
        print('\tNamed entities extracted')

        export_dict = self.create_exportable(filepath, contents, named_entities)
        print('\tExportable created')

        if export == True:
            with open(filepath[:-4] + '.json', 'w') as outfile:
                json.dump(export_dict, outfile)

        else:
            return export_dict
