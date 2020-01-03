from flask import Flask
from flask_restful import Resource, Api
from githublogin import GithubAuthorize
from facebooklogin import FacebookAuthorize
from oa import oauth
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/")
def home():
    return "hi"


api.add_resource(GithubAuthorize, "/github/authorize")
api.add_resource(FacebookAuthorize, "/facebook/authorize")

if __name__ == "__main__":
    oauth.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
