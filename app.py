from flask import Flask, jsonify
from markupsafe import escape
from database import Database

class HooHacksApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.database = Database();
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return jsonify({"message": "Homepage"})

        @self.app.route('/database')
        def database():
            return f"{escape(self.database.ping())}"

    def run(self, host="0.0.0.0", port=5000, debug=False):
        if debug:
            host = "127.0.0.1"
        self.app.run(host=host, port=port, debug=debug)

app = HooHacksApp().app

if __name__ == "__main__":
    app_instance = HooHacksApp()
    app_instance.run()
