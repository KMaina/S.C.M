from graphql import GraphQLError


def validate_password(password):
    if len(password) < 6:
        raise GraphQLError('The length of the password should be more than 6')
    return password


def validate_empty_fields(**kwargs):
    for kwarg in kwargs:
        if kwargs.get(kwarg) is None:
            raise GraphQLError('Fields should not be empty')
