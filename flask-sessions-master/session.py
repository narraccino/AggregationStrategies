import flask, json
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    lmw= ['Red Light Radio', 'Red Light Secrets Prostitution Museum', 'Cinema 1', "Muziekgebouw aan 't IJ", "Museum Ons' Lieve Heer op Solder", 'Body Worlds', 'EYE', 'Tolhuistuin', 'Paradiso Noord', 'Bitterzoet']

    fa= ["Muziekgebouw aan 't IJ", 'Red Light Secrets Prostitution Museum', 'Red Light Radio', 'Cinema 1', 'Tolhuistuin', 'EYE', "Museum Ons' Lieve Heer op Solder", 'Body Worlds', 'Paradiso Noord']

    print(json.dumps(lmw))



    return flask.render_template("recc.html", fa=fa , lmw=lmw)


# @app.route('/search')
# def search():
#
#
#     # data = flask.request.args
#     # data = data.to_dict(flat=False)
#     # print(data['share'][0])
#     # dicto = json.loads(list(data.keys())[0])
#     # print(dicto)
#
#     return flask.render_template("recommendation.html", lmw=json.dumps(lmw), fa=json.dumps(fa))

if __name__ == '__main__':
    app.run(debug=True)

