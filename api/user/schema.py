import os

import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from werkzeug.security import check_password_hash, generate_password_hash
import jwt

from .models import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


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
        user_password = kwargs.get('password')
        confirm_pasword = kwargs.get('confirm_password')
        if user_password != confirm_pasword:
            raise GraphQLError('Passwords do not match')
        hashed_password = generate_password_hash(user_password,
                                                 method='pbkdf2:sha256',
                                                 salt_length=12)
        print(hashed_password)
        user = UserModel(name, hashed_password)
        user.save()
        return CreateUser(user=user)


class LoginUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        password = graphene.String(required=True)
    user = graphene.Field(User)

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
        payload = {'role':'default'}
        token = jwt.encode(payload, key=os.getenv('SECRET_KEY'))
        return token


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field(
        description="Creates a new user with the arguments")
    login_user = LoginUser.Field(
        description="Log in a user with the arguments")
