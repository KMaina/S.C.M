import graphene

import api.user.schema
import api.products.schema


class Query(api.user.schema.Query,
            api.products.schema.Query):
    pass


class Mutation(api.user.schema.Mutation,
               api.products.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
