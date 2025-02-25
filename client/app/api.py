import json
import importlib.resources
import os
from tkinter import filedialog
from appdirs import user_data_dir

APP_NAME = "EasyFiles"
APP_AUTHOR = "EasyFiles"

class API:
    def __init__(self):
        # Set up a writable user data directory.
        data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
        os.makedirs(data_dir, exist_ok=True)
        self.user_data_file = os.path.join(data_dir, "data.json")
        
        # If the user data file doesn't exist, copy the default resource.
        if not os.path.exists(self.user_data_file):
            default_data = importlib.resources.read_text("app.data", "data.json")
            with open(self.user_data_file, "w") as f:
                f.write(default_data)
        
        # Load the title from the user data file.
        try:
            with open(self.user_data_file, "r") as f:
                data = json.load(f)
                self.title = data.get("title", "Default Title")
        except (FileNotFoundError, json.JSONDecodeError):
            self.title = "Default Title"

    def save_title(self, new_title):
        self.title = new_title
        with open(self.user_data_file, "w") as f:
            json.dump({"title": self.title}, f)
        return self.title

    def get_title(self):
        return self.title
    
    def execute(self, code):
        namespace = {"result": None}
        exec(code, namespace)
        return namespace["result"]
    
    def register_win(self, win):
        self._win = win

    def choose_new_folder(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return
        items = []
        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)
            item_type = "directory" if os.path.isdir(full_path) else "file"
            items.append({"name": item, "type": item_type})
        # Use json.dumps to properly escape values for JS
        js_call = f"server_choice_response({json.dumps(folder_path)}, {json.dumps(items)})"
        self._win.evaluate_js(js_call)
        self.current_folder = folder_path