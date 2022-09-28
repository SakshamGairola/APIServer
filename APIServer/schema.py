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
    #banksList = graphene.List(BanksTypes)
    #bankFields = graphene.Field(BanksTypes, id=graphene.Int())

    #branchesList = graphene.List(BranchesType, id=graphene.Int())
    #branchFields = graphene.Field(BranchesType)

    # branches = graphene.List(BranchesType)
    #branches = DjangoListField(BranchesType)
    #allBanks = DjangoListField(BanksTypes)

    # branches = graphene.Field(BranchesType, branch=graphene.String(required=True))
    branches = graphene.List(BranchesType, branch=graphene.String(required=True))

    def resolve_branches(self, info, branch):
        return Branches.objects.filter(branch=branch)

    # def resolve_banksList(self, info):
    #     return Banks.objects.all()

    # def resolve_bankFields(self, info, id):
    #     return Banks.objects.get(pk=id)

    # def resolve_branchesList(self, info, id):
    #     return Branches.objects.filter(bank=id)

    # def resolve_branchFields(self, info):
    #     return Banks.objects.all()


# Add a new Bank
class BankAddMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.Int(required=True)

    bank = graphene.Field(BanksTypes)

    @classmethod
    def mutate(cls, self, info, name, id):
        newBank = Banks(name=name, id=id)
        newBank.save()
        return BankAddMutation(bank=newBank)


# Update Existing Bank
class BankUpdateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.Int(required=True)

    bank = graphene.Field(BanksTypes)

    @classmethod
    def mutate(cls, self, info, name, id):
        updateBank = Banks.objects.get(id=id)
        updateBank.name = name
        updateBank.save()
        return BankUpdateMutation(bank=updateBank)


# Delete Existing id
class BankDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    bank = graphene.Field(BanksTypes)

    @classmethod
    def mutate(cls, self, info, id):
        deleteBank = Banks.objects.get(id=id)
        deleteBank.delete()
        return BankDeleteMutation(bank=deleteBank)


class Mutation(graphene.ObjectType):
    addBank = BankAddMutation.Field()
    updateBank = BankUpdateMutation.Field()
    deleteBank = BankDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
