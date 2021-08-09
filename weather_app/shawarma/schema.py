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

    # shawarmas = graphene.List(ShawarmaType)
    # ingredients = graphene.List(IngredientType)
    # shawarma = graphene.Field(ShawarmaType, id=graphene.Int())
    #
    # def resolve_shawarmas(self, info, **kwargs):
    #     return Shawarma.objects.all()
    #
    # def resolve_shawarma(self, info, id=id):
    #     return Shawarma.objects.get(pk=id)
    #
    # def resolve_ingredients(self, info, **kwargs):
    #     return Ingredient.objects.all()


schema = graphene.Schema(query=Query)

