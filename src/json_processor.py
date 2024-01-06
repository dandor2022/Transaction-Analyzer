import os
import json
from typing import Dict, List

SEPARATOR = "-----------------------------------------------------------------"


# JSON_REGEX_PATTERN = r"(\{(.*?[\n\t\s])+\})"

class JsonProcessor:
    def __init__(self, path_to_write_to: str = os.getcwd()):
        self.path_to_json_output = path_to_write_to
        self.json_db: List[Dict] = []

    def update_json_db(self, transaction: dict) -> None:
        self.json_db.append(transaction)

    def create_json_file(self):
        parent_json_dict = dict()
        parent_json_dict['Transactions'] = self.json_db
        parent_json_dict['Contracts'] = None
        parent_json_dict['Actors'] = None
        with open('output.json', 'w') as json_file:
            json.dump(parent_json_dict, json_file, indent=4)
