import mimetypes
import flask
from flask_cors import CORS

from src.controllers.index_controller import IndexController
from src.entities.configuration import Configuration

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

app = flask.Flask(__name__, template_folder="src/templates")
configuration = Configuration.create("resources/config.json")
app.config["application"] = configuration
CORS(app)

@app.route('/')
def index():
    return IndexController.index()

@app.route('/projects')
def projects():
    return IndexController.get_data()


if __name__ == '__main__':
    app.run()
