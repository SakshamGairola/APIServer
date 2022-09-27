import graphene
from graphene_django import DjangoObjectType

from APIServer.models import Banks, Branches


class BanksTypes(DjangoObjectType):
    class Meta:
        model = Banks
        fields = ('name', 'id')


class BranchesType(DjangoObjectType):
    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')


class Query(graphene.ObjectType):
    banks = graphene.List(BanksTypes)
    bankFields = graphene.Field(BanksTypes)

    branches = graphene.List(BranchesType)
    branchFields = graphene.Field(BranchesType)

    # bank = graphene.Field(Banks, id=id)

    def resolve_banks(self, info):
        return Banks.objects.all()

    def resolve_branches(self, info):
        return Branches.objects.all()


schema = graphene.Schema(query=Query)
