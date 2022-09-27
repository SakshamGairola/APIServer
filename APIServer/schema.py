import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

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
    banksList = graphene.List(BanksTypes)
    bankFields = graphene.Field(BanksTypes, id=graphene.Int())

    branchesList = graphene.List(BranchesType, id=graphene.Int())
    branchFields = graphene.Field(BranchesType)

    allBanks = DjangoListField(BanksTypes)

    test = graphene.String()

    # bank = graphene.Field(Banks, id=id)
    # def resolve_allBanks(self, info):
    #     return Banks.object.all()

    def resolve_banksList(self, info):
        return Banks.objects.all()

    def resolve_bankFields(self, info, id):
        return Banks.objects.get(pk=id)

    def resolve_branchesList(self, info, id):
        return Branches.objects.filter(bank=id)

    def resolve_branchFields(self, info):
        return Banks.objects.all

    def resolve_test(self, info):
        return "Helo"


schema = graphene.Schema(query=Query)
