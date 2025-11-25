import json

file_path = "v2/storage/main.json"
data = []
try:
    with open(file_path, "r") as file:
        data = json.load(file)
except Exception as e:
    print(f"erro ao carregar arquivo json: {e}")

class data_base():
    id_current = data[-1]['id'] if data else 0
    @staticmethod
    def get_data():
        return data

    @staticmethod
    def save(new_data):
        for new_item in new_data:
            old_item = next((item for item in data if item['id'] == new_item['id']), None)
            if old_item:
                old_item.update(new_item)
            else:
                data.append(new_item)

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
