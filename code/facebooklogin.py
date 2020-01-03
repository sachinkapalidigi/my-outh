from flask_restful import Resource
from oa import oauth, facebook
from flask import request, g


class FacebookAuthorize(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        access_token = data["access_token"]
        print(access_token)
        g.facebook_access_token = access_token

        facebook_user = facebook.get("me?fields=id,name,email")
        # facebook_name = facebook.get("name")

        print(facebook_user.data)
        # if user doesnot exist
        # add to database and get the user id
        # else get the user Id
        # use this to generate a jwt token
        # send it as a response with which they will authenticate
        return {"token": "token"}
