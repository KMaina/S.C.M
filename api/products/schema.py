import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func

from .models import Product as ProductModel
from utility.authentication import auth
from utility.utility import update_entity_fields
from helpers.validators import check_for_duplicate


class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel


class Query(graphene.ObjectType):
    all_products = graphene.List(
        Product,
        description="Query that returns a list of all products")

    def resolve_all_products(self, info):
        """
        Returns a list of all products
        """
        query = Product.get_query(info)
        return query.order_by(func.lower(ProductModel.name))


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        tax = graphene.Float(required=True)
        manufacturer = graphene.String(required=True)
        uom = graphene.String(required=True)
    product = graphene.Field(Product)

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        price = kwargs.get('price')
        tax = kwargs.get('tax')
        manufacturer = kwargs.get('manufacturer')
        uom = kwargs.get('uom')
        user = auth.decode_token().get('id')
        if user is None:
            raise GraphQLError('Invalid token detected')
        product_query = Product.get_query(info)
        product_obj = check_for_duplicate(product_query, name)
        if product_obj:
            raise GraphQLError('Product already exists')
        product = ProductModel(name, price, tax, manufacturer, uom, user)
        product.save()
        return CreateProduct(product=product)


class UpdateProduct(graphene.Mutation):
    """
        Update assigned resource in a room
    """
    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        tax = graphene.Float(required=True)
        manufacturer = graphene.String(required=True)
        uom = graphene.String(required=True)
    product = graphene.Field(Product)

    def mutate(self, info, id, **kwargs):
        product_query = Product.get_query(info)
        product = product_query.filter_by(id=id).first()
        if not product:
            raise GraphQLError('Product does not exist')
        update_entity_fields(product, **kwargs)
        product.UOM = kwargs.get('uom')
        product.save()
        return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    product = graphene.Field(Product)

    def mutate(self, info, id, **kwargs):
        query = Product.get_query(info)
        product = query.filter_by(
            id=id).first()
        if not product:
            raise GraphQLError('Product does not exist')
        product.delete()
        return DeleteProduct(product=product)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field(
        description="Creates a new product")
    update_product = UpdateProduct.Field(
        description="Update a product")
    delete_product = DeleteProduct.Field(
        description="Delete a product")
