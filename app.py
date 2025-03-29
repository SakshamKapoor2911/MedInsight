from flask import Flask, send_from_directory, abort
from flask_cors import CORS
import os
from database import Database

class HooHacksApp:
    def __init__(self):
        self.app = Flask(__name__, static_folder="medLama/out", static_url_path="/")
        CORS(self.app)
        self.database = Database()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            index_path = os.path.join(self.app.static_folder, "index.html")
            return send_from_directory(self.app.static_folder, "index.html") if os.path.exists(index_path) else abort(404)

        @self.app.route('/<path:path>')
        def serve_static_files(path):
            file_path = os.path.join(self.app.static_folder, path)
            return send_from_directory(self.app.static_folder, path) if os.path.exists(file_path) else self.index()

        # @self.app.errorhandler(404)
        # def not_found(e):
        #     index_path = os.path.join(self.app.static_folder, "index.html")
        #     return send_from_directory(self.app.static_folder, "index.html") if os.path.exists(index_path) else abort(404)

    def run(self, host="0.0.0.0", port=5000, debug=False):
        self.app.run(host="127.0.0.1" if debug else host, port=port, debug=debug)

app = HooHacksApp().app

if __name__ == "__main__":
    HooHacksApp().run()
