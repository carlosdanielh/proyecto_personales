from pathlib import Path
import json

PATH_DATA = str(Path.cwd() / 'proyecto_personales' / 'data' / 'estudies.json')


class TheFile():
    def __init__(self, data):
        self.new_data = data
        if Path(PATH_DATA).exists():
            self.update_json_file()
        else:
            self.write_data_to_json_file(self.new_data)

    def update_json_file(self):
        with open(PATH_DATA, 'r') as file:
            data = json.load(file)
            data.update(self.new_data)
            self.write_data_to_json_file(data)

    def write_data_to_json_file(self, the_data):
        with open(PATH_DATA, 'w') as file:
            json.dump(the_data, file, indent=4)
