from graphql import GraphQLError


def validate_password(password, confirm_password):
    if len(password) < 6:
        raise GraphQLError('The length of the password should be more than 6')
    if password != confirm_password:
        raise GraphQLError('Passwords do not match')
    return password


def validate_empty_fields(**kwargs):
    for kwarg in kwargs:
        if kwargs.get(kwarg) is None:
            raise GraphQLError('Fields should not be empty')


def check_for_duplicate(query, field):
    return True if query.filter_by(name=field).first() else False
