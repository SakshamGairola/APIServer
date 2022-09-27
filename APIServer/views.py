from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

from APIServer.models import Banks, Branches
from APIServer.serializers import BanksSerializers, BranchesSerializers


def apiendpoint(request):
    if request.method == 'GET':
        banks = Banks.objects.all()
        banks_serializers = BanksSerializers(banks, many=True)
        return JsonResponse(banks_serializers.data, safe=False)


def apiendpointid(request, id=0):
    if request.method == 'GET':
        banks = Banks.objects.filter(id=id)
        banks_serializers = BanksSerializers(banks, many=True)
        return JsonResponse(banks_serializers.data, safe=False)
