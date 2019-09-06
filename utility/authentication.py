import os

from flask import request
import jwt


class Authentication():

    def get_token(self):
        token = request.headers.get('Authorization')
        return token

    def decode_token(self):
        decoded_token = jwt.decode(self.get_token(),
                                   key=os.getenv('SECRET_KEY'))
        return decoded_token


auth = Authentication()
