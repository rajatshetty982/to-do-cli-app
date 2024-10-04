import json
import os


class DataHandler:
    def __init__(self):
        self.data_dir = "data"
        self.file_path = os.path.join(self.data_dir, "tasks.json")
        self._ensure_data_file()

    def _ensure_data_file(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.file_path):
            self.save_tasks([])

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_tasks(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=2)
