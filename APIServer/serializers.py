from rest_framework import serializers
from APIServer.models import Banks, Branches


class BanksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ('name', 'id')


class BranchesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')
