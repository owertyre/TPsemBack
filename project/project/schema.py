import graphene
from staff.schema import Query as staff_query
from staff.schema import Mutation


class Query(staff_query):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)