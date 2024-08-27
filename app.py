import flask

from src.controllers.index_controller import IndexController
from src.dto.configuration import Configuration

app = flask.Flask(__name__)
configuration = Configuration("resources/config.json")
app.config["application"] = configuration


@app.route('/')
def index():
    return IndexController().index()


if __name__ == '__main__':
    app.run()
