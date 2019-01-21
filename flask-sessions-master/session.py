import flask, json
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():


    return flask.render_template('provajavascript.html')


@app.route('/search')
def search():


    data = flask.request.args
    data = data.to_dict(flat=False)
    print(data['share'][0])
    # dicto = json.loads(list(data.keys())[0])
    # print(dicto)


    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

