from firstTopResults import topResults
from ratings import first_rate
from menu import createGroup,menu

import flask

app = flask.Flask(__name__)

if __name__ == "__main__":
    print("Loading chatbot")
    app.run()

