import functools

from graphql import GraphQLError
from utility.authentication import auth


def user_type(usertype):
    def user(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if auth.decode_token().get('role') not in usertype:
                raise GraphQLError(
                    'Sorry, you do not have perission to perform this task.')
            return func(*args, **kwargs)
        return wrapper
    return user
