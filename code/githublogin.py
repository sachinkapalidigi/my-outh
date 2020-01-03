from flask_restful import Resource
from oa import oauth, github
from flask import request, g
import requests


class GithubAuthorize(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        code = data["code"]
        url = "https://github.com/login/oauth/access_token"
        my_data = {
            "code": code,
            "client_id": "c1d53a4b044962c3379a",
            "client_secret": "a2b7acacd1b94dde26fc1dae18b8c6e7f9e1f22f"
        }
        x = requests.post(url, data=my_data, headers={
                          "Accept": "application/json"})

        # print(x.json())
        data = x.json()

        g.access_token = data["access_token"]

        github_user = github.get("user")
        github_email = github.get("user/emails")
        print(github_user.data)
        print(github_email.data)
        # gives complete user data
        # if user doesnot exist
        # add to database and get the user id
        # else get the user Id
        # use this to generate a jwt token
        # send it as a response with which they will authenticate

        return {"token": "xyz"}
