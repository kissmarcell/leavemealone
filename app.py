import flask
from flask_cors import CORS

from src.controllers.index_controller import IndexController
from src.entities.configuration import Configuration

app = flask.Flask(__name__, template_folder="src/templates")
configuration = Configuration.create("resources/config.json")
app.config["application"] = configuration
CORS(app)


@app.route('/projects')
def index():
    return IndexController.index()


if __name__ == '__main__':
    app.run()
