import graphene
from graphene_django import DjangoObjectType, filter
from .models import Shawarma, Ingredient


class ShawarmaNode(DjangoObjectType):
    class Meta:
        model = Shawarma
        filter_fields = {'name': ['exact', 'icontains'],
                         'weight': ['exact', 'gt', 'lt'],
                         'price': ['exact', 'gt', 'lt'],
                         'ingredients__name': ['exact', 'icontains']}
        interfaces = (graphene.relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {'name': ['exact', 'icontains']}
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    shawarma = graphene.relay.Node.Field(ShawarmaNode)
    all_shawarmas = filter.DjangoFilterConnectionField(ShawarmaNode)

    ingredient = graphene.relay.Node.Field(IngredientNode)
    all_ingredients = filter.DjangoFilterConnectionField(IngredientNode)


schema = graphene.Schema(query=Query)

