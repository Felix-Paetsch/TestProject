import webview
from .api import API
import os
import json

def main():
    api = API()
    window = webview.create_window('EasyFiles', 'http://localhost:3015/app', js_api=api, text_select=True)
    
    def on_loaded(win):
        api.register_win(win)

    webview.start(on_loaded, window) #, debug=True)

if __name__ == "__main__":
    main()
