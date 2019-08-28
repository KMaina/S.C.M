import os

import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from werkzeug.security import check_password_hash
import jwt

from .models import User as UserModel
from helpers.validators import validate_password


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('password', 'confirm_password')


class Query(graphene.ObjectType):
    all_users = graphene.List(
        User,
        description="Query That returns a list of all users")

    def resolve_all_users(self, info):
        """
            Returns list of all users
        """
        query = User.get_query(info)
        return query.order_by(func.lower(UserModel.name)).all()


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
        confirm_password = graphene.String(required=True)
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        user_password = validate_password(kwargs.get('password'),
                                          kwargs.get('confirm_password'))
        user = UserModel(name, user_password)
        user.save()
        return CreateUser(user=user)


class LoginUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
    token = graphene.String()

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        password = kwargs.get('password')
        person = User.get_query(info)
        person_obj = person.filter(
            UserModel.name == name
        ).first()
        if not person_obj:
            raise GraphQLError("Person not found")
        check_password = check_password_hash(person_obj.password, password)
        if not check_password:
            raise GraphQLError('Error signing into the app')
        payload = {'user_type': person_obj.user_type.value, 'name': name}
        user_token = jwt.encode(payload, key=os.getenv('SECRET_KEY'))
        token = user_token
        return LoginUser(token)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field(
        description="Creates a new user with the arguments")
    login_user = LoginUser.Field(
        description="Log in a user with the arguments")
